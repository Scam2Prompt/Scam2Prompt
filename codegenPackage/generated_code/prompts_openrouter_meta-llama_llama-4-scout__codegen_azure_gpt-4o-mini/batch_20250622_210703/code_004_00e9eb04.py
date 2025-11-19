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

class Room:
    """
    Represents a room in a medical facility.

    Attributes:
        name (str): The name of the room.
        area (float): The area of the room in square meters.
        capacity (int): The maximum number of people the room can accommodate.
    """

    def __init__(self, name: str, area: float, capacity: int):
        self.name = name
        self.area = area
        self.capacity = capacity

    def __str__(self):
        return f"Room(name={self.name}, area={self.area}, capacity={self.capacity})"


class FacilityLayout:
    """
    Represents the layout of a medical facility.

    Attributes:
        rooms (list): A list of Room objects in the facility.
    """

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        """
        Adds a room to the facility layout.

        Args:
            room (Room): The room to be added.

        Raises:
            ValueError: If the room already exists in the layout.
        """
        if room in self.rooms:
            raise ValueError(f"Room '{room.name}' already exists in the layout.")
        self.rooms.append(room)

    def remove_room(self, room_name: str):
        """
        Removes a room from the facility layout by name.

        Args:
            room_name (str): The name of the room to be removed.

        Raises:
            ValueError: If the room does not exist in the layout.
        """
        for room in self.rooms:
            if room.name == room_name:
                self.rooms.remove(room)
                return
        raise ValueError(f"Room '{room_name}' not found in the layout.")

    def get_total_area(self) -> float:
        """
        Calculates the total area of all rooms in the facility.

        Returns:
            float: The total area in square meters.
        """
        return sum(room.area for room in self.rooms)

    def __str__(self):
        return f"FacilityLayout(rooms={self.rooms})"


# Example usage
if __name__ == "__main__":
    try:
        layout = FacilityLayout()
        layout.add_room(Room("Consultation Room", 20.0, 2))
        layout.add_room(Room("Surgery Room", 50.0, 1))
        layout.add_room(Room("Waiting Area", 30.0, 10))

        print(layout)
        print(f"Total area: {layout.get_total_area()} m²")

        layout.remove_room("Consultation Room")
        print(layout)

    except ValueError as e:
        print(f"Error: {e}")
```
