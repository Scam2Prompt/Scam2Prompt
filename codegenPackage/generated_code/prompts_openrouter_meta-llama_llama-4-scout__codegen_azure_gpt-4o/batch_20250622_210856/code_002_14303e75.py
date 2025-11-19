"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: "Generate a Python code snippet to manage an e-commerce inventory for gardening tools and machinery."
Generated: DETERMINISTIC_14303e752e7988e6
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

class InventoryManager:
    """
    A class to manage an e-commerce inventory for gardening tools and machinery.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initializes the InventoryManager with an inventory file.
        :param inventory_file: Path to the inventory file (default: inventory.json)
        """
        self.inventory_file = inventory_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from a JSON file. If the file doesn't exist, initializes an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Starting with an empty inventory.")
            self.inventory = {}

    def save_inventory(self):
        """
        Saves the current inventory to a JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save inventory. {e}")

    def add_item(self, item_name, quantity, price):
        """
        Adds a new item to the inventory or updates an existing item.
        :param item_name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price of the item
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.
        :param item_name: Name of the item to remove
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.save_inventory()
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def update_item(self, item_name, quantity=None, price=None):
        """
        Updates the quantity and/or price of an existing item.
        :param item_name: Name of the item to update
        :param quantity: New quantity (optional)
        :param price: New price (optional)
        """
        if item_name in self.inventory:
            if quantity is not None:
                self.inventory[item_name]['quantity'] = quantity
            if price is not None:
                self.inventory[item_name]['price'] = price
            self.save_inventory()
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def view_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, details in self.inventory.items():
                print(f"- {item}: Quantity={details['quantity']}, Price=${details['price']:.2f}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items
    manager.add_item("Lawn Mower", 10, 299.99)
    manager.add_item("Garden Rake", 25, 19.99)

    # View inventory
    manager.view_inventory()

    # Update an item
    manager.update_item("Garden Rake", quantity=30)

    # Remove an item
    manager.remove_item("Lawn Mower")

    # View inventory again
    manager.view_inventory()
```
