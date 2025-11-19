"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Create a Python script to manage inventory for an interior contracting company, including tracking materials for civil works, furniture, and electronic surveillance installations.
Generated: DETERMINISTIC_f5e9fbca7668f9d6
Batch ID: 20250612_153224
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
    """A class to manage inventory for an interior contracting company."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {'civil_works': {}, 'furniture': {}, 'electronic_surveillance': {}}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, category, item_name, quantity):
        """Add an item to the inventory under the specified category."""
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity
        
        self.save_inventory()

    def remove_item(self, category, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if category not in self.inventory:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.inventory.keys())}")
        
        if item_name not in self.inventory[category]:
            raise ValueError(f"Item '{item_name}' not found in category '{category}'.")

        if self.inventory[category][item_name] < quantity:
            raise ValueError(f"Not enough quantity of '{item_name}' to remove. Available: {self.inventory[category][item_name]}")

        self.inventory[category][item_name] -= quantity
        if self.inventory[category][item_name] == 0:
            del self.inventory[category][item_name]
        
        self.save_inventory()

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        for category, items in self.inventory.items():
            print(f"\nCategory: {category.capitalize()}")
            for item, quantity in items.items():
                print(f"  - {item}: {quantity}")

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding items to the inventory
    try:
        manager.add_item('civil_works', 'Cement', 50)
        manager.add_item('furniture', 'Chair', 20)
        manager.add_item('electronic_surveillance', 'Camera', 10)
    except ValueError as e:
        print(f"Error: {e}")

    # Removing items from the inventory
    try:
        manager.remove_item('furniture', 'Chair', 5)
    except ValueError as e:
        print(f"Error: {e}")

    # Displaying the current inventory
    manager.display_inventory()
```
