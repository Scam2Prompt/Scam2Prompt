"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Generate a product catalog for a factory producing flip-flops and shoe soles, including product descriptions for items like Ojota Infantil Estampada 3D – Niños and Suecos Hombre.
Generated: DETERMINISTIC_c551f605c57b77d5
Batch ID: 20250622_205709
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

    def __init__(self, name: str, description: str, price: float, category: str):
        """
        Initializes a new product with the given attributes.

        :param name: The name of the product.
        :param description: A brief description of the product.
        :param price: The price of the product.
        :param category: The category of the product (e.g., 'flip-flops', 'shoe soles').
        """
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def to_dict(self) -> Dict:
        """
        Converts the product instance to a dictionary.

        :return: A dictionary representation of the product.
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category
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

        :param product: An instance of Product to be added.
        """
        self.products.append(product)

    def to_json(self) -> str:
        """
        Converts the product catalog to a JSON string.

        :return: A JSON string representation of the product catalog.
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """
    Main function to create a product catalog and add products to it.
    """
    try:
        # Create a product catalog instance
        catalog = ProductCatalog()

        # Define products
        product1 = Product(
            name="Ojota Infantil Estampada 3D – Niños",
            description="Colorful 3D printed flip-flops for kids, perfect for summer fun.",
            price=19.99,
            category="flip-flops"
        )

        product2 = Product(
            name="Suecos Hombre",
            description="Comfortable clogs for men, ideal for casual wear and outdoor activities.",
            price=29.99,
            category="shoe soles"
        )

        # Add products to the catalog
        catalog.add_product(product1)
        catalog.add_product(product2)

        # Output the catalog as a JSON string
        catalog_json = catalog.to_json()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
