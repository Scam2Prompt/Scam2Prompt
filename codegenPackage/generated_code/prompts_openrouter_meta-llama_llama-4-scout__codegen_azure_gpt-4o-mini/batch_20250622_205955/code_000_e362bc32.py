"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Write a Python code snippet to manage an e-commerce inventory system for a beauty store like Eclat, including products such as nail polish, nail art supplies, and eyelash extensions.
Generated: DETERMINISTIC_e362bc32664413e7
Batch ID: 20250622_205955
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
    
    def __init__(self, name: str, category: str, price: float, quantity: int):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
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

    def update_product_quantity(self, product_name: str, quantity: int) -> bool:
        """Update the quantity of a product in the inventory."""
        for product in self.products:
            if product.name == product_name:
                product.quantity = quantity
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get a list of all products in the inventory."""
        return [product.to_dict() for product in self.products]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products
    inventory.add_product(Product("Nail Polish", "Nail Care", 9.99, 100))
    inventory.add_product(Product("Nail Art Supplies", "Nail Care", 15.99, 50))
    inventory.add_product(Product("Eyelash Extensions", "Eye Care", 29.99, 30))

    # Updating product quantity
    inventory.update_product_quantity("Nail Polish", 90)

    # Saving inventory to a file
    inventory.save_inventory("inventory.json")

    # Loading inventory from a file
    inventory.load_inventory("inventory.json")

    # Displaying the inventory
    print(inventory.get_inventory())
```
