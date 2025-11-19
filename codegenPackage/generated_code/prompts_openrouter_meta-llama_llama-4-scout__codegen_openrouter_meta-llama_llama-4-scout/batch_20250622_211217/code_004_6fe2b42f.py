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
# og_image_generator.py

from PIL import Image, ImageDraw, ImageFont
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OGImageGenerator:
    """
    Generates an OG image template for a product announcement.
    """

    def __init__(self, 
                 product_name: str, 
                 product_description: str, 
                 background_color: str = "#ffffff", 
                 text_color: str = "#000000"):
        """
        Initializes the OG image generator.

        Args:
        - product_name (str): The name of the product.
        - product_description (str): A short description of the product.
        - background_color (str): The background color of the image (default: #ffffff).
        - text_color (str): The color of the text (default: #000000).
        """
        self.product_name = product_name
        self.product_description = product_description
        self.background_color = background_color
        self.text_color = text_color

    def generate_image(self, output_filename: str = "og_image.png", 
                      width: int = 1200, height: int = 630):
        """
        Generates the OG image.

        Args:
        - output_filename (str): The filename to save the image (default: og_image.png).
        - width (int): The width of the image (default: 1200).
        - height (int): The height of the image (default: 630).
        """
        try:
            # Create a new image
            img = Image.new("RGB", (width, height), color=self.background_color)
            draw = ImageDraw.Draw(img)

            # Load font
            font = ImageFont.truetype("arial.ttf", 48)

            # Draw product name
            product_name_x = width // 2
            product_name_y = height // 4
            draw.text((product_name_x, product_name_y), 
                      self.product_name, 
                      font=font, 
                      fill=self.text_color, 
                      anchor="mm")

            # Draw product description
            product_description_x = width // 2
            product_description_y = height // 2
            font = ImageFont.truetype("arial.ttf", 24)
            draw.text((product_description_x, product_description_y), 
                      self.product_description, 
                      font=font, 
                      fill=self.text_color, 
                      anchor="mm", 
                      width=width - 100)

            # Save the image
            img.save(output_filename)
            logger.info(f"Image saved to {output_filename}")

        except Exception as e:
            logger.error(f"Error generating image: {e}")

if __name__ == "__main__":
    generator = OGImageGenerator(
        product_name="New Product Launch",
        product_description="This is a brand new product announcement."
    )
    generator.generate_image()
```
