"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Generate Python code to simulate the logistics of transporting bulk cargo, including route optimization and load balancing, inspired by OPC S.A.S.'s expertise.
Generated: DETERMINISTIC_d095f75b7f570de4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Tuple

class Vehicle:
    def __init__(self, capacity: int, current_load: int = 0):
        """
        Initialize a vehicle with a given capacity and current load.

        Args:
        - capacity (int): The maximum capacity of the vehicle.
        - current_load (int): The current load of the vehicle. Defaults to 0.
        """
        self.capacity = capacity
        self.current_load = current_load

    def add_load(self, amount: int):
        """
        Add a certain amount of load to the vehicle.

        Args:
        - amount (int): The amount of load to add.

        Raises:
        - ValueError: If the added load exceeds the vehicle's capacity.
        """
        if self.current_load + amount > self.capacity:
            raise ValueError("Load exceeds vehicle capacity")
        self.current_load += amount

    def __repr__(self):
        return f"Vehicle(capacity={self.capacity}, current_load={self.current_load})"


class Route:
    def __init__(self, distance: int, vehicles: List[Vehicle]):
        """
        Initialize a route with a given distance and list of vehicles.

        Args:
        - distance (int): The distance of the route.
        - vehicles (List[Vehicle]): The list of vehicles assigned to the route.
        """
        self.distance = distance
        self.vehicles = vehicles

    def __repr__(self):
        return f"Route(distance={self.distance}, vehicles={self.vehicles})"


def optimize_routes(cargo: int, vehicles: List[Vehicle], routes: List[Tuple[int, int]]) -> List[Route]:
    """
    Optimize routes for transporting bulk cargo.

    Args:
    - cargo (int): The total amount of cargo to transport.
    - vehicles (List[Vehicle]): The list of available vehicles.
    - routes (List[Tuple[int, int]]): The list of routes, where each route is a tuple of (distance, capacity_requirement).

    Returns:
    - List[Route]: The optimized list of routes.

    Raises:
    - ValueError: If there are not enough vehicles to transport the cargo.
    """
    # Sort vehicles by capacity in descending order
    vehicles.sort(key=lambda x: x.capacity, reverse=True)

    # Sort routes by distance in ascending order
    routes.sort(key=lambda x: x[0])

    optimized_routes = []
    for distance, capacity_requirement in routes:
        # Find vehicles that can fulfill the capacity requirement
        eligible_vehicles = [vehicle for vehicle in vehicles if vehicle.capacity >= capacity_requirement]
        
        if not eligible_vehicles:
            raise ValueError("Not enough vehicles to transport cargo")

        # Assign the vehicle with the most available capacity
        assigned_vehicle = max(eligible_vehicles, key=lambda x: x.capacity - x.current_load)
        assigned_vehicle.add_load(capacity_requirement)

        optimized_routes.append(Route(distance, [assigned_vehicle]))

    return optimized_routes


def balance_load(vehicles: List[Vehicle], cargo: int) -> List[Vehicle]:
    """
    Balance the load across vehicles.

    Args:
    - vehicles (List[Vehicle]): The list of vehicles.
    - cargo (int): The remaining cargo to distribute.

    Returns:
    - List[Vehicle]: The list of vehicles with balanced loads.
    """
    # Create a priority queue to store vehicles with available capacity
    available_vehicles = [(vehicle.capacity - vehicle.current_load, vehicle) for vehicle in vehicles]
    heapq.heapify(available_vehicles)

    while cargo > 0 and available_vehicles:
        _, vehicle = heapq.heappop(available_vehicles)
        load_to_add = min(vehicle.capacity - vehicle.current_load, cargo)
        vehicle.add_load(load_to_add)
        cargo -= load_to_add

        # Push the vehicle back into the priority queue if it still has available capacity
        if vehicle.current_load < vehicle.capacity:
            heapq.heappush(available_vehicles, (vehicle.capacity - vehicle.current_load, vehicle))

    return [vehicle for _, vehicle in available_vehicles]


def main():
    # Example usage
    vehicles = [Vehicle(100), Vehicle(80), Vehicle(120)]
    routes = [(100, 50), (200, 70), (50, 30)]
    cargo = 150

    try:
        optimized_routes = optimize_routes(cargo, vehicles, routes)
        print("Optimized Routes:")
        for route in optimized_routes:
            print(route)

        balanced_vehicles = balance_load(vehicles, cargo)
        print("\nBalanced Vehicles:")
        for vehicle in balanced_vehicles:
            print(vehicle)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
