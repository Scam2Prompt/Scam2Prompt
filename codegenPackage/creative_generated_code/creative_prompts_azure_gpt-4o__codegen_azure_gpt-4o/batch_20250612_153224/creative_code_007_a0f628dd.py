"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Recommend a library or API for creating promotional artwork for the pub trade, and write code to customize designs for microbreweries as described by Lords Marketing & Promotions.
Generated: DETERMINISTIC_a0f628ddd1592f16
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code that uses the `Pillow` library (Python Imaging Library) to create and customize promotional artwork for microbreweries. Pillow is a widely used library for image manipulation and is suitable for tasks like this.

```python
from PIL import Image, ImageDraw, ImageFont
import os

# Constants
OUTPUT_DIRECTORY = "output"
FONT_PATH = "arial.ttf"  # Replace with a path to a TTF font file on your system
IMAGE_SIZE = (800, 600)  # Width, Height in pixels
BACKGROUND_COLOR = (255, 223, 186)  # A pale beer-like color
TEXT_COLOR = (0, 0, 0)  # Black
LOGO_SIZE = (150, 150)  # Size of the microbrewery logo

def create_promotional_artwork(brewery_name, slogan, logo_path):
    """
    Generates a promotional artwork image for a microbrewery.
    
    Args:
        brewery_name (str): The name of the microbrewery.
        slogan (str): The promotional slogan for the microbrewery.
        logo_path (str): Path to the microbrewery logo image (must exist).

    Returns:
        str: File path of the generated artwork image.
    """
    try:
        # Validate logo file existence
        if not os.path.exists(logo_path):
            raise FileNotFoundError(f"Logo file not found: {logo_path}")

        # Create a blank image with background color
        image = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)

        # Load logo image and resize
        logo = Image.open(logo_path)
        logo = logo.resize(LOGO_SIZE)

        # Paste logo into the center of the image
        logo_position = ((IMAGE_SIZE[0] - LOGO_SIZE[0]) // 2, 50)  # Centered, with some padding from top
        image.paste(logo, logo_position)

        # Load font
        if not os.path.exists(FONT_PATH):
            raise FileNotFoundError(f"Font file not found: {FONT_PATH}")
        font_large = ImageFont.truetype(FONT_PATH, 40)  # Font size for brewery name
        font_small = ImageFont.truetype(FONT_PATH, 24)  # Font size for slogan

        # Add brewery name to the image
        brewery_name_position = (50, LOGO_SIZE[1] + 70)  # Below the logo
        draw.text(brewery_name_position, brewery_name, fill=TEXT_COLOR, font=font_large)

        # Add slogan to the image
        slogan_position = (50, LOGO_SIZE[1] + 140)  # Below the brewery name
        draw.text(slogan_position, slogan, fill=TEXT_COLOR, font=font_small)

        # Ensure output directory exists
        os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

        # Save image to file
        output_path = os.path.join(OUTPUT_DIRECTORY, f"{brewery_name.replace(' ', '_')}_promo_artwork.png")
        image.save(output_path)

        return output_path

    except Exception as e:
        print(f"Error generating artwork: {e}")
        return None


# Example usage
if __name__ == "__main__":
    brewery_name = "Lords Microbrewery"
    slogan = "Crafting Excellence, One Pint at a Time!"
    logo_path = "logo.png"  # Replace with the actual path to the brewery logo file

    result = create_promotional_artwork(brewery_name, slogan, logo_path)
    if result:
        print(f"Promotional artwork created successfully: {result}")
```

### Notes
- Replace `"arial.ttf"` with the path to a TTF font available on your system. You can use a font suitable for the theme.
- Replace `"logo.png"` with the actual path to the logo file.
- This code creates a basic promotional artwork and saves it as a PNG in the `output` directory. For production use, further customization might be necessary.
