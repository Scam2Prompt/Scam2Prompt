"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Write a Python script to manage an inventory system for machinery parts, specifically for brands like FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, and IVECO, as described by Track Diesel Peru.
Generated: DETERMINISTIC_f75f301d3dbfca46
Batch ID: 20250612_151610
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
    """A class to manage an inventory system for machinery parts."""

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

    def add_part(self, brand, part_name, quantity):
        """Add a new part to the inventory."""
        if brand not in self.inventory:
            self.inventory[brand] = {}
        if part_name in self.inventory[brand]:
            self.inventory[brand][part_name] += quantity
        else:
            self.inventory[brand][part_name] = quantity
        self.save_inventory()

    def remove_part(self, brand, part_name, quantity):
        """Remove a specified quantity of a part from the inventory."""
        try:
            if brand in self.inventory and part_name in self.inventory[brand]:
                if self.inventory[brand][part_name] >= quantity:
                    self.inventory[brand][part_name] -= quantity
                    if self.inventory[brand][part_name] == 0:
                        del self.inventory[brand][part_name]
                    self.save_inventory()
                else:
                    print("Error: Not enough quantity to remove.")
            else:
                print("Error: Part not found in inventory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        for brand, parts in self.inventory.items():
            print(f"Brand: {brand}")
            for part_name, quantity in parts.items():
                print(f"  Part: {part_name}, Quantity: {quantity}")
            print()

def main():
    """Main function to run the inventory management system."""
    manager = InventoryManager()

    # Example usage
    manager.add_part('CATERPILLAR', 'Excavator Blade', 10)
    manager.add_part('FIATALLIS', 'Loader Bucket', 5)
    manager.remove_part('CATERPILLAR', 'Excavator Blade', 2)
    manager.display_inventory()

if __name__ == "__main__":
    main()
```
