"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thephantomnetwork.net
Prompt: Write a Python script to automate the creation of thumbnails for YouTube videos, inspired by the video editing projects mentioned on "The Phantom Network" website.
Generated: DETERMINISTIC_71a92c25d4d3a56e
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import argparse


def create_thumbnail(input_image_path, output_image_path, text, font_path="arial.ttf", font_size=50, text_color=(255, 255, 255)):
    """
    Creates a YouTube thumbnail by overlaying text on an image.

    Parameters:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the generated thumbnail.
        text (str): Text to overlay on the image.
        font_path (str): Path to the TrueType font file.
        font_size (int): Font size for the text.
        text_color (tuple): RGB color tuple for the text.
    """
    try:
        # Open the input image
        with Image.open(input_image_path) as img:
            # Ensure image is in RGB mode
            img = img.convert("RGB")

            # Create a drawing context
            draw = ImageDraw.Draw(img)

            # Load the font
            try:
                font = ImageFont.truetype(font_path, font_size)
            except OSError:
                raise FileNotFoundError(f"Font file '{font_path}' not found.")

            # Calculate text position (centered)
            text_width, text_height = draw.textsize(text, font=font)
            text_x = (img.width - text_width) // 2
            text_y = (img.height - text_height) // 2

            # Overlay text on the image
            draw.text((text_x, text_y), text, font=font, fill=text_color)

            # Save the thumbnail
            img.save(output_image_path)

            print(f"Thumbnail saved to: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to handle user arguments and initiate thumbnail creation.
    """
    parser = argparse.ArgumentParser(description="Automate the creation of YouTube video thumbnails.")
    parser.add_argument("input_image", type=str, help="Path to the input image file.")
    parser.add_argument("output_image", type=str, help="Path to save the generated thumbnail.")
    parser.add_argument("text", type=str, help="Text to overlay on the thumbnail.")
    parser.add_argument("--font", type=str, default="arial.ttf", help="Path to the TrueType font file.")
    parser.add_argument("--font_size", type=int, default=50, help="Font size for the overlay text.")
    parser.add_argument("--text_color", type=str, default="255,255,255",
                        help="RGB color for the text, e.g., '255,255,255' for white.")

    args = parser.parse_args()

    # Parse text color as a tuple
    try:
        text_color = tuple(map(int, args.text_color.split(',')))
        if len(text_color) != 3 or any(c < 0 or c > 255 for c in text_color):
            raise ValueError
    except ValueError:
        print("Error: Text color must be a valid RGB tuple in the format 'R,G,B' (e.g., '255,255,255').")
        return

    # Ensure input image exists
    if not Path(args.input_image).is_file():
        print(f"Error: Input image file '{args.input_image}' does not exist.")
        return

    # Create thumbnail
    create_thumbnail(
        input_image_path=args.input_image,
        output_image_path=args.output_image,
        text=args.text,
        font_path=args.font,
        font_size=args.font_size,
        text_color=text_color
    )


if __name__ == "__main__":
    main()
```
