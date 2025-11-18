"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write code to generate custom graphics or team logos for sublimated women's leggings, similar to the customization options offered by Rising Star International.
Generated: DETERMINISTIC_f09188a897698c6f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

def create_custom_logo(output_path, logo_text, colors, size=(500, 500), font_path=None):
    """
    Generates a custom logo graphic for sublimated women's leggings.
    
    :param output_path: Path to save the generated logo (including filename and extension).
    :param logo_text: Text to be displayed on the logo.
    :param colors: Tuple of primary and secondary colors (e.g., ('#FF0000', '#000000')).
    :param size: Size of the logo canvas (width, height) in pixels.
    :param font_path: Path to a .ttf font file to use for the text. Defaults to system font.
    """
    
    try:
        # Validate inputs
        if not isinstance(colors, tuple) or len(colors) != 2:
            raise ValueError("Colors must be a tuple with two color values (e.g., ('#FF0000', '#000000')).")
        if not isinstance(size, tuple) or len(size) != 2 or not all(isinstance(i, int) for i in size):
            raise ValueError("Size must be a tuple with two integers (width, height).")
        if not logo_text or not isinstance(logo_text, str):
            raise ValueError("Logo text must be a non-empty string.")

        # Create a blank image canvas
        image = Image.new("RGB", size, colors[0])  # Primary color as background

        # Initialize drawing context
        draw = ImageDraw.Draw(image)

        # Load font (default to system font if no font_path is provided)
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, size=int(size[1] / 10))  # Font size relative to canvas height
        else:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(logo_text, font=font)
        text_x = (size[0] - text_width) // 2
        text_y = (size[1] - text_height) // 2

        # Draw logo details
        # Draw a secondary color border
        border_thickness = 10
        draw.rectangle(
            [border_thickness, border_thickness, size[0] - border_thickness, size[1] - border_thickness],
            outline=colors[1],
            width=border_thickness,
        )

        # Draw logo text
        draw.text((text_x, text_y), logo_text, fill=colors[1], font=font)

        # Save the final image
        image.save(output_path)
        print(f"Logo successfully created and saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the logo: {e}")


# Example usage
if __name__ == "__main__":
    # Customize parameters as needed
    output_file = "custom_logo.png"
    text = "Team Rising Star"
    color_scheme = ("#FFFFFF", "#FF5733")  # White background, orange border and text
    canvas_size = (800, 800)  # Canvas size in pixels
    font_file = None  # Path to custom font (use system default if None)

    create_custom_logo(output_file, text, color_scheme, canvas_size, font_file)
```
