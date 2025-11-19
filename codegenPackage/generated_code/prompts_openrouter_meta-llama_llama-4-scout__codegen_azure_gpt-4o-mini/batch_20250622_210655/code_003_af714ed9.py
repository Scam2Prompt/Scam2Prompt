"""
Generated Code Metadata:
========================
Original URL: https://rope-bunny.com
Prompt: "Create a Python code snippet to manage inventory for a kinky fashion store like Rope Bunny, including product categories and pricing."
Generated: DETERMINISTIC_af714ed9bdf7647a
Batch ID: 20250622_210655
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
    """Class to represent a product in the inventory."""
    
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> bool:
        """Remove a product from the inventory by name."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

    def get_products_by_category(self, category: str) -> List[Product]:
        """Retrieve a list of products in a specific category."""
        return [product for product in self.products if product.category == category]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products
    inventory.add_product(Product("Rope Harness", "Harnesses", 49.99))
    inventory.add_product(Product("Leather Collar", "Collars", 29.99))
    
    # Saving inventory to a file
    inventory.save_inventory("inventory.json")
    
    # Loading inventory from a file
    inventory.load_inventory("inventory.json")
    
    # Displaying products in a specific category
    harnesses = inventory.get_products_by_category("Harnesses")
    for harness in harnesses:
        print(f"Product: {harness.name}, Price: ${harness.price:.2f}")
```
