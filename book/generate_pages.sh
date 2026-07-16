#!/usr/bin/env bash
# Generate story pages via Nano Banana (Gemini 2.5 Flash Image) WITH character references.
# Usage: FREEPIK_API_KEY=... ./generate_pages.sh <manifest.tsv> <outdir>
# manifest line: slug<TAB>refs(comma-sep slugs)<TAB>prompt
# References are the locked character sheets in prompts/characters/<slug>.png (downscaled).
set -uo pipefail
KEY="${FREEPIK_API_KEY:?set FREEPIK_API_KEY}"
MANIFEST="${1:?manifest required}"; OUTDIR="${2:?outdir required}"
CHARDIR="$(dirname "$0")/prompts/characters"
REFCACHE="$(mktemp -d)"; mkdir -p "$OUTDIR"
BASE="https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
TMPMAP="$(mktemp)"

STYLE="LOOSE WATERCOLOUR, COLOURED-PENCIL AND GOUACHE hand-painting, visible washes and paper grain, loose ink linework, hand-painted children's picture-book illustration in the style of Oliver Jeffers and classic watercolour storybooks, warm ochre palette (deep amber, lantern gold, soft clay terracotta, rust, dark olive green, warm cream paper), warm dusk lighting, atmospheric storybook depth, tiny figures in a big world. Keep the SAME characters as the reference images. Leave some calm empty space for text. NOT digital cartoon, NOT 3D, NOT vector, NOT cool teal-toned. Square 1:1."

# pre-downscale each character sheet to a base64 reference (once)
refb64() {
  local slug="$1"
  local out="$REFCACHE/$slug.b64"
  if [ ! -f "$out" ]; then
    sips -Z 640 "$CHARDIR/$slug.png" --out "$REFCACHE/$slug.png" >/dev/null 2>&1
    base64 -i "$REFCACHE/$slug.png" | tr -d '\n' > "$out"
  fi
  echo "$out"
}

while IFS=$'\t' read -r slug refs prompt; do
  [ -z "${slug:-}" ] && continue
  full="$prompt $STYLE"
  # build reference_images JSON array from comma-separated ref slugs
  reffiles=""
  IFS=',' read -ra RA <<< "$refs"
  jqargs=(); jqarr="["
  first=1
  for rs in "${RA[@]}"; do
    [ -z "$rs" ] && continue
    f=$(refb64 "$rs")
    jqargs+=(--rawfile "$rs" "$f")
    if [ $first -eq 1 ]; then jqarr="$jqarr\$$rs"; first=0; else jqarr="$jqarr,\$$rs"; fi
  done
  jqarr="$jqarr]"
  jq -nc "${jqargs[@]}" --arg p "$full" "{prompt:\$p, reference_images:$jqarr}" > "$REFCACHE/payload_$slug.json"
  resp=$(curl -s -X POST "$BASE" -H "x-freepik-api-key: $KEY" -H "Content-Type: application/json" --data @"$REFCACHE/payload_$slug.json")
  tid=$(echo "$resp" | jq -r '.data.task_id // empty')
  if [ -z "$tid" ]; then echo "SUBMIT FAIL $slug: $(echo "$resp"|head -c 200)"; continue; fi
  printf '%s\t%s\n' "$slug" "$tid" >> "$TMPMAP"
  echo "submitted $slug (refs: $refs) -> $tid"
done < "$MANIFEST"

echo "--- polling ---"
while IFS=$'\t' read -r slug tid; do
  for i in $(seq 1 60); do
    r=$(curl -s "$BASE/$tid" -H "x-freepik-api-key: $KEY")
    st=$(echo "$r" | jq -r '.data.status')
    if [ "$st" = "COMPLETED" ]; then
      echo "$r" | jq -r '.data.generated[0]' | xargs -I{} curl -s "{}" -o "$OUTDIR/$slug.png"
      echo "DONE $slug"; break
    elif [ "$st" = "FAILED" ]; then echo "FAILED $slug: $(echo "$r"|head -c 200)"; break; fi
    sleep 5
  done
done < "$TMPMAP"
rm -rf "$REFCACHE" "$TMPMAP"
echo "all pages done."
