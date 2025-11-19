"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a system to manage inventory for Whirlpool appliance replacement parts, ensuring high-quality and reliable replacements as emphasized on the website.
Generated: DETERMINISTIC_eea283fd59c91c26
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class PartStatus(str, Enum):
    """Enum for part status"""
    IN_STOCK = "In Stock"
    OUT_OF_STOCK = "Out of Stock"
    BACKORDER = "Backorder"

@dataclass
class Part:
    """Dataclass for appliance replacement parts"""
    part_number: str
    description: str
    quantity: int
    status: PartStatus
    last_updated: datetime

class Inventory:
    """Class for managing inventory of appliance replacement parts"""
    def __init__(self):
        self.parts: Dict[str, Part] = {}

    def add_part(self, part: Part):
        """Add a part to the inventory"""
        if part.part_number in self.parts:
            raise ValueError(f"Part {part.part_number} already exists in the inventory")
        self.parts[part.part_number] = part

    def update_part(self, part_number: str, quantity: int = None, status: PartStatus = None):
        """Update a part's quantity and/or status"""
        if part_number not in self.parts:
            raise ValueError(f"Part {part_number} does not exist in the inventory")
        if quantity is not None:
            self.parts[part_number].quantity = quantity
        if status is not None:
            self.parts[part_number].status = status
        self.parts[part_number].last_updated = datetime.now()

    def remove_part(self, part_number: str):
        """Remove a part from the inventory"""
        if part_number not in self.parts:
            raise ValueError(f"Part {part_number} does not exist in the inventory")
        del self.parts[part_number]

    def get_part(self, part_number: str) -> Part:
        """Get a part from the inventory"""
        return self.parts.get(part_number)

    def get_all_parts(self) -> List[Part]:
        """Get all parts in the inventory"""
        return list(self.parts.values())

    def check_availability(self, part_number: str) -> bool:
        """Check if a part is in stock"""
        part = self.get_part(part_number)
        return part.status == PartStatus.IN_STOCK if part else False

def main():
    # Create an inventory
    inventory = Inventory()

    # Add some parts
    part1 = Part("WP123", "Motor", 10, PartStatus.IN_STOCK, datetime.now())
    part2 = Part("WP456", "Pump", 5, PartStatus.OUT_OF_STOCK, datetime.now())
    inventory.add_part(part1)
    inventory.add_part(part2)

    # Print all parts
    print("All Parts:")
    for part in inventory.get_all_parts():
        print(f"Part Number: {part.part_number}, Description: {part.description}, Quantity: {part.quantity}, Status: {part.status.value}")

    # Update a part
    inventory.update_part("WP123", quantity=15)
    print("\nUpdated Part:")
    print(inventory.get_part("WP123"))

    # Check availability
    print("\nAvailability:")
    print(f"Part WP123: {inventory.check_availability('WP123')}")
    print(f"Part WP456: {inventory.check_availability('WP456')}")

if __name__ == "__main__":
    main()
```
