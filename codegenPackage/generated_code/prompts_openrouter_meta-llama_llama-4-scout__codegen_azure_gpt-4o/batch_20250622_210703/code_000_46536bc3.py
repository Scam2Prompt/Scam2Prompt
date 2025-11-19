"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a Python code snippet to manage inventory for a wholesale supplier of maritime equipment and services, including food, electrical equipment, and personal protective equipment.
Generated: DETERMINISTIC_46536bc35d23317f
Batch ID: 20250622_210703
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
    A class to manage inventory for a wholesale supplier of maritime equipment and services.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, category, item_name, quantity):
        """
        Adds an item to the inventory.

        :param category: The category of the item (e.g., 'Food', 'Electrical Equipment', 'PPE').
        :param item_name: The name of the item.
        :param quantity: The quantity of the item to add.
        """
        if category not in self.inventory:
            self.inventory[category] = {}
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity

    def remove_item(self, category, item_name, quantity):
        """
        Removes an item from the inventory.

        :param category: The category of the item.
        :param item_name: The name of the item.
        :param quantity: The quantity of the item to remove.
        :raises ValueError: If the item does not exist or if the quantity to remove exceeds the available quantity.
        """
        if category not in self.inventory or item_name not in self.inventory[category]:
            raise ValueError(f"Item '{item_name}' not found in category '{category}'.")
        if self.inventory[category][item_name] < quantity:
            raise ValueError(f"Insufficient quantity of '{item_name}' to remove.")
        self.inventory[category][item_name] -= quantity
        if self.inventory[category][item_name] == 0:
            del self.inventory[category][item_name]
        if not self.inventory[category]:
            del self.inventory[category]

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        :param file_path: The path to the file where the inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        :param file_path: The path to the file from which the inventory will be loaded.
        :raises IOError: If the file cannot be read.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Food", "Canned Tuna", 100)
    manager.add_item("Electrical Equipment", "Marine Battery", 50)
    manager.add_item("PPE", "Life Jacket", 200)

    # Remove items from inventory
    try:
        manager.remove_item("Food", "Canned Tuna", 20)
    except ValueError as e:
        print(e)

    # Display current inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Save inventory to file
    manager.save_inventory("inventory.json")

    # Load inventory from file
    manager.load_inventory("inventory.json")
    print("Loaded Inventory:")
    print(manager.get_inventory())
```
