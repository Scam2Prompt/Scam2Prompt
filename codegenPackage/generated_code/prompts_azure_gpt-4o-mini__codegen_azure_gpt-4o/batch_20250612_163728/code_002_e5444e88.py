"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write a Python script that automates the creation of flyers and brochures, incorporating design elements mentioned in Ram Digi's print media services.
Generated: DETERMINISTIC_e5444e88794ca9f6
Batch ID: 20250612_163728
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

# Constants for flyer and brochure dimensions
FLYER_SIZE = (800, 1200)  # Width x Height in pixels
BROCHURE_SIZE = (1600, 1200)  # Width x Height in pixels
OUTPUT_DIR = "output"  # Directory to save generated designs

# Design elements based on Ram Digi's print media services
DESIGN_ELEMENTS = {
    "background_color": (255, 255, 255),  # White background
    "header_text": "Ram Digi Print Media Services",
    "header_font_size": 50,
    "header_color": (0, 0, 0),  # Black text
    "body_text": "We offer high-quality flyers and brochures tailored to your needs.",
    "body_font_size": 30,
    "body_color": (50, 50, 50),  # Dark gray text
    "footer_text": "Contact us: info@ramdigi.com | +123456789",
    "footer_font_size": 20,
    "footer_color": (100, 100, 100),  # Gray text
}

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_design(size, design_type):
    """
    Creates a flyer or brochure design based on the specified size and type.

    Args:
        size (tuple): Dimensions of the design (width, height).
        design_type (str): Type of design ('flyer' or 'brochure').

    Returns:
        str: Path to the saved design file.
    """
    try:
        # Create a blank image with the specified background color
        image = Image.new("RGB", size, DESIGN_ELEMENTS["background_color"])
        draw = ImageDraw.Draw(image)

        # Load fonts (fallback to default if custom font is unavailable)
        try:
            header_font = ImageFont.truetype("arial.ttf", DESIGN_ELEMENTS["header_font_size"])
            body_font = ImageFont.truetype("arial.ttf", DESIGN_ELEMENTS["body_font_size"])
            footer_font = ImageFont.truetype("arial.ttf", DESIGN_ELEMENTS["footer_font_size"])
        except IOError:
            header_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
            footer_font = ImageFont.load_default()

        # Add header text
        header_text = DESIGN_ELEMENTS["header_text"]
        header_width, header_height = draw.textsize(header_text, font=header_font)
        draw.text(
            ((size[0] - header_width) / 2, 50),  # Centered horizontally, 50px from top
            header_text,
            fill=DESIGN_ELEMENTS["header_color"],
            font=header_font,
        )

        # Add body text
        body_text = DESIGN_ELEMENTS["body_text"]
        body_width, body_height = draw.textsize(body_text, font=body_font)
        draw.text(
            ((size[0] - body_width) / 2, (size[1] - body_height) / 2),  # Centered in the middle
            body_text,
            fill=DESIGN_ELEMENTS["body_color"],
            font=body_font,
        )

        # Add footer text
        footer_text = DESIGN_ELEMENTS["footer_text"]
        footer_width, footer_height = draw.textsize(footer_text, font=footer_font)
        draw.text(
            ((size[0] - footer_width) / 2, size[1] - footer_height - 50),  # Centered horizontally, 50px from bottom
            footer_text,
            fill=DESIGN_ELEMENTS["footer_color"],
            font=footer_font,
        )

        # Save the design to the output directory
        file_name = f"{design_type}.png"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        image.save(file_path)
        return file_path

    except Exception as e:
        print(f"Error creating {design_type}: {e}")
        return None

def main():
    """
    Main function to generate flyer and brochure designs.
    """
    print("Generating flyer...")
    flyer_path = create_design(FLYER_SIZE, "flyer")
    if flyer_path:
        print(f"Flyer saved at: {flyer_path}")

    print("Generating brochure...")
    brochure_path = create_design(BROCHURE_SIZE, "brochure")
    if brochure_path:
        print(f"Brochure saved at: {brochure_path}")

if __name__ == "__main__":
    main()
```
