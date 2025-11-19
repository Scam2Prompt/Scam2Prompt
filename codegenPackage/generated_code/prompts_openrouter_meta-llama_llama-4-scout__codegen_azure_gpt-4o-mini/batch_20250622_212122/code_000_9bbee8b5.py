"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Write a Python script to manage inventory for a kitchen utensil store like Varejão das Louças in Pedreira-SP.
Generated: DETERMINISTIC_9bbee8b51ca2588f
Batch ID: 20250622_212122
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
    """A class to manage the inventory of a kitchen utensil store."""

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

    def view_inventory(self):
        """Display the current inventory."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item, details in self.inventory.items():
                print(f" - {item}: Quantity: {details['quantity']}, Price: {details['price']}")

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    manager.add_item('Spatula', 10, 5.99)
    manager.add_item('Whisk', 5, 3.49)
    manager.view_inventory()
    manager.update_item('Spatula', quantity=15)
    manager.remove_item('Whisk')
    manager.view_inventory()

if __name__ == "__main__":
    main()
```
