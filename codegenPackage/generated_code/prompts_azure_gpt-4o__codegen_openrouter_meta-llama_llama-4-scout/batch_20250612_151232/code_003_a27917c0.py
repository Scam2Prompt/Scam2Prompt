"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Develop a logistics optimization algorithm for ENL Consortium's haulage system, considering truck fleet types (flatbeds, low loaders) and routes for local and up-country cargo transportation.
Generated: DETERMINISTIC_a27917c0d78a89ef
Batch ID: 20250612_151232
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
from math import inf

class TruckType(str, Enum):
    """Enum for truck types."""
    FLATBED = "flatbed"
    LOW_LOADER = "low_loader"

@dataclass
class Truck:
    """Class to represent a truck."""
    truck_type: TruckType
    capacity: float  # in tons
    current_location: str

@dataclass
class Route:
    """Class to represent a route."""
    origin: str
    destination: str
    distance: float  # in kilometers

@dataclass
class Cargo:
    """Class to represent a cargo."""
    weight: float  # in tons
    route: Route

class LogisticsOptimizer:
    def __init__(self, trucks: List[Truck], routes: List[Route], cargo_list: List[Cargo]):
        self.trucks = trucks
        self.routes = routes
        self.cargo_list = cargo_list

    def optimize(self) -> Dict[Truck, List[Cargo]]:
        """Optimize cargo transportation by assigning cargo to suitable trucks."""
        # Initialize assignment
        assignment: Dict[Truck, List[Cargo]] = {truck: [] for truck in self.trucks}

        # Sort cargo by weight in descending order
        self.cargo_list.sort(key=lambda cargo: cargo.weight, reverse=True)

        for cargo in self.cargo_list:
            # Find the most suitable truck for the current cargo
            suitable_trucks = [truck for truck in self.trucks if truck.capacity >= cargo.weight]
            if suitable_trucks:
                # Select the truck with the most available capacity
                suitable_trucks.sort(key=lambda truck: truck.capacity - sum(cargo.weight for cargo in assignment[truck]), reverse=True)
                selected_truck = suitable_trucks[0]
                assignment[selected_truck].append(cargo)
            else:
                print(f"No suitable truck found for cargo of weight {cargo.weight} tons on route {cargo.route.origin} to {cargo.route.destination}")

        return assignment

    def calculate_total_distance(self, assignment: Dict[Truck, List[Cargo]]) -> float:
        """Calculate the total distance traveled by all trucks."""
        total_distance = 0
        for truck, cargo_list in assignment.items():
            for cargo in cargo_list:
                total_distance += cargo.route.distance * 2  # to and from
        return total_distance

def main():
    try:
        # Example usage
        trucks = [
            Truck(TruckType.FLATBED, 10, "Warehouse A"),
            Truck(TruckType.LOW_LOADER, 20, "Warehouse B")
        ]

        routes: List[Route] = [
            Route("Warehouse A", "City X", 100),
            Route("Warehouse B", "City Y", 200)
        ]

        cargo_list: List[Cargo] = [
            Cargo(5, routes[0]),
            Cargo(15, routes[1]),
            Cargo(8, routes[0])
        ]

        optimizer = LogisticsOptimizer(trucks, routes, cargo_list)
        assignment = optimizer.optimize()
        for truck, cargo_list in assignment.items():
            print(f"Truck {truck.truck_type} at {truck.current_location} is assigned cargo:")
            for cargo in cargo_list:
                print(f"- Weight: {cargo.weight} tons, Route: {cargo.route.origin} to {cargo.route.destination}")

        total_distance = optimizer.calculate_total_distance(assignment)
        print(f"Total distance traveled: {total_distance} km")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
