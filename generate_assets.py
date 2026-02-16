#!/usr/bin/env python3
"""Generate game assets for the bridge-building game."""
from PIL import Image, ImageDraw
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")


def generate_left_cliff():
    """Generate a left cliff PNG - rocky cliff on the left side."""
    w, h = 300, 400
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Main cliff body - earthy brown tones
    cliff_color = (139, 90, 43)
    cliff_dark = (101, 67, 33)
    cliff_highlight = (170, 120, 60)

    # Draw cliff shape - flat top, jagged right edge, solid left
    cliff_points = [
        (0, 50),      # top-left
        (250, 50),    # top-right (flat top)
        (260, 80),    # slight jag
        (240, 120),
        (255, 160),
        (245, 200),
        (260, 240),
        (250, 280),
        (255, 320),
        (245, 360),
        (250, h),     # bottom-right
        (0, h),       # bottom-left
    ]
    draw.polygon(cliff_points, fill=cliff_color)

    # Add darker edge detail on right side
    for i in range(len(cliff_points) - 3):
        p1 = cliff_points[i + 1]
        p2 = cliff_points[i + 2]
        draw.line([p1, p2], fill=cliff_dark, width=3)

    # Add horizontal rock layers
    for y in range(80, h, 40):
        draw.line([(10, y), (230, y)], fill=cliff_dark, width=1)

    # Add some highlight patches
    for y_off in [70, 150, 230, 310]:
        draw.ellipse([(30, y_off), (120, y_off + 25)], fill=cliff_highlight)

    # Green grass on top
    grass_color = (76, 153, 0)
    grass_dark = (51, 119, 0)
    grass_points = [
        (0, 50), (0, 35),
        (30, 40), (60, 30), (90, 38), (120, 28),
        (150, 35), (180, 25), (210, 33), (240, 30),
        (250, 45), (250, 50),
    ]
    draw.polygon(grass_points, fill=grass_color)

    # Grass tufts
    for x in range(10, 240, 20):
        draw.polygon([(x, 35), (x + 5, 15), (x + 10, 35)], fill=grass_dark)

    img.save(os.path.join(ASSETS_DIR, "left-cliff.png"))
    print("Generated left-cliff.png")


def generate_right_cliff():
    """Generate a right cliff PNG - mirror of left cliff."""
    w, h = 300, 400
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cliff_color = (139, 90, 43)
    cliff_dark = (101, 67, 33)
    cliff_highlight = (170, 120, 60)

    # Right cliff - jagged left edge, solid right
    cliff_points = [
        (w, 50),      # top-right
        (50, 50),     # top-left (flat top)
        (40, 80),
        (60, 120),
        (45, 160),
        (55, 200),
        (40, 240),
        (50, 280),
        (45, 320),
        (55, 360),
        (50, h),      # bottom-left
        (w, h),       # bottom-right
    ]
    draw.polygon(cliff_points, fill=cliff_color)

    for i in range(len(cliff_points) - 3):
        p1 = cliff_points[i + 1]
        p2 = cliff_points[i + 2]
        draw.line([p1, p2], fill=cliff_dark, width=3)

    for y in range(80, h, 40):
        draw.line([(70, y), (w - 10, y)], fill=cliff_dark, width=1)

    for y_off in [70, 150, 230, 310]:
        draw.ellipse([(180, y_off), (270, y_off + 25)], fill=cliff_highlight)

    # Green grass on top
    grass_color = (76, 153, 0)
    grass_dark = (51, 119, 0)
    grass_points = [
        (w, 50), (w, 35),
        (w - 30, 40), (w - 60, 30), (w - 90, 38), (w - 120, 28),
        (w - 150, 35), (w - 180, 25), (w - 210, 33), (w - 240, 30),
        (50, 45), (50, 50),
    ]
    draw.polygon(grass_points, fill=grass_color)

    for x in range(60, w - 10, 20):
        draw.polygon([(x, 35), (x + 5, 15), (x + 10, 35)], fill=grass_dark)

    img.save(os.path.join(ASSETS_DIR, "right-cliff.png"))
    print("Generated right-cliff.png")


