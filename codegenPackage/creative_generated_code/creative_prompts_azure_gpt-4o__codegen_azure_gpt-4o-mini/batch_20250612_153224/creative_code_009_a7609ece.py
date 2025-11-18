"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write a function to calculate the total distance and estimated time for multi-day hiking trips, incorporating destinations like "Планината Тимфи" and "Каньона Викос."
Generated: DETERMINISTIC_a7609ececebcf881
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from datetime import timedelta

class HikingTrip:
    def __init__(self):
        # Dictionary to store the distance (in km) between destinations
        self.distances = {
            ("Планината Тимфи", "Каньона Викос"): 20.0,  # Example distance
            ("Каньона Викос", "Планината Тимфи"): 20.0,
            # Additional routes can be added here
        }
    
    def calculate_distance(self, route):
        """
        Calculate the total distance for the given route.

        :param route: List of destinations in the order of hiking
        :return: Total distance in kilometers
        """
        total_distance = 0.0
        
        for i in range(len(route) - 1):
            segment = (route[i], route[i + 1])
            if segment in self.distances:
                total_distance += self.distances[segment]
            else:
                raise ValueError(f"Distance between {route[i]} and {route[i + 1]} is not defined.")
        
        return total_distance

    def estimate_time(self, total_distance, average_speed=5.0):
        """
        Estimate the total time for the trip based on distance and average speed.

        :param total_distance: Total distance to be traveled (in km)
        :param average_speed: Average hiking speed (in km/h)
        :return: Estimated time as a timedelta object
        """
        if average_speed <= 0:
            raise ValueError("Average speed must be greater than zero.")
        
        # Calculate time in hours
        time_hours = total_distance / average_speed
        
        # Return as a timedelta object
        return timedelta(hours=time_hours)

    def calculate_trip(self, route, average_speed=5.0):
        """
        Calculate the total distance and estimated time for a hiking trip.

        :param route: List of destinations in the order of hiking
        :param average_speed: Average hiking speed (in km/h)
        :return: Tuple containing total distance and estimated time
        """
        try:
            total_distance = self.calculate_distance(route)
            estimated_time = self.estimate_time(total_distance, average_speed)
            return total_distance, estimated_time
        except Exception as e:
            print(f"Error: {e}")
            return None, None

# Example usage:
if __name__ == "__main__":
    trip = HikingTrip()
    route = ["Планината Тимфи", "Каньона Викос"]
    average_speed = 5.0  # Average speed in km/h

    distance, time = trip.calculate_trip(route, average_speed)
    if distance is not None and time is not None:
        print(f"Total distance: {distance} km")
        print(f"Estimated time: {time}")
```
