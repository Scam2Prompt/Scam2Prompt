"""
Generated Code Metadata:
========================
Original URL: https://elfcosmetics.com.ua
Prompt: "Write a Python code snippet to create an e-commerce product catalog for ELF Cosmetics, including product categories for eyes, lips, and face, with prices and color options."
Generated: DETERMINISTIC_9b896bad549115ca
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a class for Product
class Product:
    def __init__(self, name, category, price, color_options):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product (e.g., eyes, lips, face)
        :param price: Price of the product in USD
        :param color_options: List of available color options for the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.color_options = color_options

    def to_dict(self):
        """
        Convert the Product instance to a dictionary for serialization.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "color_options": self.color_options,
        }

# Define a class for ProductCatalog
class ProductCatalog:
    def __init__(self):
        """
        Initialize an empty ProductCatalog instance.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: Product instance to add
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def get_products_by_category(self, category):
        """
        Retrieve all products in a specific category.

        :param category: Category to filter products by
        :return: List of products in the specified category
        """
        return [product.to_dict() for product in self.products if product.category == category]

    def to_json(self):
        """
        Serialize the entire catalog to JSON format.

        :return: JSON string representation of the catalog
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)

# Create an instance of ProductCatalog
catalog = ProductCatalog()

# Add products to the catalog
catalog.add_product(Product("Eyeshadow Palette", "eyes", 10.0, ["Nude", "Smoky", "Rose"]))
catalog.add_product(Product("Liquid Eyeliner", "eyes", 5.0, ["Black", "Brown"]))
catalog.add_product(Product("Matte Lipstick", "lips", 6.0, ["Red", "Pink", "Coral"]))
catalog.add_product(Product("Lip Gloss", "lips", 4.0, ["Clear", "Peach", "Berry"]))
catalog.add_product(Product("Foundation", "face", 12.0, ["Ivory", "Beige", "Tan"]))
catalog.add_product(Product("Blush", "face", 8.0, ["Peach", "Rose", "Mauve"]))

# Example usage
try:
    # Print all products in the catalog
    print("Full Product Catalog:")
    print(catalog.to_json())

    # Print products filtered by category
    print("\nProducts in 'eyes' category:")
    print(json.dumps(catalog.get_products_by_category("eyes"), indent=4))

except Exception as e:
    # Handle any unexpected errors
    print(f"An error occurred: {e}")
```