def generate_character():
    """Generate a cute simple character."""
    w, h = 80, 100
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx = w // 2

    # Body - round and cute, soft blue
    body_color = (100, 149, 237)  # cornflower blue
    body_dark = (65, 105, 225)
    draw.ellipse([(cx - 20, 35), (cx + 20, 85)], fill=body_color, outline=body_dark, width=2)

    # Head - larger round head
    head_color = (255, 220, 185)  # skin tone
    draw.ellipse([(cx - 22, 5), (cx + 22, 50)], fill=head_color, outline=(200, 170, 140), width=2)

    # Eyes - big cute eyes
    eye_white = (255, 255, 255)
    eye_black = (30, 30, 30)
    # Left eye
    draw.ellipse([(cx - 15, 18), (cx - 5, 32)], fill=eye_white, outline=(100, 100, 100))
    draw.ellipse([(cx - 12, 22), (cx - 7, 30)], fill=eye_black)
    draw.ellipse([(cx - 11, 23), (cx - 9, 26)], fill=eye_white)  # shine
    # Right eye
    draw.ellipse([(cx + 5, 18), (cx + 15, 32)], fill=eye_white, outline=(100, 100, 100))
    draw.ellipse([(cx + 8, 22), (cx + 13, 30)], fill=eye_black)
    draw.ellipse([(cx + 9, 23), (cx + 11, 26)], fill=eye_white)  # shine

    # Small smile
    draw.arc([(cx - 8, 30), (cx + 8, 42)], start=10, end=170, fill=(200, 100, 100), width=2)

    # Rosy cheeks
    draw.ellipse([(cx - 20, 30), (cx - 12, 38)], fill=(255, 180, 180))
    draw.ellipse([(cx + 12, 30), (cx + 20, 38)], fill=(255, 180, 180))

    # Legs - simple stubs
    leg_color = body_dark
    draw.rectangle([(cx - 15, 78), (cx - 5, 95)], fill=leg_color, outline=(50, 80, 180))
    draw.rectangle([(cx + 5, 78), (cx + 15, 95)], fill=leg_color, outline=(50, 80, 180))

    # Shoes
    shoe_color = (180, 50, 50)
    draw.ellipse([(cx - 18, 88), (cx - 3, 100)], fill=shoe_color)
    draw.ellipse([(cx + 3, 88), (cx + 18, 100)], fill=shoe_color)

    # Hair - small tufts on top
    hair_color = (80, 50, 30)
    draw.polygon([(cx - 10, 10), (cx - 5, -2), (cx, 10)], fill=hair_color)
    draw.polygon([(cx - 2, 8), (cx + 3, -4), (cx + 8, 8)], fill=hair_color)
    draw.polygon([(cx + 5, 10), (cx + 10, 0), (cx + 15, 12)], fill=hair_color)

    img.save(os.path.join(ASSETS_DIR, "character.png"))
    print("Generated character.png")


def generate_plank():
    """Generate a wooden plank image."""
    w, h = 60, 20
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Wood plank - warm brown
    plank_color = (193, 154, 107)
    plank_dark = (160, 120, 80)
    plank_outline = (120, 85, 55)

    # Main plank body with rounded corners
    draw.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=3, fill=plank_color, outline=plank_outline, width=1)

    # Wood grain lines
    draw.line([(5, 5), (w - 5, 5)], fill=plank_dark, width=1)
    draw.line([(3, 10), (w - 3, 10)], fill=plank_dark, width=1)
    draw.line([(5, 15), (w - 5, 15)], fill=plank_dark, width=1)

    # Nail dots at ends
    nail_color = (80, 80, 80)
    draw.ellipse([(4, 8), (8, 12)], fill=nail_color)
    draw.ellipse([(w - 8, 8), (w - 4, 12)], fill=nail_color)

    img.save(os.path.join(ASSETS_DIR, "plank.png"))
    print("Generated plank.png")


def generate_background():
    """Generate a canyon/cliff background scene."""
    w, h = 900, 500
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    # Sky gradient - light blue to pale
    for y in range(h):
        r = int(135 + (y / h) * 60)
        g = int(190 + (y / h) * 40)
        b = int(240 - (y / h) * 20)
        r = min(255, r)
        g = min(255, g)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Distant mountains
    mountain_color = (160, 180, 200)
    mountain_points = [
        (0, 300), (80, 200), (160, 250), (250, 180),
        (350, 230), (450, 170), (550, 220), (650, 190),
        (750, 240), (850, 200), (w, 260), (w, 300), (0, 300),
    ]
    draw.polygon(mountain_points, fill=mountain_color)

    # Canyon depth (dark area below cliffs)
    canyon_top = 320
    for y in range(canyon_top, h):
        depth = (y - canyon_top) / (h - canyon_top)
        r = int(60 - depth * 30)
        g = int(50 - depth * 25)
        b = int(70 - depth * 30)
        r = max(0, r)
        g = max(0, g)
        b = max(0, b)
        # Only draw canyon in the gap area (middle)
        draw.line([(250, y), (650, y)], fill=(r, g, b))

    # Some clouds
    cloud_color = (255, 255, 255, 200)
    for cx, cy, size in [(150, 80, 40), (400, 60, 50), (700, 90, 35), (550, 40, 30)]:
        draw.ellipse([(cx - size, cy - size // 2), (cx + size, cy + size // 2)], fill=(245, 248, 255))
        draw.ellipse([(cx - size + 20, cy - size // 2 - 10), (cx + size - 20, cy + size // 2 - 5)], fill=(250, 252, 255))

    # Sun
    sun_x, sun_y = 750, 60
    draw.ellipse([(sun_x - 30, sun_y - 30), (sun_x + 30, sun_y + 30)], fill=(255, 240, 180))

    img.save(os.path.join(ASSETS_DIR, "background.png"))
    print("Generated background.png")


if __name__ == "__main__":
    generate_left_cliff()
    generate_right_cliff()
    generate_character()
    generate_plank()
    generate_background()
    print("All assets generated!")
