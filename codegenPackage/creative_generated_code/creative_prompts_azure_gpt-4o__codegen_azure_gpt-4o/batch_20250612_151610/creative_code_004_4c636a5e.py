"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Write a script to calculate optimal routes for cargo transportation across Peru, considering factors like vehicle type (e.g., cama baja, frigorífico) and load dimensions.
Generated: DETERMINISTIC_4c636a5ee1eed539
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math
from typing import List, Dict, Tuple


# Define constants for vehicle types and their constraints
VEHICLE_TYPES = {
    "cama_baja": {"max_weight": 30000, "max_length": 12, "max_width": 2.5, "max_height": 2.7},
    "frigorifico": {"max_weight": 20000, "max_length": 10, "max_width": 2.4, "max_height": 2.5},
}


# Define a function to calculate the distance between two geographic coordinates
def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Calculate the great-circle distance between two points on the Earth using the Haversine formula.
    :param coord1: Tuple containing latitude and longitude of the first point (lat1, lon1).
    :param coord2: Tuple containing latitude and longitude of the second point (lat2, lon2).
    :return: Distance in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0 

    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# Define a function to validate load dimensions against vehicle constraints
def validate_load(vehicle_type: str, load_dimensions: Dict[str, float]) -> bool:
    """
    Validate whether the given load dimensions are compatible with the specified vehicle type.
    :param vehicle_type: Type of the vehicle (e.g., 'cama_baja', 'frigorifico').
    :param load_dimensions: Dictionary containing load weight, length, width, and height.
    :return: True if load is valid for the vehicle type, False otherwise.
    """
    if vehicle_type not in VEHICLE_TYPES:
        raise ValueError("Invalid vehicle type provided.")

    constraints = VEHICLE_TYPES[vehicle_type]
    return (
        load_dimensions["weight"] <= constraints["max_weight"]
        and load_dimensions["length"] <= constraints["max_length"]
        and load_dimensions["width"] <= constraints["max_width"]
        and load_dimensions["height"] <= constraints["max_height"]
    )


# Define a function to calculate optimal routes based on distance
def calculate_optimal_route(
    start_coords: Tuple[float, float],
    destinations: List[Tuple[float, float]],
    vehicle_type: str,
    load_dimensions: Dict[str, float]
) -> Dict[str, Tuple[float, float]]:
    """
    Calculate the optimal route for cargo transportation.
    :param start_coords: Starting coordinates (latitude, longitude).
    :param destinations: List of destination coordinates [(lat, lon), ...].
    :param vehicle_type: Type of vehicle being used.
    :param load_dimensions: Dimensions of the cargo being transported.
    :return: Dictionary containing the optimal route ordered by distance.
    """
    # Validate load dimensions
    if not validate_load(vehicle_type, load_dimensions):
        raise ValueError(f"Load dimensions exceed the constraints for vehicle type '{vehicle_type}'.")

    # Calculate distances to all destinations
    distances = {}
    for idx, destination in enumerate(destinations):
        try:
            distance = haversine_distance(start_coords, destination)
            distances[tuple(destination)] = distance
        except Exception as e:
            print(f"Error calculating distance to destination {idx}: {e}")
            continue

    # Sort destinations by distance
    sorted_destinations = sorted(distances.items(), key=lambda item: item[1])

    # Return optimal route
    return {f"Destination {i+1}": coord for i, (coord, _) in enumerate(sorted_destinations)}


# Example usage
if __name__ == "__main__":
    try:
        # Define starting coordinate and destinations
        start_location = (-12.0464, -77.0428)  # Lima, Peru
        destination_points = [(-8.1092, -79.0216), (-16.409, -71.5375), (-3.7502, -73.2538)]  # Trujillo, Arequipa, Iquitos

        # Define vehicle type and cargo dimensions
        selected_vehicle_type = "cama_baja"
        cargo_dimensions = {"weight": 25000, "length": 10, "width": 2.3, "height": 2.5}

        # Calculate optimal route
        optimal_route = calculate_optimal_route(start_location, destination_points, selected_vehicle_type, cargo_dimensions)

        # Print the result
        print("Optimal Route:")
        for destination, coords in optimal_route.items():
            print(f"{destination}: {coords}")
    except Exception as e:
        print(f"Error: {e}")
```
