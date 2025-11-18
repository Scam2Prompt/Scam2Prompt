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
"""
Inventory and Fiscalized Goods Management System using SIAF principles.
This program allows users to manage inventory and fiscalized goods 
as taught in the "Gestión de Tesorería con el SIAF" course.

Author: Expert Programmer
Date: DD-MM-YYYY
"""

import json
import os

# Constants
DATA_FILE = "inventory_data.json"

class InventoryManager:
    """Class to manage inventory and fiscalized goods."""

    def __init__(self):
        self.inventory = {}
        self.load_data()

    def load_data(self):
        """Load inventory data from a JSON file."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data: {e}")
                self.inventory = {}
        else:
            self.inventory = {}

    def save_data(self):
        """Save inventory data to a JSON file."""
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_item(self, item_name, quantity, fiscalized):
        """
        Add a new item to the inventory.
        
        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            fiscalized (bool): Whether the item is fiscalized.
        """
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists in the inventory.")
            return
        self.inventory[item_name] = {
            "quantity": quantity,
            "fiscalized": fiscalized
        }
        self.save_data()
        print(f"Item '{item_name}' added successfully.")

    def update_item(self, item_name, quantity=None, fiscalized=None):
        """
        Update an existing item in the inventory.
        
        Args:
            item_name (str): Name of the item.
            quantity (int, optional): New quantity of the item.
            fiscalized (bool, optional): New fiscalized status of the item.
        """
        if item_name not in self.inventory:
            print(f"Item '{item_name}' does not exist in the inventory.")
            return
        if quantity is not None:
            self.inventory[item_name]["quantity"] = quantity
        if fiscalized is not None:
            self.inventory[item_name]["fiscalized"] = fiscalized
        self.save_data()
        print(f"Item '{item_name}' updated successfully.")

    def delete_item(self, item_name):
        """
        Delete an item from the inventory.
        
        Args:
            item_name (str): Name of the item to delete.
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.save_data()
            print(f"Item '{item_name}' deleted successfully.")
        else:
            print(f"Item '{item_name}' does not exist in the inventory.")

    def list_items(self):
        """List all items in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Inventory:")
        for item_name, item_data in self.inventory.items():
            print(f"- {item_name}: Quantity={item_data['quantity']}, Fiscalized={item_data['fiscalized']}")

def main():
    """Main function to interact with the inventory manager."""
    manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. List Items")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                fiscalized = input("Is the item fiscalized? (yes/no): ").strip().lower() == "yes"
                manager.add_item(item_name, quantity, fiscalized)
            except ValueError:
                print("Invalid input. Quantity must be a number.")
        elif choice == "2":
            item_name = input("Enter item name: ")
            try:
                quantity = input("Enter new quantity (leave blank to skip): ")
                quantity = int(quantity) if quantity else None
                fiscalized = input("Is the item fiscalized? (yes/no/leave blank to skip): ").strip().lower()
                fiscalized = fiscalized == "yes" if fiscalized in ["yes", "no"] else None
                manager.update_item(item_name, quantity, fiscalized)
            except ValueError:
                print("Invalid input. Quantity must be a number.")
        elif choice == "3":
            item_name = input("Enter item name to delete: ")
            manager.delete_item(item_name)
        elif choice == "4":
            manager.list_items()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
