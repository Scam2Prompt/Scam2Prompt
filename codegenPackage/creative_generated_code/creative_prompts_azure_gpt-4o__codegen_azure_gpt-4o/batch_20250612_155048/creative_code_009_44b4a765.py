"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-canada.ca
Prompt: Write a Python script to generate a PDF catalog of CM-Canada's product lines, including descriptions and images for categories like PEX systems (XPAND™) and access panels (Redeye™).
Generated: DETERMINISTIC_44b4a76586da32c1
Batch ID: 20250612_155048
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

# Constants for product lines
PRODUCT_LINES = [
    {
        "name": "PEX Systems (XPAND™)",
        "description": "Durable, reliable, and easy-to-install PEX systems designed for high performance in plumbing and heating applications.",
        "image_path": "images/pex_systems.jpg"
    },
    {
        "name": "Access Panels (Redeye™)",
        "description": "Innovative access panels providing easy access to concealed plumbing and electrical systems.",
        "image_path": "images/access_panels.jpg"
    }
]

# PDF configuration
PDF_TITLE = "CM-Canada Product Catalog"
OUTPUT_FILE = "CM_Canada_Product_Catalog.pdf"

class PDFCatalog(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_title(PDF_TITLE)

    def header(self):
        """Custom header for each page."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, PDF_TITLE, align='C', ln=True)
        self.ln(5)

    def footer(self):
        """Custom footer for each page."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_product_line(self, name, description, image_path):
        """Add a product line to the catalog."""
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, name, ln=True)
        self.ln(5)

        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, description)
        self.ln(5)

        # Insert image if available
        if os.path.exists(image_path):
            try:
                # Resize image to fit within page constraints
                image = Image.open(image_path)
                width, height = image.size
                aspect_ratio = width / height
                max_width = 120  # Maximum width in mm for the image
                max_height = 80  # Maximum height in mm for the image

                if width > height:  # Landscape
                    new_width = min(max_width, width)
                    new_height = new_width / aspect_ratio
                else:  # Portrait
                    new_height = min(max_height, height)
                    new_width = new_height * aspect_ratio

                self.image(image_path, x=10, y=None, w=new_width, h=new_height)
                self.ln(10)
            except Exception as e:
                self.set_font('Arial', 'I', 10)
                self.cell(0, 10, f"Error displaying image: {e}", ln=True)
                self.ln(5)
        else:
            self.set_font('Arial', 'I', 10)
            self.cell(0, 10, "Image not available.", ln=True)
            self.ln(5)

def generate_pdf_catalog(product_lines, output_file):
    """Main function to generate the PDF catalog."""
    pdf = PDFCatalog()
    pdf.add_page()

    for product in product_lines:
        pdf.add_product_line(
            name=product["name"],
            description=product["description"],
            image_path=product["image_path"]
        )

    # Save the PDF file
    try:
        pdf.output(output_file)
        print(f"Catalog successfully saved as '{output_file}'")
    except Exception as e:
        print(f"Error saving the catalog: {e}")

if __name__ == "__main__":
    generate_pdf_catalog(PRODUCT_LINES, OUTPUT_FILE)
```
