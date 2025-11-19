"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for auto parts, including product codes, names, and prices, similar to the one found on autopecasbrazz.
Generated: DETERMINISTIC_72c805eb833ca877
Batch ID: 20250622_205612
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
    
    def __init__(self, code: str, name: str, price: float):
        """
        Initialize a new product.

        :param code: Unique product code
        :param name: Name of the product
        :param price: Price of the product
        """
        self.code = code
        self.name = name
        self.price = price

    def to_dict(self) -> Dict[str, str]:
        """Convert the product to a dictionary format for easy serialization."""
        return {
            'code': self.code,
            'name': self.name,
            'price': self.price
        }

class ProductCatalog:
    """Class to manage a catalog of products."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the catalog.

        :param product: Product instance to be added
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

        :param filename: Name of the file to save the catalog
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
    catalog.add_product(Product("AP123", "Brake Pad", 29.99))
    catalog.add_product(Product("AP456", "Oil Filter", 15.49))
    catalog.add_product(Product("AP789", "Air Filter", 22.75))

    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")
```
