"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Write a Python code to manage an e-commerce store for figure skating accessories, including product categories for skates, clothing, and costumes."
Generated: DETERMINISTIC_aee4b34589fb20fb
Batch ID: 20250622_210806
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
    """Class to represent a product in the e-commerce store."""
    
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock
        }

class Store:
    """Class to manage the e-commerce store."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """Remove a product from the store by name."""
        self.products = [product for product in self.products if product.name != product_name]

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieve products by category."""
        return [product for product in self.products if product.category == category]

    def save_to_file(self, filename: str) -> None:
        """Save the store's products to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load products from a JSON file into the store."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate the store management."""
    store = Store()

    # Adding products to the store
    store.add_product(Product("Ice Skates", "Skates", 150.00, 10))
    store.add_product(Product("Skating Dress", "Clothing", 75.00, 5))
    store.add_product(Product("Figure Skating Costume", "Costumes", 120.00, 3))

    # Display products in the 'Clothing' category
    clothing_products = store.get_products_by_category("Clothing")
    print("Clothing Products:")
    for product in clothing_products:
        print(product.to_dict())

    # Save products to a file
    store.save_to_file("store_products.json")

    # Load products from a file
    new_store = Store()
    new_store.load_from_file("store_products.json")
    print("Loaded Products:")
    for product in new_store.products:
        print(product.to_dict())

if __name__ == "__main__":
    main()
```
