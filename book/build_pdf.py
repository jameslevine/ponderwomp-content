#!/usr/bin/env python3
"""Assemble The Ponderwump interior PDF from page PNGs at KDP print spec.
8.75x8.75in bleed pages @ 300dpi = 2625px. Reading order incl. text matter pages.
Pillow-only (no external deps)."""
import os
from PIL import Image, ImageDraw, ImageFont

BOOK = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(BOOK, "pages")
OUT = os.path.join(BOOK, "pdf", "ponderwump_interior.pdf")
PX = 2625                      # 8.75in @ 300dpi (bleed)
PAPER = (0xF4, 0xEA, 0xD3)
INK = (0x1F, 0x18, 0x11)
AMBER = (0xB4, 0x79, 0x1E)
PENCIL = (0x6E, 0x5A, 0x42)

def find_font(size):
    for p in [
        "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf",
        "/System/Library/Fonts/Supplemental/Chalkboard.ttc",
        "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def text_page(lines, sizes, colors, align="center"):
    img = Image.new("RGB", (PX, PX), PAPER)
    d = ImageDraw.Draw(img)
    blocks = []
    for text, size in zip(lines, sizes):
        f = find_font(size)
        # wrap
        maxw = PX - 600
        words, cur, wrapped = text.split(" "), "", []
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= maxw:
                cur = t
            else:
                wrapped.append(cur); cur = w
        wrapped.append(cur)
        lh = int(size * 1.4)
        blocks.append((wrapped, f, lh))
    total = sum(len(w)*lh for w, f, lh in blocks) + (len(blocks)-1)*40
    y = (PX - total)//2
    for (wrapped, f, lh), color in zip(blocks, colors):
        for line in wrapped:
            tw = d.textlength(line, font=f)
            x = (PX - tw)//2 if align == "center" else 300
            d.text((x, y), line, font=f, fill=color)
            y += lh
        y += 40
    return img

VERSES = {
 "p01":"In a crooked little cottage at the edge of the wood\nlived a girl with a head full of why, how, and could.\nHer name, it was Marnie. Behind her bright eyes\nspun a carousel wonder, forever surprise.",
 "p02":"Her father made worlds out of letters and light,\ntill a hulking new machine took his desk overnight.\n“It’s quicker than you,” the cold letter had read.\nHe came shuffling home rather grey, drooping his head.",
 "p03":"But Marnie clambered up on his knee with a grin.\n“That gadget’s not clever. Now listen. Begin.\nHow many small R’s are in strawberry, Dad?”\n“The machine answered two.” “Then the machine’s rather bad,\nfor the answer is three!” And she spelled it with glee.",
 "p04":"Now Mummy sat wrapped in a blanket, unwell,\nwith a baby curled close, like a pip in its shell.\nThey kissed her soft cheek. “You’re the dearest,” they said.\n(She still thought “the cloud” was the sky overhead.)",
 "p05":"“Go wander,” Mum murmured, “and let me lie low.”\nSo they buttoned their coats and they went, off they go,\nup over the hill to the Muddlewood, tall,\nwhere the ferns wave like feathers and hush covers all.",
 "p06":"“In this forest,” breathed Marnie, “a giant abides:\nthe Ponderwump, wisest of thinkers, who hides.\nHis thoughts are the biggest for miles, so they say.”\nDad smiled, tired and kind. “That’s a story, love. Play.”",
 "p07":"They rambled past toadstools and trickling streams,\ntill the path petered out and the light thinned to gleams.\n“We’re turned all about,” fretted Daddy. “Oh dear.”\nBut Marnie stood calm. “Then we’ll think our way clear.”",
 "p08":"By a shimmering brook sat a tortoise, forlorn,\nall baffled by which mossy stone to step on.\n“Just take them in order,” said Marnie. “This one, then next.”\n“The Ponderwump’s coat is deep moss, dusk as well.”",
 "p09":"A long line of ants heaved a crumb like a hill.\n“Then break it to pieces,” urged Marnie. “Be smart.\nOne crumb becomes crumbs, and each ant takes a part.”\n“The Ponderwump’s eyes are two lanterns of amber.”",
 "p10":"A squirrel shot past in a terrible fluster,\nhis acorns flung wide, all his hoard in a bluster.\n“Then gather them gently. Do one, then one again,\nrepeat it and repeat it, and count up to ten.”\n“The Ponderwump’s horns curl like questions, held high.”",
 "p11":"An owl on a bough hooted, ruffled and pale.\n“Then plan it,” said Marnie. “Write steps in a row:\nstep one, and step two, and step three. Then you go.”\n“The Ponderwump loops a tail, and wears spectacles, too.”",
 "p12":"“I believe it. I do.” But the trees opened wide\non a river of black, roaring, deep, swift and snide.\nToo broad and too bitter to paddle across.\nPoor Daddy sank down with a shivery loss.",
 "p13":"But a duck on a stump gave a sleepy “just you.”\nSo Marnie described, aloud through the fog,\nevery twist of the trouble — and clear as could be,\nthe answer stood up. “A bridge we can make!”",
 "p14":"Then the ferns gave a shiver, the shadows all stirred,\nand a hum, deep and gentle, was suddenly heard.\nUp rose from the gloom, taller far than the trees,\na coat the soft green of the moss, edged in seas\nof a dusky blue shimmer; two lanterns of amber.",
 "p15":"“The Ponderwump! Look!” Marnie gasped. “There he stands!”\nAnd Daddy just stared, his doubt slipping his hands.\n“He’s real,” Daddy breathed. “All this time you were right.\nMy clever, brave girl, you could see through the night.”",
 "p16":"But the great gentle giant slumped down with a moan,\n“I’ve wandered for years, cold and muddled, alone.”\nSo Marnie stood tall by his enormous left toe.\n“We’ll think it together. Just steady. Just slow.”",
 "p17":"The Ponderwump brightened. “A plan! Oh, how grand!”\nHe arched his huge back into one mighty span,\nlaid his tail like a bridge, and carried them, cradled,\nback over the water while stars swept the sky.",
 "p18":"“You found one!” laughed Mummy. “A friend, oh how dear!”\nThen Daddy knelt down by his girl in the glow.\n“A machine took my chair. But now, Marnie, I know:\na mind is a garden no engine can grow.”",
 "p19":"So the Ponderwump curled in the ferns by their door,\na friend to the family for evermore.\nAnd Marnie slept deep, with the moon on her brow,\nand a thought of her own, glowing warm. Wonder how.",
}

def load(slug):
    im = Image.open(os.path.join(PAGES, slug + ".png")).convert("RGB")
    if im.size != (PX, PX):
        im = im.resize((PX, PX), Image.LANCZOS)
    verse = VERSES.get(slug)
    if verse:
        d = ImageDraw.Draw(im, "RGBA")
        f = find_font(50)
        lines = verse.split("\n")
        lh = int(50 * 1.35)
        pad, safe = 48, 150
        boxw = PX - safe*2
        th = len(lines)*lh + pad*2
        bx, by = safe, PX - safe - th
        # cream scrim
        d.rounded_rectangle([bx, by, bx+boxw, by+th], radius=24, fill=(0xF4, 0xEA, 0xD3, 210))
        y = by + pad
        for ln in lines:
            d.text((bx+pad, y), ln, font=f, fill=INK)
            y += lh
    return im

# Text matter pages rendered simply (Figma has the styled versions; this keeps the PDF self-contained)
title = text_page(
    ["The Ponderwump", "A rhyming picture book for brave little thinkers", "written by  ·  illustrated by"],
    [200, 66, 48], [INK, AMBER, PENCIL])
copyright = text_page(
    ["The Ponderwump", "Text and illustrations © 2026 [Author Name]. All rights reserved.",
     "Illustrations created with AI assistance and hand-finished. Set in Shantell Sans.",
     "First edition, 2026.   ISBN: 000-0-0000000-0-0"],
    [90, 46, 46, 46], [INK, PENCIL, PENCIL, PENCIL])
grownup = text_page(
    ["For the grown-up reading along",
     "Four quiet ideas hide inside the story, never named so a small child just hears a good tale: putting steps in order (the tortoise), breaking a big job into small pieces (the ants), repeating a step until it is done (the squirrel), and following a clear plan (the owl). Marnie reuses all four to cross the river, so the lessons solve the ending.",
     "A few jokes are for you: the strawberry the machine miscounts, Mummy picturing the cloud in the sky, the squirrel who shipped it and skipped it, and the drowsy duck Marnie explains her problem to."],
    [84, 46, 46], [INK, PENCIL, PENCIL])

order = ([title, copyright]
         + [load(f"p{ i:02d}") for i in range(1, 20)]
         + [grownup])

os.makedirs(os.path.dirname(OUT), exist_ok=True)
order[0].save(OUT, "PDF", resolution=300.0, save_all=True, append_images=order[1:])
print(f"Wrote {OUT}  ({len(order)} pages, {PX}x{PX}px @300dpi)")
