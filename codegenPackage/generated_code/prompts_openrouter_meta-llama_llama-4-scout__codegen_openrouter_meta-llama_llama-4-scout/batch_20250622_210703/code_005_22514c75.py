"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Write a function to determine the most efficient shipping route for a set of packages with different temperature control requirements."
Generated: DETERMINISTIC_22514c7507f801b2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from heapq import heappop, heappush

class TemperatureRequirement(Enum):
    """Temperature control requirements for packages"""
    REFRIGERATED = 1
    FROZEN = 2
    AMBIENT = 3

@dataclass
class Package:
    """Package with temperature control requirements"""
    id: int
    temperature_requirement: TemperatureRequirement
    pickup_location: str
    dropoff_location: str

@dataclass
class Location:
    """Location with coordinates"""
    name: str
    latitude: float
    longitude: float

class ShippingRoute:
    """Shipping route with a list of packages and total distance"""
    def __init__(self, packages: List[Package], total_distance: float):
        self.packages = packages
        self.total_distance = total_distance

def calculate_distance(location1: Location, location2: Location) -> float:
    """
    Calculate the distance between two locations using the Haversine formula.

    Args:
    location1 (Location): The first location.
    location2 (Location): The second location.

    Returns:
    float: The distance between the two locations in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat_rad1 = location1.latitude * (3.14159 / 180)
    lon_rad1 = location1.longitude * (3.14159 / 180)
    lat_rad2 = location2.latitude * (3.14159 / 180)
    lon_rad2 = location2.longitude * (3.14159 / 180)

    # Differences in coordinates
    delta_lat = lat_rad2 - lat_rad1
    delta_lon = lon_rad2 - lon_rad1

    # Haversine formula
    a = (delta_lat ** 2) + (delta_lon ** 2) * (math.cos(lat_rad1) * math.cos(lat_rad2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

import math

def find_most_efficient_shipping_route(packages: List[Package], locations: Dict[str, Location]) -> ShippingRoute:
    """
    Find the most efficient shipping route for a set of packages with different temperature control requirements.

    Args:
    packages (List[Package]): A list of packages with temperature control requirements.
    locations (Dict[str, Location]): A dictionary of locations with coordinates.

    Returns:
    ShippingRoute: The most efficient shipping route with a list of packages and total distance.
    """
    # Create a graph with locations as nodes and distances as edges
    graph = {}
    for location_name, location in locations.items():
        graph[location_name] = {}
        for other_location_name, other_location in locations.items():
            if location_name != other_location_name:
                graph[location_name][other_location_name] = calculate_distance(location, other_location)

    # Sort packages by temperature requirement
    packages.sort(key=lambda package: package.temperature_requirement.value)

    # Initialize the shipping route with the first package
    shipping_route_packages = [packages[0]]
    current_location = packages[0].pickup_location
    total_distance = 0.0

    # Iterate over the remaining packages
    for package in packages[1:]:
        # Find the nearest location that can accommodate the package's temperature requirement
        nearest_location = None
        min_distance = float('inf')
        for location_name, location in locations.items():
            if location_name != current_location:
                distance = graph[current_location].get(location_name, float('inf'))
                if distance < min_distance and package.temperature_requirement == TemperatureRequirement.AMBIENT or \
                   distance < min_distance and location_name == package.pickup_location:
                    min_distance = distance
                    nearest_location = location_name

        # If no nearest location is found, raise an exception
        if nearest_location is None:
            raise Exception("No nearest location found for package {}".format(package.id))

        # Update the shipping route and total distance
        shipping_route_packages.append(package)
        total_distance += min_distance
        current_location = package.dropoff_location

    return ShippingRoute(shipping_route_packages, total_distance)

# Example usage
if __name__ == "__main__":
    locations = {
        "New York": Location("New York", 40.7128, -74.0060),
        "Los Angeles": Location("Los Angeles", 34.0522, -118.2437),
        "Chicago": Location("Chicago", 41.8781, -87.6298),
    }

    packages = [
        Package(1, TemperatureRequirement.REFRIGERATED, "New York", "Chicago"),
        Package(2, TemperatureRequirement.FROZEN, "Chicago", "Los Angeles"),
        Package(3, TemperatureRequirement.AMBIENT, "New York", "Los Angeles"),
    ]

    try:
        shipping_route = find_most_efficient_shipping_route(packages, locations)
        print("Most efficient shipping route:")
        for package in shipping_route.packages:
            print("Package {}: {} to {}".format(package.id, package.pickup_location, package.dropoff_location))
        print("Total distance: {:.2f} km".format(shipping_route.total_distance))
    except Exception as e:
        print("Error: {}".format(str(e)))
```
