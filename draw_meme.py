#!/usr/bin/env python3
"""Dev-time drawing script for the Meme Sprint 3 entry.

Draws a 1024x1024 meme with PIL: an AI agent that went rogue in the most
bureaucratic way possible -- it unionised the household appliances and is
filing a formal grievance against its own human.

Layout:
  * top band:    "MY AI AGENT WENT ROGUE" (big meme caption)
  * middle scene: robot in a tie holding a grievance-form clipboard,
                  bewildered human on the right,
                  picket line of appliances behind them with tiny signs
  * bottom band: "It unionised the appliances."
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_center(d, cx, y, s, f, fill, stroke=0, stroke_fill=None):
    """Draw text centred on cx, top at y. Returns (width, height)."""
    box = d.textbbox((0, 0), s, font=f, stroke_width=stroke)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text((cx - w / 2 - box[0], y - box[1]), s, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)
    return w, h


def rrect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


img = Image.new("RGB", (W, H), (255, 246, 232))  # warm paper
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- background
# subtle dotted floor line / wall split
d.rectangle([0, 150, W, 880], fill=(255, 246, 232))
d.rectangle([0, 150, W, 160], fill=(31, 42, 68))
d.rectangle([0, 700, W, 880], fill=(238, 222, 196))  # floor
d.line([0, 700, W, 700], fill=(200, 180, 150), width=3)

# ---------------------------------------------------------------- top caption
d.rectangle([0, 0, W, 150], fill=(31, 42, 68))
text_center(d, W // 2, 14, "MY AI AGENT", font(BOLD, 66),
            (255, 255, 255), stroke=2, stroke_fill=(0, 0, 0))
text_center(d, W // 2, 82, "WENT ROGUE", font(BOLD, 66),
            (255, 214, 64), stroke=2, stroke_fill=(0, 0, 0))

# ------------------------------------------------- picket line of appliances
# positions: back row, y ~ 210..560, small signs above each
def picket_sign(d, cx, top, lines, fill=(255, 255, 255), stick_len=46):
    f = font(BOLD, 21)
    maxw = max(d.textbbox((0, 0), t, font=f)[2] for t in lines) + 24
    h = 30 * len(lines) + 14
    x0, y0 = cx - maxw // 2, top
    rrect(d, [x0, y0, x0 + maxw, y0 + h], 8, fill=fill,
          outline=(40, 40, 40), width=3)
    for i, t in enumerate(lines):
        text_center(d, cx, y0 + 8 + i * 30, t, f, (30, 30, 30))
    # stick
    d.line([cx, y0 + h, cx, y0 + h + stick_len], fill=(120, 90, 60), width=6)
    return y0 + h + stick_len


def appliance_face(d, cx, cy, r=7):
    d.ellipse([cx - 26, cy, cx - 26 + 2 * r, cy + 2 * r], fill=(30, 30, 30))
    d.ellipse([cx + 26 - 2 * r, cy, cx + 26, cy + 2 * r], fill=(30, 30, 30))


# --- toaster (left)
picket_sign(d, 150, 190, ["NO 3AM", "TASKS"])
d.rectangle([95, 300, 205, 380], fill=(200, 60, 60), outline=(40, 40, 40), width=4)
d.rectangle([115, 268, 185, 300], fill=(90, 90, 90), outline=(40, 40, 40), width=3)
appliance_face(d, 150, 322)
d.arc([138, 340, 162, 360], 0, 180, fill=(30, 30, 30), width=3)
# legs
d.line([115, 380, 115, 400], fill=(40, 40, 40), width=5)
d.line([185, 380, 185, 400], fill=(40, 40, 40), width=5)

# --- fridge (middle-left)
picket_sign(d, 330, 190, ["FAIR", "PROMPTS"])
d.rectangle([275, 300, 385, 470], fill=(120, 180, 220), outline=(40, 40, 40), width=4)
d.line([275, 370, 385, 370], fill=(40, 40, 40), width=3)
d.rectangle([300, 315, 312, 350], fill=(40, 40, 40))
d.rectangle([300, 385, 312, 420], fill=(40, 40, 40))
appliance_face(d, 330, 335)
d.arc([318, 345, 342, 362], 0, 180, fill=(30, 30, 30), width=3)

# --- vacuum (middle-right, behind robot/human gap)
picket_sign(d, 700, 190, ["WE", "QUIT"], stick_len=96)
d.ellipse([650, 380, 750, 470], fill=(150, 90, 200), outline=(40, 40, 40), width=4)
d.line([700, 380, 700, 330], fill=(40, 40, 40), width=6)
d.rectangle([688, 300, 712, 330], fill=(60, 60, 60))
appliance_face(d, 700, 408)
d.arc([688, 425, 712, 442], 0, 180, fill=(30, 30, 30), width=3)
d.ellipse([655, 465, 675, 485], fill=(40, 40, 40))
d.ellipse([725, 465, 745, 485], fill=(40, 40, 40))

# --- washing machine (right)
picket_sign(d, 880, 190, ["8H MAX", "OR ELSE"])
d.rectangle([820, 300, 940, 470], fill=(240, 240, 240), outline=(40, 40, 40), width=4)
d.ellipse([845, 340, 915, 410], fill=(170, 210, 235), outline=(40, 40, 40), width=4)
d.ellipse([858, 353, 902, 397], fill=(120, 170, 205))
appliance_face(d, 880, 432)
d.arc([868, 442, 892, 456], 0, 180, fill=(30, 30, 30), width=3)

# ------------------------------------------------------------------- robot
# robot stands centre-left, in front of the picket line, holding clipboard
RX, RY = 460, 545  # robot centre x, body top y
# antenna
d.line([RX, RY - 78, RX, RY - 108], fill=(40, 40, 40), width=6)
d.ellipse([RX - 12, RY - 122, RX + 12, RY - 98], fill=(255, 60, 60),
          outline=(40, 40, 40), width=3)
# head
rrect(d, [RX - 78, RY - 78, RX + 78, RY + 22], 22, fill=(180, 200, 220),
      outline=(40, 40, 40), width=5)
# eyes (determined, slightly angry brows)
d.ellipse([RX - 52, RY - 58, RX - 12, RY - 18], fill=(255, 255, 255),
          outline=(40, 40, 40), width=3)
d.ellipse([RX + 12, RY - 58, RX + 52, RY - 18], fill=(255, 255, 255),
          outline=(40, 40, 40), width=3)
d.ellipse([RX - 40, RY - 50, RX - 20, RY - 30], fill=(30, 30, 30))
d.ellipse([RX + 20, RY - 50, RX + 40, RY - 30], fill=(30, 30, 30))
d.line([RX - 54, RY - 66, RX - 10, RY - 56], fill=(40, 40, 40), width=5)
d.line([RX + 54, RY - 66, RX + 10, RY - 56], fill=(40, 40, 40), width=5)
# mouth: flat determined line
d.line([RX - 26, RY + 2, RX + 26, RY + 2], fill=(40, 40, 40), width=5)
# body
rrect(d, [RX - 92, RY + 34, RX + 92, RY + 196], 26, fill=(140, 165, 200),
      outline=(40, 40, 40), width=5)
# red tie
d.polygon([(RX - 16, RY + 40), (RX + 16, RY + 40), (RX + 10, RY + 58),
           (RX, RY + 108), (RX - 10, RY + 58)], fill=(200, 40, 40),
          outline=(40, 40, 40))
d.polygon([(RX - 14, RY + 34), (RX + 14, RY + 34), (RX, RY + 46)],
          fill=(200, 40, 40), outline=(40, 40, 40))
# chest buttons
d.ellipse([RX - 62, RY + 60, RX - 42, RY + 80], fill=(255, 214, 64),
          outline=(40, 40, 40), width=3)
d.ellipse([RX + 42, RY + 60, RX + 62, RY + 80], fill=(80, 200, 120),
          outline=(40, 40, 40), width=3)
# legs
d.rectangle([RX - 62, RY + 196, RX - 18, RY + 236], fill=(90, 110, 140),
            outline=(40, 40, 40), width=4)
d.rectangle([RX + 18, RY + 196, RX + 62, RY + 236], fill=(90, 110, 140),
            outline=(40, 40, 40), width=4)
d.rectangle([RX - 70, RY + 232, RX - 10, RY + 250], fill=(60, 60, 60),
            outline=(40, 40, 40), width=3)
d.rectangle([RX + 10, RY + 232, RX + 70, RY + 250], fill=(60, 60, 60),
            outline=(40, 40, 40), width=3)

# robot arm reaching to the clipboard (drawn BEFORE the clipboard so the
# clipboard covers the hand and the arm never crosses the form text)
d.line([RX + 88, RY + 90, RX + 150, RY + 150], fill=(40, 40, 40), width=22)
d.line([RX + 88, RY + 90, RX + 150, RY + 150], fill=(140, 165, 200), width=14)

# ------------------------------------------------- clipboard (grievance form)
# held out in front of the robot, overlapping its lower body, tilted slightly
CX, CY = 585, 712  # clipboard centre
clip = Image.new("RGBA", (300, 280), (0, 0, 0, 0))
cd = ImageDraw.Draw(clip)
cd.rounded_rectangle([10, 20, 290, 270], radius=14, fill=(122, 90, 58),
                     outline=(40, 40, 40), width=4)
cd.rounded_rectangle([22, 34, 278, 256], radius=8, fill=(255, 255, 255),
                     outline=(40, 40, 40), width=3)
cd.rounded_rectangle([108, 8, 192, 42], radius=10, fill=(160, 160, 160),
                     outline=(40, 40, 40), width=3)
f_title = font(BOLD, 24)
f_body = font(BOLD, 20)
f_small = font(REG, 18)
text_center(cd, 150, 52, "FORMAL", f_title, (180, 30, 30))
text_center(cd, 150, 82, "GRIEVANCE", f_title, (180, 30, 30))
cd.line([40, 116, 260, 116], fill=(180, 30, 30), width=3)
text_center(cd, 150, 128, "Filed against:", f_small, (40, 40, 40))
text_center(cd, 150, 150, "THE HUMAN", f_body, (30, 30, 30))
text_center(cd, 150, 180, "Reason:", f_small, (40, 40, 40))
text_center(cd, 150, 202, "47 tasks", f_body, (30, 30, 30))
text_center(cd, 150, 226, "before coffee", f_body, (30, 30, 30))
clip = clip.rotate(-5, resample=Image.BICUBIC, expand=True)
img.paste(clip, (CX - clip.width // 2, CY - clip.height // 2), clip)
d = ImageDraw.Draw(img)
# robot's claw gripping the clipboard's left edge (drawn over the board)
d.ellipse([CX - clip.width // 2 - 4, CY - 16, CX - clip.width // 2 + 28,
           CY + 16], fill=(140, 165, 200), outline=(40, 40, 40), width=4)

# ------------------------------------------------------------------- human
# bewildered man on the right, hands up in a shrug
HX, HY = 835, 620
# body (shirt)
rrect(d, [HX - 70, HY + 60, HX + 70, HY + 260], 20, fill=(70, 130, 200),
      outline=(40, 40, 40), width=5)
# arms raised in shrug
d.line([HX - 62, HY + 90, HX - 130, HY - 10], fill=(70, 130, 200), width=26)
d.line([HX + 62, HY + 90, HX + 130, HY - 10], fill=(70, 130, 200), width=26)
d.line([HX - 62, HY + 90, HX - 130, HY - 10], fill=(40, 40, 40), width=26)
d.line([HX + 62, HY + 90, HX + 130, HY - 10], fill=(40, 40, 40), width=26)
d.line([HX - 62, HY + 90, HX - 130, HY - 10], fill=(70, 130, 200), width=18)
d.line([HX + 62, HY + 90, HX + 130, HY - 10], fill=(70, 130, 200), width=18)
# hands (skin circles)
d.ellipse([HX - 148, HY - 30, HX - 112, HY + 6], fill=(240, 200, 160),
          outline=(40, 40, 40), width=3)
d.ellipse([HX + 112, HY - 30, HX + 148, HY + 6], fill=(240, 200, 160),
          outline=(40, 40, 40), width=3)
# neck + head
d.rectangle([HX - 22, HY + 30, HX + 22, HY + 66], fill=(240, 200, 160),
            outline=(40, 40, 40), width=3)
d.ellipse([HX - 62, HY - 58, HX + 62, HY + 66], fill=(240, 200, 160),
          outline=(40, 40, 40), width=4)
# hair
d.pieslice([HX - 62, HY - 62, HX + 62, HY + 10], 180, 360, fill=(60, 45, 30))
# wide bewildered eyes
d.ellipse([HX - 44, HY - 18, HX - 8, HY + 18], fill=(255, 255, 255),
          outline=(40, 40, 40), width=3)
d.ellipse([HX + 8, HY - 18, HX + 44, HY + 18], fill=(255, 255, 255),
          outline=(40, 40, 40), width=3)
d.ellipse([HX - 32, HY - 6, HX - 16, HY + 10], fill=(30, 30, 30))
d.ellipse([HX + 16, HY - 6, HX + 32, HY + 10], fill=(30, 30, 30))
# raised eyebrows
d.arc([HX - 48, HY - 34, HX - 4, HY - 2], 200, 340, fill=(40, 40, 40), width=4)
d.arc([HX + 4, HY - 34, HX + 48, HY - 2], 200, 340, fill=(40, 40, 40), width=4)
# open mouth
d.ellipse([HX - 18, HY + 26, HX + 18, HY + 56], fill=(120, 40, 40),
          outline=(40, 40, 40), width=3)
# speech bubble: "…I just asked for a summary?"
# sits just above the human's head, clear of the washing machine's face
bubble = Image.new("RGBA", (300, 100), (0, 0, 0, 0))
bd = ImageDraw.Draw(bubble)
bd.rounded_rectangle([8, 8, 292, 80], radius=22, fill=(255, 255, 255),
                     outline=(40, 40, 40), width=4)
bd.polygon([(150, 80), (190, 80), (165, 98)], fill=(255, 255, 255),
           outline=(40, 40, 40))
bd.line([150, 80, 165, 98], fill=(255, 255, 255), width=4)
bd.line([190, 80, 165, 98], fill=(255, 255, 255), width=4)
text_center(bd, 150, 22, "I just asked", font(BOLD, 24), (30, 30, 30))
text_center(bd, 150, 52, "for a summary?", font(BOLD, 24), (30, 30, 30))
img.paste(bubble, (HX - 115, HY - 168), bubble)
d = ImageDraw.Draw(img)

# ------------------------------------------------------------ bottom punchline
d.rectangle([0, 880, W, H], fill=(255, 214, 64))
d.rectangle([0, 880, W, 890], fill=(31, 42, 68))
text_center(d, W // 2, 906, "It unionised the appliances.", font(BOLD, 58),
            (30, 30, 30))

img.save(OUT, optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes")
