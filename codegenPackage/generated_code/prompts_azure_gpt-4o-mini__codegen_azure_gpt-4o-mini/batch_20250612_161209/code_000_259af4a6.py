"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Generate a code snippet for an inventory management system that tracks high-quality hardware products like hinges, locks, and latches, similar to those offered by DEVA.
Generated: DETERMINISTIC_259af4a66f9d96cd
Batch ID: 20250612_161209
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

class HardwareProduct:
    """Class representing a hardware product in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the product to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of hardware products."""
    
    def __init__(self):
        self.products: List[HardwareProduct] = []

    def add_product(self, product: HardwareProduct) -> None:
        """Add a new product to the inventory."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """Remove a product from the inventory by name."""
        self.products = [p for p in self.products if p.name != product_name]

    def update_product_quantity(self, product_name: str, quantity: int) -> None:
        """Update the quantity of a specific product."""
        for product in self.products:
            if product.name == product_name:
                product.quantity = quantity
                return
        raise ValueError(f"Product '{product_name}' not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get a list of all products in the inventory."""
        return [product.to_dict() for product in self.products]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [HardwareProduct(**data) for data in products_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products
    inventory.add_product(HardwareProduct("Heavy Duty Hinge", "Hinges", 100, 2.50))
    inventory.add_product(HardwareProduct("High Security Lock", "Locks", 50, 15.00))
    inventory.add_product(HardwareProduct("Stainless Steel Latch", "Latches", 75, 5.00))
    
    # Updating product quantity
    try:
        inventory.update_product_quantity("Heavy Duty Hinge", 90)
    except ValueError as e:
        print(e)

    # Saving inventory to file
    inventory.save_to_file("inventory.json")

    # Loading inventory from file
    inventory.load_from_file("inventory.json")

    # Displaying inventory
    print(inventory.get_inventory())
```
