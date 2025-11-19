"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: "Write a Python code snippet to manage the inventory of raw vegan desserts, including cakes like Snickers and Cheesecake de lamaie, with their respective ingredients and prices."
Generated: DETERMINISTIC_781551cc9d5ee1d4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

# Import necessary modules
import json

class InventoryManager:
    """
    A class to manage the inventory of raw vegan desserts.
    """

    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_dessert(self, name, ingredients, price):
        """
        Add a new dessert to the inventory.

        :param name: Name of the dessert (string)
        :param ingredients: List of ingredients (list of strings)
        :param price: Price of the dessert (float)
        """
        if name in self.inventory:
            raise ValueError(f"Dessert '{name}' already exists in the inventory.")
        self.inventory[name] = {
            "ingredients": ingredients,
            "price": price
        }

    def update_dessert(self, name, ingredients=None, price=None):
        """
        Update the details of an existing dessert.

        :param name: Name of the dessert (string)
        :param ingredients: Updated list of ingredients (list of strings, optional)
        :param price: Updated price of the dessert (float, optional)
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' does not exist in the inventory.")
        if ingredients is not None:
            self.inventory[name]["ingredients"] = ingredients
        if price is not None:
            self.inventory[name]["price"] = price

    def remove_dessert(self, name):
        """
        Remove a dessert from the inventory.

        :param name: Name of the dessert (string)
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' does not exist in the inventory.")
        del self.inventory[name]

    def get_dessert(self, name):
        """
        Retrieve details of a specific dessert.

        :param name: Name of the dessert (string)
        :return: Dictionary containing dessert details
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' does not exist in the inventory.")
        return self.inventory[name]

    def list_desserts(self):
        """
        List all desserts in the inventory.

        :return: Dictionary containing all desserts
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Save the inventory to a JSON file.

        :param file_path: Path to the file (string)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Load the inventory from a JSON file.

        :param file_path: Path to the file (string)
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse inventory file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add desserts
    manager.add_dessert("Snickers", ["dates", "peanuts", "cocoa powder"], 5.99)
    manager.add_dessert("Cheesecake de lamaie", ["cashews", "lemon juice", "coconut oil"], 6.99)

    # Update a dessert
    manager.update_dessert("Snickers", price=6.49)

    # List all desserts
    print("Current Inventory:")
    print(manager.list_desserts())

    # Save inventory to file
    manager.save_inventory("inventory.json")

    # Load inventory from file
    manager.load_inventory("inventory.json")
    print("Loaded Inventory:")
    print(manager.list_desserts())
```
