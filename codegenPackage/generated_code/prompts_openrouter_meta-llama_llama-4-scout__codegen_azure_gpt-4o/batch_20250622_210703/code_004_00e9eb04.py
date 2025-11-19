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
"""
medical_layout.py

A Python library for designing medical facility layouts inspired by Pahubel's specialization in healthcare center design.
This library provides tools to create, validate, and visualize layouts for healthcare facilities.

Author: Expert Programmer
Version: 1.0
"""

import json


class MedicalFacilityLayout:
    """
    A class to represent and manage medical facility layouts.
    """

    def __init__(self, name):
        """
        Initialize a new medical facility layout.

        :param name: Name of the medical facility.
        """
        self.name = name
        self.rooms = []
        self.connections = []

    def add_room(self, room_name, room_type, dimensions):
        """
        Add a room to the layout.

        :param room_name: Name of the room.
        :param room_type: Type of the room (e.g., "Operating Room", "Waiting Area").
        :param dimensions: Dimensions of the room as a tuple (length, width).
        :raises ValueError: If dimensions are invalid.
        """
        if not isinstance(dimensions, tuple) or len(dimensions) != 2 or not all(isinstance(d, (int, float)) and d > 0 for d in dimensions):
            raise ValueError("Invalid dimensions. Must be a tuple of two positive numbers (length, width).")
        self.rooms.append({
            "name": room_name,
            "type": room_type,
            "dimensions": dimensions
        })

    def connect_rooms(self, room1, room2):
        """
        Connect two rooms in the layout.

        :param room1: Name of the first room.
        :param room2: Name of the second room.
        :raises ValueError: If either room does not exist.
        """
        room_names = [room["name"] for room in self.rooms]
        if room1 not in room_names or room2 not in room_names:
            raise ValueError("Both rooms must exist in the layout to create a connection.")
        self.connections.append((room1, room2))

    def validate_layout(self):
        """
        Validate the layout to ensure all rooms are connected.

        :return: True if the layout is valid, False otherwise.
        """
        if not self.rooms:
            return False  # No rooms in the layout
        connected_rooms = set()
        for connection in self.connections:
            connected_rooms.update(connection)
        return len(connected_rooms) == len(self.rooms)

    def export_layout(self, file_path):
        """
        Export the layout to a JSON file.

        :param file_path: Path to the file where the layout will be saved.
        """
        layout_data = {
            "name": self.name,
            "rooms": self.rooms,
            "connections": self.connections
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(layout_data, file, indent=4)
        except IOError as e:
            print(f"Error saving layout to file: {e}")

    def import_layout(self, file_path):
        """
        Import a layout from a JSON file.

        :param file_path: Path to the file containing the layout data.
        :raises ValueError: If the file contains invalid layout data.
        """
        try:
            with open(file_path, 'r') as file:
                layout_data = json.load(file)
            self.name = layout_data["name"]
            self.rooms = layout_data["rooms"]
            self.connections = layout_data["connections"]
        except (IOError, KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading layout from file: {e}")

    def display_layout(self):
        """
        Display the layout in a human-readable format.
        """
        print(f"Medical Facility Layout: {self.name}")
        print("Rooms:")
        for room in self.rooms:
            print(f"  - {room['name']} ({room['type']}): {room['dimensions'][0]}x{room['dimensions'][1]}")
        print("Connections:")
        for connection in self.connections:
            print(f"  - {connection[0]} <-> {connection[1]}")


# Example usage (uncomment to test):
# layout = MedicalFacilityLayout("City Hospital")
# layout.add_room("Operating Room 1", "Operating Room", (20, 15))
# layout.add_room("Waiting Area", "Waiting Room", (10, 10))
# layout.connect_rooms("Operating Room 1", "Waiting Area")
# layout.display_layout()
# layout.export_layout("hospital_layout.json")
# layout.import_layout("hospital_layout.json")
# print(layout.validate_layout())
```
