"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script that manages inventory for door knobs and levers, focusing on finishes like satin nickel and bronze.
Generated: DETERMINISTIC_fd3130f7306b6e8a
Batch ID: 20250612_162050
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
    """A class to manage the inventory of door knobs and levers with various finishes."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, finish, quantity):
        """Add a new item to the inventory or update the quantity if it already exists."""
        if item_name not in self.inventory:
            self.inventory[item_name] = {}
        if finish not in self.inventory[item_name]:
            self.inventory[item_name][finish] = 0
        self.inventory[item_name][finish] += quantity
        self.save_inventory()

    def remove_item(self, item_name, finish, quantity):
        """Remove a specified quantity of an item from the inventory."""
        try:
            if item_name in self.inventory and finish in self.inventory[item_name]:
                if self.inventory[item_name][finish] >= quantity:
                    self.inventory[item_name][finish] -= quantity
                    if self.inventory[item_name][finish] == 0:
                        del self.inventory[item_name][finish]
                    if not self.inventory[item_name]:  # Remove item if no finishes left
                        del self.inventory[item_name]
                    self.save_inventory()
                else:
                    raise ValueError("Not enough quantity to remove.")
            else:
                raise KeyError("Item or finish not found in inventory.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item, finishes in self.inventory.items():
            for finish, quantity in finishes.items():
                print(f"{item} - {finish}: {quantity}")

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding items to the inventory
    manager.add_item("Door Knob", "Satin Nickel", 10)
    manager.add_item("Door Lever", "Bronze", 5)

    # Displaying the current inventory
    manager.display_inventory()

    # Removing items from the inventory
    manager.remove_item("Door Knob", "Satin Nickel", 3)

    # Displaying the updated inventory
    manager.display_inventory()
```
