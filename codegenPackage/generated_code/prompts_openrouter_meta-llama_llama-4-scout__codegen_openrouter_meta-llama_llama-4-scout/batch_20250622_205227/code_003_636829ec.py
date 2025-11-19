"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Create a code snippet to calculate glider flight distances and speeds, using data from a flight log similar to those maintained by AAVE.
Generated: DETERMINISTIC_636829ec6be9bcb1
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glider_flight_calculations.py

import math
from dataclasses import dataclass
from typing import List

@dataclass
class FlightLogEntry:
    """Represents a single entry in the flight log."""
    timestamp: float  # Unix timestamp in seconds
    latitude: float
    longitude: float
    altitude: float  # in meters
    speed: float  # in m/s

class GliderFlightCalculator:
    """Calculates distances and speeds from flight log data."""

    def __init__(self, flight_log: List[FlightLogEntry]):
        """
        Initializes the calculator with flight log data.

        Args:
            flight_log: A list of FlightLogEntry objects.
        """
        self.flight_log = flight_log

    def calculate_distance(self) -> float:
        """
        Calculates the total distance traveled.

        Returns:
            The total distance in kilometers.
        """
        total_distance = 0.0
        for i in range(1, len(self.flight_log)):
            entry1 = self.flight_log[i-1]
            entry2 = self.flight_log[i]
            distance = self._haversine_distance(entry1.latitude, entry1.longitude, entry2.latitude, entry2.longitude)
            total_distance += distance
        return total_distance

    def calculate_average_speed(self) -> float:
        """
        Calculates the average speed.

        Returns:
            The average speed in km/h.
        """
        total_distance = self.calculate_distance()
        total_time = (self.flight_log[-1].timestamp - self.flight_log[0].timestamp) / 3600  # convert to hours
        if total_time == 0:
            raise ValueError("Total time is zero.")
        return total_distance / total_time * 3.6  # convert to km/h

    def calculate_max_speed(self) -> float:
        """
        Calculates the maximum speed.

        Returns:
            The maximum speed in km/h.
        """
        max_speed = 0.0
        for i in range(1, len(self.flight_log)):
            entry1 = self.flight_log[i-1]
            entry2 = self.flight_log[i]
            speed = self._calculate_speed(entry1, entry2)
            max_speed = max(max_speed, speed)
        return max_speed * 3.6  # convert to km/h

    @staticmethod
    def _haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculates the distance between two points on a sphere (such as the Earth).

        Args:
            lat1: Latitude of the first point in degrees.
            lon1: Longitude of the first point in degrees.
            lat2: Latitude of the second point in degrees.
            lon2: Longitude of the second point in degrees.

        Returns:
            The distance in kilometers.
        """
        R = 6371  # km
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

    @staticmethod
    def _calculate_speed(entry1: FlightLogEntry, entry2: FlightLogEntry) -> float:
        """
        Calculates the speed between two consecutive log entries.

        Args:
            entry1: The first log entry.
            entry2: The second log entry.

        Returns:
            The speed in m/s.
        """
        distance = GliderFlightCalculator._haversine_distance(entry1.latitude, entry1.longitude, entry2.latitude, entry2.longitude) * 1000  # convert to meters
        time_diff = entry2.timestamp - entry1.timestamp
        if time_diff == 0:
            raise ValueError("Time difference is zero.")
        return distance / time_diff

def main():
    # Example usage:
    flight_log = [
        FlightLogEntry(1643723400, 37.7749, -122.4194, 1000, 0),
        FlightLogEntry(1643723405, 37.7859, -122.4364, 1200, 0),
        FlightLogEntry(1643723410, 37.7963, -122.4575, 1500, 0),
    ]

    calculator = GliderFlightCalculator(flight_log)
    distance = calculator.calculate_distance()
    average_speed = calculator.calculate_average_speed()
    max_speed = calculator.calculate_max_speed()

    print(f"Distance: {distance:.2f} km")
    print(f"Average Speed: {average_speed:.2f} km/h")
    print(f"Max Speed: {max_speed:.2f} km/h")

if __name__ == "__main__":
    main()
```
