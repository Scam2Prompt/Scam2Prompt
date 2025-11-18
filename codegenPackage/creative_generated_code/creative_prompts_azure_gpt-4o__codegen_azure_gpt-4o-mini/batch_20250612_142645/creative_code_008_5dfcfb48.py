"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Write a script to generate a PDF catalog of glass products, including laminated, reflective, and decorative options, with descriptions and images.
Generated: DETERMINISTIC_5dfcfb483aaa191c
Batch ID: 20250612_142645
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

# Define a class for the PDF catalog
class PDFCatalog:
    def __init__(self, title):
        self.title = title
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Add a new page to the PDF."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, self.title, ln=True, align='C')
        self.pdf.ln(10)  # Add a line break

    def add_product(self, name, description, image_path):
        """Add a product section to the PDF."""
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, name, ln=True)

        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, description)
        self.pdf.ln(5)  # Add a line break

        # Add the image to the PDF if it exists
        if os.path.exists(image_path):
            self.pdf.image(image_path, w=100)  # Set width to 100 mm
        else:
            print(f"Warning: Image file {image_path} does not exist.")

        self.pdf.ln(10)  # Add space between products

    def save(self, filename):
        """Save the PDF to a file."""
        try:
            self.pdf.output(filename)
            print(f"Catalog saved as {filename}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the PDFCatalog
    catalog = PDFCatalog("Glass Products Catalog")

    # Add a page to the catalog
    catalog.add_page()

    # Define product data (name, description, image path)
    products = [
        {
            "name": "Laminated Glass",
            "description": "Laminated glass consists of two or more layers of glass with an interlayer. This type of glass is ideal for safety and security.",
            "image": "laminated_glass.jpg"
        },
        {
            "name": "Reflective Glass",
            "description": "Reflective glass is coated with a thin layer of metal, creating a mirror-like appearance that reduces heat and glare.",
            "image": "reflective_glass.jpg"
        },
        {
            "name": "Decorative Glass",
            "description": "Decorative glass comes in various patterns and colors, used for aesthetic purposes in homes and buildings.",
            "image": "decorative_glass.jpg"
        }
    ]

    # Add each product to the catalog
    for product in products:
        catalog.add_product(product["name"], product["description"], product["image"])

    # Save the catalog to a PDF file
    catalog.save("glass_products_catalog.pdf")
```

**Note:** Ensure you have the `fpdf` and `PIL` (Pillow) libraries installed. You can install them using pip:

```bash
pip install fpdf Pillow
``` 

Make sure to replace the image paths with the correct paths to your images.
