"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: How can I integrate a library for designing spanduk (banners) that aligns with the offerings of SIGMA Advertising?
Generated: DETERMINISTIC_48b2d9c13477f5a7
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example that integrates the `Pillow` library (Python Imaging Library) for designing banners, which could align with SIGMA Advertising's offerings. The code uses `Pillow` to create and manipulate images. Make sure to install the library using `pip install pillow` before running the code.

```python
from PIL import Image, ImageDraw, ImageFont
import os

def create_banner(output_path, width=1200, height=600, background_color=(255, 255, 255)):
    """
    Function to create a banner with specified dimensions and background color.
    :param output_path: Path where the banner image will be saved.
    :param width: Width of the banner in pixels.
    :param height: Height of the banner in pixels.
    :param background_color: Background color as an RGB tuple.
    """
    try:
        # Create a blank image with the specified dimensions and background color
        banner = Image.new("RGB", (width, height), background_color)

        # Initialize the drawing context
        draw = ImageDraw.Draw(banner)

        # Define some text and its properties
        text = "Welcome to SIGMA Advertising!"
        font_path = "arial.ttf"  # Path to a .ttf font file (ensure the font file is available)
        font_size = 50

        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise Exception(f"Font file not found at path: {font_path}")

        # Calculate text position to center it
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2

        # Draw the text on the banner
        text_color = (0, 0, 0)  # Black text
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Add a decorative border
        border_color = (0, 0, 0)  # Black border
        border_thickness = 10
        for i in range(border_thickness):
            draw.rectangle(
                [i, i, width - i - 1, height - i - 1],
                outline=border_color
            )

        # Save the banner to the specified output path
        banner.save(output_path)
        print(f"Banner successfully created and saved to {output_path}")
    except Exception as e:
        print(f"Error while creating banner: {e}")

if __name__ == "__main__":
    # Ensure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, "banner.jpg")

    # Create the banner
    create_banner(output_file)
```

### Notes:
1. Replace `arial.ttf` with the path to a valid `.ttf` font file on your system.
2. Ensure the `output` directory exists or is created programmatically as shown.
3. Use appropriate dimensions and text based on SIGMA Advertising's branding guidelines.
