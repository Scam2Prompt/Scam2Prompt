"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Develop a logistics optimization algorithm for ENL Consortium's haulage system, considering truck fleet types (flatbeds, low loaders) and routes for local and up-country cargo transportation.
Generated: DETERMINISTIC_a27917c0d78a89ef
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from typing import List, Dict, Tuple, Any

class Truck:
    """
    This class represents a truck in the fleet.
    Attributes:
        truck_id (str): Unique identifier for the truck.
        truck_type (str): Type of the truck (e.g., 'flatbed', 'low loader').
        capacity (float): Maximum weight capacity of the truck in tons.
    """
    def __init__(self, truck_id: str, truck_type: str, capacity: float):
        self.truck_id = truck_id
        self.truck_type = truck_type
        self.capacity = capacity

class Route:
    """
    This class represents a transportation route.
    Attributes:
        route_id (str): Unique identifier for the route.
        distance (float): Distance of the route in kilometers.
        cargo_weight (float): Weight of the cargo to be transported in tons.
    """
    def __init__(self, route_id: str, distance: float, cargo_weight: float):
        self.route_id = route_id
        self.distance = distance
        self.cargo_weight = cargo_weight

class LogisticsOptimizer:
    """
    This class implements the logistics optimization algorithm.
    It assigns trucks to routes based on availability and capacity.
    """
    def __init__(self, trucks: List[Truck], routes: List[Route]):
        """
        Initializes the logistics optimizer with a list of trucks and routes.
        
        :param trucks: List of Truck objects representing the fleet.
        :param routes: List of Route objects representing the transportation routes.
        """
        self.trucks = trucks
        self.routes = routes
        self.assignments: Dict[str, str] = {}  # Maps route_id to truck_id

    def optimize(self):
        """
        Optimizes the truck assignments to routes based on capacity and distance.
        """
        for route in self.routes:
            assigned = False
            for truck in self.trucks:
                if self._can_assign(truck, route) and not assigned:
                    self.assignments[route.route_id] = truck.truck_id
                    assigned = True
                    break
            if not assigned:
                self.assignments[route.route_id] = "No suitable truck available"

    def _can_assign(self, truck: Truck, route: Route) -> bool:
        """
        Checks if a truck can be assigned to a route based on capacity.

        :param truck: The Truck object to check.
        :param route: The Route object to check.
        :return: True if the truck can be assigned to the route, else False.
        """
        return truck.capacity >= route.cargo_weight

    def get_assignments(self) -> Dict[str, str]:
        """
        Returns the current assignments of trucks to routes.

        :return: A dictionary mapping route_id to truck_id.
        """
        return self.assignments

def main():
    """
    Main function to execute the logistics optimization algorithm.
    """
    # Example truck fleet
    trucks = [
        Truck(truck_id="T001", truck_type="flatbed", capacity=10.0),
        Truck(truck_id="T002", truck_type="low loader", capacity=12.0),
        Truck(truck_id="T003", truck_type="flatbed", capacity=8.0),
    ]

    # Example routes
    routes = [
        Route(route_id="R001", distance=100.0, cargo_weight=5.0),
        Route(route_id="R002", distance=200.0, cargo_weight=11.0),
        Route(route_id="R003", distance=150.0, cargo_weight=15.0),  # No suitable truck
    ]

    # Create and run the logistics optimizer
    optimizer = LogisticsOptimizer(trucks, routes)
    optimizer.optimize()

    # Output the assignments
    assignments = optimizer.get_assignments()
    for route_id, truck_id in assignments.items():
        print(f"Route {route_id} is assigned to Truck {truck_id}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
