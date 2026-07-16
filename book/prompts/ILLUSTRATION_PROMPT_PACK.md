# The Ponderwump — Illustration Prompt Pack (for Magnific)

*How to get 19 consistent, on-style spreads. Read the workflow first, then generate the character sheets, then the pages.*

---

## How to use this in Magnific

Magnific is primarily an **upscaler + image-to-image "Reimagine/Relight"** tool, not a pure text-to-image generator. The reliable workflow for a picture book is:

1. **Generate base images elsewhere first** (Midjourney, Ideogram, or Flux — whichever you have). Use the prompts below as the base prompts.
2. **Bring each base image into Magnific → Upscale & Enhance** with the *Illustration/Artistic* engine, Creativity low–medium (so it enhances the painterly texture without redrawing content), to get the watercolour-pencil-gouache finish and print-resolution output.
3. For scenes where a character drifts off-model, use **Magnific's image-to-image with a character reference** (drop the locked character sheet as reference, low creativity) to pull it back on-model.

If your text-to-image tool supports **reference/character images** (Midjourney `--cref`, Flux redux, etc.), feed it the character sheets from Step A so faces stay consistent across all 19 pages.

**Global style suffix — append to EVERY prompt:**

> `--- STYLE: hand-painted children's picture-book illustration, watercolour and coloured-pencil and gouache mixed media, visible paper grain and loose ink linework, painterly washes, low WARM dusk/night lighting (warm-dark, never blue), glowing amber lantern light against warm brown shadow, atmospheric depth, storybook scale (tiny figures in a big world), soft simple expressive faces, warm OCHRE palette: deep amber #B4791E, lantern gold #E8B54D, soft clay terracotta #C47B5A, rust #9C3D1C accents, dark olive green #556B2F, warm near-black ink #1F1811, warm cream paper #F4EAD3. NOT digital-flat, NOT vector, NOT 3D render, NOT photorealistic, NOT cool/teal-toned. Aspect 1:1 square.`

**Note on the Ponderwump's coat:** the verse describes it as "moss green edged in dusky blue." Keep the coat **dark olive/moss green** (`#556B2F`) as the hero colour; render the "dusky blue" edge as a subtle, muted teal-shimmer rim-light only — a thin accent, so the giant still sits inside the warm-ochre world rather than turning the scene cool.

