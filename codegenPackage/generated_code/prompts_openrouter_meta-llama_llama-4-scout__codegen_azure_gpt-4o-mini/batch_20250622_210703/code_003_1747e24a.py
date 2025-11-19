"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Create a branding guide for a company, including a logo design, brand design, and social graphics, using Henfruit's approach to visual identity."
Generated: DETERMINISTIC_1747e24a5209177c
Batch ID: 20250622_210703
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

class BrandingGuide:
    def __init__(self, company_name, logo_text, color_palette, font_path):
        """
        Initializes the BrandingGuide with company details.

        :param company_name: Name of the company
        :param logo_text: Text to be included in the logo
        :param color_palette: Dictionary of brand colors
        :param font_path: Path to the font file for logo text
        """
        self.company_name = company_name
        self.logo_text = logo_text
        self.color_palette = color_palette
        self.font_path = font_path

    def create_logo(self, size=(200, 200)):
        """
        Creates a simple logo for the company.

        :param size: Tuple representing the size of the logo
        :return: Image object of the logo
        """
        try:
            # Create a blank image with a white background
            logo = Image.new("RGB", size, self.color_palette['background'])
            draw = ImageDraw.Draw(logo)

            # Load the font
            font = ImageFont.truetype(self.font_path, 20)

            # Calculate text size and position
            text_size = draw.textsize(self.logo_text, font=font)
            text_position = ((size[0] - text_size[0]) // 2, (size[1] - text_size[1]) // 2)

            # Draw the text on the logo
            draw.text(text_position, self.logo_text, fill=self.color_palette['text'], font=font)

            return logo
        except Exception as e:
            print(f"Error creating logo: {e}")
            return None

    def create_social_graphics(self, platform, size=(1080, 1080)):
        """
        Creates social media graphics for the specified platform.

        :param platform: Name of the social media platform
        :param size: Tuple representing the size of the graphic
        :return: Image object of the social graphic
        """
        try:
            # Create a blank image with a background color
            graphic = Image.new("RGB", size, self.color_palette['background'])
            draw = ImageDraw.Draw(graphic)

            # Load the font
            font = ImageFont.truetype(self.font_path, 40)

            # Draw the company name on the graphic
            text_position = (size[0] // 2 - 100, size[1] // 2 - 20)
            draw.text(text_position, self.company_name, fill=self.color_palette['text'], font=font)

            # Add platform name
            platform_position = (size[0] // 2 - 100, size[1] // 2 + 30)
            draw.text(platform_position, platform, fill=self.color_palette['accent'], font=font)

            return graphic
        except Exception as e:
            print(f"Error creating social graphic for {platform}: {e}")
            return None

    def save_images(self, logo, social_graphics, output_dir):
        """
        Saves the logo and social graphics to the specified directory.

        :param logo: Image object of the logo
        :param social_graphics: Dictionary of social graphics
        :param output_dir: Directory to save the images
        """
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Save logo
            logo_path = os.path.join(output_dir, f"{self.company_name}_logo.png")
            logo.save(logo_path)
            print(f"Logo saved to {logo_path}")

            # Save social graphics
            for platform, graphic in social_graphics.items():
                graphic_path = os.path.join(output_dir, f"{self.company_name}_{platform}_graphic.png")
                graphic.save(graphic_path)
                print(f"{platform.capitalize()} graphic saved to {graphic_path}")

        except Exception as e:
            print(f"Error saving images: {e}")

# Example usage
if __name__ == "__main__":
    # Define company branding details
    company_name = "Henfruit"
    logo_text = "Henfruit"
    color_palette = {
        'background': (255, 255, 255),  # White
        'text': (0, 0, 0),               # Black
        'accent': (255, 204, 0)          # Yellow
    }
    font_path = "path/to/your/font.ttf"  # Update with the actual font path

    # Create branding guide
    branding_guide = BrandingGuide(company_name, logo_text, color_palette, font_path)

    # Create logo
    logo = branding_guide.create_logo()

    # Create social graphics for different platforms
    platforms = ['facebook', 'instagram', 'twitter']
    social_graphics = {platform: branding_guide.create_social_graphics(platform) for platform in platforms}

    # Save images to output directory
    branding_guide.save_images(logo, social_graphics, output_dir="branding_assets")
```
