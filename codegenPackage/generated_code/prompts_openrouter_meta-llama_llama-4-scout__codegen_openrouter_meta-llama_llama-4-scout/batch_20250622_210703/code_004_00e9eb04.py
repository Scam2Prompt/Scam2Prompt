"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Create a library for designing medical facility layouts, inspired by Pahubel's specialization in healthcare center design."
Generated: DETERMINISTIC_00e9eb048410e5de
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# medical_facility_layout.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class RoomType(Enum):
    """Enum for different types of rooms in a medical facility."""
    EXAMINATION_ROOM = 1
    OPERATING_ROOM = 2
    PATIENT_ROOM = 3
    WAITING_ROOM = 4

@dataclass
class Room:
    """Class to represent a room in a medical facility."""
    room_type: RoomType
    area: float  # in square meters
    capacity: int

@dataclass
class Floor:
    """Class to represent a floor in a medical facility."""
    rooms: List[Room]
    floor_number: int

class MedicalFacility:
    """Class to represent a medical facility."""
    def __init__(self, name: str):
        self.name = name
        self.floors = []

    def add_floor(self, floor: Floor):
        """Add a floor to the medical facility."""
        self.floors.append(floor)

    def get_total_area(self) -> float:
        """Get the total area of all rooms in the medical facility."""
        total_area = 0
        for floor in self.floors:
            for room in floor.rooms:
                total_area += room.area
        return total_area

    def get_room_count(self) -> int:
        """Get the total number of rooms in the medical facility."""
        room_count = 0
        for floor in self.floors:
            room_count += len(floor.rooms)
        return room_count

def create_medical_facility_layout() -> MedicalFacility:
    """Create a sample medical facility layout."""
    facility = MedicalFacility("Healthcare Center")

    # Create rooms
    examination_room = Room(RoomType.EXAMINATION_ROOM, 10.0, 2)
    operating_room = Room(RoomType.OPERATING_ROOM, 20.0, 1)
    patient_room = Room(RoomType.PATIENT_ROOM, 15.0, 4)
    waiting_room = Room(RoomType.WAITING_ROOM, 30.0, 10)

    # Create floor
    floor1 = Floor([examination_room, operating_room], 1)
    floor2 = Floor([patient_room, waiting_room], 2)

    # Add floors to facility
    facility.add_floor(floor1)
    facility.add_floor(floor2)

    return facility

def main():
    try:
        facility = create_medical_facility_layout()
        print(f"Medical Facility: {facility.name}")
        print(f"Total Area: {facility.get_total_area()} sqm")
        print(f"Total Rooms: {facility.get_room_count()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
