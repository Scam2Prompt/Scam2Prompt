"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Write a Python script to manage an inventory of 4x4 vehicle accessories, including items like skid plates, snorkels, and winches."
Generated: DETERMINISTIC_3962fe05efb02f9d
Batch ID: 20250622_210316
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
    """A class to manage an inventory of 4x4 vehicle accessories."""

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

    def add_item(self, item_name, quantity):
        """Add an item to the inventory with the specified quantity."""
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        self.save_inventory()

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                if self.inventory[item_name] == 0:
                    del self.inventory[item_name]
                self.save_inventory()
            else:
                raise ValueError(f"Cannot remove {quantity} of {item_name}. Only {self.inventory[item_name]} available.")
        else:
            raise KeyError(f"Item '{item_name}' not found in inventory.")

    def get_inventory(self):
        """Return the current inventory as a dictionary."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a user-friendly format."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_item("Skid Plate", 5)
        manager.add_item("Snorkel", 3)
        manager.add_item("Winch", 2)
        manager.display_inventory()

        manager.remove_item("Snorkel", 1)
        manager.display_inventory()

        manager.remove_item("Winch", 3)  # This will raise an error
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
