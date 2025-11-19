"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: "Create a sample interior design plan for a small bedroom with a bàn học (study desk) and giường ngủ (bed), incorporating Viva's wooden furniture products."
Generated: DETERMINISTIC_35ced075260d80bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for furniture types
class FurnitureType(str, Enum):
    STUDY_DESK = "bàn học"
    BED = "giường ngủ"

# Define a data class for furniture
@dataclass
class Furniture:
    name: str
    type: FurnitureType
    dimensions: str
    material: str

# Define a data class for room
@dataclass
class Room:
    name: str
    dimensions: str
    furniture: List[Furniture]

# Define a class for interior design plan
class InteriorDesignPlan:
    def __init__(self, room: Room):
        self.room = room

    def generate_plan(self):
        plan = f"Sample Interior Design Plan for {self.room.name}\n"
        plan += f"Room Dimensions: {self.room.dimensions}\n\n"

        for furniture in self.room.furniture:
            plan += f"- {furniture.name} ({furniture.type.value}): {furniture.dimensions}, Material: {furniture.material}\n"

        return plan

# Define Viva's wooden furniture products
class VivaFurniture:
    def __init__(self):
        self.products = [
            Furniture("Viva Study Desk", FurnitureType.STUDY_DESK, "120cm x 60cm x 75cm", "Wooden"),
            Furniture("Viva Single Bed", FurnitureType.BED, "190cm x 90cm x 40cm", "Wooden"),
        ]

    def get_product(self, type: FurnitureType):
        for product in self.products:
            if product.type == type:
                return product
        return None

# Create a sample interior design plan
def main():
    viva_furniture = VivaFurniture()

    room = Room(
        "Small Bedroom",
        "300cm x 400cm",
        [
            viva_furniture.get_product(FurnitureType.STUDY_DESK),
            viva_furniture.get_product(FurnitureType.BED),
        ],
    )

    plan = InteriorDesignPlan(room)
    print(plan.generate_plan())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
