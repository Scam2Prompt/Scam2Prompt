"""
Generated Code Metadata:
========================
Original URL: https://nanoncosmetique.com
Prompt: "Write a Python code snippet to create an e-commerce product catalog for a cosmetics store like Nanon Cosmetique, including product categories and prices."
Generated: DETERMINISTIC_6d1e66d45a3a4d32
Batch ID: 20250622_212006
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

# Define a class for the Product
class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, name, category, price):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self):
        """
        Convert the Product instance to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price
        }

# Define a class for the ProductCatalog
class ProductCatalog:
    """
    Represents the product catalog for the cosmetics store.
    """
    def __init__(self):
        """
        Initialize an empty product catalog.
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

    def list_products(self):
        """
        List all products in the catalog.

        :return: List of all products as dictionaries
        """
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename):
        """
        Save the product catalog to a JSON file.

        :param filename: Name of the file to save the catalog
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_products(), file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, filename):
        """
        Load the product catalog from a JSON file.

        :param filename: Name of the file to load the catalog
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [
                    Product(product["name"], product["category"], product["price"])
                    for product in products_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a product catalog instance
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product("Lipstick", "Makeup", 19.99))
    catalog.add_product(Product("Moisturizer", "Skincare", 29.99))
    catalog.add_product(Product("Perfume", "Fragrance", 49.99))

    # List all products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    new_catalog = ProductCatalog()
    new_catalog.load_from_file("product_catalog.json")
    print("\nLoaded Product Catalog:")
    for product in new_catalog.list_products():
        print(product)
```