**Print spec:** target ≥ 3000×3000px after Magnific upscale (8.5×8.5" @ 300dpi + bleed = 2625px min; go bigger).

---

## A. Character reference sheets — GENERATE THESE FIRST, SAVE THEM

Generate each on a plain warm-paper background, front + 3/4 views, then reuse as the reference image for every page they appear on. These lock the cast.

### A1 — Marnie (protagonist)
> Character reference sheet, front and three-quarter views on plain warm-paper background. **Marnie:** a small girl, about 2–3 years old, fair/blonde tufty short hair, big bright curious eyes, round rosy cheeks, small joyful smile. Wears a **poppy-red knitted jumper** and blue denim trousers, little red shoes. Cheerful, brave, thinking expression. Soft simple painted features.

### A2 — Daddy
> Character reference sheet, front and three-quarter views on plain warm-paper background. **Daddy:** a young man, short ginger/auburn hair, neat ginger beard, kind tired eyes. Wears a **muted moss-green long coat over a soft grey-green shirt**, tan tones. Begins slightly grey and deflated; gentle, warm. Soft simple painted features.

### A3 — Mummy (bookends only)
> Character reference sheet, front view on plain warm-paper background. **Mummy:** a woman with dark brown hair and a fringe, warm smile, wrapped in a **cream cable-knit blanket/cardigan**, softly pregnant. Cosy, poorly-but-loved, gentle. Seen at cottage window at night, moonlit. Soft simple painted features.

### A4 — The Ponderwump (THE hero design — lock this hard)
> Character reference sheet, full body + head close-up on plain warm-paper background. **The Ponderwump:** an enormous gentle giant, taller than trees, kind and slightly muddled expression. **Coat/fur of soft moss green edged with a dusky-blue shimmer** (green touched with blue, like the last of the day). **Two eyes that glow like amber lanterns.** **Two horns that curl upward into shy little question-mark shapes.** **A long looping tail he wears like a crest.** **Small round old-fashioned spectacles perched on his snout.** Huge, soft, benevolent, a walking picture of a mind with too many thoughts. Fur texture in coloured pencil over watercolour.

### A5 — The four creatures (one sheet)
> Character reference sheet on warm-paper background, four woodland creatures in painterly storybook style: **a small forlorn Tortoise** by mossy stepping stones; **a line of tiny Ants** carrying a crumb; **a flustered russet Squirrel** with a big fluffy orange tail, acorns scattered; **a pale Owl** on a branch. Soft, characterful, gentle.

---

## B. Page-by-page scene prompts (19 pages)

Each references the story beats. Keep a **text-safe area** (empty warm-paper zone) noted per page for Figma to drop verse into. Feed the relevant character sheet(s) as reference.

**P1 — Marnie introduced.** Interior of a cosy crooked cottage at dusk, warm terracotta lamplight. Marnie sits with a "carousel" of tiny glowing thought-doodles (question marks, stars, tiny gears) swirling above her head. Cosy, wonder. *Text-safe: top-left.* [ref: A1]

**P2 — Daddy loses his desk to the machine.** Daddy shuffling home at dusk down a tumbling terracotta-and-teal street (like the reference town), head drooping, grey and deflated; a cold hulking glowing machine looms behind at his old desk in a lit window. Melancholy. *Text-safe: sky top.* [ref: A2]

**P3 — Strawberry joke, Marnie cheers him.** Cottage interior, Marnie clambered onto Daddy's knee with a big grin, spelling on her fingers; a warm cloud of grey lifting away. First laugh. Warm terracotta glow. *Text-safe: right.* [ref: A1, A2]

**P4 — Mummy poorly, the baby, the cloud joke.** Mummy wrapped in a cream blanket on a settle by the fire, softly pregnant, hand on bump; Marnie and Daddy kissing her cheek. Tender, golden firelight, a small window showing sky/clouds. *Text-safe: left.* [ref: A1, A2, A3]

**P5 — They set off into the Muddlewood.** Wide dusk landscape: two tiny figures (Marnie + Daddy) walking up over a hill toward a tall dark wood, ferns waving like feathers, teal sky. Storybook scale. *Text-safe: sky.* [ref: A1, A2]

**P6 — Belief vs doubt (refrain).** In the wood among tall ferns and toadstools, Marnie gestures up in wonder describing the giant; faint dreamy hint of the Ponderwump in the misty background (barely there). Daddy smiles, tired and kind. *Text-safe: lower.* [ref: A1, A2]

**P7 — Lost.** The path petering out, light thinned to gleams, tall dark trees closing in, the two small figures turned about. Slightly anxious but safe. Deep teal shadow, tiny warm figures. *Text-safe: top.* [ref: A1, A2]

**P8 — Tortoise (sequencing).** A shimmering brook, a small forlorn tortoise before mossy stepping stones; Marnie crouched pointing out the stones one-by-one in order. Warm, gentle. *Text-safe: right.* [ref: A1, A2, A5-tortoise]

**P9 — Ants (decomposition).** A long line of tiny ants heaving a huge crumb, then breaking it into small pieces each ant carries; Marnie kneeling, delighted. Forest floor, dappled dusk. *Text-safe: top.* [ref: A1, A5-ants]

**P10 — Squirrel (loops + vibe-coder joke).** A flustered russet squirrel with acorns flung everywhere in a bluster, then calmly gathering them one by one; a tiny wrecked "nut-flinger" contraption. Comic, warm. (Echo the reference squirrel image.) *Text-safe: right.* [ref: A1, A5-squirrel]

**P11 — Owl (algorithm), Daddy nearly believes.** A pale owl on a bough, several dim path-lines fanning out behind her; Marnie writing steps in the air; Daddy's face softening into near-belief, a little warmer/less grey. *Text-safe: lower.* [ref: A1, A2, A5-owl]

**P12 — The black river blocks them.** The trees open on a wide black roaring river, deep and swift; Daddy sinks down in shivery loss; Marnie stands looking. Dramatic dark water, cool. *Text-safe: sky.* [ref: A1, A2]

**P13 — The duck (rubber-duck), the plan forms.** A sleepy duck on a stump/log by the river blinking; Marnie talking her problem aloud into the foggy air, tiny glowing thought-lines assembling into a plan. Foggy, intimate. *Text-safe: top.* [ref: A1]

**P14 — THE REVEAL.** The full-page hero spread. The ferns shiver, and the Ponderwump rises from the gloom taller than the trees — moss-green coat edged in dusky blue, two amber lantern eyes glowing, two question-mark horns, long looping tail crest, little round spectacles. Marnie gasps, Daddy stares. Awe, amber light flooding the cool dark. *Full bleed, minimal text (title-style zone bottom).* [ref: A1, A2, A4]

**P15 — Daddy believes.** Close, warm: Daddy kneeling, hand to chest, looking up at the giant with wonder, doubt slipping away; Marnie beside him beaming. Amber glow on their faces. *Text-safe: side.* [ref: A1, A2, A4]

**P16 — The muddle & the plan.** The giant slumped, sad and muddled, a tangle of glowing thought-threads knotting around his head; tiny Marnie standing tall by his enormous toe, gesturing a clear plan; the threads beginning to straighten. *Text-safe: top.* [ref: A1, A4]

**P17 — Carried home / the bridge.** The Ponderwump arched as a bridge, tail laid to the far bank, cradling Marnie and Daddy softly as he carries them across the black water under a sky full of stars. Magical, sweeping. *Text-safe: sky.* [ref: A1, A2, A4]

**P18 — Home to Mummy + Daddy's healing.** The crooked cottage glowing gold through mist, Mummy at the lit window moonlit; Daddy kneeling by Marnie in the golden doorway light, the giant peeping in kindly behind. Warm reunion. *Text-safe: sky/side.* [ref: A1, A2, A3, A4]

**P19 — Marnie asleep on her own glowing thought.** Marnie asleep in bed, moon on her brow, a single small warm glowing thought (a tiny lantern/idea) hovering above her; the Ponderwump curled in the ferns by the door outside the window. Peaceful, tender close. *Text-safe: top.* [ref: A1, A4]

---

## C. Cover prompts

**Front cover:** night Muddlewood, the Ponderwump revealed rising among tall trees with amber lantern eyes glowing, tiny Marnie (poppy-red jumper) and Daddy looking up in wonder, room at top for title "The Ponderwump" and space for author name at bottom. Awe + warmth. [ref: A1, A2, A4]

**Back cover:** simpler — the cottage glowing at dusk, the giant curled peacefully in the ferns by the door, warm-paper panel space for blurb text. [ref: A4]

**Spine:** solid Muddlewood Ink with the wordmark; a small amber-eye glyph.

---

## D. Consistency checklist (run before accepting any page)

- [ ] Marnie in poppy-red jumper, fair tufty hair — same face as A1?
- [ ] Daddy ginger beard + moss-green coat — same as A2?
- [ ] Ponderwump has ALL five features: moss/blue coat, amber eyes, question-horns, looping tail, round specs?
- [ ] Lighting warm-against-cool dusk/night?
- [ ] Watercolour/pencil/gouache texture, not flat digital?
- [ ] Palette within the six brand colours?
- [ ] Text-safe area preserved for the verse?
