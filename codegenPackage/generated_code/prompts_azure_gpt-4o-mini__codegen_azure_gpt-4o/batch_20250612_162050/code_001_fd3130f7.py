"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script that manages inventory for door knobs and levers, focusing on finishes like satin nickel and bronze.
Generated: DETERMINISTIC_fd3130f7306b6e8a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Inventory Management System for Door Knobs and Levers

This script allows users to manage inventory for door knobs and levers, 
focusing on finishes like satin nickel and bronze. It provides functionality 
to add, update, remove, and view inventory items.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

class InventoryManager:
    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        The inventory is stored as a dictionary with the following structure:
        {
            "item_name": {
                "type": "knob/lever",
                "finish": "satin nickel/bronze",
                "quantity": int
            }
        }
        """
        self.inventory = {}

    def add_item(self, item_name, item_type, finish, quantity):
        """
        Adds a new item to the inventory or updates an existing item.

        :param item_name: Name of the item (string)
        :param item_type: Type of the item ('knob' or 'lever') (string)
        :param finish: Finish of the item ('satin nickel' or 'bronze') (string)
        :param quantity: Quantity of the item (integer)
        """
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists. Updating quantity.")
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {
                "type": item_type,
                "finish": finish,
                "quantity": quantity
            }
        print(f"Item '{item_name}' added/updated successfully.")

    def update_item(self, item_name, quantity):
        """
        Updates the quantity of an existing item.

        :param item_name: Name of the item (string)
        :param quantity: New quantity of the item (integer)
        """
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] = quantity
            print(f"Item '{item_name}' updated successfully.")
        else:
            print(f"Error: Item '{item_name}' does not exist in the inventory.")

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.

        :param item_name: Name of the item (string)
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Item '{item_name}' removed successfully.")
        else:
            print(f"Error: Item '{item_name}' does not exist in the inventory.")

    def view_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f" - {item_name}: Type={details['type']}, Finish={details['finish']}, Quantity={details['quantity']}")

def main():
    """
    Main function to interact with the inventory manager.
    """
    manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            item_name = input("Enter item name: ")
            item_type = input("Enter item type (knob/lever): ").lower()
            finish = input("Enter finish (satin nickel/bronze): ").lower()
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                continue
            manager.add_item(item_name, item_type, finish, quantity)
        elif choice == 2:
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                continue
            manager.update_item(item_name, quantity)
        elif choice == 3:
            item_name = input("Enter item name: ")
            manager.remove_item(item_name)
        elif choice == 4:
            manager.view_inventory()
        elif choice == 5:
            print("Exiting the Inventory Management System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
```
