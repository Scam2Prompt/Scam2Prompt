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
# Import necessary libraries
from fpdf import FPDF  # FPDF is a lightweight library for generating PDFs in Python

# Define a class for the PDF catalog
class PDFCatalog(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

    def header(self):
        """Define the header for each page."""
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Hardware Products Catalog", border=False, ln=True, align="C")
        self.ln(10)  # Add a line break

    def footer(self):
        """Define the footer for each page."""
        self.set_y(-15)  # Position footer at 15mm from the bottom
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", border=False, ln=True, align="C")

    def add_product(self, name, description, features):
        """
        Add a product to the catalog.
        
        :param name: Name of the product
        :param description: Short description of the product
        :param features: List of features for the product
        """
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, name, ln=True)  # Product name
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, description)  # Product description
        self.ln(5)  # Add a line break

        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "Features:", ln=True)
        self.set_font("Arial", size=12)
        for feature in features:
            self.cell(5)  # Indentation
            self.cell(0, 10, f"- {feature}", ln=True)  # List each feature
        self.ln(10)  # Add a line break after the product

# Function to generate the PDF catalog
def generate_pdf_catalog(output_file):
    """
    Generate a PDF catalog of hardware products.
    
    :param output_file: Path to save the generated PDF file
    """
    try:
        # Create an instance of the PDFCatalog class
        pdf = PDFCatalog()
        pdf.add_page()

        # Define the products
        products = [
            {
                "name": "Cylinder Lock",
                "description": "High-security cylinder lock suitable for residential and commercial use.",
                "features": [
                    "Durable stainless steel construction",
                    "Anti-pick and anti-drill technology",
                    "Available in multiple sizes and finishes"
                ]
            },
            {
                "name": "Door Hinge",
                "description": "Heavy-duty door hinge designed for smooth and silent operation.",
                "features": [
                    "Made from corrosion-resistant materials",
                    "Supports heavy doors up to 120kg",
                    "Easy installation with included screws"
                ]
            }
        ]

        # Add each product to the PDF
        for product in products:
            pdf.add_product(product["name"], product["description"], product["features"])

        # Output the PDF to a file
        pdf.output(output_file)
        print(f"PDF catalog successfully generated: {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the PDF catalog: {e}")

# Main execution
if __name__ == "__main__":
    # Specify the output file name
    output_file = "hardware_products_catalog.pdf"
    generate_pdf_catalog(output_file)
```

This code uses the `FPDF` library to generate a PDF catalog of hardware products, including cylinder locks and door hinges. It is clean, well-documented, and includes error handling for production readiness.
