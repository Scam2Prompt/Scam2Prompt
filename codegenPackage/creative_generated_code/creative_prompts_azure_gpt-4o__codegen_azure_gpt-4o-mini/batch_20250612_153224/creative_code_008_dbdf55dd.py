"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Recommend a library or tool to generate PDF catalogs for Ecoplast furniture, including product images, descriptions, and pricing.
Generated: DETERMINISTIC_dbdf55ddcd815a1a
Batch ID: 20250612_153224
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
from typing import List, Dict

class PDFCatalogGenerator:
    def __init__(self, title: str, output_file: str):
        """
        Initializes the PDF catalog generator.

        Args:
            title (str): The title of the catalog.
            output_file (str): The name of the output PDF file.
        """
        self.title = title
        self.output_file = output_file
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_product(self, product: Dict[str, str]) -> None:
        """
        Adds a product to the PDF catalog.

        Args:
            product (Dict[str, str]): A dictionary containing product details.
                Expected keys: 'image', 'description', 'price'.
        """
        if not all(key in product for key in ('image', 'description', 'price')):
            raise ValueError("Product must contain 'image', 'description', and 'price'.")

        # Add a new page for each product
        self.pdf.add_page()
        
        # Add image
        image_path = product['image']
        if os.path.exists(image_path):
            self.pdf.image(image_path, x=10, y=20, w=90)  # Adjust width as needed
        else:
            raise FileNotFoundError(f"Image file not found: {image_path}")

        # Add product description and price
        self.pdf.set_xy(10, 110)  # Set position to add text
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, f"Description: {product['description']}")
        self.pdf.multi_cell(0, 10, f"Price: {product['price']}")

    def generate_pdf(self) -> None:
        """
        Generates the PDF catalog and saves it to the specified output file.
        """
        try:
            self.pdf.set_title(self.title)
            self.pdf.output(self.output_file)
            print(f"Catalog generated successfully: {self.output_file}")
        except Exception as e:
            print(f"An error occurred while generating the PDF: {e}")

# Example usage
if __name__ == "__main__":
    catalog = PDFCatalogGenerator("Ecoplast Furniture Catalog", "ecoplast_catalog.pdf")

    products = [
        {"image": "path/to/image1.jpg", "description": "Stylish chair", "price": "$199"},
        {"image": "path/to/image2.jpg", "description": "Modern table", "price": "$299"},
        # Add more products as needed
    ]

    for product in products:
        try:
            catalog.add_product(product)
        except Exception as e:
            print(f"Failed to add product: {e}")

    catalog.generate_pdf()
```
