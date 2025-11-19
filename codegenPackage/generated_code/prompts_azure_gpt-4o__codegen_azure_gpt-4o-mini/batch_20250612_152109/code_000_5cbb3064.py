"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write Python code to generate a product catalog for a flip-flop manufacturing company, including categories like "Ojota Hombre Estampada Rider" and "Ojota Infantil Estampada 3D – Niñas," with descriptions and pricing.
Generated: DETERMINISTIC_5cbb30646ef3d3a3
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Product:
    """Class to represent a product in the catalog."""
    
    def __init__(self, name: str, category: str, description: str, price: float):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product
        :param description: Description of the product
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "price": self.price
        }

class ProductCatalog:
    """Class to manage a product catalog."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: Product instance to add
        """
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """Main function to create a product catalog and output it as JSON."""
    try:
        # Create a product catalog
        catalog = ProductCatalog()

        # Define products
        products = [
            Product("Ojota Hombre Estampada Rider", "Hombres", "Flip-flop estampada para hombres, cómoda y duradera.", 29.99),
            Product("Ojota Infantil Estampada 3D – Niñas", "Infantil", "Ojota 3D para niñas, divertida y colorida.", 19.99),
            Product("Ojota Hombre Clásica", "Hombres", "Ojota clásica, ideal para el verano.", 24.99),
            Product("Ojota Infantil Clásica", "Infantil", "Ojota clásica para niños, fácil de usar.", 14.99)
        ]

        # Add products to the catalog
        for product in products:
            catalog.add_product(product)

        # Output the catalog as JSON
        catalog_json = catalog.to_json()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
