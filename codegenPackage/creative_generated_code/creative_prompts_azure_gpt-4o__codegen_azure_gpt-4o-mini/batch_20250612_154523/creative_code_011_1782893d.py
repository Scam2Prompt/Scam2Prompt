"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write a program to manage inventory and fiscalized goods using SIAF (Sistema Integrado de Administración Financiera), as taught in the "Gestión de Tesorería con el SIAF" course on AulaContable.
Generated: DETERMINISTIC_1782893db3e2aa0c
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class InventoryManager:
    """
    A class to manage inventory and fiscalized goods using SIAF (Sistema Integrado de Administración Financiera).
    """

    def __init__(self, inventory_file='inventory.json'):
        """
        Initializes the InventoryManager with the specified inventory file.

        Args:
            inventory_file (str): Path to the inventory JSON file.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from the JSON file. If the file does not exist, returns an empty dictionary.

        Returns:
            dict: The loaded inventory.
        """
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: JSON decode error. Returning an empty inventory.")
                    return {}
        return {}

    def save_inventory(self):
        """Saves the current inventory to the JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_code, item_name, quantity, price):
        """
        Adds a new item to the inventory.

        Args:
            item_code (str): Unique code for the item.
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            price (float): Price of the item.

        Raises:
            ValueError: If the quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        self.inventory[item_code] = {
            'name': item_name,
            'quantity': quantity,
            'price': price
        }
        self.save_inventory()

    def update_item(self, item_code, quantity=None, price=None):
        """
        Updates the quantity and/or price of an existing item in the inventory.

        Args:
            item_code (str): Unique code for the item.
            quantity (int, optional): New quantity of the item.
            price (float, optional): New price of the item.

        Raises:
            KeyError: If the item code does not exist in the inventory.
        """
        if item_code not in self.inventory:
            raise KeyError("Item code not found in inventory.")

        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be non-negative.")
            self.inventory[item_code]['quantity'] = quantity

        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative.")
            self.inventory[item_code]['price'] = price

        self.save_inventory()

    def remove_item(self, item_code):
        """
        Removes an item from the inventory.

        Args:
            item_code (str): Unique code for the item.

        Raises:
            KeyError: If the item code does not exist in the inventory.
        """
        if item_code not in self.inventory:
            raise KeyError("Item code not found in inventory.")

        del self.inventory[item_code]
        self.save_inventory()

    def get_inventory(self):
        """
        Retrieves the current inventory.

        Returns:
            dict: The current inventory.
        """
        return self.inventory

def main():
    """Main function to demonstrate the InventoryManager."""
    manager = InventoryManager()

    try:
        # Adding sample items
        manager.add_item('001', 'Laptop', 10, 1500.00)
        manager.add_item('002', 'Smartphone', 25, 700.00)

        # Updating an item
        manager.update_item('001', quantity=8)

        # Removing an item
        manager.remove_item('002')

        # Print current inventory
        print(json.dumps(manager.get_inventory(), indent=4))
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
