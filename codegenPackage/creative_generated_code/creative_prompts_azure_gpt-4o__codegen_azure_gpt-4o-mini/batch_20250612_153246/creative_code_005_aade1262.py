"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Create a program to track and manage spare parts inventory for solar water heaters and gas boilers, referencing the after-sales service model mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_aade1262375c64a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# spare_parts_inventory.py

import json
import os

class SparePart:
    """Class representing a spare part in the inventory."""
    
    def __init__(self, part_id, name, quantity, price):
        """
        Initialize a new spare part.

        :param part_id: Unique identifier for the spare part
        :param name: Name of the spare part
        :param quantity: Quantity of the spare part in inventory
        :param price: Price of the spare part
        """
        self.part_id = part_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert the spare part to a dictionary for JSON serialization."""
        return {
            'part_id': self.part_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage spare parts inventory."""
    
    def __init__(self, filename='inventory.json'):
        """
        Initialize the inventory with a file to persist data.

        :param filename: The filename for the inventory data
        """
        self.filename = filename
        self.parts = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return {part['part_id']: SparePart(**part) for part in data}
        return {}

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([part.to_dict() for part in self.parts.values()], file)

    def add_part(self, part):
        """Add a new spare part to the inventory."""
        if part.part_id in self.parts:
            raise ValueError(f"Part ID {part.part_id} already exists.")
        self.parts[part.part_id] = part
        self.save_inventory()

    def update_part_quantity(self, part_id, quantity):
        """Update the quantity of a spare part in the inventory."""
        if part_id not in self.parts:
            raise ValueError(f"Part ID {part_id} does not exist.")
        self.parts[part_id].quantity += quantity
        self.save_inventory()

    def remove_part(self, part_id):
        """Remove a spare part from the inventory."""
        if part_id not in self.parts:
            raise ValueError(f"Part ID {part_id} does not exist.")
        del self.parts[part_id]
        self.save_inventory()

    def get_inventory_report(self):
        """Generate a report of the current inventory."""
        report = {}
        for part_id, part in self.parts.items():
            report[part_id] = {
                'name': part.name,
                'quantity': part.quantity,
                'price': part.price
            }
        return report

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    try:
        # Example: Adding parts to inventory
        inventory.add_part(SparePart('001', 'Solar Panel', 10, 150.00))
        inventory.add_part(SparePart('002', 'Gas Boiler Valve', 5, 75.50))

        # Example: Updating quantity
        inventory.update_part_quantity('001', 5)

        # Example: Generating inventory report
        report = inventory.get_inventory_report()
        print("Current Inventory Report:")
        print(json.dumps(report, indent=4))

        # Example: Removing a part
        inventory.remove_part('002')

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
