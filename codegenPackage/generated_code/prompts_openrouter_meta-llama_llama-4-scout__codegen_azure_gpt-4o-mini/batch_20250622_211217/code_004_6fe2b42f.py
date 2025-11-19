"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Design a template for an OG image using Senja's tools, incorporating a product announcement theme.
Generated: DETERMINISTIC_6fe2b42f6f418c3f
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

# Constants for the image dimensions and colors
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
BACKGROUND_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text
FONT_PATH = "path/to/your/font.ttf"  # Update with the path to your font file
FONT_SIZE = 60
SUBFONT_SIZE = 40

def create_og_image(product_name, product_description, output_path):
    """
    Create an Open Graph image for a product announcement.

    Args:
        product_name (str): The name of the product.
        product_description (str): A brief description of the product.
        output_path (str): The file path where the image will be saved.

    Raises:
        ValueError: If the product name or description is empty.
        IOError: If there is an issue saving the image.
    """
    # Validate input
    if not product_name or not product_description:
        raise ValueError("Product name and description must not be empty.")

    # Create a blank image with the specified background color
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    # Load the font
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        subfont = ImageFont.truetype(FONT_PATH, SUBFONT_SIZE)
    except IOError:
        raise IOError("Font file not found. Please check the FONT_PATH.")

    # Calculate text size and position for the product name
    name_width, name_height = draw.textsize(product_name, font=font)
    name_x = (IMAGE_WIDTH - name_width) / 2
    name_y = (IMAGE_HEIGHT - name_height) / 4

    # Draw the product name on the image
    draw.text((name_x, name_y), product_name, fill=TEXT_COLOR, font=font)

    # Calculate text size and position for the product description
    description_width, description_height = draw.textsize(product_description, font=subfont)
    description_x = (IMAGE_WIDTH - description_width) / 2
    description_y = name_y + name_height + 20  # 20 pixels below the product name

    # Draw the product description on the image
    draw.text((description_x, description_y), product_description, fill=TEXT_COLOR, font=subfont)

    # Save the image to the specified output path
    try:
        image.save(output_path)
    except IOError as e:
        raise IOError(f"Failed to save image: {e}")

    print(f"Open Graph image created successfully at {output_path}")

# Example usage
if __name__ == "__main__":
    try:
        create_og_image("New Product Launch", "Introducing our latest innovation!", "og_image.png")
    except Exception as e:
        print(f"Error: {e}")
```
