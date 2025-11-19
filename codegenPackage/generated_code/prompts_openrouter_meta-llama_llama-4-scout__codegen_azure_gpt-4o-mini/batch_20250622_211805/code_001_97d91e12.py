"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Write a Python script to manage inventory for a packaging manufacturer that produces bakery and biscuit trays, ABS Atlas trays, and other food packaging products."
Generated: DETERMINISTIC_97d91e120c9004f6
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class InventoryManager:
    """A class to manage the inventory of a packaging manufacturer."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_product(self, product_name, quantity):
        """Add a new product to the inventory or update the quantity if it exists."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity
        
        self.save_inventory()
        print(f"Added {quantity} of {product_name}. Current stock: {self.inventory[product_name]}")

    def remove_product(self, product_name, quantity):
        """Remove a specified quantity of a product from the inventory."""
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if self.inventory[product_name] < quantity:
            raise ValueError("Insufficient stock to remove the specified quantity.")
        
        self.inventory[product_name] -= quantity
        
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]
        
        self.save_inventory()
        print(f"Removed {quantity} of {product_name}. Current stock: {self.inventory.get(product_name, 0)}")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        
        print("Current Inventory:")
        for product, quantity in self.inventory.items():
            print(f"- {product}: {quantity}")

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding products
    try:
        manager.add_product("Bakery Tray", 50)
        manager.add_product("Biscuit Tray", 30)
        manager.add_product("ABS Atlas Tray", 20)
    except Exception as e:
        print(f"Error: {e}")

    # Displaying inventory
    manager.display_inventory()

    # Removing products
    try:
        manager.remove_product("Bakery Tray", 10)
    except Exception as e:
        print(f"Error: {e}")

    # Displaying inventory again
    manager.display_inventory()
```
