"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Illustrate how to use a library to generate a PDF catalog of hardware products, including features for items like cylinder locks and door hinges, inspired by DEVA's offerings.
Generated: DETERMINISTIC_61858a981ba02225
Batch ID: 20250612_161209
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

class PDFCatalog(FPDF):
    def header(self):
        """Add a header to the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Hardware Products Catalog', 0, 1, 'C')

    def footer(self):
        """Add a footer to the PDF."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_product(self, name, features):
        """Add a product section to the PDF."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, name, 0, 1)
        self.set_font('Arial', '', 10)
        for feature in features:
            self.cell(0, 10, f'- {feature}', 0, 1)
        self.ln(5)  # Add a line break after each product

def create_pdf_catalog(products, output_file):
    """Create a PDF catalog of hardware products.

    Args:
        products (dict): A dictionary where keys are product names and values are lists of features.
        output_file (str): The path to the output PDF file.
    """
    pdf = PDFCatalog()
    pdf.add_page()

    for product_name, features in products.items():
        pdf.add_product(product_name, features)

    try:
        pdf.output(output_file)
        print(f"Catalog successfully created: {output_file}")
    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")

if __name__ == "__main__":
    # Define the hardware products and their features
    hardware_products = {
        "Cylinder Lock": [
            "High security with anti-pick features",
            "Available in multiple finishes",
            "Easy installation with standard tools"
        ],
        "Door Hinge": [
            "Heavy-duty steel construction",
            "Rust-resistant coating",
            "Smooth operation with minimal friction"
        ]
    }

    # Specify the output PDF file path
    output_pdf_path = os.path.join(os.getcwd(), 'hardware_catalog.pdf')

    # Create the PDF catalog
    create_pdf_catalog(hardware_products, output_pdf_path)
```
