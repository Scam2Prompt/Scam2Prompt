"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write a Python script that automates the creation of flyers and brochures, incorporating design elements mentioned in Ram Digi's print media services.
Generated: DETERMINISTIC_e5444e88794ca9f6
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
from PIL import Image

class FlyerBrochureGenerator:
    def __init__(self, title, subtitle, content, output_dir='output'):
        """
        Initializes the flyer and brochure generator.
        
        :param title: Title of the flyer/brochure
        :param subtitle: Subtitle of the flyer/brochure
        :param content: Main content text
        :param output_dir: Directory to save generated flyers/brochures
        """
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def create_flyer(self, filename):
        """
        Creates a flyer as a PDF file.

        :param filename: The name of the file to save the flyer
        """
        pdf = FPDF()
        pdf.add_page()

        # Title
        pdf.set_font("Arial", 'B', 24)
        pdf.cell(0, 10, self.title, ln=True, align='C')

        # Subtitle
        pdf.set_font("Arial", 'I', 18)
        pdf.cell(0, 10, self.subtitle, ln=True, align='C')

        # Content
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, self.content)

        # Output the PDF
        output_path = os.path.join(self.output_dir, filename)
        try:
            pdf.output(output_path)
            print(f"Flyer created successfully: {output_path}")
        except Exception as e:
            print(f"Error creating flyer: {e}")

    def add_image(self, image_path, x, y, width, height):
        """
        Adds an image to the flyer.

        :param image_path: Path to the image file
        :param x: X coordinate for the image placement
        :param y: Y coordinate for the image placement
        :param width: Width of the image
        :param height: Height of the image
        """
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(image_path)  # Overwrite the image with the new size
                pdf = FPDF()
                pdf.add_page()
                pdf.image(image_path, x=x, y=y, w=width, h=height)
            except Exception as e:
                print(f"Error adding image: {e}")
        else:
            print(f"Image not found: {image_path}")

if __name__ == "__main__":
    # User-defined content for the flyer
    flyer_title = "Grand Opening!"
    flyer_subtitle = "Join Us for the Celebration"
    flyer_content = (
        "We are excited to announce the grand opening of our new store! "
        "Come and enjoy exclusive promotions, refreshments, and giveaways. "
        "Date: Saturday, March 25th, 2023\n"
        "Location: 123 Main St, Anytown\n"
        "Time: 10 AM - 6 PM"
    )

    # Create an instance of the flyer brochure generator
    generator = FlyerBrochureGenerator(flyer_title, flyer_subtitle, flyer_content)

    # Create the flyer
    generator.create_flyer('flyer_grand_opening.pdf')

    # Optionally add an image
    # generator.add_image('path/to/image.jpg', x=10, y=100, width=100, height=100)
```

Make sure to have `fpdf` and `Pillow` libraries installed:
```bash
pip install fpdf Pillow
```
