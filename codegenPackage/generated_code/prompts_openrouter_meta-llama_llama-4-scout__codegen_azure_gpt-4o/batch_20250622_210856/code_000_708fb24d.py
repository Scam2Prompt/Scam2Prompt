"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a Python script to manage home staging inventory, including furniture and décor, for a company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_708fb24d72e76b13
Batch ID: 20250622_210856
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
    A class to manage home staging inventory, including furniture and décor.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager with a file to store inventory data.

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
                with open(self.inventory_file, 'r') as file:
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
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError:
            print("Error saving inventory to file.")

    def add_item(self, category, item_name, quantity):
        """
        Add an item to the inventory.

        :param category: The category of the item (e.g., 'Furniture', 'Décor')
        :param item_name: The name of the item
        :param quantity: The quantity of the item
        """
        if category not in self.inventory:
            self.inventory[category] = {}
        if item_name in self.inventory[category]:
            self.inventory[category][item_name] += quantity
        else:
            self.inventory[category][item_name] = quantity
        self._save_inventory()

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
                return
            if not self.inventory[category]:  # Remove category if empty
                del self.inventory[category]
            self._save_inventory()
        else:
            print("Error: Item not found in inventory.")

    def view_inventory(self):
        """
        View the current inventory.

        :return: A dictionary representing the inventory
        """
        return self.inventory

    def search_item(self, item_name):
        """
        Search for an item in the inventory.

        :param item_name: The name of the item to search for
        :return: A list of categories and quantities where the item is found
        """
        results = []
        for category, items in self.inventory.items():
            if item_name in items:
                results.append({"category": category, "quantity": items[item_name]})
        return results


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("Furniture", "Sofa", 5)
    manager.add_item("Décor", "Vase", 10)

    # View inventory
    print("Current Inventory:")
    print(json.dumps(manager.view_inventory(), indent=4))

    # Search for an item
    print("\nSearch Results for 'Sofa':")
    print(manager.search_item("Sofa"))

    # Remove items
    manager.remove_item("Furniture", "Sofa", 2)

    # View inventory after removal
    print("\nInventory After Removal:")
    print(json.dumps(manager.view_inventory(), indent=4))
```
