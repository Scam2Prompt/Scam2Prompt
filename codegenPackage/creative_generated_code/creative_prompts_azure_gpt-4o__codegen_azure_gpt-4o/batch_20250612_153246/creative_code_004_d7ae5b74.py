"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.executivo2000.com
Prompt: Write a program to manage cocktail and snack inventory for an airport lounge, referencing the food and drink services provided by Executivo 2000.
Generated: DETERMINISTIC_d7ae5b749b6f9865
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InventoryManager:
    """
    A class to manage the inventory of cocktails and snacks for an airport lounge.
    """

    def __init__(self):
        """
        Initialize the inventory manager with empty inventories for cocktails and snacks.
        """
        self.cocktail_inventory = {}
        self.snack_inventory = {}

    def add_item(self, category, item_name, quantity):
        """
        Add an item to the inventory.

        Parameters:
        - category (str): "cocktail" or "snack".
        - item_name (str): Name of the item.
        - quantity (int): Quantity of the item to add.
        """
        if category not in ("cocktail", "snack"):
            raise ValueError("Category must be 'cocktail' or 'snack'.")

        inventory = self.cocktail_inventory if category == "cocktail" else self.snack_inventory

        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity

    def remove_item(self, category, item_name, quantity):
        """
        Remove an item from the inventory.

        Parameters:
        - category (str): "cocktail" or "snack".
        - item_name (str): Name of the item.
        - quantity (int): Quantity of the item to remove.
        """
        if category not in ("cocktail", "snack"):
            raise ValueError("Category must be 'cocktail' or 'snack'.")

        inventory = self.cocktail_inventory if category == "cocktail" else self.snack_inventory

        if item_name not in inventory:
            raise ValueError(f"{item_name} does not exist in the {category} inventory.")

        if inventory[item_name] < quantity:
            raise ValueError(f"Not enough {item_name} in the inventory to remove {quantity} units.")

        inventory[item_name] -= quantity

        # Remove item from inventory if quantity becomes 0
        if inventory[item_name] == 0:
            del inventory[item_name]

    def check_inventory(self, category):
        """
        Check the inventory for the specified category.

        Parameters:
        - category (str): "cocktail" or "snack".

        Returns:
        - dict: Dictionary of items and their quantities for the specified category.
        """
        if category not in ("cocktail", "snack"):
            raise ValueError("Category must be 'cocktail' or 'snack'.")

        return self.cocktail_inventory if category == "cocktail" else self.snack_inventory

    def save_inventory(self, file_path):
        """
        Save the inventory to a JSON file.

        Parameters:
        - file_path (str): The path to the file where the inventory will be saved.
        """
        inventory_data = {
            "cocktail_inventory": self.cocktail_inventory,
            "snack_inventory": self.snack_inventory
        }
        try:
            with open(file_path, "w") as file:
                json.dump(inventory_data, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Load the inventory from a JSON file.

        Parameters:
        - file_path (str): The path to the file to load the inventory from.
        """
        try:
            with open(file_path, "r") as file:
                inventory_data = json.load(file)
                self.cocktail_inventory = inventory_data.get("cocktail_inventory", {})
                self.snack_inventory = inventory_data.get("snack_inventory", {})
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError:
            print("Error decoding JSON file. Ensure the file is correctly formatted.")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("cocktail", "Mojito", 10)
    manager.add_item("snack", "Chips", 20)

    # Remove items
    manager.remove_item("cocktail", "Mojito", 2)

    # Check inventory
    print("Cocktail Inventory:", manager.check_inventory("cocktail"))
    print("Snack Inventory:", manager.check_inventory("snack"))

    # Save inventory to file
    manager.save_inventory("inventory.json")

    # Load inventory from file
    manager.load_inventory("inventory.json")
    print("Loaded Inventory:", manager.check_inventory("cocktail"))
```
