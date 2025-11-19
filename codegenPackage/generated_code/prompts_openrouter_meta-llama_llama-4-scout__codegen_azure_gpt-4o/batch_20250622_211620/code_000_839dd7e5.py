"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Write a Python code snippet to manage inventory for a wholesale distributor of natural stone products and deicing materials, including bulk salt and packaged deicers.
Generated: DETERMINISTIC_839dd7e5d6acf8d1
Batch ID: 20250622_211620
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
    A class to manage inventory for a wholesale distributor of natural stone products 
    and deicing materials, including bulk salt and packaged deicers.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item_name, category, quantity, unit_price):
        """
        Adds a new item to the inventory or updates an existing item.

        :param item_name: Name of the item (string)
        :param category: Category of the item (e.g., 'Natural Stone', 'Bulk Salt', 'Packaged Deicers') (string)
        :param quantity: Quantity of the item (integer)
        :param unit_price: Price per unit of the item (float)
        """
        if item_name in self.inventory:
            # Update existing item
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['unit_price'] = unit_price
        else:
            # Add new item
            self.inventory[item_name] = {
                'category': category,
                'quantity': quantity,
                'unit_price': unit_price
            }

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        :param item_name: Name of the item (string)
        :param quantity: Quantity to remove (integer)
        :raises ValueError: If the item does not exist or if the quantity to remove exceeds available stock.
        """
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' does not exist in the inventory.")
        
        if self.inventory[item_name]['quantity'] < quantity:
            raise ValueError(f"Insufficient stock for item '{item_name}'. Available: {self.inventory[item_name]['quantity']}, Requested: {quantity}")
        
        self.inventory[item_name]['quantity'] -= quantity
        
        # Remove item completely if quantity becomes zero
        if self.inventory[item_name]['quantity'] == 0:
            del self.inventory[item_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        :return: Dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.

        :param file_path: Path to the file where inventory will be saved (string)
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory from a JSON file.

        :param file_path: Path to the file from which inventory will be loaded (string)
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
    manager.add_item("Granite Slab", "Natural Stone", 50, 120.0)
    manager.add_item("Bulk Salt", "Bulk Salt", 200, 15.0)
    manager.add_item("Packaged Deicer", "Packaged Deicers", 100, 25.0)

    # Remove items from inventory
    try:
        manager.remove_item("Bulk Salt", 50)
    except ValueError as e:
        print(e)

    # Display current inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(manager.get_inventory())
```
