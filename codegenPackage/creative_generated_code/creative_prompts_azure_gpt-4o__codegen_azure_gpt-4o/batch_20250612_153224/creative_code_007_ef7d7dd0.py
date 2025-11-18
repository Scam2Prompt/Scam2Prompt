"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Write a program to manage inventory for a charitable bakery system, inspired by the "Aden Charity Bakery" initiative described on the Gulf and Aden Development and Humanitarian Services Authority's site.
Generated: DETERMINISTIC_ef7d7dd0106dff65
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: bakery_inventory.py

"""
Bakery Inventory Management System
Inspired by the Aden Charity Bakery initiative, this program allows a charitable bakery 
to manage its inventory efficiently. The system includes features to add items, 
update quantities, view inventory, and remove items.

Author: Expert Programmer
Date: 2023
"""

import sys

class BakeryInventory:
    def __init__(self):
        """
        Initialize an empty inventory dictionary.
        """
        self.inventory = {}

    def add_item(self, item_name, quantity):
        """
        Add a new item to the inventory or update the quantity of an existing item.
        
        :param item_name: str - Name of the item to add.
        :param quantity: int - Quantity of the item to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def update_item(self, item_name, new_quantity):
        """
        Update the quantity of an existing item in the inventory.
        
        :param item_name: str - Name of the item to update.
        :param new_quantity: int - New quantity of the item.
        """
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if item_name in self.inventory:
            self.inventory[item_name] = new_quantity
        else:
            raise KeyError(f"Item '{item_name}' not found in inventory.")

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.
        
        :param item_name: str - Name of the item to remove.
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
        else:
            raise KeyError(f"Item '{item_name}' not found in inventory.")

    def view_inventory(self):
        """
        View the current inventory.
        
        :return: dict - Dictionary containing the current inventory.
        """
        return self.inventory

def main():
    """
    Main function to interact with the BakeryInventory system.
    """
    inventory = BakeryInventory()

    while True:
        print("\n--- Aden Charity Bakery Inventory System ---")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            # Add item to inventory
            item_name = input("Enter item name: ").strip()
            try:
                quantity = int(input("Enter quantity: "))
                inventory.add_item(item_name, quantity)
                print(f"Item '{item_name}' added with quantity {quantity}.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 2:
            # Update item quantity
            item_name = input("Enter item name: ").strip()
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_item(item_name, new_quantity)
                print(f"Item '{item_name}' updated to quantity {new_quantity}.")
            except ValueError as e:
                print(f"Error: {e}")
            except KeyError as e:
                print(f"Error: {e}")
        
        elif choice == 3:
            # Remove item from inventory
            item_name = input("Enter item name to remove: ").strip()
            try:
                inventory.remove_item(item_name)
                print(f"Item '{item_name}' removed.")
            except KeyError as e:
                print(f"Error: {e}")
        
        elif choice == 4:
            # View inventory
            current_inventory = inventory.view_inventory()
            if not current_inventory:
                print("Inventory is empty.")
            else:
                print("\nCurrent Inventory:")
                for item, quantity in current_inventory.items():
                    print(f"{item}: {quantity}")
        
        elif choice == 5:
            # Exit the program
            print("Exiting Aden Charity Bakery Inventory System. Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
```
