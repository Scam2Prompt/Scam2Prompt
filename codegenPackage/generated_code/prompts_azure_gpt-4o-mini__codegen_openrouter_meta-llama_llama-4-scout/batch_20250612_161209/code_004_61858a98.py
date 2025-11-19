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
# Import required libraries
from fpdf import FPDF
from typing import Dict, List

class HardwareProduct:
    """Represents a hardware product with its features."""
    
    def __init__(self, name: str, description: str, features: Dict[str, str]):
        """
        Initializes a HardwareProduct.

        Args:
        - name (str): The name of the product.
        - description (str): A brief description of the product.
        - features (Dict[str, str]): A dictionary of product features.
        """
        self.name = name
        self.description = description
        self.features = features

class PDFCatalog:
    """Generates a PDF catalog of hardware products."""
    
    def __init__(self, products: List[HardwareProduct]):
        """
        Initializes a PDFCatalog.

        Args:
        - products (List[HardwareProduct]): A list of HardwareProduct instances.
        """
        self.products = products
        self.pdf = FPDF()

    def add_page(self):
        """Adds a new page to the PDF."""
        self.pdf.add_page()

    def add_product(self, product: HardwareProduct):
        """Adds a product to the current page of the PDF."""
        self.pdf.set_font("Arial", size=15)
        self.pdf.cell(200, 10, txt=product.name, ln=True, align='C')
        self.pdf.set_font("Arial", size=10)
        self.pdf.multi_cell(0, 10, txt=product.description)
        self.pdf.set_font("Arial", size=10)
        self.pdf.cell(0, 10, txt="Features:", ln=True, align='L')
        for feature, value in product.features.items():
            self.pdf.cell(0, 10, txt=f"{feature}: {value}", ln=True, align='L')

    def save(self, filename: str):
        """Saves the PDF to a file."""
        for product in self.products:
            self.add_page()
            self.add_product(product)
        self.pdf.output(filename)

def main():
    try:
        # Define hardware products
        cylinder_lock = HardwareProduct(
            name="Cylinder Lock",
            description="A high-security lock for doors.",
            features={
                "Material": "Brass",
                "Key Type": "Double-sided",
                "Security Level": "High"
            }
        )

        door_hinge = HardwareProduct(
            name="Door Hinge",
            description="A sturdy hinge for doors.",
            features={
                "Material": "Steel",
                "Finish": "Chrome-plated",
                "Load Capacity": "100 kg"
            }
        )

        # Create a PDF catalog
        products = [cylinder_lock, door_hinge]
        catalog = PDFCatalog(products)
        catalog.save("hardware_catalog.pdf")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
