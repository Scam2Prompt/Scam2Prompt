"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Write a program to manage inventory for spare parts used in car repairs, such as batteries, brake pads, and spark plugs, with tracking for each car brand.
Generated: DETERMINISTIC_ccf06bb93cd7715d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Optional

class SparePart:
    """Class representing a spare part with its attributes."""

    def __init__(self, name: str, brand: str, quantity: int):
        """Initialize the SparePart with a name, brand, and quantity."""
        self.name = name
        self.brand = brand
        self.quantity = quantity

    def to_dict(self) -> Dict[str, str]:
        """Convert SparePart to dictionary for easy serialization."""
        return {
            'name': self.name,
            'brand': self.brand,
            'quantity': self.quantity
        }

class InventoryManager:
    """Class to manage the inventory of spare parts."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.inventory: Dict[str, List[SparePart]] = {}

    def add_part(self, part: SparePart) -> None:
        """Add a spare part to the inventory."""
        if part.brand not in self.inventory:
            self.inventory[part.brand] = []
        self.inventory[part.brand].append(part)

    def remove_part(self, part_name: str, brand: str) -> bool:
        """Remove a spare part from the inventory."""
        if brand in self.inventory:
            for part in self.inventory[brand]:
                if part.name == part_name:
                    self.inventory[brand].remove(part)
                    return True
        return False

    def update_quantity(self, part_name: str, brand: str, quantity: int) -> bool:
        """Update the quantity of a specific spare part."""
        if brand in self.inventory:
            for part in self.inventory[brand]:
                if part.name == part_name:
                    part.quantity = quantity
                    return True
        return False

    def get_inventory(self) -> Dict[str, List[Dict[str, str]]]:
        """Get the entire inventory as a dictionary."""
        return {
            brand: [part.to_dict() for part in parts]
            for brand, parts in self.inventory.items()
        }

    def save_inventory(self, file_path: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for brand, parts in data.items():
                    for part_data in parts:
                        part = SparePart(part_data['name'], brand, part_data['quantity'])
                        self.add_part(part)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    manager.load_inventory('inventory.json')  # Load existing inventory
    manager.add_part(SparePart("Battery", "Toyota", 10))
    manager.add_part(SparePart("Brake Pad", "Honda", 5))
    manager.update_quantity("Battery", "Toyota", 15)
    manager.remove_part("Brake Pad", "Honda")
    manager.save_inventory('inventory.json')  # Save updated inventory
```
