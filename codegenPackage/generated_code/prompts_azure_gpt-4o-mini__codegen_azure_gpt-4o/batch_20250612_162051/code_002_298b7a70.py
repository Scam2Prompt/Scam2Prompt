"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Create a Python script that automates the design process for marketing materials in the pub sector, reflecting the strategic approach of Lords Marketing.
Generated: DETERMINISTIC_298b7a70cd5f7ebf
Batch ID: 20250612_162051
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
import textwrap

# Constants
OUTPUT_DIR = "marketing_materials"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update path as needed
DEFAULT_FONT_SIZE = 36
IMAGE_SIZE = (800, 600)  # Width x Height
BACKGROUND_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 0)  # Black
LOGO_PATH = "logo.png"  # Path to the logo file

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_marketing_material(title, subtitle, content, output_filename):
    """
    Automates the creation of marketing materials with a strategic design.

    Args:
        title (str): The title of the marketing material.
        subtitle (str): The subtitle of the marketing material.
        content (str): The main content text.
        output_filename (str): The name of the output file (without extension).

    Returns:
        str: The path to the generated marketing material image.
    """
    try:
        # Create a blank image
        image = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Load font
        try:
            font = ImageFont.truetype(FONT_PATH, DEFAULT_FONT_SIZE)
        except IOError:
            raise RuntimeError("Font file not found. Please check the FONT_PATH.")

        # Add title
        title_y = 20
        draw.text((20, title_y), title, fill=TEXT_COLOR, font=font)

        # Add subtitle
        subtitle_y = title_y + 50
        draw.text((20, subtitle_y), subtitle, fill=TEXT_COLOR, font=font)

        # Add content (wrapped text)
        content_y = subtitle_y + 50
        wrapped_content = textwrap.fill(content, width=70)
        draw.text((20, content_y), wrapped_content, fill=TEXT_COLOR, font=font)

        # Add logo (if exists)
        if os.path.exists(LOGO_PATH):
            logo = Image.open(LOGO_PATH)
            logo.thumbnail((100, 100))  # Resize logo to fit
            image.paste(logo, (IMAGE_SIZE[0] - 120, 20))  # Place logo at top-right corner

        # Save the image
        output_path = os.path.join(OUTPUT_DIR, f"{output_filename}.png")
        image.save(output_path)
        return output_path

    except Exception as e:
        print(f"Error creating marketing material: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Example data
    title = "Pub Specials This Week"
    subtitle = "Exclusive Offers for Our Valued Customers"
    content = (
        "Join us this week for amazing deals on food and drinks! "
        "Happy hour every day from 5 PM to 7 PM. Don't miss out on our live music events!"
    )
    output_filename = "pub_specials"

    # Generate marketing material
    result = create_marketing_material(title, subtitle, content, output_filename)
    if result:
        print(f"Marketing material created successfully: {result}")
    else:
        print("Failed to create marketing material.")
```
