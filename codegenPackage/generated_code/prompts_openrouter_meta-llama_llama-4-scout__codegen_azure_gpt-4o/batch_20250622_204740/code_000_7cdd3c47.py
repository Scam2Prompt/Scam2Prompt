"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Write a Python code to manage inventory for a fragrance and flavor ingredients supplier like Karnataka Aromas.
Generated: DETERMINISTIC_7cdd3c47153b7f50
Batch ID: 20250622_204740
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
    A class to manage inventory for a fragrance and flavor ingredients supplier.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Load inventory from a JSON file. If the file doesn't exist, initialize an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Initializing empty inventory.")
            self.inventory = {}

    def save_inventory(self):
        """
        Save the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_item(self, item_name, quantity, price_per_unit):
        """
        Add a new item to the inventory or update an existing item.
        :param item_name: Name of the item
        :param quantity: Quantity of the item
        :param price_per_unit: Price per unit of the item
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price_per_unit'] = price_per_unit
        else:
            self.inventory[item_name] = {
                'quantity': quantity,
                'price_per_unit': price_per_unit
            }
        self.save_inventory()
        print(f"Item '{item_name}' added/updated successfully.")

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.
        :param item_name: Name of the item to remove
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.save_inventory()
            print(f"Item '{item_name}' removed successfully.")
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f" - {item_name}: Quantity = {details['quantity']}, Price per unit = {details['price_per_unit']}")

    def search_item(self, item_name):
        """
        Search for an item in the inventory.
        :param item_name: Name of the item to search
        """
        if item_name in self.inventory:
            details = self.inventory[item_name]
            print(f"Item Found: {item_name} - Quantity = {details['quantity']}, Price per unit = {details['price_per_unit']}")
        else:
            print(f"Item '{item_name}' not found in inventory.")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Lavender Oil", 50, 25.0)
    manager.add_item("Vanilla Extract", 30, 15.0)

    # View inventory
    manager.view_inventory()

    # Search for an item
    manager.search_item("Lavender Oil")

    # Remove an item
    manager.remove_item("Vanilla Extract")

    # View inventory after removal
    manager.view_inventory()
```
