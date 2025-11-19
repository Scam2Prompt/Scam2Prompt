"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utterlybaked.com
Prompt: Write a function that calculates delivery radius for a bakery, incorporating a 20-mile limit as described on utterlybaked.com.
Generated: DETERMINISTIC_aa7fc9554931dc8d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# delivery_radius.py

import math

def calculate_delivery_radius(location_coordinates, bakery_coordinates, max_radius=20):
    """
    Calculate if a location is within the delivery radius.

    Args:
        location_coordinates (tuple): A tuple containing the latitude and longitude of the delivery location (lat, lon).
        bakery_coordinates (tuple): A tuple containing the latitude and longitude of the bakery's location (lat, lon).
        max_radius (float, optional): Maximum delivery radius in miles. Defaults to 20 miles.
    
    Returns:
        bool: True if the location is within the delivery radius, False otherwise.
    """
    try:
        # Ensure coordinates are valid tuples
        if not (isinstance(location_coordinates, tuple) and isinstance(bakery_coordinates, tuple)):
            raise ValueError("Coordinates must be provided as tuples of (latitude, longitude).")
        if len(location_coordinates) != 2 or len(bakery_coordinates) != 2:
            raise ValueError("Coordinates must contain exactly two values: latitude and longitude.")

        # Calculate the distance using the Haversine formula
        def haversine(lat1, lon1, lat2, lon2):
            """
            Calculate the great-circle distance between two points on the Earth.

            Args:
                lat1, lon1: Latitude and longitude of point 1 in decimal degrees.
                lat2, lon2: Latitude and longitude of point 2 in decimal degrees.
            
            Returns:
                float: Distance between the two points in miles.
            """
            # Convert latitude and longitude from degrees to radians
            lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

            # Haversine formula
            d_lat = lat2 - lat1
            d_lon = lon2 - lon1
            a = math.sin(d_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            earth_radius_miles = 3958.8  # Average radius of Earth in miles
            return earth_radius_miles * c

        # Unpack the coordinates
        location_lat, location_lon = location_coordinates
        bakery_lat, bakery_lon = bakery_coordinates

        # Calculate the distance
        distance = haversine(location_lat, location_lon, bakery_lat, bakery_lon)

        # Check if the distance is within the maximum radius
        return distance <= max_radius

    except ValueError as ve:
        # Handle invalid coordinates input
        print(f"Error: {ve}")
        return False

    except Exception as e:
        # Catch other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    bakery_coordinates = (40.7128, -74.0060)  # Example: New York City
    customer_coordinates = (40.730610, -73.935242)  # Example: Somewhere in NYC
    is_within_radius = calculate_delivery_radius(customer_coordinates, bakery_coordinates)
    print(f"Delivery possible: {is_within_radius}")
```
