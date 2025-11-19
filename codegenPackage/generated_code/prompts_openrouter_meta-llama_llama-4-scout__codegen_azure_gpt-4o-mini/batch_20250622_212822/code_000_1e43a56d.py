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
from typing import List, Dict, Any

class Product:
    """Class to represent a product in the catalog."""
    
    def __init__(self, name: str, category: str, price: float, stock: int, description: str):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "description": self.description
        }

class ProductCatalog:
    """Class to manage a product catalog."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieve products by category."""
        return [product for product in self.products if product.category == category]

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = Product(**product_data)
                    self.add_product(product)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    catalog = ProductCatalog()

    # Adding products to the catalog
    catalog.add_product(Product("Casual Shirt", "Shirts", 29.99, 100, "A comfortable casual shirt."))
    catalog.add_product(Product("Formal Pants", "Pants", 49.99, 50, "Stylish formal pants for office wear."))
    catalog.add_product(Product("Leather Belt", "Accessories", 19.99, 200, "A classic leather belt."))

    # Save the catalog to a file
    catalog.save_to_file("product_catalog.json")

    # Load the catalog from a file
    catalog.load_from_file("product_catalog.json")

    # Retrieve and print products in the 'Shirts' category
    shirts = catalog.get_products_by_category("Shirts")
    for shirt in shirts:
        print(shirt.to_dict())
```
