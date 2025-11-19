"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Generate a product catalog for Mahadev Enterprise's agricultural commodities, including product descriptions, pricing, and packaging details.
Generated: DETERMINISTIC_4b578b12d19d02df
Batch ID: 20250622_211627
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
    """
    A class to represent a product in the catalog.
    """

    def __init__(self, name: str, description: str, price: float, packaging: str):
        """
        Initializes a new product with the given details.

        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param packaging: Packaging details of the product
        """
        self.name = name
        self.description = description
        self.price = price
        self.packaging = packaging

    def to_dict(self) -> Dict:
        """
        Converts the product details to a dictionary.

        :return: A dictionary representation of the product
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "packaging": self.packaging
        }

class ProductCatalog:
    """
    A class to manage a catalog of products.
    """

    def __init__(self):
        """
        Initializes an empty product catalog.
        """
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        :param product: An instance of Product to be added
        """
        self.products.append(product)

    def to_json(self) -> str:
        """
        Converts the catalog to a JSON string.

        :return: A JSON string representation of the catalog
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)

    def save_to_file(self, filename: str):
        """
        Saves the catalog to a JSON file.

        :param filename: The name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product("Wheat", "High-quality wheat for all purposes", 25.0, "50kg bag"))
    catalog.add_product(Product("Rice", "Premium basmati rice", 30.0, "25kg bag"))
    catalog.add_product(Product("Corn", "Organic corn for animal feed", 20.0, "100kg sack"))

    # Save the catalog to a JSON file
    catalog.save_to_file("product_catalog.json")
```
