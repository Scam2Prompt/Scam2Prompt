"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Write code to design a visual identity package for a client, including logo design, social graphics, and infographics, as described in Henfruit's branding services.
Generated: DETERMINISTIC_c0da6939cc653b55
Batch ID: 20250612_153246
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

class VisualIdentityPackage:
    def __init__(self, client_name):
        """
        Initialize the VisualIdentityPackage with the client's name.
        
        :param client_name: Name of the client for whom the package is created.
        """
        self.client_name = client_name
        self.assets_dir = f"{client_name}_branding_assets"
        os.makedirs(self.assets_dir, exist_ok=True)

    def create_logo(self, text, size=(200, 200), color=(255, 0, 0)):
        """
        Create a simple logo with the specified text, size, and color.
        
        :param text: Text to include in the logo.
        :param size: Size of the logo image.
        :param color: Color of the logo text in RGB format.
        """
        try:
            logo = Image.new("RGB", size, (255, 255, 255))  # White background
            draw = ImageDraw.Draw(logo)
            font = ImageFont.load_default()
            text_size = draw.textsize(text, font=font)
            text_position = ((size[0] - text_size[0]) // 2, (size[1] - text_size[1]) // 2)
            draw.text(text_position, text, fill=color, font=font)
            logo_path = os.path.join(self.assets_dir, f"{self.client_name}_logo.png")
            logo.save(logo_path)
            print(f"Logo created at: {logo_path}")
        except Exception as e:
            print(f"Error creating logo: {e}")

    def create_social_graphics(self, platform, dimensions=(1080, 1080)):
        """
        Create a social media graphic for the specified platform.
        
        :param platform: Name of the social media platform.
        :param dimensions: Dimensions of the graphic.
        """
        try:
            graphic = Image.new("RGB", dimensions, (240, 240, 240))  # Light gray background
            draw = ImageDraw.Draw(graphic)
            font = ImageFont.load_default()
            text = f"{self.client_name} on {platform}"
            text_size = draw.textsize(text, font=font)
            text_position = ((dimensions[0] - text_size[0]) // 2, (dimensions[1] - text_size[1]) // 2)
            draw.text(text_position, text, fill=(0, 0, 0), font=font)  # Black text
            graphic_path = os.path.join(self.assets_dir, f"{self.client_name}_{platform}_graphic.png")
            graphic.save(graphic_path)
            print(f"Social graphic created at: {graphic_path}")
        except Exception as e:
            print(f"Error creating social graphic: {e}")

    def create_infographic(self, data):
        """
        Create a simple infographic based on the provided data.
        
        :param data: Dictionary containing data for the infographic.
        """
        try:
            infographic = Image.new("RGB", (800, 600), (255, 255, 255))  # White background
            draw = ImageDraw.Draw(infographic)
            font = ImageFont.load_default()
            y_position = 20
            
            for key, value in data.items():
                draw.text((20, y_position), f"{key}: {value}", fill=(0, 0, 0), font=font)
                y_position += 30
            
            infographic_path = os.path.join(self.assets_dir, f"{self.client_name}_infographic.png")
            infographic.save(infographic_path)
            print(f"Infographic created at: {infographic_path}")
        except Exception as e:
            print(f"Error creating infographic: {e}")

if __name__ == "__main__":
    # Example usage
    client = VisualIdentityPackage("Henfruit")
    client.create_logo("Henfruit")
    client.create_social_graphics("Instagram")
    client.create_infographic({"Service A": "Description A", "Service B": "Description B"})
```
