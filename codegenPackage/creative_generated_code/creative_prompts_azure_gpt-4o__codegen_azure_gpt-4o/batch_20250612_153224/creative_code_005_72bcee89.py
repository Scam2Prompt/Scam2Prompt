"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Create a Python script to automate the generation of tailored illustrations for branding purposes, similar to the services described by Meta Force 360.
Generated: DETERMINISTIC_72bcee89642d10cf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import random


def create_brand_illustration(output_path, text, font_path=None, canvas_size=(800, 800), bg_color=None):
    """
    Generate a tailored illustration for branding purposes.

    Args:
        output_path (str): Path to save the generated illustration.
        text (str): Text to include in the illustration.
        font_path (str): Path to a custom font file (Optional).
        canvas_size (tuple): Size of the canvas in pixels (width, height).
        bg_color (tuple): Background color as RGB (Optional, defaults to random light color).

    Raises:
        Exception: If an error occurs during image creation or saving.
    """
    try:
        # Generate a random light background color if not provided
        if bg_color is None:
            bg_color = tuple(random.randint(200, 255) for _ in range(3))

        # Create a blank canvas
        image = Image.new("RGB", canvas_size, bg_color)
        draw = ImageDraw.Draw(image)

        # Define font
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, size=50)
        else:
            font = ImageFont.load_default()

        # Determine text position
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (canvas_size[0] - text_width) // 2
        text_y = (canvas_size[1] - text_height) // 2

        # Draw text onto the canvas
        text_color = (0, 0, 0)  # Black text color
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the illustration
        image.save(output_path)
        print(f"Illustration saved successfully at: {output_path}")

    except Exception as e:
        print(f"Error occurred while generating the illustration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage of the script

    # Customizable parameters
    output_file = "branding_illustration.png"
    branding_text = "Your Brand"
    custom_font_path = None  # Provide path to a .ttf font file if desired
    canvas_dimensions = (800, 800)

    # Generate illustration
    create_brand_illustration(output_file, branding_text, custom_font_path, canvas_dimensions)
```
