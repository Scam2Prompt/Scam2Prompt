"""
Generated Code Metadata:
========================
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for a men's fashion brand like Vila Romana, including categories for shirts, pants, and accessories.
Generated: DETERMINISTIC_1e43a56d1085613f
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, product_id, name, category, price, stock):
        """
        Initialize a product with its details.
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., 'Shirts', 'Pants', 'Accessories')
        :param price: Price of the product
        :param stock: Number of items available in stock
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self):
        """
        Convert the product object to a dictionary for serialization.
        :return: Dictionary representation of the product
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }


class ProductCatalog:
    """
    Represents the product catalog for the e-commerce platform.
    """
    def __init__(self):
        """
        Initialize an empty product catalog.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.
        :param product: Product object to be added
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product object")
        self.products.append(product)

    def get_products_by_category(self, category):
        """
        Retrieve all products in a specific category.
        :param category: Category name to filter products
        :return: List of products in the specified category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

    def save_to_file(self, file_path):
        """
        Save the product catalog to a JSON file.
        :param file_path: Path to the file where the catalog will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the product catalog from a JSON file.
        :param file_path: Path to the file from which the catalog will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                product_data = json.load(file)
                self.products = [Product(**data) for data in product_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product(1, "Classic White Shirt", "Shirts", 49.99, 20))
    catalog.add_product(Product(2, "Slim Fit Jeans", "Pants", 79.99, 15))
    catalog.add_product(Product(3, "Leather Belt", "Accessories", 29.99, 50))

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("product_catalog.json")

    # Retrieve products by category
    shirts = catalog.get_products_by_category("Shirts")
    for shirt in shirts:
        print(shirt.to_dict())
```
