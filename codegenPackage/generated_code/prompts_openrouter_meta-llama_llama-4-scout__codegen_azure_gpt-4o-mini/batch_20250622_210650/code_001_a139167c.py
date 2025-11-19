"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Write a Python script to manage inventory for a special effects company like Agnelo SFX."
Generated: DETERMINISTIC_a139167cc2e6ffe0
Batch ID: 20250622_210650
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
    """A class to manage inventory for a special effects company."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from the inventory file.")
                    return {}
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, quantity, description=''):
        """Add a new item to the inventory."""
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists. Updating quantity.")
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {
                'quantity': quantity,
                'description': description
            }
        self.save_inventory()
        print(f"Added/Updated item '{item_name}' with quantity {quantity}.")

    def remove_item(self, item_name, quantity):
        """Remove a specified quantity of an item from the inventory."""
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity:
                self.inventory[item_name]['quantity'] -= quantity
                if self.inventory[item_name]['quantity'] == 0:
                    del self.inventory[item_name]
                self.save_inventory()
                print(f"Removed {quantity} of item '{item_name}'.")
            else:
                print(f"Error: Not enough quantity of '{item_name}' to remove.")
        else:
            print(f"Error: Item '{item_name}' not found in inventory.")

    def view_inventory(self):
        """Display the current inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f"- {item_name}: {details['quantity']} (Description: {details['description']})")

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    while True:
        print("\nInventory Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            description = input("Enter description (optional): ")
            manager.add_item(name, quantity, description)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            manager.remove_item(name, quantity)
        elif choice == '3':
            manager.view_inventory()
        elif choice == '4':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
