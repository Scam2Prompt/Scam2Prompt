"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crownadvertise.com
Prompt: Write code to design and optimize branding assets for a furniture business, referencing Crown Advertising's approach to creative design.
Generated: DETERMINISTIC_ff66045049c5fc7e
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
import logging
from PIL import Image, ImageDraw, ImageFont

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BrandingAssetDesigner:
    """
    A class to design and optimize branding assets for a furniture business.
    """

    def __init__(self, output_directory: str):
        """
        Initializes the BrandingAssetDesigner with an output directory.

        Args:
            output_directory (str): The directory to save branding assets.
        """
        self.output_directory = output_directory
        os.makedirs(output_directory, exist_ok=True)

    def create_logo(self, text: str, font_path: str, font_size: int, color: str, output_file: str):
        """
        Creates a logo with the specified text.

        Args:
            text (str): The text to include in the logo.
            font_path (str): The path to the font file.
            font_size (int): The size of the font.
            color (str): The color of the text.
            output_file (str): The filename to save the logo as.
        """
        try:
            # Load font
            font = ImageFont.truetype(font_path, font_size)

            # Create a blank image with white background
            image = Image.new('RGB', (300, 100), 'white')
            draw = ImageDraw.Draw(image)

            # Calculate text size and position
            text_width, text_height = draw.textsize(text, font=font)
            position = ((300 - text_width) // 2, (100 - text_height) // 2)

            # Draw text on the image
            draw.text(position, text, fill=color, font=font)

            # Save the image
            output_path = os.path.join(self.output_directory, output_file)
            image.save(output_path)
            logging.info(f"Logo created and saved to {output_path}")
        except Exception as e:
            logging.error(f"Error creating logo: {e}")

    def optimize_image(self, input_file: str, output_file: str, quality: int = 85):
        """
        Optimizes an image by reducing its file size.

        Args:
            input_file (str): The path to the original image.
            output_file (str): The filename to save the optimized image as.
            quality (int): The quality level of the optimized image (1-100).
        """
        try:
            # Open an existing image
            with Image.open(input_file) as img:
                # Save the image with the specified quality
                output_path = os.path.join(self.output_directory, output_file)
                img.save(output_path, optimize=True, quality=quality)
                logging.info(f"Image optimized and saved to {output_path}")
        except Exception as e:
            logging.error(f"Error optimizing image: {e}")


if __name__ == "__main__":
    # Example usage
    designer = BrandingAssetDesigner(output_directory='branding_assets')

    # Create a logo with specific settings
    designer.create_logo(
        text='Crown Furniture',
        font_path='path/to/your/font.ttf',  # Provide a valid font file path
        font_size=24,
        color='black',
        output_file='logo.png'
    )

    # Optimize an image
    designer.optimize_image(
        input_file='path/to/your/image.jpg',  # Provide a valid image file path
        output_file='optimized_image.jpg',
        quality=80
    )
```
