#!/usr/bin/env bash
# Ponderwump illustration generator via Freepik "Nano Banana" (Gemini 2.5 Flash Image).
# Usage: FREEPIK_API_KEY=... ./generate.sh <manifest.tsv> <outdir>
# manifest.tsv: each line = "slug<TAB>prompt"  (tab-separated)
# bash 3.2 compatible (macOS default) — no associative arrays.
set -uo pipefail

KEY="${FREEPIK_API_KEY:?set FREEPIK_API_KEY}"
MANIFEST="${1:?manifest.tsv required}"
OUTDIR="${2:?outdir required}"
mkdir -p "$OUTDIR"
BASE="https://api.freepik.com/v1/ai/gemini-2-5-flash-image-preview"
TMPMAP="$(mktemp)"

# Shared watercolour style suffix appended to every prompt.
STYLE="LOOSE WATERCOLOUR AND COLOURED-PENCIL AND GOUACHE hand-painting, visible watercolour washes and paper grain, loose expressive ink linework, hand-painted children's picture-book illustration in the style of Oliver Jeffers and classic watercolour storybooks, warm ochre palette (deep amber, lantern gold, soft clay terracotta, rust, dark olive green, warm cream paper), soft painterly, warm dusk lighting. NOT digital cartoon, NOT smooth 3D render, NOT vector, NOT airbrushed, NOT cool teal-toned."

while IFS=$'\t' read -r slug prompt; do
  [ -z "${slug:-}" ] && continue
  full="$prompt $STYLE"
  payload=$(jq -nc --arg p "$full" '{prompt:$p}')
  resp=$(curl -s -X POST "$BASE" -H "x-freepik-api-key: $KEY" -H "Content-Type: application/json" -d "$payload")
  tid=$(echo "$resp" | jq -r '.data.task_id // empty')
  if [ -z "$tid" ]; then echo "SUBMIT FAIL $slug: $resp"; continue; fi
  printf '%s\t%s\n' "$slug" "$tid" >> "$TMPMAP"
  echo "submitted $slug -> $tid"
done < "$MANIFEST"

while IFS=$'\t' read -r slug tid; do
  for i in $(seq 1 50); do
    r=$(curl -s "$BASE/$tid" -H "x-freepik-api-key: $KEY")
    st=$(echo "$r" | jq -r '.data.status')
    if [ "$st" = "COMPLETED" ]; then
      echo "$r" | jq -r '.data.generated[0]' | xargs -I{} curl -s "{}" -o "$OUTDIR/$slug.png"
      echo "DONE $slug -> $OUTDIR/$slug.png"; break
    elif [ "$st" = "FAILED" ]; then echo "FAILED $slug: $r"; break; fi
    sleep 5
  done
done < "$TMPMAP"
rm -f "$TMPMAP"
echo "all done."
