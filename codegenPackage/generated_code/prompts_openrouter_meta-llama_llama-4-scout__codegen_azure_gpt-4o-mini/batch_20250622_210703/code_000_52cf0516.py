"""
Generated Code Metadata:
========================
Original URL: https://medanresortcity.com
Prompt: Write a Python script to generate a brochure for Medan Resort City's Holland & Eindhoven cluster, including images and descriptions of the units.
Generated: DETERMINISTIC_52cf05167995ba20
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
from fpdf import FPDF

class BrochureGenerator:
    def __init__(self, title, output_file):
        """
        Initialize the BrochureGenerator with a title and output file name.

        :param title: Title of the brochure
        :param output_file: Name of the output PDF file
        """
        self.title = title
        self.output_file = output_file
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Add a new page to the PDF."""
        self.pdf.add_page()

    def set_title(self):
        """Set the title of the brochure."""
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, self.title, ln=True, align='C')
        self.pdf.ln(10)

    def add_image(self, image_path, x=10, y=20, w=0, h=0):
        """
        Add an image to the PDF.

        :param image_path: Path to the image file
        :param x: X position of the image
        :param y: Y position of the image
        :param w: Width of the image
        :param h: Height of the image
        """
        if os.path.exists(image_path):
            self.pdf.image(image_path, x=x, y=y, w=w, h=h)
        else:
            print(f"Warning: Image {image_path} not found. Skipping.")

    def add_description(self, description):
        """
        Add a description text to the PDF.

        :param description: Description text to add
        """
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, description)
        self.pdf.ln(5)

    def save(self):
        """Save the PDF to the specified output file."""
        try:
            self.pdf.output(self.output_file)
            print(f"Brochure saved as {self.output_file}")
        except Exception as e:
            print(f"Error saving brochure: {e}")

def main():
    # Define brochure details
    brochure_title = "Medan Resort City: Holland & Eindhoven Cluster"
    output_file = "medan_resort_brochure.pdf"

    # Create a brochure generator instance
    brochure = BrochureGenerator(brochure_title, output_file)

    # Add content to the brochure
    brochure.add_page()
    brochure.set_title()

    # Example images and descriptions
    units = [
        {
            "image": "images/holland_unit.jpg",
            "description": "Holland Unit: A beautiful unit with modern amenities and stunning views."
        },
        {
            "image": "images/eindhoven_unit.jpg",
            "description": "Eindhoven Unit: Spacious living with a touch of elegance and comfort."
        }
    ]

    for unit in units:
        brochure.add_image(unit["image"], w=100)
        brochure.add_description(unit["description"])

    # Save the brochure
    brochure.save()

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the images specified in the `units` list exist in the `images` directory relative to the script's location for the code to run successfully.
