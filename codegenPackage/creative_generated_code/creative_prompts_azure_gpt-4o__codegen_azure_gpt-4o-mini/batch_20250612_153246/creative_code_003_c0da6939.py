"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://henfruit.ro
Prompt: Write code to design a visual identity package for a client, including logo design, social graphics, and infographics, as described in Henfruit's branding services.
Generated: DETERMINISTIC_c0da6939cc653b55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont

class VisualIdentityPackage:
    """
    A class to create a visual identity package including logo design,
    social graphics, and infographics for a client.
    """

    def __init__(self, client_name):
        """
        Initialize the VisualIdentityPackage with the client's name.

        :param client_name: str - The name of the client
        """
        self.client_name = client_name
        self.assets_directory = f"{client_name}_branding_assets"
        self._create_directory(self.assets_directory)

    def _create_directory(self, directory):
        """
        Create a directory to store the branding assets.

        :param directory: str - The path of the directory to create
        """
        try:
            os.makedirs(directory, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory {directory}: {e}")

    def create_logo(self, logo_text, size=(300, 100), color=(0, 128, 255)):
        """
        Create a logo image with specified text, size, and color.

        :param logo_text: str - The text to include in the logo
        :param size: tuple - The size of the logo as (width, height)
        :param color: tuple - The color of the logo in RGB format
        """
        logo = Image.new('RGB', size, (255, 255, 255))  # White background
        draw = ImageDraw.Draw(logo)
        font = ImageFont.load_default()
        
        text_size = draw.textsize(logo_text, font=font)
        text_position = ((size[0] - text_size[0]) // 2, (size[1] - text_size[1]) // 2)
        
        draw.text(text_position, logo_text, fill=color, font=font)
        logo_path = os.path.join(self.assets_directory, f"{self.client_name}_logo.png")
        logo.save(logo_path)
        print(f"Logo saved at {logo_path}")

    def create_social_graphics(self, platform='Instagram', dimensions=(1080, 1080)):
        """
        Create a social media graphic.

        :param platform: str - The social media platform
        :param dimensions: tuple - The dimensions of the graphic
        """
        graphic = Image.new('RGB', dimensions, (255, 255, 255))  # White background
        draw = ImageDraw.Draw(graphic)
        message = f"Follow us on {platform}"
        font = ImageFont.load_default()

        text_size = draw.textsize(message, font=font)
        text_position = ((dimensions[0] - text_size[0]) // 2, (dimensions[1] - text_size[1]) // 2)

        draw.text(text_position, message, fill=(0, 128, 255), font=font)
        graphic_path = os.path.join(self.assets_directory, f"{self.client_name}_{platform}_graphic.png")
        graphic.save(graphic_path)
        print(f"Social graphic saved at {graphic_path}")

    def create_infographic(self, content):
        """
        Create a simple infographic based on provided content.

        :param content: str - The text content for the infographic
        """
        infographic = Image.new('RGB', (800, 600), (255, 255, 255))  # White background
        draw = ImageDraw.Draw(infographic)
        font = ImageFont.load_default()

        # Draw content
        draw.text((10, 10), content, fill=(0, 0, 0), font=font)
        infographic_path = os.path.join(self.assets_directory, f"{self.client_name}_infographic.png")
        infographic.save(infographic_path)
        print(f"Infographic saved at {infographic_path}")

# Example usage
if __name__ == "__main__":
    try:
        client_package = VisualIdentityPackage("Henfruit")
        client_package.create_logo("Henfruit Logo")
        client_package.create_social_graphics("Instagram")
        client_package.create_infographic("This is a simple infographic about Henfruit.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
