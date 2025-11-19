"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Create a Python program to optimize furniture transportation logistics, ensuring safety during transit, as per the methods described on the "شمس المملكة" website.
Generated: DETERMINISTIC_a30c863796c22bf5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Furniture Transportation Logistics Optimizer

This program optimizes the logistics of furniture transportation, ensuring safety during transit.
It includes features for route optimization, load balancing, and safety checks based on the
methods described on the "شمس المملكة" website.

Key Features:
- Route optimization using Dijkstra's algorithm
- Load balancing calculations
- Safety checks for furniture dimensions and weight
- Transportation cost estimation
"""

import heapq
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import math

@dataclass
class FurnitureItem:
    """Class representing a furniture item to be transported."""
    name: str
    length: float  # in meters
    width: float   # in meters
    height: float  # in meters
    weight: float  # in kilograms
    fragile: bool

@dataclass
class Vehicle:
    """Class representing a transportation vehicle."""
    name: str
    max_length: float  # in meters
    max_width: float   # in meters
    max_height: float  # in meters
    max_weight: float  # in kilograms
    cost_per_km: float # in currency

class TransportationOptimizer:
    """Main class for optimizing furniture transportation logistics."""
    
    def __init__(self):
        self.vehicles: List[Vehicle] = []
        self.graph: Dict[str, Dict[str, float]] = {}
        
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the available fleet."""
        self.vehicles.append(vehicle)
    
    def add_route(self, location1: str, location2: str, distance: float) -> None:
        """Add a route between two locations with the given distance."""
        if location1 not in self.graph:
            self.graph[location1] = {}
        if location2 not in self.graph:
            self.graph[location2] = {}
        
        self.graph[location1][location2] = distance
        self.graph[location2][location1] = distance
    
    def find_optimal_route(self, start: str, end: str) -> Tuple[float, List[str]]:
        """
        Find the shortest route between two locations using Dijkstra's algorithm.
        
        Returns:
            Tuple of (total_distance, path) where path is a list of locations.
        """
        if start not in self.graph or end not in self.graph:
            raise ValueError("Start or end location not found in the network")
        
        # Priority queue: (distance, current_location, path)
        heap = [(0, start, [])]
        visited = set()
        
        while heap:
            dist, current, path = heapq.heappop(heap)
            
            if current in visited:
                continue
                
            if current == end:
                return (dist, path + [current])
                
            visited.add(current)
            
            for neighbor, distance in self.graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (dist + distance, neighbor, path + [current]))
        
        raise ValueError("No path found between the specified locations")
    
    def select_vehicle(self, items: List[FurnitureItem]) -> Vehicle:
        """
        Select the most appropriate vehicle for the given furniture items.
        
        Returns:
            The optimal Vehicle object.
        Raises:
            ValueError if no suitable vehicle is found.
        """
        total_volume = sum(item.length * item.width * item.height for item in items)
        total_weight = sum(item.weight for item in items)
        max_length = max(item.length for item in items)
        max_width = max(item.width for item in items)
        max_height = max(item.height for item in items)
        
        suitable_vehicles = []
        
        for vehicle in self.vehicles:
            if (vehicle.max_length >= max_length and
                vehicle.max_width >= max_width and
                vehicle.max_height >= max_height and
                vehicle.max_weight >= total_weight):
                suitable_vehicles.append(vehicle)
        
        if not suitable_vehicles:
            raise ValueError("No suitable vehicle found for the given furniture items")
        
        # Select the smallest vehicle that can accommodate the load
        return min(suitable_vehicles, key=lambda v: v.max_weight)
    
    def calculate_safety_score(self, items: List[FurnitureItem], vehicle: Vehicle) -> float:
        """
        Calculate a safety score (0-1) for transporting the given items in the specified vehicle.
        
        Higher scores indicate safer transportation.
        """
        total_volume = sum(item.length * item.width * item.height for item in items)
        vehicle_volume = vehicle.max_length * vehicle.max_width * vehicle.max_height
        
        volume_ratio = total_volume / vehicle_volume
        weight_ratio = sum(item.weight for item in items) / vehicle.max_weight
        
        # Penalize fragile items
        fragile_penalty = sum(1 for item in items if item.fragile) * 0.1
        
        # Calculate base score (lower is better)
        base_score = (volume_ratio * 0.6) + (weight_ratio * 0.4)
        
        # Normalize to 0-1 range (higher is better)
        safety_score = 1.0 - min(max(base_score, 0), 1)
        
        # Apply fragile penalty
        safety_score = max(0, safety_score - fragile_penalty)
        
        return round(safety_score, 2)
    
    def optimize_transport(self, items: List[FurnitureItem], start: str, end: str) -> Dict:
        """
        Optimize the transportation of furniture items from start to end location.
        
        Returns:
            Dictionary containing optimization results.
        """
        try:
            # Step 1: Select appropriate vehicle
            vehicle = self.select_vehicle(items)
            
            # Step 2: Find optimal route
            distance, path = self.find_optimal_route(start, end)
            
            # Step 3: Calculate safety score
            safety_score = self.calculate_safety_score(items, vehicle)
            
            # Step 4: Calculate cost
            cost = distance * vehicle.cost_per_km
            
            return {
                'vehicle': vehicle.name,
                'route': path,
                'distance': round(distance, 2),
                'cost': round(cost, 2),
                'safety_score': safety_score,
                'items': [item.name for item in items],
                'status': 'success'
            }
        except ValueError as e:
            return {
                'status': 'error',
                'message': str(e)
            }

# Example usage
if __name__ == "__main__":
    # Initialize optimizer
    optimizer = TransportationOptimizer()
    
    # Add vehicles
    optimizer.add_vehicle(Vehicle("Small Truck", 3, 2, 2, 1000, 1.5))
    optimizer.add_vehicle(Vehicle("Medium Truck", 4, 2.5, 2.5, 2000, 2.0))
    optimizer.add_vehicle(Vehicle("Large Truck", 5, 3, 3, 3000, 2.5))
    
    # Add routes
    optimizer.add_route("Warehouse", "Location A", 10.5)
    optimizer.add_route("Warehouse", "Location B", 8.2)
    optimizer.add_route("Location A", "Location B", 5.1)
    optimizer.add_route("Location A", "Location C", 12.3)
    optimizer.add_route("Location B", "Location C", 7.8)
    
    # Define furniture items
    items = [
        FurnitureItem("Sofa", 2.5, 1, 0.8, 120, True),
        FurnitureItem("Coffee Table", 1.2, 0.8, 0.5, 25, False),
        FurnitureItem("Bookshelf", 1.8, 0.4, 2, 40, True)
    ]
    
    # Optimize transport
    result = optimizer.optimize_transport(items, "Warehouse", "Location C")
    print(result)
```
