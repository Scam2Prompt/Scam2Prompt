"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deva.cl
Prompt: Illustrate how to use a library to generate a PDF catalog of hardware products, including features for items like cylinder locks and door hinges, inspired by DEVA's offerings.
Generated: DETERMINISTIC_61858a981ba02225
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from fpdf import FPDF

class PDFCatalog:
    def __init__(self, title):
        """Initialize the PDF catalog with a title."""
        self.pdf = FPDF()
        self.title = title
        self.products = []

    def add_product(self, name, features):
        """Add a product with its features to the catalog."""
        self.products.append({'name': name, 'features': features})

    def generate_pdf(self, filename):
        """Generate the PDF catalog and save it to the specified filename."""
        try:
            # Add a page to the PDF
            self.pdf.add_page()
            
            # Set title
            self.pdf.set_font('Arial', 'B', 16)
            self.pdf.cell(0, 10, self.title, ln=True, align='C')
            self.pdf.ln(10)  # Line break

            # Set font for product details
            self.pdf.set_font('Arial', '', 12)

            # Loop through products and add them to the PDF
            for product in self.products:
                self.pdf.cell(0, 10, f"Product: {product['name']}", ln=True)
                self.pdf.multi_cell(0, 10, f"Features: {', '.join(product['features'])}")
                self.pdf.ln(5)  # Space between products
            
            # Output the PDF to a file
            self.pdf.output(filename)
            print(f"PDF catalog '{filename}' generated successfully.")

        except Exception as e:
            print(f"An error occurred while generating the PDF: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the PDFCatalog
    catalog = PDFCatalog(title="Hardware Products Catalog")

    # Add products to the catalog
    catalog.add_product("Cylinder Lock", ["High security", "Durable", "Easy installation"])
    catalog.add_product("Door Hinge", ["Rust resistant", "Smooth operation", "Variety of finishes"])

    # Generate the PDF catalog
    catalog.generate_pdf("hardware_products_catalog.pdf")
```
