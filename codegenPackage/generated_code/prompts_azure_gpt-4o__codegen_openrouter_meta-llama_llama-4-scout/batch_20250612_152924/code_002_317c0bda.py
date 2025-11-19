"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Create a script that automates space planning for interior design, optimizing layouts for small offices and kitchens, inspired by Amazing Interior's "making the best possible use of available space" philosophy.
Generated: DETERMINISTIC_317c0bdaf35ff0c3
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Room:
    def __init__(self, width, height, furniture=None):
        """
        Initialize a Room object.

        Args:
            width (float): The width of the room in meters.
            height (float): The height of the room in meters.
            furniture (list, optional): A list of Furniture objects. Defaults to None.
        """
        self.width = width
        self.height = height
        self.furniture = furniture if furniture else []

    def add_furniture(self, furniture):
        """
        Add a piece of furniture to the room.

        Args:
            furniture (Furniture): A Furniture object.
        """
        self.furniture.append(furniture)

    def calculate_area(self):
        """
        Calculate the area of the room.

        Returns:
            float: The area of the room in square meters.
        """
        return self.width * self.height

    def calculate_usable_area(self):
        """
        Calculate the usable area of the room.

        Returns:
            float: The usable area of the room in square meters.
        """
        usable_area = self.calculate_area()
        for furniture in self.furniture:
            usable_area -= furniture.calculate_area()
        return usable_area


class Furniture:
    def __init__(self, width, height, depth):
        """
        Initialize a Furniture object.

        Args:
            width (float): The width of the furniture in meters.
            height (float): The height of the furniture in meters.
            depth (float): The depth of the furniture in meters.
        """
        self.width = width
        self.height = height
        self.depth = depth

    def calculate_area(self):
        """
        Calculate the area of the furniture.

        Returns:
            float: The area of the furniture in square meters.
        """
        return self.width * self.depth


def optimize_layout(room, furniture_list):
    """
    Optimize the layout of a room by placing furniture in a way that maximizes usable space.

    Args:
        room (Room): A Room object.
        furniture_list (list): A list of Furniture objects.

    Returns:
        list: A list of tuples representing the positions of the furniture in the room.
    """
    # Sort furniture by area in descending order
    furniture_list.sort(key=lambda x: x.calculate_area(), reverse=True)

    # Initialize positions list
    positions = []

    # Iterate over furniture list
    for furniture in furniture_list:
        # Find a position for the furniture that minimizes overlap with other furniture
        position = find_position(room, furniture, positions)
        if position:
            positions.append((furniture, position))

    return positions


def find_position(room, furniture, positions):
    """
    Find a position for a piece of furniture in a room that minimizes overlap with other furniture.

    Args:
        room (Room): A Room object.
        furniture (Furniture): A Furniture object.
        positions (list): A list of tuples representing the positions of other furniture in the room.

    Returns:
        tuple: A tuple representing the position of the furniture in the room, or None if no position is found.
    """
    # Try to place furniture along the walls
    for x in [0, room.width - furniture.width]:
        for y in [0, room.height - furniture.depth]:
            if not overlaps(positions, (x, y), furniture, room):
                return (x, y)

    # If no position is found along the walls, try to place furniture in the center of the room
    center_x = room.width / 2 - furniture.width / 2
    center_y = room.height / 2 - furniture.depth / 2
    if not overlaps(positions, (center_x, center_y), furniture, room):
        return (center_x, center_y)

    return None


def overlaps(positions, position, furniture, room):
    """
    Check if a piece of furniture overlaps with other furniture in a room.

    Args:
        positions (list): A list of tuples representing the positions of other furniture in the room.
        position (tuple): A tuple representing the position of the furniture in the room.
        furniture (Furniture): A Furniture object.
        room (Room): A Room object.

    Returns:
        bool: True if the furniture overlaps with other furniture, False otherwise.
    """
    for other_furniture, other_position in positions:
        if (position[0] < other_position[0] + other_furniture.width and
            position[0] + furniture.width > other_position[0] and
            position[1] < other_position[1] + other_furniture.depth and
            position[1] + furniture.depth > other_position[1]):
            return True

    # Check if furniture is within room boundaries
    if (position[0] < 0 or position[0] + furniture.width > room.width or
        position[1] < 0 or position[1] + furniture.depth > room.height):
        return True

    return False


def main():
    # Create a room
    room = Room(5, 5)

    # Create furniture
    desk = Furniture(1.5, 0.8, 0.8)
    chair = Furniture(0.5, 0.5, 0.5)
    bookshelf = Furniture(1, 2, 0.3)

    # Add furniture to room
    room.add_furniture(desk)
    room.add_furniture(chair)
    room.add_furniture(bookshelf)

    # Optimize layout
    furniture_list = [desk, chair, bookshelf]
    positions = optimize_layout(room, furniture_list)

    # Print positions
    for furniture, position in positions:
        print(f"Furniture: {furniture.width}x{furniture.depth}, Position: {position[0]}x{position[1]}")

    # Calculate and print usable area
    usable_area = room.calculate_usable_area()
    print(f"Usable area: {usable_area} sqm")


if __name__ == "__main__":
    main()
```
