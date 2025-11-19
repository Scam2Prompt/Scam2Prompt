"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to create an inventory management system for a toolbox containing items like alicate, furadeira, martelo, and parafusadeira.
Generated: DETERMINISTIC_193a321af9c617ff
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ToolboxInventory:
    def __init__(self):
        """
        Initializes the toolbox inventory with an empty dictionary.
        """
        self.inventory = {}

    def add_item(self, item_name, quantity):
        """
        Adds an item to the inventory or updates its quantity if it already exists.

        Args:
            item_name (str): Name of the item to add.
            quantity (int): Quantity of the item to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        Args:
            item_name (str): Name of the item to remove.
            quantity (int): Quantity of the item to remove.

        Raises:
            ValueError: If the item does not exist or if the quantity is invalid.
        """
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' does not exist in the inventory.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Not enough '{item_name}' in inventory to remove {quantity}.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]

    def view_inventory(self):
        """
        Returns the current inventory as a dictionary.

        Returns:
            dict: The current inventory.
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Saves the current inventory to a JSON file.

        Args:
            file_path (str): Path to the file where the inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads inventory data from a JSON file.

        Args:
            file_path (str): Path to the file from which the inventory will be loaded.

        Raises:
            IOError: If the file cannot be read.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid data in inventory file: {e}")


# Example usage
if __name__ == "__main__":
    toolbox = ToolboxInventory()

    try:
        # Add items to the inventory
        toolbox.add_item("alicate", 5)
        toolbox.add_item("furadeira", 2)
        toolbox.add_item("martelo", 3)
        toolbox.add_item("parafusadeira", 4)

        # View the inventory
        print("Current Inventory:", toolbox.view_inventory())

        # Remove items from the inventory
        toolbox.remove_item("martelo", 1)
        print("Inventory after removing 1 martelo:", toolbox.view_inventory())

        # Save the inventory to a file
        toolbox.save_inventory("toolbox_inventory.json")
        print("Inventory saved to 'toolbox_inventory.json'.")

        # Load the inventory from a file
        toolbox.load_inventory("toolbox_inventory.json")
        print("Inventory loaded from 'toolbox_inventory.json':", toolbox.view_inventory())

    except Exception as e:
        print(f"Error: {e}")
```
