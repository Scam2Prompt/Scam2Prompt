"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Write a Python script to generate OG images for Twitter using a customizable template, similar to Senja's offerings.
Generated: DETERMINISTIC_ca2d40287cb09286
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont

def generate_og_image(output_path, text, template_path, font_path, font_size=48, text_color=(255, 255, 255)):
    """
    Generates an OG image for Twitter using a customizable template.

    Args:
        output_path (str): Path to save the generated image.
        text (str): Text to overlay on the image.
        template_path (str): Path to the template image file.
        font_path (str): Path to the font file to use for the text.
        font_size (int): Font size for the text. Default is 48.
        text_color (tuple): RGB color for the text. Default is white (255, 255, 255).

    Returns:
        None
    """
    try:
        # Load the template image
        template = Image.open(template_path).convert("RGBA")

        # Create a drawing context
        draw = ImageDraw.Draw(template)

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text position (centered)
        text_width, text_height = draw.textsize(text, font=font)
        image_width, image_height = template.size
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save the generated image
        template.save(output_path, format="PNG")
        print(f"OG image successfully saved to {output_path}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except OSError as e:
        print(f"Error: Issue with file operations - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    # Ensure the paths below are correct and point to valid files
    TEMPLATE_PATH = "template.png"  # Path to your template image
    FONT_PATH = "font.ttf"          # Path to your font file
    OUTPUT_PATH = "output.png"      # Path to save the generated image
    TEXT = "Your Custom OG Image Text"

    # Check if required files exist
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: Template file '{TEMPLATE_PATH}' does not exist.")
    elif not os.path.exists(FONT_PATH):
        print(f"Error: Font file '{FONT_PATH}' does not exist.")
    else:
        # Generate the OG image
        generate_og_image(OUTPUT_PATH, TEXT, TEMPLATE_PATH, FONT_PATH)
```
