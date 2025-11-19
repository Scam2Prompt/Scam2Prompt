"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Generate a Python script that simulates the inventory management for a hardware store, including tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_0e16e23d0579bb1c
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_management.py
# A Python script to simulate inventory management for a hardware store.

import sys

class InventoryManager:
    """Class to manage the inventory of a hardware store."""

    def __init__(self):
        # Initialize the inventory as a dictionary {item_name: quantity}.
        self.inventory = {
            "alicate": 10,
            "furadeira": 5,
            "parafusadeira": 8
        }

    def display_inventory(self):
        """Display the current inventory."""
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"- {item}: {quantity} units")
        print()

    def add_item(self, item_name, quantity):
        """
        Add items to the inventory.
        :param item_name: Name of the item to add.
        :param quantity: Quantity of the item to add.
        """
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return

        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        print(f"{quantity} units of '{item_name}' added to the inventory.")

    def remove_item(self, item_name, quantity):
        """
        Remove items from the inventory.
        :param item_name: Name of the item to remove.
        :param quantity: Quantity of the item to remove.
        """
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return

        if item_name not in self.inventory:
            print(f"Error: '{item_name}' does not exist in the inventory.")
            return

        if self.inventory[item_name] < quantity:
            print(f"Error: Not enough stock of '{item_name}' to remove {quantity} units.")
            return

        self.inventory[item_name] -= quantity
        print(f"{quantity} units of '{item_name}' removed from the inventory.")

        # Remove the item from the inventory if the quantity becomes zero.
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
            print(f"'{item_name}' removed from the inventory as its stock is now zero.")

    def handle_user_input(self):
        """Handle user input for inventory actions."""
        while True:
            print("\nOptions:")
            print("1. Display inventory")
            print("2. Add item")
            print("3. Remove item")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                self.display_inventory()
            elif choice == "2":
                item_name = input("Enter the name of the item to add: ").strip()
                try:
                    quantity = int(input("Enter the quantity to add: ").strip())
                    self.add_item(item_name, quantity)
                except ValueError:
                    print("Error: Quantity must be a valid integer.")
            elif choice == "3":
                item_name = input("Enter the name of the item to remove: ").strip()
                try:
                    quantity = int(input("Enter the quantity to remove: ").strip())
                    self.remove_item(item_name, quantity)
                except ValueError:
                    print("Error: Quantity must be a valid integer.")
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")

def main():
    """Main function to start the inventory management system."""
    print("Welcome to the Hardware Store Inventory Management System!")
    manager = InventoryManager()
    try:
        manager.handle_user_input()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
```
