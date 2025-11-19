"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write a script to generate a printable brochure for food packaging solutions, including ABS Atlas trays and microwavable containers, based on Isoplas Corporation's product offerings.
Generated: DETERMINISTIC_d0145b6a1f1635c9
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# brochure_generator.py

from fpdf import FPDF
from typing import List

class Product:
    def __init__(self, name: str, description: str, dimensions: str, material: str):
        """
        Initialize a Product object.

        Args:
        - name (str): Product name
        - description (str): Product description
        - dimensions (str): Product dimensions
        - material (str): Product material
        """
        self.name = name
        self.description = description
        self.dimensions = dimensions
        self.material = material

class BrochureGenerator:
    def __init__(self, products: List[Product]):
        """
        Initialize a BrochureGenerator object.

        Args:
        - products (List[Product]): List of products to include in the brochure
        """
        self.products = products

    def generate_brochure(self, output_file: str):
        """
        Generate a printable brochure.

        Args:
        - output_file (str): Output file path
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Isoplas Corporation Food Packaging Solutions", ln=True, align='C')

        for product in self.products:
            pdf.ln(10)
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=product.name, ln=True, align='L')
            pdf.multi_cell(0, 10, txt=product.description)
            pdf.cell(200, 10, txt=f"Dimensions: {product.dimensions}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Material: {product.material}", ln=True, align='L')

        pdf.output(output_file)

def main():
    try:
        # Define products
        products = [
            Product(
                name="ABS Atlas Trays",
                description="Our ABS Atlas trays are designed for food packaging, offering excellent durability and resistance to extreme temperatures.",
                dimensions="12 x 8 x 2 inches",
                material="ABS (Acrylonitrile Butadiene Styrene)"
            ),
            Product(
                name="Microwavable Containers",
                description="Our microwavable containers are safe for reheating and offer a convenient solution for food packaging.",
                dimensions="10 x 6 x 1.5 inches",
                material="PP (Polypropylene)"
            )
        ]

        # Generate brochure
        generator = BrochureGenerator(products)
        output_file = "brochure.pdf"
        generator.generate_brochure(output_file)
        print(f"Brochure generated successfully: {output_file}")

    except Exception as e:
        print(f"Error generating brochure: {e}")

if __name__ == "__main__":
    main()
```
