"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for baby clothing and accessories, including product names, prices, and descriptions, similar to the ones listed on Somos Corujas.
Generated: DETERMINISTIC_6e390d6182ad20bb
Batch ID: 20250622_212549
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
    """Class to represent a product in the e-commerce catalog."""
    
    def __init__(self, name: str, price: float, description: str):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param price: The price of the product.
        :param description: A brief description of the product.
        """
        self.name = name
        self.price = price
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for easy serialization."""
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description
        }

class ProductCatalog:
    """Class to manage a catalog of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: An instance of Product to be added.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the catalog.")
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

    def save_to_file(self, filename: str):
        """
        Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Adding sample products to the catalog
    catalog.add_product(Product("Baby Onesie", 19.99, "Soft cotton onesie for babies."))
    catalog.add_product(Product("Diaper Bag", 49.99, "Stylish and functional diaper bag."))
    catalog.add_product(Product("Baby Booties", 15.99, "Warm and cozy booties for infants."))

    # Save the catalog to a JSON file
    catalog.save_to_file("baby_clothing_catalog.json")
```
