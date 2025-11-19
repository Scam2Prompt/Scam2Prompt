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

def calculate_trip_metrics(route_points, average_speed=15, elevation_gain_per_km=50):
    """
    Calculate distance, elevation gain, and estimated time for a bikepacking trip.

    Parameters:
        route_points (list of tuples): List of (latitude, longitude, elevation) points defining the route.
        average_speed (float): Average speed in km/h. Default is 15 km/h.
        elevation_gain_per_km (float): Additional time (in minutes) per km for elevation gain. Default is 50 minutes/km.

    Returns:
        dict: A dictionary containing total distance (km), total elevation gain (m), and estimated time (hours).
    """
    def haversine_distance(lat1, lon1, lat2, lon2):
        """
        Calculate the great-circle distance between two points on the Earth using the Haversine formula.

        Parameters:
            lat1, lon1: Latitude and longitude of the first point in decimal degrees.
            lat2, lon2: Latitude and longitude of the second point in decimal degrees.

        Returns:
            float: Distance in kilometers.
        """
        R = 6371  # Radius of the Earth in kilometers
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    total_distance = 0
    total_elevation_gain = 0

    # Iterate through route points to calculate distance and elevation gain
    for i in range(len(route_points) - 1):
        lat1, lon1, ele1 = route_points[i]
        lat2, lon2, ele2 = route_points[i + 1]
        
        # Calculate distance between consecutive points
        total_distance += haversine_distance(lat1, lon1, lat2, lon2)
        
        # Calculate elevation gain (only positive elevation changes are considered)
        elevation_change = ele2 - ele1
        if elevation_change > 0:
            total_elevation_gain += elevation_change

    # Calculate estimated time
    flat_time = total_distance / average_speed  # Time in hours for flat terrain
    elevation_time = (total_elevation_gain / 1000) * elevation_gain_per_km / 60  # Time in hours for elevation gain
    estimated_time = flat_time + elevation_time

    return {
        "total_distance_km": round(total_distance, 2),
        "total_elevation_gain_m": round(total_elevation_gain, 2),
        "estimated_time_hours": round(estimated_time, 2)
    }

# Example usage
if __name__ == "__main__":
    # Define a sample route with (latitude, longitude, elevation in meters)
    route = [
        (37.7749, -122.4194, 10),  # San Francisco
        (37.8715, -122.2730, 50),  # Berkeley
        (38.5816, -121.4944, 15),  # Sacramento
    ]

    try:
        trip_metrics = calculate_trip_metrics(route)
        print("Bikepacking Trip Metrics:")
        print(f"Total Distance: {trip_metrics['total_distance_km']} km")
        print(f"Total Elevation Gain: {trip_metrics['total_elevation_gain_m']} m")
        print(f"Estimated Time: {trip_metrics['estimated_time_hours']} hours")
    except Exception as e:
        print(f"An error occurred while calculating trip metrics: {e}")
```
