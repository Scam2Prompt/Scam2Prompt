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

class PDFCatalog(FPDF):
    def header(self):
        # Set font for header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'CM-Canada Product Catalog', 0, 1, 'C')

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font for footer
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_product(self, title, description, image_path):
        # Add a new page
        self.add_page()
        # Title
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1)
        # Description
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, description)
        # Adding image
        if os.path.exists(image_path):
            try:
                # Resize image to fit the page width
                img = Image.open(image_path)
                img_width, img_height = img.size
                max_width = self.w - 20  # 10mm margins on each side
                img_ratio = img_height / img_width
                img_height = max_width * img_ratio
                self.image(image_path, x=10, w=max_width, h=img_height)
            except Exception as e:
                # Log error if image cannot be processed
                self.multi_cell(0, 10, f'Error loading image: {e}')
        else:
            self.multi_cell(0, 10, 'Image not found.')

def main():
    # Create a PDF catalog object
    pdf = PDFCatalog()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Define product lines with descriptions and images
    products = [
        {
            'title': 'PEX Systems (XPAND™)',
            'description': 'XPAND™ PEX systems are designed for durability and efficiency, providing exceptional performance in any plumbing application.',
            'image_path': 'images/xpand_pex.jpg'  # Path to the image file
        },
        {
            'title': 'Access Panels (Redeye™)',
            'description': 'Redeye™ access panels offer convenient access to walls and ceilings, making maintenance and monitoring easy and efficient.',
            'image_path': 'images/redeye_access_panel.jpg'  # Path to the image file
        }
    ]

    # Add products to the PDF
    for product in products:
        pdf.add_product(product['title'], product['description'], product['image_path'])

    # Save the PDF file
    try:
        output_file = 'cm_canada_product_catalog.pdf'
        pdf.output(output_file)
        print(f'PDF catalog generated: {output_file}')
    except Exception as e:
        print(f'Failed to save PDF: {e}')

if __name__ == '__main__':
    main()
```

Make sure to have the `fpdf2` and `Pillow` libraries installed in your Python environment. You can install them using pip:

```bash
pip install fpdf2 Pillow
```

Ensure that the image files specified in the `products` list exist in the correct location before running the script. Adjust the paths as necessary.
