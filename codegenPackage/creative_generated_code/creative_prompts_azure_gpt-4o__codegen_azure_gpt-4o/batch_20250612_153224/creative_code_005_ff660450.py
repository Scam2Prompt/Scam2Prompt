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

Certainly! Below is the Python code implementation for designing and optimizing branding assets for a furniture business, following best practices:

```python
import os
from PIL import Image, ImageDraw, ImageFont


class BrandingAssetsGenerator:
    """
    A class to design and optimize branding assets for a furniture business.

    Attributes:
    - output_directory (str): Directory to save generated branding assets.
    """
    def __init__(self, output_directory="branding_assets"):
        self.output_directory = output_directory
        self._setup_output_directory()

    def _setup_output_directory(self):
        """Create the output directory if it does not exist."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def create_logo(self, text="FurnitureCo", font_path=None, font_size=100, image_size=(500, 500), color=(50, 50, 50)):
        """
        Generate a logo image with specified text.

        Parameters:
        - text (str): The text to display in the logo.
        - font_path (str): Path to the font file. Uses default font if None.
        - font_size (int): Size of the font for the logo text.
        - image_size (tuple): Size of the logo image (width, height) in pixels.
        - color (tuple): RGB color for the logo text.

        Returns:
        - str: Path to the saved logo image file.
        """
        try:
            # Create a blank image
            logo_image = Image.new("RGB", image_size, (255, 255, 255))  # White background
            draw = ImageDraw.Draw(logo_image)

            # Load font
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()

            # Calculate text position to center the text in the image
            text_width, text_height = draw.textsize(text, font=font)
            position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

            # Draw the text on the image
            draw.text(position, text, fill=color, font=font)

            # Save the logo to the output directory
            logo_path = os.path.join(self.output_directory, "logo.png")
            logo_image.save(logo_path)

            return logo_path

        except Exception as e:
            raise RuntimeError(f"Failed to create logo: {e}")

    def optimize_image(self, image_path, output_quality=85):
        """
        Optimize an image for branding usage by reducing file size while preserving quality.

        Parameters:
        - image_path (str): Path to the image file to optimize.
        - output_quality (int): Quality of the optimized image (1-100).

        Returns:
        - str: Path to the optimized image file.
        """
        try:
            # Open the original image
            with Image.open(image_path) as img:
                # Optimize and save the image
                optimized_path = os.path.join(self.output_directory, f"optimized_{os.path.basename(image_path)}")
                img.save(optimized_path, "JPEG", quality=output_quality, optimize=True)

                return optimized_path

        except Exception as e:
            raise RuntimeError(f"Failed to optimize image: {e}")

    def create_banner(self, text="Stylish Furniture for Everyone", banner_size=(1200, 600), color=(60, 120, 200), font_path=None, font_size=50):
        """
        Generate a banner image for promotional use.

        Parameters:
        - text (str): The text to display on the banner.
        - banner_size (tuple): Size of the banner image (width, height) in pixels.
        - color (tuple): RGB background color for the banner.
        - font_path (str): Path to the font file. Uses default font if None.
        - font_size (int): Size of the font for the banner text.

        Returns:
        - str: Path to the saved banner image file.
        """
        try:
            # Create a blank banner image
            banner_image = Image.new("RGB", banner_size, color)
            draw = ImageDraw.Draw(banner_image)

            # Load font
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()

            # Calculate text position to center the text in the banner
            text_width, text_height = draw.textsize(text, font=font)
            position = ((banner_size[0] - text_width) // 2, (banner_size[1] - text_height) // 2)

            # Draw the text on the banner
            draw.text(position, text, fill=(255, 255, 255), font=font)  # White text

            # Save the banner to the output directory
            banner_path = os.path.join(self.output_directory, "banner.png")
            banner_image.save(banner_path)

            return banner_path

        except Exception as e:
            raise RuntimeError(f"Failed to create banner: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        generator = BrandingAssetsGenerator()

        # Create a logo
        logo_path = generator.create_logo()
        print(f"Logo generated: {logo_path}")

        # Optimize an image
        optimized_image_path = generator.optimize_image("sample_image.jpg")
        print(f"Optimized image: {optimized_image_path}")

        # Create a banner
        banner_path = generator.create_banner()
        print(f"Banner generated: {banner_path}")

    except RuntimeError as error:
        print(f"Error: {error}")
```

### Requirements:
- Install Pillow (`pip install pillow`) for image processing.

This code adheres to the requested standards and includes error handling, comments, and modular, reusable methods for production-ready implementation.
