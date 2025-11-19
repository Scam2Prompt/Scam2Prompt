"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Write a Python script to manage inventory for a snow cone truck business like King Of Icecream.
Generated: DETERMINISTIC_446b6d8fcc280854
Batch ID: 20250622_210650
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
    """
    A class to manage inventory for a snow cone truck business.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with a file to store inventory data.

        :param inventory_file: Path to the inventory file (default: 'inventory.json')
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self._load_inventory()

    def _load_inventory(self):
        """
        Load inventory from the file. If the file doesn't exist, initialize an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, "r") as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading inventory file. Initializing empty inventory.")
                self.inventory = {}
        else:
            self.inventory = {}

    def _save_inventory(self):
        """
        Save the current inventory to the file.
        """
        try:
            with open(self.inventory_file, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError:
            print("Error saving inventory to file.")

    def add_item(self, item_name, quantity):
        """
        Add a new item to the inventory or update the quantity of an existing item.

        :param item_name: Name of the item
        :param quantity: Quantity to add
        """
        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
        self._save_inventory()
        print(f"Added {quantity} of {item_name} to inventory.")

    def remove_item(self, item_name, quantity):
        """
        Remove a specified quantity of an item from the inventory.

        :param item_name: Name of the item
        :param quantity: Quantity to remove
        """
        if item_name not in self.inventory:
            print(f"Item '{item_name}' not found in inventory.")
            return

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if self.inventory[item_name] < quantity:
            print(f"Not enough {item_name} in inventory to remove {quantity}.")
            return

        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]  # Remove item if quantity reaches zero
        self._save_inventory()
        print(f"Removed {quantity} of {item_name} from inventory.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def clear_inventory(self):
        """
        Clear all items from the inventory.
        """
        self.inventory = {}
        self._save_inventory()
        print("Inventory cleared.")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Cherry Syrup", 10)
    manager.add_item("Ice Blocks", 20)

    # View inventory
    manager.view_inventory()

    # Remove items from inventory
    manager.remove_item("Cherry Syrup", 5)

    # View inventory again
    manager.view_inventory()

    # Clear inventory
    manager.clear_inventory()

    # View inventory after clearing
    manager.view_inventory()
```
