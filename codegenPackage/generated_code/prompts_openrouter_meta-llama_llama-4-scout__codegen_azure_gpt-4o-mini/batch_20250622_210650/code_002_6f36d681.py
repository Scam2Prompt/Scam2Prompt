"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: "Write a Python script to manage inventory of materials like อะคริลิคสี, ฟิว, and โฟมบอร์ด for a custom printing business."
Generated: DETERMINISTIC_6f36d68146d12ad4
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
    """A class to manage the inventory of materials for a custom printing business."""

    def __init__(self, inventory_file='inventory.json'):
        """Initialize the InventoryManager with a specified inventory file."""
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file. If the file does not exist, return an empty dictionary."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w', encoding='utf-8') as file:
            json.dump(self.inventory, file, ensure_ascii=False, indent=4)

    def add_material(self, name, quantity):
        """Add a new material to the inventory or update the quantity if it already exists."""
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
        self.save_inventory()

    def remove_material(self, name, quantity):
        """Remove a specified quantity of a material from the inventory."""
        if name in self.inventory:
            if self.inventory[name] >= quantity:
                self.inventory[name] -= quantity
                if self.inventory[name] == 0:
                    del self.inventory[name]
                self.save_inventory()
            else:
                raise ValueError(f"Not enough {name} in inventory to remove {quantity}.")
        else:
            raise KeyError(f"{name} not found in inventory.")

    def get_inventory(self):
        """Return the current inventory."""
        return self.inventory

    def display_inventory(self):
        """Display the current inventory in a readable format."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for name, quantity in self.inventory.items():
                print(f"{name}: {quantity}")

def main():
    """Main function to run the inventory management system."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_material("อะคริลิคสี", 50)
        manager.add_material("ฟิว", 30)
        manager.add_material("โฟมบอร์ด", 20)
        manager.display_inventory()

        manager.remove_material("ฟิว", 10)
        manager.display_inventory()

        # Attempt to remove more than available
        manager.remove_material("ฟิว", 50)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
