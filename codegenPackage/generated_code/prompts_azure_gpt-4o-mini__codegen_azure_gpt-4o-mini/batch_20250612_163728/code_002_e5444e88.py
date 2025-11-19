"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write a Python script that automates the creation of flyers and brochures, incorporating design elements mentioned in Ram Digi's print media services.
Generated: DETERMINISTIC_e5444e88794ca9f6
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF
from PIL import Image

class FlyerBrochureCreator:
    def __init__(self, title, subtitle, content, image_path, output_path):
        """
        Initializes the FlyerBrochureCreator with the necessary parameters.

        :param title: Title of the flyer/brochure
        :param subtitle: Subtitle of the flyer/brochure
        :param content: Main content text for the flyer/brochure
        :param image_path: Path to the image to be included
        :param output_path: Path where the generated PDF will be saved
        """
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.image_path = image_path
        self.output_path = output_path

    def create_pdf(self):
        """Creates a PDF flyer/brochure with the specified design elements."""
        try:
            # Create a PDF object
            pdf = FPDF()
            pdf.add_page()

            # Set title font and add title
            pdf.set_font("Arial", 'B', 24)
            pdf.cell(0, 10, self.title, ln=True, align='C')

            # Set subtitle font and add subtitle
            pdf.set_font("Arial", 'I', 16)
            pdf.cell(0, 10, self.subtitle, ln=True, align='C')

            # Add a line break
            pdf.ln(10)

            # Set content font and add content
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, self.content)

            # Add an image if the path is valid
            if os.path.exists(self.image_path):
                pdf.image(self.image_path, x=10, y=pdf.get_y(), w=100)
            else:
                print(f"Warning: Image not found at {self.image_path}")

            # Save the PDF to the specified output path
            pdf.output(self.output_path)
            print(f"Flyer/Brochure created successfully at {self.output_path}")

        except Exception as e:
            print(f"An error occurred while creating the PDF: {e}")

if __name__ == "__main__":
    # Example usage
    title = "Welcome to Ram Digi"
    subtitle = "Your Partner in Print Media"
    content = ("At Ram Digi, we provide top-notch print media services. "
               "From flyers to brochures, we ensure high-quality designs "
               "that capture your audience's attention.")
    image_path = "path/to/your/image.jpg"  # Update with your image path
    output_path = "flyer_brochure.pdf"

    # Create an instance of the FlyerBrochureCreator
    flyer_creator = FlyerBrochureCreator(title, subtitle, content, image_path, output_path)
    
    # Generate the PDF
    flyer_creator.create_pdf()
```

Make sure to install the required libraries before running the script:
```bash
pip install fpdf Pillow
```
