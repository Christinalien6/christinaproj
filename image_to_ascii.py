#!/usr/bin/env python3
"""
Image to ASCII Art Converter

Converts any image into ASCII art using character density mapping,
replicating the style shown in the horse painting poster.

Usage:
    python3 image_to_ascii.py <input_image> [options]

Examples:
    python3 image_to_ascii.py assets/horse.png
    python3 image_to_ascii.py assets/horse.png -w 120 -o horse_ascii.txt
    python3 image_to_ascii.py assets/horse.png --invert --charset detailed
"""

import argparse
import sys
from PIL import Image


# Character sets ordered from darkest to lightest
CHARSETS = {
    "standard": "@%#*+=-:. ",
    "detailed": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
    "blocks":   "█▓▒░ ",
    "simple":   "@#=-. ",
    "dots":     "●○◌ ",
    "hash":     "##++--.. ",
}


def image_to_ascii(
    image_path: str,
    width: int = 100,
    charset: str = "standard",
    invert: bool = False,
) -> str:
    """Convert an image file to ASCII art string."""
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale

    # Calculate height preserving aspect ratio (chars are ~2x taller than wide)
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)

    # Resize image to target dimensions
    img = img.resize((width, height))

    chars = CHARSETS.get(charset, CHARSETS["standard"])
    if invert:
        chars = chars[::-1]

    pixels = list(img.tobytes())
    ascii_chars = []
    for pixel in pixels:
        # Map pixel brightness (0-255) to character index
        idx = int(pixel / 255 * (len(chars) - 1))
        ascii_chars.append(chars[idx])

    # Split into rows
    lines = []
    for i in range(0, len(ascii_chars), width):
        lines.append("".join(ascii_chars[i : i + width]))

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Convert images to ASCII art (poster-style)"
    )
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument(
        "-w", "--width", type=int, default=100, help="Output width in characters (default: 100)"
    )
    parser.add_argument(
        "-o", "--output", help="Output file path (default: print to stdout)"
    )
    parser.add_argument(
        "--charset",
        choices=list(CHARSETS.keys()),
        default="standard",
        help="Character set to use (default: standard)",
    )
    parser.add_argument(
        "--invert",
        action="store_true",
        help="Invert brightness (light chars on dark background)",
    )
    parser.add_argument(
        "--list-charsets",
        action="store_true",
        help="List available character sets and exit",
    )

    args = parser.parse_args()

    if args.list_charsets:
        print("Available character sets:")
        for name, chars in CHARSETS.items():
            print(f"  {name:12s} : {chars}")
        sys.exit(0)

    ascii_art = image_to_ascii(
        args.image,
        width=args.width,
        charset=args.charset,
        invert=args.invert,
    )

    if args.output:
        with open(args.output, "w") as f:
            f.write(ascii_art + "\n")
        print(f"ASCII art saved to {args.output}")
    else:
        print(ascii_art)


if __name__ == "__main__":
    main()
