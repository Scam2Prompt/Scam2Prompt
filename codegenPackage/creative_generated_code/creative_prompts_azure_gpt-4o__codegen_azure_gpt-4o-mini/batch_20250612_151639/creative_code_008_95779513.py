"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbr.com.br
Prompt: Create a program to calculate the optimal placement of Wi-Fi routers in a multi-room house, inspired by the planning services offered by Maxnet Telecom.
Generated: DETERMINISTIC_95779513f69c98f2
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple


class Room:
    """
    A class representing a room in the house.

    Attributes:
        length (float): The length of the room in meters.
        width (float): The width of the room in meters.
        position (Tuple[float, float]): The (x, y) coordinates of the room's bottom-left corner.
    """

    def __init__(self, length: float, width: float, position: Tuple[float, float]):
        self.length = length
        self.width = width
        self.position = position

    def area(self) -> float:
        """Calculate the area of the room."""
        return self.length * self.width


class Router:
    """
    A class representing a Wi-Fi router.

    Attributes:
        range (float): The effective range of the router in meters.
        position (Tuple[float, float]): The (x, y) coordinates of the router's position.
    """

    def __init__(self, range: float, position: Tuple[float, float]):
        self.range = range
        self.position = position


def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def is_covering_room(router: Router, room: Room) -> bool:
    """
    Check if the router covers the entire room.

    A router covers the room if the distance from the router to the corners of the room
    is less than or equal to the router's range.
    """
    room_corners = [
        room.position,
        (room.position[0] + room.length, room.position[1]),
        (room.position[0], room.position[1] + room.width),
        (room.position[0] + room.length, room.position[1] + room.width)
    ]

    return all(calculate_distance(router.position, corner) <= router.range for corner in room_corners)


def find_optimal_router_positions(rooms: List[Room], router_range: float) -> List[Router]:
    """
    Calculate optimal positions for Wi-Fi routers to cover all rooms.

    Parameters:
        rooms (List[Room]): A list of rooms to cover.
        router_range (float): The effective range of the routers.

    Returns:
        List[Router]: A list of optimal router positions.
    """
    routers = []

    # Simple placement strategy: place a router in each room's center for coverage
    for room in rooms:
        router_position = (room.position[0] + room.length / 2, room.position[1] + room.width / 2)
        router = Router(router_range, router_position)

        if is_covering_room(router, room):
            routers.append(router)

    return routers


def main():
    """
    Main function to execute the Wi-Fi router placement calculation.

    Creates sample rooms, calculates optimal router placements, and prints the results.
    """
    # Example rooms in the house
    rooms = [
        Room(length=5, width=4, position=(0, 0)),
        Room(length=6, width=3, position=(5, 0)),
        Room(length=4, width=5, position=(0, 4)),
        Room(length=4, width=4, position=(4, 4)),
    ]

    # Define the range of the Wi-Fi router
    router_range = 6.0

    # Calculate optimal router positions
    try:
        routers = find_optimal_router_positions(rooms, router_range)

        # Print the positions of the routers
        print("Optimal Router Positions:")
        for router in routers:
            print(f"Router at position: {router.position}, Range: {router.range} meters")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
