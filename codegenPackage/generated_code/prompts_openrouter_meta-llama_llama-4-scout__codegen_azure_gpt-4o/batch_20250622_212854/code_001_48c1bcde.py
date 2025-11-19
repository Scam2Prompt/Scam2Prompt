"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Generate a Python code snippet to manage the inventory of PET bottles and jars for a company like MM Group.
Generated: DETERMINISTIC_48c1bcdea8f58c3f
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage the inventory of PET bottles and jars.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item_name, quantity):
        """
        Adds a new item or updates the quantity of an existing item in the inventory.

        :param item_name: Name of the item (e.g., 'PET Bottle', 'Jar')
        :param quantity: Quantity to add (must be a positive integer)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        :param item_name: Name of the item to remove
        :param quantity: Quantity to remove (must be a positive integer)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Not enough '{item_name}' in inventory to remove {quantity}.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]  # Remove item if quantity becomes zero

    def get_inventory(self):
        """
        Returns the current inventory as a dictionary.

        :return: Dictionary containing item names and their quantities
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory from a JSON file.

        :param file_path: Path to the file from which inventory will be loaded
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from file '{file_path}'.")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("PET Bottle", 100)
    manager.add_item("Jar", 50)

    # Remove items from inventory
    try:
        manager.remove_item("PET Bottle", 20)
    except Exception as e:
        print(f"Error: {e}")

    # Display current inventory
    print("Current Inventory:", manager.get_inventory())

    # Save inventory to file
    try:
        manager.save_inventory_to_file("inventory.json")
    except Exception as e:
        print(f"Error: {e}")

    # Load inventory from file
    try:
        manager.load_inventory_from_file("inventory.json")
        print("Loaded Inventory:", manager.get_inventory())
    except Exception as e:
        print(f"Error: {e}")
```
