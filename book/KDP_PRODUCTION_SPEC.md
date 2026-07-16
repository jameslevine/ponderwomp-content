# The Ponderwump — Amazon KDP Print Production Spec

Target: **8.5 × 8.5" square paperback**, full-colour, printed via Amazon KDP.

## Trim & bleed (the numbers Figma/PDF must hit)

- **Trim size:** 8.5 × 8.5 in (215.9 × 215.9 mm)
- **Bleed:** add 0.125 in on all *outside* edges → **full-bleed page = 8.75 × 8.625 in** per KDP's asymmetric bleed rule (0.125" top, bottom, outer; 0" on the spine/bind side).
  - Simpler safe approach used here: design each page at **8.75 × 8.75 in** with art running to the edge; KDP trims to 8.5.
- **Safe/live area (keep text + key art inside):** ≥ 0.25 in from every trimmed edge, and ≥ 0.375 in from the spine side. Put verse well inside.
- **Resolution:** 300 DPI. So each full-bleed page = **2625 × 2625 px** minimum. (Prompt pack targets ≥3000px — good.)
- **Colour:** design in RGB, export PDF; KDP converts to CMYK. Avoid pure #000 for text — use Muddlewood Ink `#16323F` or Soft Charcoal.

## Page count

- Story = 19 illustrated spreads. With front/back matter, aim for a multiple that KDP likes.
- **Recommended interior sequence (single pages):**
  1. Half-title / title page
  2. Copyright page (ISBN, © line, "Printed by Amazon")
  3. Dedication (optional)
  4. Story pages 1–19
  5. "For the grown-up reading along" note (the four-ideas + jokes page)
  6. Blank / About the author
- Total ≈ 24–26 interior pages. KDP paperback minimum is 24 pages — confirm final count is ≥24.

## Cover (separate file)

- KDP generates a **full wraparound cover template** based on final page count + paper type. Do NOT guess the spine width.
- After the interior is finalised, use KDP's **Cover Template Generator** (enter trim 8.5×8.5, page count, paper = premium colour) to get exact spine width + wrap dimensions, then lay the cover art (front/spine/back from the prompt pack) into that template.

## Two export files KDP needs

1. **Interior PDF** — all interior pages, PDF/X or standard PDF, fonts embedded, 300 DPI, bleed included.
2. **Cover PDF** — single wraparound page matching KDP's generated template.

## Fonts
- Embed Fraunces (titles/verse) + Inter (any UI/back-matter) in the PDF. Both are OFL-licensed → free to embed commercially.

## Pre-flight checklist
- [ ] Every page 2625×2625px+ at 300 DPI
- [ ] Bleed present, no important content in the 0.25" trim margin
- [ ] Verse never split across a page turn (see PAGINATION.md)
- [ ] Text uses Ink/Charcoal, not pure black
- [ ] Fonts embedded
- [ ] Copyright page complete (author, ©year, ISBN if using own)
- [ ] Cover built from KDP's generated template (correct spine width)
- [ ] Final page count ≥ 24
