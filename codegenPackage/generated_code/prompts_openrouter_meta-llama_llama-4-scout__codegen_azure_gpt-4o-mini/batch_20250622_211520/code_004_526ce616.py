"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Write a code snippet in Python to help plan a bikepacking trip, including calculating the distance, elevation gain, and estimated time for a given route.
Generated: DETERMINISTIC_526ce61659b6253b
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class BikepackingTrip:
    def __init__(self, route):
        """
        Initializes the BikepackingTrip with a given route.

        :param route: List of tuples, where each tuple contains (latitude, longitude, elevation)
        """
        self.route = route

    def calculate_distance(self):
        """
        Calculates the total distance of the route in kilometers using the Haversine formula.

        :return: Total distance in kilometers
        """
        total_distance = 0.0
        for i in range(len(self.route) - 1):
            lat1, lon1, _ = self.route[i]
            lat2, lon2, _ = self.route[i + 1]
            total_distance += self.haversine(lat1, lon1, lat2, lon2)
        return total_distance

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Calculates the distance between two points on the Earth specified in decimal degrees.

        :param lat1: Latitude of point 1
        :param lon1: Longitude of point 1
        :param lat2: Latitude of point 2
        :param lon2: Longitude of point 2
        :return: Distance in kilometers
        """
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of Earth in kilometers
        return c * r

    def calculate_elevation_gain(self):
        """
        Calculates the total elevation gain of the route in meters.

        :return: Total elevation gain in meters
        """
        total_gain = 0.0
        for i in range(1, len(self.route)):
            elevation_change = self.route[i][2] - self.route[i - 1][2]
            if elevation_change > 0:
                total_gain += elevation_change
        return total_gain

    def estimate_time(self, average_speed_kmh):
        """
        Estimates the time required to complete the trip based on average speed.

        :param average_speed_kmh: Average speed in kilometers per hour
        :return: Estimated time in hours
        """
        if average_speed_kmh <= 0:
            raise ValueError("Average speed must be greater than zero.")
        
        distance = self.calculate_distance()
        return distance / average_speed_kmh

    def trip_summary(self, average_speed_kmh):
        """
        Provides a summary of the trip including distance, elevation gain, and estimated time.

        :param average_speed_kmh: Average speed in kilometers per hour
        :return: Dictionary containing trip summary
        """
        try:
            distance = self.calculate_distance()
            elevation_gain = self.calculate_elevation_gain()
            estimated_time = self.estimate_time(average_speed_kmh)

            return {
                "Total Distance (km)": distance,
                "Total Elevation Gain (m)": elevation_gain,
                "Estimated Time (hours)": estimated_time
            }
        except Exception as e:
            print(f"Error calculating trip summary: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample route: (latitude, longitude, elevation in meters)
    route = [
        (34.0522, -118.2437, 100),  # Start point
        (34.0522, -118.2537, 150),  # Point 1
        (34.0622, -118.2637, 200),  # Point 2
        (34.0722, -118.2737, 50)     # End point
    ]

    trip = BikepackingTrip(route)
    summary = trip.trip_summary(average_speed_kmh=15)  # Average speed of 15 km/h
    print(summary)
```
