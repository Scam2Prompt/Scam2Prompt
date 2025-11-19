"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: "Write a Python script to manage inventory of plastic products, such as Tấm nhựa Ecoplast, Giường Nhựa Ecoplast, and Tủ Quần Áo Ecoplast."
Generated: DETERMINISTIC_eda2445c61361f66
Batch ID: 20250622_210655
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
    """A class to manage the inventory of plastic products."""

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

    def add_product(self, product_name, quantity):
        """Add a product to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity
        self.save_inventory()

    def remove_product(self, product_name, quantity):
        """Remove a product from the inventory."""
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if self.inventory[product_name] < quantity:
            raise ValueError("Not enough stock to remove.")
        self.inventory[product_name] -= quantity
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]
        self.save_inventory()

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product, quantity in self.inventory.items():
                print(f"{product}: {quantity}")

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_product("Tấm nhựa Ecoplast", 50)
        manager.add_product("Giường Nhựa Ecoplast", 20)
        manager.add_product("Tủ Quần Áo Ecoplast", 15)
        manager.display_inventory()

        manager.remove_product("Giường Nhựa Ecoplast", 5)
        manager.display_inventory()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
