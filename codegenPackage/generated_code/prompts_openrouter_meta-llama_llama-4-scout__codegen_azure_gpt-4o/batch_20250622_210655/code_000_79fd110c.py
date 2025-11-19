"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: "Write a Python script to manage an online store's inventory for Airsoft products, including tracking stock levels for items like Velcros Casco Balístico and Sudadera «GLITCH»."
Generated: DETERMINISTIC_79fd110c3cafcf3f
Batch ID: 20250622_210655
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
    A class to manage inventory for an online store selling Airsoft products.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.

        :param inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the JSON file. If the file doesn't exist, initialize an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty inventory
            self.inventory = {}
        except json.JSONDecodeError:
            # Handle corrupted JSON file
            print("Error: Inventory file is corrupted. Initializing empty inventory.")
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory data to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_item(self, item_name, stock):
        """
        Add a new item to the inventory or update the stock of an existing item.

        :param item_name: Name of the item.
        :param stock: Initial stock level for the item.
        """
        if stock < 0:
            print("Error: Stock level cannot be negative.")
            return

        self.inventory[item_name] = self.inventory.get(item_name, 0) + stock
        print(f"Item '{item_name}' added/updated with stock level: {self.inventory[item_name]}")
        self.save_inventory()

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.

        :param item_name: Name of the item to remove.
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Item '{item_name}' removed from inventory.")
            self.save_inventory()
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def update_stock(self, item_name, stock):
        """
        Update the stock level of an existing item.

        :param item_name: Name of the item.
        :param stock: New stock level for the item.
        """
        if stock < 0:
            print("Error: Stock level cannot be negative.")
            return

        if item_name in self.inventory:
            self.inventory[item_name] = stock
            print(f"Stock level for '{item_name}' updated to: {stock}")
            self.save_inventory()
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def check_stock(self, item_name):
        """
        Check the stock level of an item.

        :param item_name: Name of the item.
        :return: Stock level of the item or None if the item doesn't exist.
        """
        if item_name in self.inventory:
            print(f"Stock level for '{item_name}': {self.inventory[item_name]}")
            return self.inventory[item_name]
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")
            return None

    def display_inventory(self):
        """
        Display the entire inventory.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, stock in self.inventory.items():
                print(f" - {item}: {stock}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Velcros Casco Balístico", 10)
    manager.add_item("Sudadera «GLITCH»", 5)

    # Display inventory
    manager.display_inventory()

    # Update stock
    manager.update_stock("Velcros Casco Balístico", 15)

    # Check stock
    manager.check_stock("Sudadera «GLITCH»")

    # Remove an item
    manager.remove_item("Velcros Casco Balístico")

    # Display inventory again
    manager.display_inventory()
```
