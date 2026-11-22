#!/usr/bin/env python3
"""news-image-20261122 — deterministic front-page render (32 verified stories).

Parent-direct build (20261121 precedent: parent builds directly).
Story data: ~/workspace/makefun/news-image-20261122-research.md
  (30 verified + 4 parent supplementary verifications S1-S4).
Concept: ChatGPT-approved Concept A (editorial broadsheet); Rizky 22 Nov 18:02
  picked the dense 32-33 story version. Top-8 leaderboard entries studied
  (ranks 1,2,5,8 read in full): masthead + number strip + region bar + UTC
  timeline + 3 illustrated leads + 12 small cards + map + ALSO list + DATE
  CHECK box. COP31 depicted honestly: text released, ADOPTION PENDING.
Output: entry.png, 1024x1024, <=1 MiB. Deterministic: no randomness, no time.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
GREY = (107, 114, 128)
LIGHT = (232, 226, 208)
RED = (185, 28, 28)
DARKRED = (127, 29, 29)
NAVY = (30, 58, 95)
OCEAN = (220, 233, 242)
LAND = (232, 220, 195)
LANDLINE = (180, 168, 140)
GOLD = (217, 119, 6)
GREEN = (22, 101, 52)
AMBER = (146, 64, 14)
TEAL = (13, 100, 100)
SKY = (235, 228, 210)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(SANS, size)


F = {
    "band": font(SANS_B, 10),
    "mast": font(SERIF_B, 50),
    "sub": font(SANS_B, 14),
    "stat_n": font(SANS_B, 26),
    "stat_l": font(SANS_B, 8),
    "reg": font(SANS_B, 10),
    "time": font(SANS_B, 10),
    "lead": font(SERIF_B, 18),
    "lead_s": font(SANS_B, 10),
    "lead_b": font(SANS, 10),
    "cap": font(SANS, 9),
    "cap_b": font(SANS_B, 9),
    "card_h": font(SANS_B, 10),
    "card_c": font(SANS, 8),
    "sect": font(SANS_B, 12),
    "list": font(SANS, 10),
    "list_b": font(SANS_B, 10),
    "dc": font(SANS, 9),
    "dc_b": font(SANS_B, 10),
    "foot": font(SANS, 8),
    "badge": font(SANS_B, 8),
    "pin": font(SANS_B, 8),
}


def wrap(d, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(d, cx, y, text, fnt, fill=INK):
    d.text((cx - d.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def tag(d, x, y, text, color):
    w = d.textlength(text, font=F["badge"]) + 8
    d.rectangle([x, y, x + w, y + 12], fill=color)
    d.text((x + 4, y + 1.5), text, font=F["badge"], fill=(255, 255, 255))
    return w


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- top band 0-18
d.rectangle([0, 0, 1024, 18], fill=NAVY)
d.text((10, 3), "THE WORLD IN ONE DAY", font=F["band"], fill=(255, 255, 255))
r = "32 STORIES  ·  6 REGIONS  ·  EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"
d.text((1014 - d.textlength(r, font=F["band"]), 3), r, font=F["band"],
       fill=(255, 220, 130))

# ---------------------------------------------------------------- masthead 18-78
center(d, 512, 24, "Sunday 22 November 2026", F["mast"])
center(d, 512, 80,
       "COP31's deal names no fossil fuels  ·  186 drones over Ukraine in the night  ·  Iran's radar claim meets Bahrain's denial",
       F["sub"], RED)
d.rectangle([8, 98, 1016, 100], fill=INK)

# ---------------------------------------------------------------- stat strip 100-136
stats = [("186", "DRONES FIRED OVERNIGHT"),
         ("161", "DOWNED OR SUPPRESSED"),
         ("35%", "ELECTRICITY GOAL 2035"),
         ("$120bn", "ADAPTATION TARGET DROPPED"),
         ("720/9", "INDIA'S RECORD TEST TOTAL"),
         ("50", "WEMBANYAMA PTS, 19 REB")]
for i, (n, lab) in enumerate(stats):
    x0 = 8 + i * 168
    center(d, x0 + 84, 103, n, F["stat_n"], RED if i in (0, 3) else INK)
    center(d, x0 + 84, 129, lab, F["stat_l"], GREY)
    if i:
        d.line([x0, 105, x0, 135], fill=GREY, width=1)
d.line([8, 138, 1016, 138], fill=INK, width=1)

# ---------------------------------------------------------------- region bar 138-158
regs = [("ASIA-PACIFIC", 12, (184, 120, 20)), ("MIDDLE EAST", 7, RED),
        ("AMERICAS", 5, (13, 100, 100)), ("GLOBAL", 4, NAVY),
        ("EUROPE", 3, (60, 90, 140)), ("AFRICA", 1, GREEN)]
rx = 8
for name, n, col in regs:
    label = f"{name} {n}"
    w = d.textlength(label, font=F["reg"]) + 22
    d.rectangle([rx, 140, rx + w, 156], fill=col)
    d.text((rx + 11, 143), label, font=F["reg"], fill=(255, 255, 255))
    rx += w + 4
d.text((rx + 4, 143), "ONE DAY  ·  ONE PAGE", font=F["reg"], fill=GREY)

# ---------------------------------------------------------------- timeline 158-178
d.rectangle([8, 160, 1016, 178], fill=INK)
tl = ("THE DAY IN UTC   01:00 HK POLLS OPEN   ·   03:00 COP31 OBJECTIONS CLOSE   ·   "
      "03:56 INDONESIA FIRE: 36 MISSING   ·   06:00 COP31 PLENARY DUE   ·   "
      "08:00 161 OF 186 DRONES DOWNED   ·   08:05 SPARTA II STILL BURNING")
f = F["time"]
while d.textlength(tl, font=f) > 1000 and f.size > 8:
    f = font(SANS_B, f.size - 1)
center(d, 512, 164, tl, f, (255, 255, 255))

# ---------------------------------------------------------------- leads 182-382
LY0, LH = 182, 200
LW = 330


def lead_card(x0, num, place, field, tag_text, tag_color, headline, body):
    d.rectangle([x0, LY0, x0 + LW, LY0 + LH], outline=INK, width=2)
    return x0


# --- lead 1: COP31 (illustration: conference table + globe + clock)
x0 = 8
lead_card(x0, 1, "", "", "", NAVY, "", "")
ix0, iy0, iw, ih = x0, LY0, LW, 88
d.rectangle([ix0, iy0, ix0 + iw, iy0 + ih], fill=(214, 232, 214))
d.rectangle([ix0 + 16, iy0 + 52, ix0 + 110, iy0 + 76], fill=(120, 90, 60))
d.rectangle([ix0 + 16, iy0 + 76, ix0 + 110, iy0 + 80], fill=(90, 65, 40))
for fx in (36, 62, 88):
    d.ellipse([ix0 + fx - 6, iy0 + 30, ix0 + fx + 6, iy0 + 42], fill=(200, 160, 120))
    d.rectangle([ix0 + fx - 7, iy0 + 42, ix0 + fx + 7, iy0 + 52],
                fill=(40, 70, 110) if fx != 62 else (150, 40, 40))
d.ellipse([ix0 + 200, iy0 + 12, ix0 + 260, iy0 + 72], fill=(90, 140, 190),
          outline=NAVY, width=2)
d.ellipse([ix0 + 214, iy0 + 24, ix0 + 232, iy0 + 40], fill=(120, 180, 120))
d.ellipse([ix0 + 236, iy0 + 44, ix0 + 250, iy0 + 60], fill=(120, 180, 120))
d.ellipse([ix0 + 286, iy0 + 14, ix0 + 316, iy0 + 44], fill=(255, 255, 255),
          outline=INK, width=2)
d.line([ix0 + 301, iy0 + 29, ix0 + 301, iy0 + 19], fill=INK, width=2)
d.line([ix0 + 301, iy0 + 29, ix0 + 309, iy0 + 29], fill=INK, width=2)
d.text((ix0 + 124, iy0 + 8), "COP31", font=font(SANS_B, 16), fill=NAVY)
d.text((ix0 + 124, iy0 + 28), "ANTALYA", font=F["cap_b"], fill=INK)
d.text((x0 + 8, LY0 + 94), "1  ·  ANTALYA, TÜRKIYE  ·  CLIMATE", font=F["lead_s"],
       fill=INK)
tag(d, x0 + LW - 118, LY0 + 93, "ADOPTION PENDING", AMBER)
for j, ln in enumerate(wrap(d, "COP31's final text lands with no mention of fossil fuels",
                            F["lead"], LW - 16)):
    d.text((x0 + 8, LY0 + 110 + j * 20), ln, font=F["lead"], fill=INK)
body1 = ("Ten-page package drops the $120bn adaptation target, keeps a 35% "
         "electricity goal for 2035, and is the first COP text to admit 1.5°C "
         "will be missed. Plenary delayed; adoption pending. (Reuters, BBC)")
for j, ln in enumerate(wrap(d, body1, F["lead_b"], LW - 16)):
    d.text((x0 + 8, LY0 + 150 + j * 12), ln, font=F["lead_b"], fill=INK)

# --- lead 2: Bahrain claim (illustration: night radar + streaks + fire)
x0 = 346
lead_card(x0, 2, "", "", "", NAVY, "", "")
ix0, iy0, iw, ih = x0, LY0, LW, 88
d.rectangle([ix0, iy0, ix0 + iw, iy0 + ih], fill=(16, 24, 44))
for sx, sy in [(30, 18), (90, 10), (150, 22), (210, 12), (270, 20)]:
    d.ellipse([ix0 + sx, iy0 + sy, ix0 + sx + 3, iy0 + sy + 3],
              fill=(255, 255, 255))
d.rectangle([ix0 + 20, iy0 + 56, ix0 + 60, iy0 + 88], fill=(60, 70, 90))
d.arc([ix0 + 22, iy0 + 30, ix0 + 58, iy0 + 66], 180, 360, fill=(200, 200, 200),
      width=3)
d.rectangle([ix0 + 90, iy0 + 60, ix0 + 130, iy0 + 88], fill=(60, 70, 90))
d.arc([ix0 + 92, iy0 + 34, ix0 + 128, iy0 + 70], 180, 360, fill=(200, 200, 200),
      width=3)
for mx, my in [(170, 20), (220, 30), (260, 14)]:
    d.line([ix0 + mx, iy0 + my + 18, ix0 + mx + 16, iy0 + my], fill=GOLD, width=3)
    d.ellipse([ix0 + mx + 13, iy0 + my - 3, ix0 + mx + 19, iy0 + my + 3],
              fill=GOLD)
d.polygon([(ix0 + 290, iy0 + 88), (ix0 + 302, iy0 + 52), (ix0 + 314, iy0 + 88)],
          fill=GOLD)
d.polygon([(ix0 + 296, iy0 + 88), (ix0 + 302, iy0 + 66), (ix0 + 308, iy0 + 88)],
          fill=RED)
d.text((x0 + 8, LY0 + 94), "2  ·  MANAMA, BAHRAIN  ·  IRAN", font=F["lead_s"],
       fill=INK)
tag(d, x0 + LW - 52, LY0 + 93, "CLAIM", RED)
for j, ln in enumerate(wrap(d, "Iran claims two US radars hit; Bahrain denies it",
                            F["lead"], LW - 16)):
    d.text((x0 + 8, LY0 + 110 + j * 20), ln, font=F["lead"], fill=INK)
body2 = ("IRGC says it struck Patriot radars at al-Riffa and Awali on Saturday "
         "night. Bahrain says its defences intercepted the attack; a civilian "
         "site burned, no injuries. (IRNA, Bahrain Interior Ministry)")
for j, ln in enumerate(wrap(d, body2, F["lead_b"], LW - 16)):
    d.text((x0 + 8, LY0 + 150 + j * 12), ln, font=F["lead_b"], fill=INK)

# --- lead 3: 186 drones / Kyiv (illustration: night skyline + drones)
x0 = 684
lead_card(x0, 3, "", "", "", NAVY, "", "")
ix0, iy0, iw, ih = x0, LY0, LW, 88
d.rectangle([ix0, iy0, ix0 + iw, iy0 + ih], fill=(20, 28, 48))
d.ellipse([ix0 + 286, iy0 + 8, ix0 + 310, iy0 + 32], fill=(230, 230, 210))
for bx, bw, bh in [(10, 44, 46), (62, 36, 60), (106, 48, 40), (162, 40, 54),
                   (210, 44, 44), (262, 40, 58)]:
    d.rectangle([ix0 + bx, iy0 + 88 - bh, ix0 + bx + bw, iy0 + 88],
                fill=(50, 60, 85))
    for wy in range(iy0 + 88 - bh + 6, iy0 + 84, 12):
        for wx in range(ix0 + bx + 6, ix0 + bx + bw - 6, 12):
            d.rectangle([wx, wy, wx + 5, wy + 6], fill=(255, 220, 120))
for dx_, dy_ in [(40, 14), (120, 8), (190, 18), (250, 10)]:
    d.line([ix0 + dx_, iy0 + dy_ + 10, ix0 + dx_ + 12, iy0 + dy_], fill=RED,
           width=2)
    d.ellipse([ix0 + dx_ + 10, iy0 + dy_ - 2, ix0 + dx_ + 15, iy0 + dy_ + 3],
              fill=RED)
d.polygon([(ix0 + 106, iy0 + 48), (ix0 + 118, iy0 + 22), (ix0 + 130, iy0 + 48)],
          fill=GOLD)
d.text((x0 + 8, LY0 + 94), "3  ·  KYIV REGION, UKRAINE  ·  WAR", font=F["lead_s"],
       fill=INK)
tag(d, x0 + LW - 74, LY0 + 93, "REPORTED", GREEN)
for j, ln in enumerate(wrap(d, "Russia fires 186 drones; a Kyiv-region block is destroyed",
                            F["lead"], LW - 16)):
    d.text((x0 + 8, LY0 + 110 + j * 20), ln, font=F["lead"], fill=INK)
body3 = ("Air defences downed or suppressed 161 of 186 strike drones, 72 of "
         "them jet-powered. One destroyed a five-storey block: 14 feared "
         "trapped, two injured, nine evacuated. (Ukrainian Air Force, Reuters)")
for j, ln in enumerate(wrap(d, body3, F["lead_b"], LW - 16)):
    d.text((x0 + 8, LY0 + 150 + j * 12), ln, font=F["lead_b"], fill=INK)

# ---------------------------------------------------------------- secondary cards 386-598
cards = [
    ("Hong Kong elects its Election Committee",
     "856 candidates, 723 seats;", "record 98.79% turnout (govt)", "vote"),
    ("India declare on 720/9, a record in NZ",
     "Pant 128, Rahul 136; hosts 119/2,", "trailing by 233 (ESPNcricinfo)", "cricket"),
    ("Verstappen takes the Las Vegas GP",
     "Beats Norris by 0.639s;", "Piastri third (Reuters, F1)", "f1"),
    ("Iran begins rationing electricity",
     "Rolling cuts up to two hours a day", "as war damage bites (RFE/RL)", "power"),
    ("Candy-factory fire in Cikande",
     "3 dead, 36 missing; search goes", "on at the Milkita plant (Reuters)", "fire"),
    ("S. Korea's education minister resigns",
     "Over AI exam-cheating fiasco;", "president accepts in an hour", "exam"),
    ("Nepal PM Shah lands in Delhi",
     "First state visit; talks with Modi", "on Monday (IANS)", "flags"),
    ("Adnoc shuttles oil past Iran",
     "Night convoys under US protection;", "11 crew hurt, 1 missing (WSJ)", "tanker"),
    ("OpenRouter drops 3 providers",
     "After canary-token research", "exposed data leaks (THN)", "chip"),
    ("Russian ship still burning off Finland",
     "Sparta II hit Saturday; 16 crew", "safe, fire fought overnight (Reuters)", "ship"),
    ("Wembanyama scores 50 as Spurs roll on",
     "50 pts, 19 rebounds, 5 blocks;", "114-91 over Pelicans (AP)", "ball"),
    ("Pope shares lunch with 1,300 poor",
     "World Day of the Poor; 106 tables", "in Paul VI Hall (Vatican)", "table"),
]
CW, CH, GAP = 163, 106, 6
for idx, (h, c1, c2, kind) in enumerate(cards):
    col, row = idx % 6, idx // 6
    x0 = 8 + col * (CW + GAP)
    y0 = 386 + row * (CH + GAP)
    d.rectangle([x0, y0, x0 + CW, y0 + CH], outline=INK, width=1)
    d.rectangle([x0, y0, x0 + CW, y0 + 50], fill=SKY)
    ix, iy = x0 + 8, y0 + 6
    if kind == "vote":
        d.rectangle([ix + 44, iy + 12, ix + 104, iy + 42], fill=(255, 255, 255),
                    outline=NAVY, width=2)
        d.line([ix + 58, iy + 12, ix + 72, iy + 4, ix + 92, iy + 4], fill=RED,
               width=3)
        d.line([ix + 58, iy + 28, ix + 68, iy + 36, ix + 90, iy + 16], fill=GREEN,
               width=3)
        d.text((ix + 6, iy + 8), "856", font=font(SANS_B, 16), fill=NAVY)
        d.text((ix + 108, iy + 26), "723", font=font(SANS_B, 12), fill=NAVY)
    elif kind == "cricket":
        d.rectangle([ix, iy + 26, ix + 147, iy + 44], fill=(120, 180, 100))
        d.line([ix + 10, iy + 14, ix + 60, iy + 14], fill=(150, 110, 70), width=6)
        d.line([ix + 60, iy + 14, ix + 74, iy + 26], fill=(150, 110, 70), width=5)
        d.ellipse([ix + 96, iy + 6, ix + 108, iy + 18], fill=RED)
        for sx in (118, 126, 134):
            d.line([ix + sx, iy + 24, ix + sx, iy + 38], fill=GOLD, width=3)
        d.text((ix + 6, iy + 28), "720/9", font=font(SANS_B, 13), fill=(255, 255, 255))
    elif kind == "f1":
        d.rectangle([ix + 14, iy + 22, ix + 128, iy + 36], fill=RED)
        d.rectangle([ix + 52, iy + 12, ix + 84, iy + 22], fill=RED)
        d.ellipse([ix + 26, iy + 30, ix + 42, iy + 46], fill=INK)
        d.ellipse([ix + 96, iy + 30, ix + 112, iy + 46], fill=INK)
        for cx in range(0, 24, 8):
            for cy in range(0, 16, 8):
                if (cx + cy) % 16 == 0:
                    d.rectangle([ix + 120 + cx, iy + 2 + cy, ix + 128 + cx,
                                 iy + 10 + cy], fill=INK)
        d.line([ix + 4, iy + 44, ix + 144, iy + 44], fill=GREY, width=1)
    elif kind == "power":
        d.ellipse([ix + 56, iy + 2, ix + 92, iy + 38], fill=(255, 230, 130),
                  outline=INK, width=2)
        d.rectangle([ix + 66, iy + 38, ix + 82, iy + 46], fill=GREY)
        d.line([ix + 62, iy + 18, ix + 86, iy + 18], fill=INK, width=2)
        d.line([ix + 74, iy + 6, ix + 74, iy + 30], fill=INK, width=2)
        d.text((ix + 8, iy + 12), "2h", font=font(SANS_B, 18), fill=NAVY)
        d.text((ix + 100, iy + 28), "DAY", font=F["cap_b"], fill=INK)
    elif kind == "fire":
        d.rectangle([ix + 10, iy + 20, ix + 70, iy + 44], fill=NAVY)
        d.rectangle([ix + 80, iy + 10, ix + 88, iy + 44], fill=NAVY)
        d.rectangle([ix + 96, iy + 14, ix + 104, iy + 44], fill=NAVY)
        d.polygon([(ix + 116, iy + 44), (ix + 126, iy + 16), (ix + 136, iy + 44)],
                  fill=GOLD)
        d.polygon([(ix + 122, iy + 44), (ix + 128, iy + 28), (ix + 134, iy + 44)],
                  fill=RED)
    elif kind == "exam":
        d.rectangle([ix + 50, iy + 4, ix + 100, iy + 42], fill=(255, 255, 255),
                    outline=INK, width=1)
        for ly in (12, 20, 28):
            d.line([ix + 56, iy + ly, ix + 94, iy + ly], fill=GREY, width=2)
        d.line([ix + 56, iy + 36, ix + 76, iy + 36], fill=RED, width=2)
        d.ellipse([ix + 108, iy + 8, ix + 132, iy + 32], outline=NAVY, width=3)
        d.line([ix + 128, iy + 28, ix + 142, iy + 42], fill=NAVY, width=3)
        d.text((ix + 6, iy + 10), "AI", font=font(SANS_B, 20), fill=RED)
    elif kind == "flags":
        d.rectangle([ix + 6, iy + 8, ix + 66, iy + 40], fill=(220, 40, 60))
        d.polygon([(ix + 6, iy + 8), (ix + 66, iy + 8), (ix + 6, iy + 24)],
                  fill=(200, 30, 50))
        d.polygon([(ix + 6, iy + 24), (ix + 48, iy + 24), (ix + 6, iy + 40)],
                  fill=(200, 30, 50))
        d.rectangle([ix + 82, iy + 8, ix + 142, iy + 18], fill=(255, 153, 51))
        d.rectangle([ix + 82, iy + 18, ix + 142, iy + 29], fill=(255, 255, 255))
        d.rectangle([ix + 82, iy + 29, ix + 142, iy + 40], fill=(19, 136, 8))
        d.ellipse([ix + 106, iy + 20, ix + 118, iy + 27], outline=NAVY, width=2)
    elif kind == "tanker":
        d.rectangle([ix, iy + 26, ix + 147, iy + 44], fill=OCEAN)
        d.polygon([(ix + 16, iy + 26), (ix + 130, iy + 26), (ix + 120, iy + 40),
                   (ix + 26, iy + 40)], fill=(40, 40, 40))
        d.rectangle([ix + 92, iy + 12, ix + 112, iy + 26], fill=(40, 40, 40))
        d.ellipse([ix + 20, iy + 4, ix + 34, iy + 18], fill=(255, 240, 180))
        for wx in range(6, 140, 22):
            d.arc([ix + wx, iy + 34, ix + wx + 18, iy + 44], 180, 360,
                  fill=NAVY, width=2)
    elif kind == "chip":
        d.rectangle([ix + 52, iy + 8, ix + 96, iy + 40], fill=NAVY)
        d.rectangle([ix + 62, iy + 18, ix + 86, iy + 30], fill=(255, 255, 255))
        for px in (60, 72, 84):
            d.line([ix + px, iy + 2, ix + px, iy + 8], fill=INK, width=2)
            d.line([ix + px, iy + 40, ix + px, iy + 46], fill=INK, width=2)
        d.text((ix + 6, iy + 12), "3", font=font(SANS_B, 22), fill=RED)
        d.text((ix + 104, iy + 12), "OUT", font=F["cap_b"], fill=RED)
    elif kind == "ship":
        d.rectangle([ix, iy + 26, ix + 147, iy + 44], fill=OCEAN)
        d.polygon([(ix + 16, iy + 26), (ix + 130, iy + 26), (ix + 120, iy + 40),
                   (ix + 26, iy + 40)], fill=(90, 60, 40))
        d.rectangle([ix + 92, iy + 12, ix + 112, iy + 26], fill=(90, 60, 40))
        d.polygon([(ix + 30, iy + 26), (ix + 38, iy + 8), (ix + 46, iy + 26)],
                  fill=GOLD)
        d.polygon([(ix + 34, iy + 26), (ix + 38, iy + 16), (ix + 42, iy + 26)],
                  fill=RED)
        d.ellipse([ix + 60, iy + 2, ix + 68, iy + 10], fill=(120, 120, 120))
        d.ellipse([ix + 76, iy + 6, ix + 84, iy + 14], fill=(120, 120, 120))
    elif kind == "ball":
        d.ellipse([ix + 52, iy + 2, ix + 96, iy + 46], fill=(230, 120, 50),
                  outline=(160, 70, 20), width=2)
        d.arc([ix + 52, iy + 2, ix + 96, iy + 46], 300, 60, fill=(160, 70, 20),
              width=2)
        d.line([ix + 52, iy + 24, ix + 96, iy + 24], fill=(160, 70, 20), width=2)
        d.line([ix + 74, iy + 2, ix + 74, iy + 46], fill=(160, 70, 20), width=2)
        d.text((ix + 6, iy + 10), "50", font=font(SANS_B, 20), fill=NAVY)
        d.text((ix + 104, iy + 26), "19 REB", font=F["cap_b"], fill=INK)
    elif kind == "table":
        d.rectangle([ix + 20, iy + 24, ix + 128, iy + 30], fill=(150, 110, 70))
        d.rectangle([ix + 28, iy + 30, ix + 34, iy + 44], fill=(120, 85, 50))
        d.rectangle([ix + 114, iy + 30, ix + 120, iy + 44], fill=(120, 85, 50))
        for px in (36, 62, 88, 112):
            d.ellipse([ix + px - 5, iy + 16, ix + px + 5, iy + 24],
                      fill=(255, 255, 255), outline=GREY, width=1)
        d.ellipse([ix + 66, iy + 2, ix + 82, iy + 14], fill=(255, 255, 255),
                  outline=GREY, width=1)
        d.text((ix + 4, iy + 30), "1,300", font=font(SANS_B, 11), fill=NAVY)
    d.text((x0 + 5, y0 + 51), f"{idx + 4:02d}", font=F["cap_b"], fill=RED)
    for j, ln in enumerate(wrap(d, h, F["card_h"], CW - 10)[:2]):
        d.text((x0 + 5, y0 + 62 + j * 11), ln, font=F["card_h"], fill=INK)
    d.text((x0 + 5, y0 + 85), c1, font=F["card_c"], fill=GREY)
    d.text((x0 + 5, y0 + 95), c2, font=F["card_c"], fill=GREY)

# ---------------------------------------------------------------- map + date check 602-790
MX0, MX1, MY0, MY1 = 8, 520, 602, 790
d.rectangle([MX0, MY0, MX1, MY1], outline=INK, width=2)
d.text((MX0 + 8, MY0 + 5), "WHERE IT HAPPENED", font=F["sect"], fill=INK)
d.text((MX1 - 150, MY0 + 7), "pins = story numbers", font=F["cap"], fill=GREY)
MAPX0, MAPY0, MAPW, MAPH = MX0 + 8, MY0 + 24, MX1 - MX0 - 16, 136
d.rectangle([MAPX0, MAPY0, MAPX0 + MAPW, MAPY0 + MAPH], fill=OCEAN)


def proj(lon, lat):
    return (MAPX0 + (lon + 180) / 360 * MAPW,
            MAPY0 + (90 - lat) / 180 * MAPH)


CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 80),
     (-80, 73), (-70, 62), (-60, 52), (-55, 47), (-65, 44), (-70, 42),
     (-75, 35), (-80, 32), (-81, 25), (-90, 21), (-97, 16), (-94, 17),
     (-86, 15), (-83, 9), (-79, 9), (-85, 13), (-92, 15), (-97, 16),
     (-105, 20), (-110, 23), (-114, 29), (-120, 34), (-124, 40), (-124, 48),
     (-130, 55), (-140, 60), (-155, 58), (-165, 60)],
    [(-79, 9), (-72, 12), (-64, 10), (-55, 6), (-50, 0), (-44, -3), (-35, -8),
     (-38, -15), (-40, -22), (-48, -28), (-52, -33), (-58, -38), (-62, -41),
     (-65, -45), (-68, -50), (-68, -55), (-72, -54), (-73, -45), (-73, -37),
     (-71, -30), (-70, -20), (-75, -15), (-79, -8), (-81, -3), (-80, 1)],
    [(-17, 15), (-10, 6), (-8, 4), (0, 6), (6, 4), (9, -1), (13, -12),
     (12, -18), (16, -28), (20, -35), (28, -33), (32, -29), (35, -23),
     (40, -15), (41, -10), (46, -11), (51, 11), (44, 11), (40, 15), (38, 18),
     (35, 20), (32, 31), (30, 31), (20, 32), (11, 34), (10, 37), (0, 36),
     (-6, 35), (-10, 31), (-15, 27), (-17, 21)],
    [(-10, 36), (-9, 43), (-2, 48), (-4, 50), (0, 53), (5, 58), (10, 58),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 70), (40, 68), (50, 69),
     (60, 69), (70, 72), (80, 73), (90, 75), (100, 77), (110, 74), (120, 73),
     (130, 72), (140, 72), (150, 70), (160, 70), (170, 67), (178, 65),
     (178, 62), (170, 60), (162, 56), (156, 51), (150, 45), (142, 42),
     (140, 35), (135, 34), (130, 33), (127, 35), (122, 38), (120, 32),
     (122, 28), (118, 25), (110, 20), (108, 12), (105, 9), (103, 1), (100, 7),
     (98, 12), (95, 16), (92, 21), (88, 22), (85, 19), (80, 15), (77, 8),
     (75, 12), (72, 20), (68, 23), (66, 25), (62, 25), (58, 26), (56, 27),
     (52, 26), (50, 29), (48, 30), (44, 29), (40, 31), (36, 36), (30, 36),
     (27, 37), (23, 36), (19, 40), (16, 42), (12, 44), (8, 44), (3, 43),
     (-2, 37), (-6, 36)],
    [(114, -22), (114, -30), (118, -35), (124, -33), (129, -32), (132, -32),
     (135, -35), (138, -35), (140, -38), (145, -38), (147, -42), (150, -37),
     (153, -30), (153, -27), (146, -19), (142, -15), (142, -11), (137, -12),
     (135, -15), (132, -12), (129, -15), (126, -14), (122, -17), (118, -20)],
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (1, 52), (1, 51), (-3, 50)],
    [(130, 31), (133, 34), (137, 35), (140, 36), (141, 40), (143, 43),
     (145, 44), (142, 44), (140, 40), (138, 37), (135, 34), (132, 33)],
    [(167, -45), (170, -42), (173, -39), (175, -37), (178, -38), (175, -41),
     (172, -43), (169, -46)],
]
for poly in CONTINENTS:
    d.polygon([proj(lon, lat) for lon, lat in poly], fill=LAND,
              outline=LANDLINE)

# pins: (num, lon, lat, label dx, dy)
PINS = [
    ("13", 28.5, 59.8, -30, -14),
    ("3", 30.5, 50.5, 8, 8),
    ("15", 12.5, 41.9, -32, -14),
    ("1", 30.7, 36.9, -34, 10),
    ("10", 77.2, 28.6, -34, -16),
    ("2·7·11", 53.0, 30.0, 8, 10),
    ("9", 127.0, 37.5, 8, -14),
    ("4", 114.2, 22.3, 8, 8),
    ("8", 106.3, -6.1, -40, 8),
    ("5", 174.8, -41.3, -36, -14),
    ("6", -115.1, 36.2, 8, -14),
    ("14", -98.5, 29.4, -30, 10),
]
for num, lon, lat, dx, dy in PINS:
    px, py = proj(lon, lat)
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED, outline=(255, 255, 255))
    lx, ly = px + dx, py + dy
    w = d.textlength(num, font=F["pin"]) + 6
    d.line([px, py, lx + w / 2, ly + 6], fill=RED, width=1)
    d.rectangle([lx, ly, lx + w, ly + 12], fill=(255, 255, 255),
                outline=RED, width=1)
    d.text((lx + 3, ly + 1.5), num, font=F["pin"], fill=RED)
d.text((MAPX0, MY0 + 164),
       "No pin: 12 OpenRouter (global) · 16-32 listed at right.",
       font=F["cap"], fill=GREY)

# DATE CHECK (right)
DX0, DX1, DY0, DY1 = 528, 1016, 602, 790
d.rectangle([DX0, DY0, DX1, DY1], outline=INK, width=2)
d.text((DX0 + 8, DY0 + 5), "DATE CHECK — WHAT COUNTS AS 22 NOVEMBER",
       font=F["sect"], fill=INK)
dc_rows = [
    (RED, "LEFT OUT — OTHER DAYS' NEWS",
     "Peru M6.7 quake (Fri 20 Nov) · 'El Chapo Isidro' captured (Fri) · "
     "EU–Indonesia pact signed (Sat) · BepiColombo Mercury orbit (Sat) · "
     "FBI crime-database hack (Fri)"),
    (GREEN, "INCLUDED — 22 NOV 2026",
     "COP31 text released · 186-drone night · Bahrain claim vs denial · "
     "Sparta II still burning (Sunday update) · Wembanyama 50 "
     "(Sat night US = Sun UTC)"),
    (AMBER, "NOT YET DECIDED AT PRESS TIME",
     "COP31 adoption · ATP Finals final, Alcaraz v Zverev · "
     "Liverpool v Man Utd"),
]
y = DY0 + 25
for color, head, text in dc_rows:
    d.rectangle([DX0 + 8, y + 2, DX0 + 18, y + 12], fill=color)
    d.text((DX0 + 22, y), head, font=F["dc_b"], fill=color)
    y += 15
    for ln in wrap(d, text, F["dc"], DX1 - DX0 - 36):
        d.text((DX0 + 22, y), ln, font=F["dc"], fill=INK)
        y += 12
    y += 6
d.text((DX0 + 8, DY1 - 16), "Sources read to ~11:00 UTC, Sun 22 Nov 2026.",
       font=F["cap"], fill=GREY)

# ---------------------------------------------------------------- ALSO list 794-978
d.text((8, 796), "ALSO ON SUNDAY 22 NOVEMBER — 17 MORE STORIES",
       font=F["sect"], fill=INK)
d.line([8, 814, 1016, 814], fill=INK, width=1)
also = [
    "India–China hold 2nd Corps Commander talks in Arunachal",
    "Houthi missile intercepted near Mecca — coalition claim",
    "M5.6 quake off Sarangani, Philippines; no damage",
    "Kansas City Current win first NWSL title, 2–1",
    "Two Palestinians die of wounds from al-Mawasi strike",
    "IRGC chief: Iran's airspace is a 'red line'",
    "Indian poet Rajendra Shukla dies, 84",
    "COP31: $120bn adaptation target dropped from text",
    "Pant 128, Rahul 136 — six 70+ scores in one innings",
    "Thailand to block chemical exports for Myanmar mining",
    "ICE arrests two travellers at Seattle airport",
    "Nigeria boat toll rises to 24 (Friday capsize)",
    "Pakistan: 15 militants killed in Mastung operations",
    "Ghostscript 'Upload2Shell' flaw; Debian 12 exposed",
    "Hamas seeks urgent mediator talks after aid strike",
    "BJP MP Ramrao Wadkute dies at the weekend, 72",
    "Bedard to have shoulder surgery; MacKinnon out 12 weeks",
]
for i, item in enumerate(also):
    col, row = i % 3, i // 3
    x0 = 8 + col * 336
    y0 = 820 + row * 27
    d.text((x0, y0), f"{i + 16:02d}", font=F["list_b"], fill=RED)
    for j, ln in enumerate(wrap(d, item, F["list"], 306)[:2]):
        d.text((x0 + 26, y0 + j * 12), ln, font=F["list"], fill=INK)

# ---------------------------------------------------------------- footer 982-1024
d.line([8, 984, 1016, 984], fill=INK, width=2)
d.text((8, 990),
       "Sources: Reuters · BBC · AP · AFP · The Guardian · ESPNcricinfo · WSJ · RFE/RL · Vatican News · official statements",
       font=F["foot"], fill=GREY)
d.text((8, 1002),
       "32 stories verified against sources dated 22 Nov 2026. Scenes are drawn illustrations of reported events, not photographs.",
       font=F["foot"], fill=GREY)
r1 = "REPORTED = carried by the day's wires   CLAIM = one side's account, labelled"
d.text((1014 - d.textlength(r1, font=F["foot"]), 990), r1, font=F["foot"],
       fill=GREY)
r2 = "ADOPTION PENDING = text released, not yet adopted"
d.text((1014 - d.textlength(r2, font=F["foot"]), 1002), r2, font=F["foot"],
       fill=GREY)

img.save("entry.png", format="PNG")
print("saved entry.png")
