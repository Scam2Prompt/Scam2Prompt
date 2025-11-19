"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write a Python script that simulates the planning process for optimal Wi-Fi signal distribution in a home based on user-defined room layouts.
Generated: DETERMINISTIC_2f116fad9106f43c
Batch ID: 20250612_155200
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
    """Represents a room in the home with its dimensions and Wi-Fi signal strength."""

    def __init__(self, name, length, width, signal_strength=0):
        """
        Initializes a Room object.

        Args:
            name (str): The name of the room.
            length (float): The length of the room in meters.
            width (float): The width of the room in meters.
            signal_strength (float, optional): The initial Wi-Fi signal strength in the room. Defaults to 0.
        """
        self.name = name
        self.length = length
        self.width = width
        self.signal_strength = signal_strength
        self.access_points = []

    def add_access_point(self, access_point):
        """
        Adds a Wi-Fi access point to the room.

        Args:
            access_point (AccessPoint): The access point to add.
        """
        self.access_points.append(access_point)

    def calculate_signal_strength(self):
        """
        Calculates the overall Wi-Fi signal strength in the room based on its access points.

        Returns:
            float: The calculated signal strength.
        """
        total_signal = 0
        for access_point in self.access_points:
            distance = access_point.calculate_distance(self.length, self.width)
            signal_attenuation = access_point.calculate_signal_attenuation(distance)
            total_signal += signal_attenuation * access_point.signal_strength
        self.signal_strength = total_signal
        return self.signal_strength


class AccessPoint:
    """Represents a Wi-Fi access point with its location and signal strength."""

    def __init__(self, x, y, signal_strength):
        """
        Initializes an AccessPoint object.

        Args:
            x (float): The x-coordinate of the access point.
            y (float): The y-coordinate of the access point.
            signal_strength (float): The signal strength of the access point.
        """
        self.x = x
        self.y = y
        self.signal_strength = signal_strength

    def calculate_distance(self, room_length, room_width):
        """
        Calculates the distance from the access point to the center of the room.

        Args:
            room_length (float): The length of the room.
            room_width (float): The width of the room.

        Returns:
            float: The calculated distance.
        """
        room_center_x = room_length / 2
        room_center_y = room_width / 2
        distance = math.sqrt((self.x - room_center_x) ** 2 + (self.y - room_center_y) ** 2)
        return distance

    def calculate_signal_attenuation(self, distance):
        """
        Calculates the signal attenuation based on the distance from the access point.

        Args:
            distance (float): The distance from the access point.

        Returns:
            float: The calculated signal attenuation.
        """
        # Assuming a simple inverse square law for signal attenuation
        if distance == 0:
            return 1
        return 1 / (distance ** 2)


def plan_wifi_distribution(rooms):
    """
    Plans the optimal Wi-Fi signal distribution in a home based on user-defined room layouts.

    Args:
        rooms (list[Room]): A list of Room objects.

    Returns:
        dict: A dictionary with room names as keys and their calculated signal strengths as values.
    """
    signal_strengths = {}
    for room in rooms:
        signal_strength = room.calculate_signal_strength()
        signal_strengths[room.name] = signal_strength
    return signal_strengths


def main():
    try:
        # Create rooms
        living_room = Room("Living Room", 5, 4)
        bedroom = Room("Bedroom", 4, 3)

        # Create access points
        living_room_access_point = AccessPoint(2.5, 2, 100)
        bedroom_access_point = AccessPoint(2, 1.5, 80)

        # Add access points to rooms
        living_room.add_access_point(living_room_access_point)
        bedroom.add_access_point(bedroom_access_point)

        # Plan Wi-Fi distribution
        rooms = [living_room, bedroom]
        signal_strengths = plan_wifi_distribution(rooms)

        # Print results
        print("Optimal Wi-Fi Signal Distribution:")
        for room, signal_strength in signal_strengths.items():
            print(f"{room}: {signal_strength:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
