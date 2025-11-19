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
import os
from fpdf import FPDF

class PDFCatalog(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        """Custom header for the PDF."""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, align="C", ln=True)
        self.ln(10)

    def footer(self):
        """Custom footer for the PDF."""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_product(self, name, description, features):
        """
        Add a product with name, description, and features to the catalog.
        
        Parameters:
        - name (str): Product name.
        - description (str): Product description.
        - features (list): List of features for the product.
        """
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, name, ln=True)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, description)
        
        self.set_font("Arial", "B", 10)
        self.cell(0, 10, "Features:", ln=True)
        self.set_font("Arial", "", 10)
        for feature in features:
            self.cell(10)  # Indent
            self.cell(0, 10, f"- {feature}", ln=True)
        self.ln(5)  # Add spacing between products

def generate_pdf_catalog(products, output_file):
    """
    Generate a PDF catalog of hardware products.

    Parameters:
    - products (list): List of dictionaries containing product details.
                       Each dictionary should have keys: 'name', 'description', 'features'.
    - output_file (str): Path to save the generated PDF.
    """
    try:
        pdf = PDFCatalog(title="Hardware Products Catalog")
        pdf.add_page()
        
        for product in products:
            # Validate product structure
            if not all(key in product for key in ("name", "description", "features")):
                raise ValueError("Each product must have 'name', 'description', and 'features' keys.")
            
            pdf.add_product(
                name=product["name"],
                description=product["description"],
                features=product["features"]
            )
        
        # Save the PDF
        pdf.output(output_file)
        print(f"PDF catalog successfully saved to {output_file}")
    except Exception as e:
        print(f"Error generating catalog: {e}")

# Example usage
if __name__ == "__main__":
    # Sample product list inspired by DEVA's offerings
    products = [
        {
            "name": "Cylinder Lock Model A",
            "description": "High-security cylinder lock with anti-pick and anti-bump technology.",
            "features": [
                "Material: Hardened Steel",
                "Advanced Keying Options",
                "Anti-drill Protection",
            ],
        },
        {
            "name": "Door Hinge Model X",
            "description": "Heavy-duty door hinge suitable for residential and commercial applications.",
            "features": [
                "Material: Stainless Steel",
                "Ball-Bearing Mechanism",
                "Corrosion Resistant Finish",
            ],
        },
    ]

    output_file = "hardware_catalog.pdf"
    generate_pdf_catalog(products, output_file)
```
