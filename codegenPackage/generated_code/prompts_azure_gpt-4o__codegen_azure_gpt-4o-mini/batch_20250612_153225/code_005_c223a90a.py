"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Write code to design a logo and banner using Python libraries, following the branding guidelines mentioned in Vital Corporate Solutions' graphic design services.
Generated: DETERMINISTIC_c223a90a32ba0836
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Function to create a logo
def create_logo(text, font_path, output_path, size=(200, 200), bg_color=(255, 255, 255), text_color=(0, 0, 0)):
    """
    Create a logo with specified text and save it as an image.

    :param text: Text to display in the logo
    :param font_path: Path to the .ttf font file
    :param output_path: Path to save the logo image
    :param size: Size of the logo (width, height)
    :param bg_color: Background color in RGB tuple
    :param text_color: Text color in RGB tuple
    """
    try:
        # Create a blank image with the specified background color
        logo = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(logo)

        # Load the font
        font = ImageFont.truetype(font_path, size[1] // 5)

        # Calculate text size and position
        text_size = draw.textsize(text, font=font)
        text_x = (size[0] - text_size[0]) / 2
        text_y = (size[1] - text_size[1]) / 2

        # Draw the text on the logo
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the logo image
        logo.save(output_path)
        print(f"Logo saved to {output_path}")
    except Exception as e:
        print(f"Error creating logo: {e}")

# Function to create a banner
def create_banner(text, font_path, output_path, size=(800, 200), bg_color=(0, 102, 204), text_color=(255, 255, 255)):
    """
    Create a banner with specified text and save it as an image.

    :param text: Text to display in the banner
    :param font_path: Path to the .ttf font file
    :param output_path: Path to save the banner image
    :param size: Size of the banner (width, height)
    :param bg_color: Background color in RGB tuple
    :param text_color: Text color in RGB tuple
    """
    try:
        # Create a blank image with the specified background color
        banner = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(banner)

        # Load the font
        font = ImageFont.truetype(font_path, size[1] // 2)

        # Calculate text size and position
        text_size = draw.textsize(text, font=font)
        text_x = (size[0] - text_size[0]) / 2
        text_y = (size[1] - text_size[1]) / 2

        # Draw the text on the banner
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the banner image
        banner.save(output_path)
        print(f"Banner saved to {output_path}")
    except Exception as e:
        print(f"Error creating banner: {e}")

# Example usage
if __name__ == "__main__":
    logo_text = "Vital Corp"
    banner_text = "Welcome to Vital Corporate Solutions"
    font_path = "path/to/your/font.ttf"  # Update with the path to your font file

    create_logo(logo_text, font_path, "logo.png")
    create_banner(banner_text, font_path, "banner.png")
```

Make sure to replace `"path/to/your/font.ttf"` with the actual path to a TrueType font file on your system.
