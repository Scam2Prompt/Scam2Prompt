"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greystoneinfra.in
Prompt: Write Python code to simulate a virtual reality 3D interior design model for a commercial office space, incorporating features like layout visualization and material selection, as described on the Greystone Infra website.
Generated: DETERMINISTIC_c19afaeb9c8398fa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import random
import json
from typing import List, Dict, Any

class Room:
    """Class to represent a room in the interior design model."""
    
    def __init__(self, name: str, width: float, length: float) -> None:
        self.name = name
        self.width = width
        self.length = length
        self.materials: List[str] = []
    
    def add_material(self, material: str) -> None:
        """Add a material to the room."""
        self.materials.append(material)

    def get_area(self) -> float:
        """Calculate the area of the room."""
        return self.width * self.length

class OfficeSpace:
    """Class to represent the entire office space."""
    
    def __init__(self, rooms: List[Room]) -> None:
        self.rooms = rooms
    
    def total_area(self) -> float:
        """Calculate the total area of all rooms in the office space."""
        return sum(room.get_area() for room in self.rooms)

    def to_json(self) -> str:
        """Convert the office space details to JSON format."""
        return json.dumps({
            'rooms': [
                {'name': room.name, 'width': room.width, 'length': room.length, 'materials': room.materials}
                for room in self.rooms
            ]
        }, indent=4)

def select_random_material() -> str:
    """Select a random material from a predefined list."""
    materials = ['Wood', 'Metal', 'Glass', 'Stone', 'Fabric']
    return random.choice(materials)

def main() -> None:
    """Main function to simulate the interior design model."""
    try:
        # Define rooms for the office space
        rooms = [
            Room(name='Conference Room', width=20, length=15),
            Room(name='Office 1', width=10, length=12),
            Room(name='Office 2', width=10, length=12),
            Room(name='Break Room', width=8, length=10)
        ]
        
        # Select materials for each room
        for room in rooms:
            for _ in range(2):  # Assign two materials per room as an example
                material = select_random_material()
                room.add_material(material)
        
        # Create an office space object
        office_space = OfficeSpace(rooms)

        # Display the total area of the office space
        print(f"Total area of the office space: {office_space.total_area()} sq ft")

        # Output the office space details in JSON format
        print("Office Space Details (JSON):")
        print(office_space.to_json())

    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
