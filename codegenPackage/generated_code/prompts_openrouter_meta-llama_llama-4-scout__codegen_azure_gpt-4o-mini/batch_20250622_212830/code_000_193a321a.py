"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to create an inventory management system for a toolbox containing items like alicate, furadeira, martelo, and parafusadeira.
Generated: DETERMINISTIC_193a321af9c617ff
Batch ID: 20250622_212830
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
    """A class to manage the inventory of a toolbox."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load the inventory from a JSON file, or create a new one if it doesn't exist."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, quantity):
        """Add a specified quantity of an item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        self.save_inventory()

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[item_name] < quantity:
            raise ValueError("Not enough quantity to remove.")
        self.inventory[item_name] -= quantity
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
        self.save_inventory()

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("The inventory is empty.")
        else:
            print("Current Inventory:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

def main():
    """Main function to run the inventory management system."""
    manager = InventoryManager()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display inventory")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            try:
                manager.add_item(item_name, quantity)
                print(f"Added {quantity} of {item_name}.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            try:
                manager.remove_item(item_name, quantity)
                print(f"Removed {quantity} of {item_name}.")
            except (KeyError, ValueError) as e:
                print(e)

        elif choice == '3':
            manager.display_inventory()

        elif choice == '4':
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```
