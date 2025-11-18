"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Create a promotional banner generator for a crypto casino website, referencing the promotions and bonus terms described on Jups.io.
Generated: DETERMINISTIC_9a0d5eb633fbeec6
Batch ID: 20250612_154412
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


class PromoBannerGenerator:
    """
    A class to generate promotional banners for a crypto casino website.
    Banners are generated based on promotional terms and bonuses provided.
    """

    def __init__(self, output_dir="banners", banner_size=(800, 400)):
        """
        Initialize the banner generator.

        :param output_dir: Directory where generated banners will be saved.
        :param banner_size: Size of the banner in pixels (width, height).
        """
        self.output_dir = output_dir
        self.banner_size = banner_size
        os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

    def create_banner(self, title, subtitle, bonus_terms, output_filename):
        """
        Generate a promotional banner with the given text details.

        :param title: Main promotional headline.
        :param subtitle: Secondary promotional text.
        :param bonus_terms: List of bonus terms to be displayed.
        :param output_filename: Filename to save the banner as.
        """
        try:
            # Create a blank banner image
            banner = Image.new("RGB", self.banner_size, color=(25, 25, 25))  # Dark background
            draw = ImageDraw.Draw(banner)

            # Load fonts
            try:
                title_font = ImageFont.truetype("arial.ttf", 40)  # Load title font
                subtitle_font = ImageFont.truetype("arial.ttf", 20)  # Load subtitle font
                terms_font = ImageFont.truetype("arial.ttf", 18)  # Load bonus terms font
            except IOError:
                raise FileNotFoundError("Required font files not found. Place 'arial.ttf' in the working directory.")

            # Draw title
            draw.text((20, 30), title, font=title_font, fill=(255, 215, 0))  # Gold color for headline

            # Draw subtitle
            draw.text((20, 100), subtitle, font=subtitle_font, fill=(255, 255, 255))  # White color for subtitle

            # Draw bonus terms
            y_offset = 150  # Start position for bonus terms
            for term in bonus_terms:
                draw.text((20, y_offset), f"- {term}", font=terms_font, fill=(200, 200, 200))  # Light gray color
                y_offset += 30  # Adjust vertical spacing

            # Save the banner
            output_path = os.path.join(self.output_dir, output_filename)
            banner.save(output_path)
            print(f"Banner saved successfully: {output_path}")

        except Exception as e:
            print(f"Error occurred while creating the banner: {e}")

    def generate_sample_banner(self):
        """
        Generate a sample banner based on Jups.io promotional terms.
        """
        title = "Welcome to Jups.io Crypto Casino!"
        subtitle = "Claim Your Exclusive Bonuses Now!"
        bonus_terms = [
            "Get up to 100% deposit bonus!",
            "Earn up to 50 free spins daily.",
            "VIP rewards for loyal players.",
            "Fast withdrawals with zero fees.",
        ]
        output_filename = "promo_banner_sample.jpg"
        self.create_banner(title, subtitle, bonus_terms, output_filename)


if __name__ == "__main__":
    # Instantiate the banner generator
    generator = PromoBannerGenerator()

    # Generate a sample promotional banner
    generator.generate_sample_banner()
```
