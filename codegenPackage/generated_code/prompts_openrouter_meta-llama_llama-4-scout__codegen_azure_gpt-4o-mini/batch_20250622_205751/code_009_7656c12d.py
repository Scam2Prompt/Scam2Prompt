"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Write a script to generate a catalog of products and services offered by a sign manufacturing company like Nova Forma d.o.o."
Generated: DETERMINISTIC_7656c12d1a57262c
Batch ID: 20250622_205751
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
    """Class representing a product in the catalog."""
    
    def __init__(self, name: str, description: str, price: float, category: str):
        """
        Initialize a new product.

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param category: Category of the product
        """
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category
        }

class Catalog:
    """Class representing a catalog of products and services."""
    
    def __init__(self):
        """Initialize an empty catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the catalog.

        :param product: An instance of Product to add
        """
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

    def save_to_file(self, filename: str):
        """Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

def main():
    """Main function to create a product catalog and save it to a file."""
    catalog = Catalog()

    # Sample products
    catalog.add_product(Product("Vinyl Banner", "Durable vinyl banner for outdoor use", 150.00, "Banners"))
    catalog.add_product(Product("Acrylic Sign", "High-quality acrylic sign for indoor display", 200.00, "Signs"))
    catalog.add_product(Product("LED Sign", "Bright LED sign for visibility at night", 350.00, "Signs"))
    catalog.add_product(Product("Business Card", "Custom printed business cards", 50.00, "Prints"))
    catalog.add_product(Product("Vehicle Wrap", "Full vehicle wrap for advertising", 1200.00, "Wraps"))

    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")

if __name__ == "__main__":
    main()
```
