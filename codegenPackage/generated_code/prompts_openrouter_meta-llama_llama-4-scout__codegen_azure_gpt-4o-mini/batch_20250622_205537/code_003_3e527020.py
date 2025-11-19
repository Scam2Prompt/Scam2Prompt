"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Write a Python script to create a simple music equipment inventory management system.
Generated: DETERMINISTIC_3e527020e40463ae
Batch ID: 20250622_205537
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
    """A class to manage a music equipment inventory."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_item(self, item_name, quantity, price):
        """Add a new item to the inventory."""
        if item_name in self.inventory:
            print(f"Item '{item_name}' already exists. Updating quantity.")
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()
        print(f"Added/Updated item '{item_name}' with quantity {quantity} and price {price}.")

    def remove_item(self, item_name):
        """Remove an item from the inventory."""
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.save_inventory()
            print(f"Removed item '{item_name}' from inventory.")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    def update_item(self, item_name, quantity=None, price=None):
        """Update the quantity or price of an existing item."""
        if item_name in self.inventory:
            if quantity is not None:
                self.inventory[item_name]['quantity'] = quantity
            if price is not None:
                self.inventory[item_name]['price'] = price
            self.save_inventory()
            print(f"Updated item '{item_name}'. New quantity: {quantity}, New price: {price}.")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    def display_inventory(self):
        """Display the current inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for item_name, details in self.inventory.items():
            print(f" - {item_name}: Quantity: {details['quantity']}, Price: {details['price']}")

def main():
    """Main function to run the inventory management system."""
    manager = InventoryManager()

    while True:
        print("\nMusic Equipment Inventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Display Inventory")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            manager.add_item(name, quantity, price)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            manager.remove_item(name)
        elif choice == '3':
            name = input("Enter item name to update: ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            manager.update_item(name, quantity, price)
        elif choice == '4':
            manager.display_inventory()
        elif choice == '5':
            print("Exiting the inventory management system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
