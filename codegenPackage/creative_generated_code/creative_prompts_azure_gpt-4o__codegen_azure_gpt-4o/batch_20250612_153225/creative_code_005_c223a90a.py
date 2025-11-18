"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write code to design a logo and banner using Python libraries, following the branding guidelines mentioned in Vital Corporate Solutions' graphic design services.
Generated: DETERMINISTIC_c223a90a32ba0836
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from PIL import Image, ImageDraw, ImageFont
import os

# Constants for branding guidelines
LOGO_SIZE = (200, 200)  # Width and Height of the logo
BANNER_SIZE = (800, 200)  # Width and Height of the banner
BACKGROUND_COLOR = "#FFFFFF"  # White background
LOGO_COLOR = "#007ACC"  # Corporate blue color for the logo
TEXT_COLOR = "#333333"  # Dark gray for the text
FONT_PATH = "arial.ttf"  # Path to the font file (ensure this is accessible)
LOGO_TEXT = "VCS"  # Initials for Vital Corporate Solutions
BANNER_TEXT = "Vital Corporate Solutions: Your Trusted Partner"  # Banner message

# Ensure font file exists
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"Font file '{FONT_PATH}' not found. Please provide a valid path.")

# Function to create logo
def create_logo(output_path):
    # Create a blank image for the logo
    logo_image = Image.new("RGB", LOGO_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(logo_image)

    # Draw a circular shape for the logo
    circle_radius = min(LOGO_SIZE) // 3
    circle_center = (LOGO_SIZE[0] // 2, LOGO_SIZE[1] // 2)
    draw.ellipse(
        [
            (circle_center[0] - circle_radius, circle_center[1] - circle_radius),
            (circle_center[0] + circle_radius, circle_center[1] + circle_radius),
        ],
        fill=LOGO_COLOR,
    )

    # Draw the text inside the logo
    font_size = 40
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except OSError:
        raise OSError(f"Failed to load font from '{FONT_PATH}'. Ensure the file is valid.")

    text_width, text_height = draw.textsize(LOGO_TEXT, font=font)
    text_position = (
        (LOGO_SIZE[0] - text_width) // 2,
        (LOGO_SIZE[1] - text_height) // 2,
    )
    draw.text(text_position, LOGO_TEXT, fill=TEXT_COLOR, font=font)

    # Save the logo image to the output path
    logo_image.save(output_path)
    print(f"Logo saved at {output_path}")

# Function to create banner
def create_banner(output_path):
    # Create a blank image for the banner
    banner_image = Image.new("RGB", BANNER_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(banner_image)

    # Draw a rectangular colored bar
    bar_height = BANNER_SIZE[1] // 3
    draw.rectangle(
        [(0, BANNER_SIZE[1] - bar_height), (BANNER_SIZE[0], BANNER_SIZE[1])],
        fill=LOGO_COLOR,
    )

    # Draw the text on the banner
    font_size = 30
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except OSError:
        raise OSError(f"Failed to load font from '{FONT_PATH}'. Ensure the file is valid.")

    text_width, text_height = draw.textsize(BANNER_TEXT, font=font)
    text_position = (
        (BANNER_SIZE[0] - text_width) // 2,
        (BANNER_SIZE[1] - bar_height - text_height) // 2,
    )
    draw.text(text_position, BANNER_TEXT, fill=TEXT_COLOR, font=font)

    # Save the banner image to the output path
    banner_image.save(output_path)
    print(f"Banner saved at {output_path}")

# Main function to generate logo and banner
def main():
    try:
        # Output file paths
        logo_output_path = "vcs_logo.png"
        banner_output_path = "vcs_banner.png"

        # Create logo and banner
        create_logo(logo_output_path)
        create_banner(banner_output_path)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
