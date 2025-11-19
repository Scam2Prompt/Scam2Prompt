"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Write a Python script to manage an inventory of tractor pulling equipment, including tracking spare parts for engines and drivetrains, similar to what is discussed on jobbo.com.au."
Generated: DETERMINISTIC_20d0aceca3b670b3
Batch ID: 20250622_205138
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
    """A class to manage an inventory of tractor pulling equipment and spare parts."""

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

    def add_item(self, category, item_name, quantity):
        """Add a new item to the inventory under the specified category."""
        if category not in self.inventory:
            self.inventory[category] = {}
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity
        self.save_inventory()

    def remove_item(self, category, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        try:
            if category in self.inventory and item_name in self.inventory[category]:
                if self.inventory[category][item_name] >= quantity:
                    self.inventory[category][item_name] -= quantity
                    if self.inventory[category][item_name] == 0:
                        del self.inventory[category][item_name]
                    self.save_inventory()
                else:
                    raise ValueError("Not enough quantity to remove.")
            else:
                raise KeyError("Item not found in inventory.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        for category, items in self.inventory.items():
            print(f"Category: {category}")
            for item, quantity in items.items():
                print(f"  {item}: {quantity}")
            print()

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    manager.add_item('Engines', 'Engine A', 5)
    manager.add_item('Drivetrains', 'Drivetrain A', 3)
    manager.remove_item('Engines', 'Engine A', 2)
    manager.display_inventory()

if __name__ == "__main__":
    main()
```
