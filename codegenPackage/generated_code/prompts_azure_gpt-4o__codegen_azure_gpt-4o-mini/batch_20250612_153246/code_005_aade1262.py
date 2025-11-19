"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Create a program to track and manage spare parts inventory for solar water heaters and gas boilers, referencing the after-sales service model mentioned on the Accutrol Systems website.
Generated: DETERMINISTIC_aade1262375c64a3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class SparePart:
    """Class to represent a spare part in the inventory."""
    
    def __init__(self, part_id: str, name: str, quantity: int, price: float):
        self.part_id = part_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert SparePart instance to dictionary."""
        return {
            "part_id": self.part_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

class Inventory:
    """Class to manage the spare parts inventory."""
    
    def __init__(self):
        self.parts: List[SparePart] = []

    def add_part(self, part: SparePart) -> None:
        """Add a new spare part to the inventory."""
        self.parts.append(part)

    def remove_part(self, part_id: str) -> bool:
        """Remove a spare part from the inventory by part_id."""
        for part in self.parts:
            if part.part_id == part_id:
                self.parts.remove(part)
                return True
        return False

    def update_quantity(self, part_id: str, quantity: int) -> bool:
        """Update the quantity of a spare part in the inventory."""
        for part in self.parts:
            if part.part_id == part_id:
                part.quantity = quantity
                return True
        return False

    def get_part(self, part_id: str) -> Optional[SparePart]:
        """Retrieve a spare part by part_id."""
        for part in self.parts:
            if part.part_id == part_id:
                return part
        return None

    def list_parts(self) -> List[Dict]:
        """List all spare parts in the inventory."""
        return [part.to_dict() for part in self.parts]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_parts(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                parts_data = json.load(file)
                self.parts = [SparePart(**part) for part in parts_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    # Load existing inventory from file
    inventory.load_from_file('inventory.json')

    # Add some spare parts
    inventory.add_part(SparePart("SP001", "Solar Panel", 10, 150.0))
    inventory.add_part(SparePart("SP002", "Gas Valve", 5, 75.0))

    # Update quantity of a part
    inventory.update_quantity("SP001", 8)

    # List all parts
    print("Current Inventory:")
    for part in inventory.list_parts():
        print(part)

    # Save inventory to file
    inventory.save_to_file('inventory.json')

if __name__ == "__main__":
    main()
```
