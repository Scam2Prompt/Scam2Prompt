"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: "Write a Python script to manage an online store's inventory for Airsoft products, including tracking stock levels for items like Velcros Casco Balístico and Sudadera «GLITCH»."
Generated: DETERMINISTIC_79fd110c3cafcf3f
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
import os

class InventoryManager:
    """A class to manage the inventory of an online store for Airsoft products."""

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

    def add_item(self, item_name, quantity):
        """Add a new item to the inventory or update the quantity if it exists."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        self.save_inventory()

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[item_name] < quantity:
            raise ValueError("Insufficient stock to remove the specified quantity.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
        self.save_inventory()

    def check_stock(self, item_name):
        """Check the stock level of a specific item."""
        return self.inventory.get(item_name, 0)

    def list_inventory(self):
        """List all items in the inventory with their stock levels."""
        return self.inventory

def main():
    """Main function to demonstrate the InventoryManager functionality."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_item("Velcros Casco Balístico", 10)
        manager.add_item("Sudadera «GLITCH»", 5)
        print("Current Inventory:", manager.list_inventory())

        manager.remove_item("Velcros Casco Balístico", 3)
        print("Updated Inventory:", manager.list_inventory())

        stock_level = manager.check_stock("Sudadera «GLITCH»")
        print(f"Stock level for Sudadera «GLITCH»: {stock_level}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
