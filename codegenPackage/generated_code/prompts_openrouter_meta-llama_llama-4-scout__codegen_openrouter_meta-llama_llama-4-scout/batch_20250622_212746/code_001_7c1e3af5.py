"""
Generated Code Metadata:
========================
Original URL: https://saldias.net
Prompt: Write a Python script to manage inventory for a Toyota spare parts supplier with delivery times of 2-4 weeks from North America, Europe, and Asia.
Generated: DETERMINISTIC_7c1e3af542bfb7e6
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from enum import Enum
from typing import Dict, List

class Region(Enum):
    """Enum for regions"""
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    ASIA = "Asia"

class Part:
    """Class to represent a spare part"""
    def __init__(self, part_number: str, name: str, quantity: int, region: Region, delivery_time: int):
        """
        Initialize a Part object.

        Args:
        - part_number (str): Unique part number
        - name (str): Part name
        - quantity (int): Current quantity in stock
        - region (Region): Region where part is sourced from
        - delivery_time (int): Delivery time in weeks
        """
        self.part_number = part_number
        self.name = name
        self.quantity = quantity
        self.region = region
        self.delivery_time = delivery_time

class Inventory:
    """Class to manage inventory"""
    def __init__(self):
        self.parts: Dict[str, Part] = {}

    def add_part(self, part: Part):
        """Add a part to the inventory"""
        self.parts[part.part_number] = part

    def remove_part(self, part_number: str):
        """Remove a part from the inventory"""
        if part_number in self.parts:
            del self.parts[part_number]
        else:
            raise ValueError(f"Part {part_number} not found in inventory")

    def update_quantity(self, part_number: str, new_quantity: int):
        """Update the quantity of a part in the inventory"""
        if part_number in self.parts:
            self.parts[part_number].quantity = new_quantity
        else:
            raise ValueError(f"Part {part_number} not found in inventory")

    def get_part(self, part_number: str) -> Part:
        """Get a part from the inventory"""
        return self.parts.get(part_number)

    def list_parts(self) -> List[Part]:
        """List all parts in the inventory"""
        return list(self.parts.values())

def main():
    # Create an inventory
    inventory = Inventory()

    # Add some parts
    part1 = Part("TP001", "Toyota Air Filter", 10, Region.NORTH_AMERICA, 2)
    part2 = Part("TP002", "Toyota Oil Filter", 20, Region.EUROPE, 3)
    part3 = Part("TP003", "Toyota Spark Plug", 5, Region.ASIA, 4)
    inventory.add_part(part1)
    inventory.add_part(part2)
    inventory.add_part(part3)

    # List all parts
    print("All parts:")
    for part in inventory.list_parts():
        print(f"Part Number: {part.part_number}, Name: {part.name}, Quantity: {part.quantity}, Region: {part.region.value}, Delivery Time: {part.delivery_time} weeks")

    # Update quantity
    inventory.update_quantity("TP001", 15)
    print("\nUpdated quantity:")
    print(f"Part Number: {part1.part_number}, Name: {part1.name}, Quantity: {part1.quantity}")

    # Get a part
    part = inventory.get_part("TP002")
    print("\nPart details:")
    print(f"Part Number: {part.part_number}, Name: {part.name}, Quantity: {part.quantity}, Region: {part.region.value}, Delivery Time: {part.delivery_time} weeks")

    # Remove a part
    inventory.remove_part("TP003")
    print("\nParts after removal:")
    for part in inventory.list_parts():
        print(f"Part Number: {part.part_number}, Name: {part.name}, Quantity: {part.quantity}")

if __name__ == "__main__":
    main()
```
