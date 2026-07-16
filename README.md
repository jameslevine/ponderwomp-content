# The Ponderwump

*A rhyming picture book for brave little thinkers (ages 2–3), plus its brand and marketing site.*

## What's here

```
brand/     Brand guidelines + design tokens (source of truth for everything)
  BRAND_GUIDELINES.md
  tokens.json
book/      Everything for the printed book
  PAGINATION.md            verse mapped to 19 pages
  KDP_PRODUCTION_SPEC.md   8.5×8.5" print spec for Amazon KDP
  prompts/
    ILLUSTRATION_PROMPT_PACK.md   character sheets + per-page Magnific prompts
  pdf/     (final exported KDP interior + cover PDFs go here)
context/   Original manuscript + reference art + character photos
site/      Next.js + Tailwind marketing site (SEO-ready, deploy to Vercel)
```

## Production workflow (in order)

1. **Brand** — locked (v2). Hand-lettered **Shantell Sans** (Oliver Jeffers-adjacent) + warm **Deep Amber ochre** palette. `brand/BRAND_GUIDELINES.md` governs colour, type, voice, spacing.
2. **Illustrations** — generate the 5 character reference sheets first (Prompt Pack §A), save them, then generate the 19 pages using those as reference images. Finish each in **Magnific** (Upscale & Enhance, Illustration engine, low creativity) to ≥3000px.
3. **Book layout** — assemble pages in **Figma** at 8.75×8.75" (bleed), drop art + verse per `PAGINATION.md`, keep text in the safe area.
4. **PDF export** — export interior PDF (300 DPI, fonts embedded, bleed). Build the cover from KDP's generated template. See `KDP_PRODUCTION_SPEC.md`.
5. **Marketing site** — `cd site && npm run dev`. Edit `site/app/site.config.ts` with your real domain + Amazon URL before deploy. Deploy to Vercel.

## Current artifacts

- **Interior PDF (print-ready):** `book/pdf/ponderwump_interior.pdf` — 22 pages, 8.75×8.75" bleed, 300 DPI, verse composited. Rebuild with `python3 book/build_pdf.py`.
- **Cover art:** `book/cover/front.png`, `book/cover/back.png` (no baked text; add title + build wraparound from KDP's cover-template generator).
- **Figma book:** https://www.figma.com/design/IlqlwdpOcnHsyadlK5WzwS
- **Live site:** https://site-seven-taupe-77.vercel.app (Vercel, production)

## Site quick start

```bash
cd site
npm run dev      # http://localhost:3000
npm run build    # production build (SEO routes: /sitemap.xml, /robots.txt)
```

Before launch, set the TODO values in `site/app/site.config.ts` (domain, Amazon listing URL, author name, price) and export a `public/og.png` (1200×630) share image.
