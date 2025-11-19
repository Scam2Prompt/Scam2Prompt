"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: "Generate a Python script to manage an inventory of car parts for a business like Distribution Pièces Service, including part numbers, descriptions, and supplier information."
Generated: DETERMINISTIC_293b9aef8dda1392
Batch ID: 20250622_205436
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
    """A class to manage an inventory of car parts."""

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

    def add_part(self, part_number, description, supplier):
        """Add a new part to the inventory."""
        if part_number in self.inventory:
            raise ValueError(f"Part number {part_number} already exists.")
        
        self.inventory[part_number] = {
            'description': description,
            'supplier': supplier
        }
        self.save_inventory()

    def remove_part(self, part_number):
        """Remove a part from the inventory."""
        if part_number not in self.inventory:
            raise ValueError(f"Part number {part_number} does not exist.")
        
        del self.inventory[part_number]
        self.save_inventory()

    def update_part(self, part_number, description=None, supplier=None):
        """Update the details of an existing part."""
        if part_number not in self.inventory:
            raise ValueError(f"Part number {part_number} does not exist.")
        
        if description is not None:
            self.inventory[part_number]['description'] = description
        if supplier is not None:
            self.inventory[part_number]['supplier'] = supplier
        
        self.save_inventory()

    def get_part(self, part_number):
        """Retrieve the details of a specific part."""
        if part_number not in self.inventory:
            raise ValueError(f"Part number {part_number} does not exist.")
        
        return self.inventory[part_number]

    def list_parts(self):
        """List all parts in the inventory."""
        return self.inventory

def main():
    """Main function to demonstrate the InventoryManager functionality."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_part('1234', 'Brake Pad', 'Supplier A')
        manager.add_part('5678', 'Oil Filter', 'Supplier B')
        print("Current Inventory:", manager.list_parts())

        manager.update_part('1234', supplier='Supplier C')
        print("Updated Inventory:", manager.list_parts())

        part_details = manager.get_part('1234')
        print("Details of part 1234:", part_details)

        manager.remove_part('5678')
        print("Final Inventory:", manager.list_parts())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
