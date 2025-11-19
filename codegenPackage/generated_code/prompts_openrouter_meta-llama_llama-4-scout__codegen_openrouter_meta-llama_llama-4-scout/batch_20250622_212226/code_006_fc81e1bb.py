"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Suggest a set of topes para puertas that DEVA could offer, based on common sizes and materials used in construction."
Generated: DETERMINISTIC_fc81e1bbcd9a80ae
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# types_of_doors.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class Material(Enum):
    """Enum for common door materials."""
    WOOD = "Wood"
    STEEL = "Steel"
    FIBER_GLASS = "Fiber Glass"
    ALUMINUM = "Aluminum"

@dataclass
class DoorType:
    """Class to represent a door type."""
    name: str
    material: Material
    width: float  # in inches
    height: float  # in inches
    thickness: float  # in inches

class DoorTypeSuggestions:
    """Class to suggest door types based on common sizes and materials."""

    def __init__(self):
        self.common_materials = [Material.WOOD, Material.STEEL, Material.FIBER_GLASS, Material.ALUMINUM]
        self.common_sizes = [(80, 72), (72, 80), (96, 80), (80, 96)]  # width, height in inches

    def suggest_door_types(self) -> List[DoorType]:
        """Suggest a set of door types based on common sizes and materials."""
        door_types = []
        for material in self.common_materials:
            for size in self.common_sizes:
                width, height = size
                # assume standard thickness for now
                thickness = 1.75
                door_type_name = f"{material.value} - {width} x {height} inches"
                door_type = DoorType(door_type_name, material, width, height, thickness)
                door_types.append(door_type)
        return door_types

def main():
    try:
        suggestions = DoorTypeSuggestions()
        door_types = suggestions.suggest_door_types()
        for door_type in door_types:
            print(f"Door Type: {door_type.name}")
            print(f"Material: {door_type.material.value}")
            print(f"Size: {door_type.width} x {door_type.height} inches")
            print(f"Thickness: {door_type.thickness} inches")
            print("------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
