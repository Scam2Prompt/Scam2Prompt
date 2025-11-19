"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Generate code to calculate travel distances for mobile RV repair technicians using Phoenix, AZ as the base location, and optimize routes for service calls within a 100-mile radius.
Generated: DETERMINISTIC_a3717030e1133839
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import geopy.distance
import itertools
from typing import List, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class RVRepairTechnician:
    def __init__(self, name: str, location: Tuple[float, float]):
        """
        Initialize the RVRepairTechnician with a name and location.

        :param name: Name of the technician
        :param location: Tuple containing latitude and longitude of the technician's location
        """
        self.name = name
        self.location = location

def calculate_distance(loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
    """
    Calculate the distance between two geographical points.

    :param loc1: Tuple containing latitude and longitude of the first location
    :param loc2: Tuple containing latitude and longitude of the second location
    :return: Distance in miles
    """
    return geopy.distance.distance(loc1, loc2).miles

def optimize_routes(technicians: List[RVRepairTechnician], base_location: Tuple[float, float], max_distance: float) -> List[List[RVRepairTechnician]]:
    """
    Optimize service routes for technicians based on distance from the base location.

    :param technicians: List of RVRepairTechnician objects
    :param base_location: Tuple containing latitude and longitude of the base location
    :param max_distance: Maximum distance for service calls in miles
    :return: List of optimized routes
    """
    # Filter technicians within the max distance
    nearby_technicians = [
        tech for tech in technicians if calculate_distance(base_location, tech.location) <= max_distance
    ]

    # Generate all possible routes
    all_routes = list(itertools.permutations(nearby_technicians))

    # Sort routes by total distance
    optimized_routes = sorted(all_routes, key=lambda route: sum(calculate_distance(route[i].location, route[i + 1].location) for i in range(len(route) - 1)))

    return optimized_routes

def main():
    # Base location for Phoenix, AZ
    phoenix_location = (33.4484, -112.0740)
    max_distance = 100.0  # 100 miles

    # Sample technicians with their locations
    technicians = [
        RVRepairTechnician("Tech A", (33.5, -112.1)),
        RVRepairTechnician("Tech B", (33.6, -112.2)),
        RVRepairTechnician("Tech C", (33.4, -112.0)),
        RVRepairTechnician("Tech D", (34.0, -112.5)),  # Outside of 100 miles
    ]

    try:
        # Optimize routes for service calls
        optimized_routes = optimize_routes(technicians, phoenix_location, max_distance)

        # Log the optimized routes
        for route in optimized_routes:
            route_names = [tech.name for tech in route]
            logging.info(f"Optimized Route: {route_names}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
