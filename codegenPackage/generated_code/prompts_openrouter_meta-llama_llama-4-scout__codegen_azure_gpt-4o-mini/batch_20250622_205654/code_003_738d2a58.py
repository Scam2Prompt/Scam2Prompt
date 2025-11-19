"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: "Write a Python script to manage inventory for an online store that sells upcycled products, such as plushies, miniatures, and potholders, with a focus on reducing waste and promoting sustainability."
Generated: DETERMINISTIC_738d2a58d63a6a44
Batch ID: 20250622_205654
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
    """A class to manage the inventory of an online store selling upcycled products."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Inventory file is corrupted. Starting with an empty inventory.")
                    return {}
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_product(self, product_name, quantity, price):
        """Add a new product to the inventory."""
        if product_name in self.inventory:
            print(f"Product '{product_name}' already exists. Updating quantity.")
            self.inventory[product_name]['quantity'] += quantity
        else:
            self.inventory[product_name] = {'quantity': quantity, 'price': price}
        self.save_inventory()
        print(f"Added/Updated product '{product_name}' with quantity {quantity} and price {price}.")

    def remove_product(self, product_name):
        """Remove a product from the inventory."""
        if product_name in self.inventory:
            del self.inventory[product_name]
            self.save_inventory()
            print(f"Removed product '{product_name}' from inventory.")
        else:
            print(f"Product '{product_name}' not found in inventory.")

    def update_product(self, product_name, quantity=None, price=None):
        """Update the quantity and/or price of an existing product."""
        if product_name in self.inventory:
            if quantity is not None:
                self.inventory[product_name]['quantity'] = quantity
            if price is not None:
                self.inventory[product_name]['price'] = price
            self.save_inventory()
            print(f"Updated product '{product_name}'. New quantity: {quantity}, New price: {price}.")
        else:
            print(f"Product '{product_name}' not found in inventory.")

    def list_inventory(self):
        """List all products in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for product, details in self.inventory.items():
            print(f"- {product}: Quantity: {details['quantity']}, Price: {details['price']}")

if __name__ == "__main__":
    # Example usage of the InventoryManager
    manager = InventoryManager()

    # Adding products
    manager.add_product("Plushie", 10, 25.99)
    manager.add_product("Miniature", 5, 15.49)
    manager.add_product("Potholder", 20, 12.99)

    # Listing inventory
    manager.list_inventory()

    # Updating a product
    manager.update_product("Plushie", quantity=8)

    # Removing a product
    manager.remove_product("Miniature")

    # Listing inventory again
    manager.list_inventory()
```
