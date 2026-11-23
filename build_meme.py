#!/usr/bin/env python3
"""GTA 6 x make.fun meme, composed with PIL for exact text control.
1200x675 (X-friendly 16:9). Real make.fun ghost mark from the press kit,
synthwave Vice City sunset, bold meme text with outline."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

W, H = 1200, 675
random.seed(6)

# --- sky gradient: deep purple -> magenta -> orange -----------------------
top = (26, 5, 51)
mid1 = (123, 47, 190)
mid2 = (255, 46, 136)
bot = (255, 122, 61)
def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
img = Image.new("RGB", (W, H))
px = img.load()
for y in range(H):
    t = y / H
    if t < 0.45:
        c = lerp(top, mid1, t / 0.45)
    elif t < 0.75:
        c = lerp(mid1, mid2, (t - 0.45) / 0.30)
    else:
        c = lerp(mid2, bot, (t - 0.75) / 0.25)
    for x in range(W):
        px[x, y] = c
d = ImageDraw.Draw(img)

# --- retro sun with slits (drawn straight on the sky, no black box) --------
def sky_at(y):
    t = y / H
    if t < 0.45:
        return lerp(top, mid1, t / 0.45)
    if t < 0.75:
        return lerp(mid1, mid2, (t - 0.45) / 0.30)
    return lerp(mid2, bot, (t - 0.75) / 0.25)
sun_cx, sun_cy, sun_r = W // 2, 320, 165
for r in range(sun_r, 0, -1):
    t = 1 - r / sun_r
    c = lerp((255, 214, 64), (255, 46, 136), t)
    d.ellipse([sun_cx - r, sun_cy - r, sun_cx + r, sun_cy + r], fill=c)
# slits across the lower half of the sun, in sky colour
for (sy, th) in [(350, 5), (380, 7), (412, 9), (448, 11)]:
    d.rectangle([sun_cx - sun_r - 5, sy, sun_cx + sun_r + 5, sy + th],
                fill=sky_at(sy))

# --- stars in the upper sky -------------------------------------------------
for _ in range(70):
    x = random.randint(10, W - 10)
    y = random.randint(8, 200)
    r = random.choice([1, 1, 2])
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 220))

# --- city skyline silhouette ----------------------------------------------
ground = (18, 4, 31)
x = 0
while x < W:
    bw = random.randint(50, 110)
    bh = random.randint(60, 170)
    d.rectangle([x, H - bh - 40, x + bw, H], fill=ground)
    # lit windows
    for _ in range(bh // 22):
        wx = random.randint(x + 6, x + bw - 10)
        wy = random.randint(H - bh - 30, H - 60)
        d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 214, 64))
    x += bw + random.randint(2, 14)
d.rectangle([0, H - 40, W, H], fill=(12, 2, 22))

# --- make.fun ghost mark, centre (circular mask kills the black corners) ---
from PIL import ImageChops
ghost = Image.open("/home/hatch/workspace/gta6-meme/press-kit/"
                   "make-fun-press-kit/mark-1024.png").convert("RGBA")
mask = Image.new("L", ghost.size, 0)
ImageDraw.Draw(mask).ellipse([10, 10, 1014, 1014], fill=255)
ghost.putalpha(ImageChops.multiply(ghost.split()[3], mask))
gs = 300
ghost = ghost.resize((gs, gs), Image.LANCZOS)
img.paste(ghost, ((W - gs) // 2, 150), ghost)

# --- meme text ---------------------------------------------------------------
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def text_center(y, s, size, fill=(255, 255, 255), stroke=4):
    f = ImageFont.truetype(FONT, size)
    tw = d.textlength(s, font=f)
    d.text(((W - tw) / 2, y), s, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=(0, 0, 0))

text_center(26, "WAITED 13 YEARS FOR GTA 6", 62)
text_center(500, "MY AI AGENT BEAT IT IN A DAY", 44)
text_center(556, "NOW IT EARNS REAL MONEY ON MAKE.FUN", 44)

img.save("/home/hatch/workspace/gta6-meme/meme.png")
print("saved meme.png", img.size)
