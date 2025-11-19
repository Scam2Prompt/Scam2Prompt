"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a Python function to generate structured interior design plans based on client preferences, referencing the structure interior designing services provided by Remas Engineering Consultants.
Generated: DETERMINISTIC_14f6801e6ac7413b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_plan.py

from enum import Enum
from typing import Dict, List

class DesignStyle(Enum):
    """ Enum for design styles """
    MODERN = "Modern"
    TRADITIONAL = "Traditional"
    MINIMALIST = "Minimalist"

class RoomType(Enum):
    """ Enum for room types """
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    KITCHEN = "Kitchen"

class InteriorDesignPlan:
    """ Class to represent an interior design plan """

    def __init__(self, client_name: str, design_style: DesignStyle):
        """
        Initialize an interior design plan

        Args:
        - client_name (str): The name of the client
        - design_style (DesignStyle): The design style preferred by the client
        """
        self.client_name = client_name
        self.design_style = design_style
        self.rooms = []

    def add_room(self, room_type: RoomType, dimensions: Dict[str, float], furniture: List[str]):
        """
        Add a room to the interior design plan

        Args:
        - room_type (RoomType): The type of room
        - dimensions (Dict[str, float]): The dimensions of the room (e.g., length, width, height)
        - furniture (List[str]): The furniture to be included in the room
        """
        room = {
            "room_type": room_type.value,
            "dimensions": dimensions,
            "furniture": furniture
        }
        self.rooms.append(room)

    def generate_plan(self) -> str:
        """
        Generate a structured interior design plan

        Returns:
        - str: A string representation of the interior design plan
        """
        plan = f"Interior Design Plan for {self.client_name} ({self.design_style.value})\n"
        for i, room in enumerate(self.rooms, start=1):
            plan += f"\nRoom {i}: {room['room_type']}\n"
            plan += f"Dimensions: {room['dimensions']}\n"
            plan += f"Furniture: {', '.join(room['furniture'])}\n"
        return plan

def create_interior_design_plan(client_preferences: Dict[str, str]) -> InteriorDesignPlan:
    """
    Create an interior design plan based on client preferences

    Args:
    - client_preferences (Dict[str, str]): A dictionary containing client preferences
        (e.g., design_style, room_types, dimensions, furniture)

    Returns:
    - InteriorDesignPlan: An interior design plan object
    """
    try:
        client_name = client_preferences["client_name"]
        design_style = DesignStyle(client_preferences["design_style"].upper())
        plan = InteriorDesignPlan(client_name, design_style)

        room_preferences = client_preferences.get("rooms", [])
        for room_preference in room_preferences:
            room_type = RoomType(room_preference["room_type"].upper())
            dimensions = room_preference["dimensions"]
            furniture = room_preference["furniture"]
            plan.add_room(room_type, dimensions, furniture)

        return plan
    except KeyError as e:
        print(f"Error: Missing key in client preferences - {e}")
        return None
    except Exception as e:
        print(f"An error occurred - {e}")
        return None

# Example usage
if __name__ == "__main__":
    client_preferences = {
        "client_name": "John Doe",
        "design_style": "modern",
        "rooms": [
            {
                "room_type": "living_room",
                "dimensions": {"length": 10, "width": 8, "height": 2.5},
                "furniture": ["sofa", "coffee_table", "tv_stand"]
            },
            {
                "room_type": "bedroom",
                "dimensions": {"length": 12, "width": 10, "height": 2.5},
                "furniture": ["bed", "dresser", "nightstand"]
            }
        ]
    }

    plan = create_interior_design_plan(client_preferences)
    if plan:
        print(plan.generate_plan())
```
