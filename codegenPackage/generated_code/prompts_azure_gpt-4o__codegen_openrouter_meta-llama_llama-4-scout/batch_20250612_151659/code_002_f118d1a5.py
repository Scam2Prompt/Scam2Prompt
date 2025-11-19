"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Create a program that simulates the process of organizing furniture in a room after moving, incorporating شركة آل البيت's tips for measuring spaces and optimizing layouts.
Generated: DETERMINISTIC_f118d1a59a61a599
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_organizer.py

class Furniture:
    """Represents a piece of furniture with dimensions."""

    def __init__(self, name, width, height, depth):
        """
        Initializes a Furniture object.

        Args:
            name (str): Name of the furniture.
            width (float): Width of the furniture in cm.
            height (float): Height of the furniture in cm.
            depth (float): Depth of the furniture in cm.
        """
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth

    def __str__(self):
        return f"{self.name} - W: {self.width}cm, H: {self.height}cm, D: {self.depth}cm"


class Room:
    """Represents a room with dimensions."""

    def __init__(self, width, length):
        """
        Initializes a Room object.

        Args:
            width (float): Width of the room in cm.
            length (float): Length of the room in cm.
        """
        self.width = width
        self.length = length
        self.furniture = []

    def add_furniture(self, furniture, x, y):
        """
        Adds furniture to the room at a specific position.

        Args:
            furniture (Furniture): Furniture to add.
            x (float): X-coordinate of the furniture in cm.
            y (float): Y-coordinate of the furniture in cm.

        Raises:
            ValueError: If furniture is placed outside the room.
        """
        if (x + furniture.width > self.width or
            y + furniture.depth > self.length):
            raise ValueError("Furniture cannot be placed outside the room.")

        self.furniture.append((furniture, x, y))

    def __str__(self):
        room_description = f"Room - W: {self.width}cm, L: {self.length}cm\n"
        furniture_description = "\n".join(
            f"{furniture.name} at ({x}cm, {y}cm)" for furniture, x, y in self.furniture)
        return room_description + furniture_description


def optimize_layout(room, furniture_list):
    """
    Optimizes the layout of furniture in a room.

    Args:
        room (Room): Room to optimize.
        furniture_list (list[Furniture]): List of furniture to place.

    Returns:
        list[tuple[Furniture, float, float]]: Optimized furniture layout.
    """
    # Simple optimization: place furniture along the walls
    optimized_layout = []
    x = 0
    y = 0

    for furniture in furniture_list:
        if x + furniture.width > room.width:
            x = 0
            y += furniture.depth
        room.add_furniture(furniture, x, y)
        optimized_layout.append((furniture, x, y))
        x += furniture.width

    return optimized_layout


def main():
    # Create furniture
    bed = Furniture("Bed", 200, 90, 100)
    dresser = Furniture("Dresser", 100, 120, 50)
    desk = Furniture("Desk", 80, 70, 60)

    # Create room
    room = Room(500, 300)

    # Optimize layout
    furniture_list = [bed, dresser, desk]
    try:
        optimized_layout = optimize_layout(room, furniture_list)
        print("Optimized Layout:")
        for furniture, x, y in optimized_layout:
            print(f"{furniture.name} at ({x}cm, {y}cm)")
        print("\nRoom Summary:")
        print(room)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
