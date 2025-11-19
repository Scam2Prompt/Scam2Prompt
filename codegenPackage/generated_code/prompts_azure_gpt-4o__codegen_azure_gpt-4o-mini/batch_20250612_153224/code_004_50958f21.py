"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Create a program that generates a catalog of carpentry products, including aluminum doors, iron railings, and glass installations, inspired by the product variety showcased by Aluivars.
Generated: DETERMINISTIC_50958f217db6c18d
Batch ID: 20250612_153224
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
    """Class representing a carpentry product."""
    
    def __init__(self, name: str, category: str, price: float, description: str):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product (e.g., Aluminum Door, Iron Railing, Glass Installation)
        :param price: Price of the product
        :param description: Description of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "description": self.description
        }

class ProductCatalog:
    """Class representing a catalog of carpentry products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: An instance of Product to be added
        """
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

    def save_to_file(self, filename: str):
        """
        Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

def main():
    """Main function to create and save a product catalog."""
    catalog = ProductCatalog()

    # Sample products
    catalog.add_product(Product("Aluminum Door Model A", "Aluminum Door", 299.99, "High-quality aluminum door with modern design."))
    catalog.add_product(Product("Iron Railing Model B", "Iron Railing", 199.99, "Durable iron railing for stairs and balconies."))
    catalog.add_product(Product("Glass Installation Model C", "Glass Installation", 399.99, "Elegant glass installation for residential and commercial use."))

    # Save the catalog to a JSON file
    catalog.save_to_file("carpentry_catalog.json")

if __name__ == "__main__":
    main()
```
