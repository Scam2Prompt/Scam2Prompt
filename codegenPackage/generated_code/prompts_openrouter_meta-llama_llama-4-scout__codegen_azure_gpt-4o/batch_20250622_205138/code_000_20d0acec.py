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
    """
    A class to manage inventory for tractor pulling equipment, including spare parts for engines and drivetrains.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager with a file to store inventory data.

        :param inventory_file: Path to the inventory file (default: 'inventory.json')
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the file. If the file does not exist, initialize an empty inventory.
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading inventory file: {e}")
                self.inventory = {}
        else:
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory data to the file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")

    def add_item(self, category, item_name, quantity):
        """
        Add an item to the inventory.

        :param category: The category of the item (e.g., 'Engine Parts', 'Drivetrain Parts')
        :param item_name: The name of the item
        :param quantity: The quantity of the item
        """
        if category not in self.inventory:
            self.inventory[category] = {}
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity
        self.save_inventory()

    def remove_item(self, category, item_name, quantity):
        """
        Remove an item or reduce its quantity in the inventory.

        :param category: The category of the item
        :param item_name: The name of the item
        :param quantity: The quantity to remove
        """
        if category in self.inventory and item_name in self.inventory[category]:
            if self.inventory[category][item_name] > quantity:
                self.inventory[category][item_name] -= quantity
            elif self.inventory[category][item_name] == quantity:
                del self.inventory[category][item_name]
            else:
                print("Error: Not enough quantity to remove.")
            self.save_inventory()
        else:
            print("Error: Item not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        print("Current Inventory:")
        for category, items in self.inventory.items():
            print(f"Category: {category}")
            for item_name, quantity in items.items():
                print(f"  {item_name}: {quantity}")

    def search_item(self, item_name):
        """
        Search for an item in the inventory.

        :param item_name: The name of the item to search for
        :return: A list of categories and quantities where the item is found
        """
        results = []
        for category, items in self.inventory.items():
            if item_name in items:
                results.append((category, items[item_name]))
        return results


# Main script
if __name__ == "__main__":
    manager = InventoryManager()

    # Example usage
    manager.add_item("Engine Parts", "Piston", 10)
    manager.add_item("Drivetrain Parts", "Gearbox", 5)
    manager.view_inventory()

    manager.remove_item("Engine Parts", "Piston", 3)
    manager.view_inventory()

    search_results = manager.search_item("Gearbox")
    if search_results:
        print("Search Results:")
        for category, quantity in search_results:
            print(f"Category: {category}, Quantity: {quantity}")
    else:
        print("Item not found.")
```
