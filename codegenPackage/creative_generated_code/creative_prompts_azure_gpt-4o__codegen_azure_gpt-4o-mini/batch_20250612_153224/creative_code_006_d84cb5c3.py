"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to automate the generation of social media ad designs, inspired by Alpha Digital Solutions' graphic design services.
Generated: DETERMINISTIC_d84cb5c32998f016
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
import random
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

# Constants for image generation
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 800
BACKGROUND_COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A1"]
FONT_SIZE = 50
OUTPUT_DIR = "ad_designs"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

class SocialMediaAdGenerator:
    """A class to generate social media ad designs."""

    def __init__(self, ad_text):
        self.ad_text = ad_text

    def generate_image(self):
        """Generates an image for the ad with specified text."""
        try:
            # Create a blank image with a random background color
            background_color = random.choice(BACKGROUND_COLORS)
            image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), background_color)
            draw = ImageDraw.Draw(image)

            # Load a default font
            font = ImageFont.load_default()

            # Calculate text size and position
            text_size = draw.textsize(self.ad_text, font=font)
            text_x = (IMAGE_WIDTH - text_size[0]) / 2
            text_y = (IMAGE_HEIGHT - text_size[1]) / 2

            # Draw the text on the image
            draw.text((text_x, text_y), self.ad_text, fill="white", font=font)

            # Save the image to the output directory
            file_name = f"{self.ad_text.replace(' ', '_')}.png"
            image_path = os.path.join(OUTPUT_DIR, file_name)
            image.save(image_path)
            print(f"Image saved: {image_path}")
        except Exception as e:
            print(f"Error generating image: {e}")

    def create_pdf(self):
        """Creates a PDF file containing the ad image."""
        pdf = FPDF()
        pdf.add_page()
        
        # Add image to the PDF
        file_name = f"{self.ad_text.replace(' ', '_')}.png"
        image_path = os.path.join(OUTPUT_DIR, file_name)
        
        try:
            pdf.image(image_path, x=10, y=10, w=190)
            pdf_file_name = f"{self.ad_text.replace(' ', '_')}.pdf"
            pdf_output_path = os.path.join(OUTPUT_DIR, pdf_file_name)
            pdf.output(pdf_output_path)
            print(f"PDF saved: {pdf_output_path}")
        except Exception as e:
            print(f"Error creating PDF: {e}")

def main():
    """Main function to generate ad designs."""
    ad_text = "Your Ad Here!"  # Replace with dynamic input as needed

    # Create an instance of the ad generator
    ad_generator = SocialMediaAdGenerator(ad_text)

    # Generate the ad image and PDF
    ad_generator.generate_image()
    ad_generator.create_pdf()

if __name__ == "__main__":
    main()
```
