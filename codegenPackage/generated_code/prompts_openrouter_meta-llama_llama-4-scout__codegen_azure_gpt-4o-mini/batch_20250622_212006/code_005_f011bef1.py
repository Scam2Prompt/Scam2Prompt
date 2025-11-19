"""
Generated Code Metadata:
========================
Original URL: https://nanoncosmetique.com
Prompt: "Design a product information management system for a cosmetics company, including fields for product name, description, price, and image."
Generated: DETERMINISTIC_f011bef1dbd455ad
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_management.py

import os
import json
from typing import List, Dict, Any

class Product:
    """Class to represent a product in the cosmetics company."""
    
    def __init__(self, name: str, description: str, price: float, image_path: str):
        self.name = name
        self.description = description
        self.price = price
        self.image_path = image_path

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_path": self.image_path
        }

class ProductManager:
    """Class to manage a collection of products."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.products: List[Product] = []
        self.load_products()

    def load_products(self) -> None:
        """Load products from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    products_data = json.load(file)
                    self.products = [Product(**data) for data in products_data]
                except json.JSONDecodeError as e:
                    print(f"Error loading products: {e}")
                    self.products = []

    def save_products(self) -> None:
        """Save products to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=4)

    def add_product(self, product: Product) -> None:
        """Add a new product to the collection."""
        self.products.append(product)
        self.save_products()

    def get_all_products(self) -> List[Product]:
        """Return a list of all products."""
        return self.products

    def find_product_by_name(self, name: str) -> List[Product]:
        """Find products by name."""
        return [product for product in self.products if product.name.lower() == name.lower()]

# Example usage
if __name__ == "__main__":
    # Initialize the product manager with a storage file
    manager = ProductManager('products.json')

    # Create a new product
    new_product = Product(
        name="Lipstick",
        description="Long-lasting matte lipstick.",
        price=19.99,
        image_path="images/lipstick.jpg"
    )

    # Add the new product to the manager
    manager.add_product(new_product)

    # Retrieve and print all products
    all_products = manager.get_all_products()
    for product in all_products:
        print(product.to_dict())
```
