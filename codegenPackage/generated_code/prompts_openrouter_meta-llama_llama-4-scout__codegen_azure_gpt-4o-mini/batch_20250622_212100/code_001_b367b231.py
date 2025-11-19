"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: "Write a Python script to manage an inventory of automotive spare parts, including batteries, alternators, starters, lighting, suspension, lubricants, and filters."
Generated: DETERMINISTIC_b367b231ab3937c7
Batch ID: 20250622_212100
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
    """A class to manage an inventory of automotive spare parts."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_part(self, part_name, quantity):
        """Add a specified quantity of a part to the inventory."""
        if part_name in self.inventory:
            self.inventory[part_name] += quantity
        else:
            self.inventory[part_name] = quantity
        self.save_inventory()

    def remove_part(self, part_name, quantity):
        """Remove a specified quantity of a part from the inventory."""
        if part_name in self.inventory:
            if self.inventory[part_name] >= quantity:
                self.inventory[part_name] -= quantity
                if self.inventory[part_name] == 0:
                    del self.inventory[part_name]
                self.save_inventory()
            else:
                raise ValueError("Not enough quantity to remove.")
        else:
            raise KeyError("Part not found in inventory.")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for part, quantity in self.inventory.items():
                print(f"{part}: {quantity}")

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_part('Battery', 10)
        manager.add_part('Alternator', 5)
        manager.add_part('Starter', 3)
        manager.display_inventory()

        manager.remove_part('Battery', 2)
        manager.display_inventory()

        manager.remove_part('Starter', 5)  # This will raise an error
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
