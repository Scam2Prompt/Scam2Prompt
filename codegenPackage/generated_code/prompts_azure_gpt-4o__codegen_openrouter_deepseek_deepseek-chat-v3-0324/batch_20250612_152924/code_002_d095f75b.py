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
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class CargoType(Enum):
    """Types of cargo that can be transported."""
    DRY_BULK = 1
    LIQUID_BULK = 2
    CONTAINERIZED = 3
    REFRIGERATED = 4

@dataclass
class Cargo:
    """Represents a cargo shipment."""
    id: str
    weight: float  # in tons
    volume: float  # in cubic meters
    cargo_type: CargoType
    origin: str
    destination: str
    priority: int  # 1 (highest) to 5 (lowest)

@dataclass
class Vehicle:
    """Represents a transport vehicle."""
    id: str
    max_weight: float  # in tons
    max_volume: float  # in cubic meters
    cost_per_km: float
    speed: float  # km/h
    supported_cargo_types: List[CargoType]
    current_location: str

@dataclass
class Route:
    """Represents a transportation route between locations."""
    origin: str
    destination: str
    distance: float  # in km
    estimated_time: float  # in hours
    cost: float

class LogisticsSimulator:
    """Simulates bulk cargo transportation with route optimization and load balancing."""
    
    def __init__(self):
        self.cargos: Dict[str, Cargo] = {}
        self.vehicles: Dict[str, Vehicle] = {}
        self.routes: Dict[Tuple[str, str], Route] = {}
        self.locations: set = set()
    
    def add_cargo(self, cargo: Cargo) -> None:
        """Add a cargo shipment to the system."""
        if cargo.id in self.cargos:
            raise ValueError(f"Cargo with ID {cargo.id} already exists.")
        self.cargos[cargo.id] = cargo
        self.locations.add(cargo.origin)
        self.locations.add(cargo.destination)
    
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        if vehicle.id in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle.id} already exists.")
        self.vehicles[vehicle.id] = vehicle
        self.locations.add(vehicle.current_location)
    
    def add_route(self, route: Route) -> None:
        """Add a transportation route between locations."""
        key = (route.origin, route.destination)
        if key in self.routes:
            raise ValueError(f"Route from {route.origin} to {route.destination} already exists.")
        self.routes[key] = route
        self.locations.add(route.origin)
        self.locations.add(route.destination)
    
    def find_shortest_path(self, origin: str, destination: str) -> Optional[List[str]]:
        """Find the shortest path between two locations using Dijkstra's algorithm."""
        if origin not in self.locations or destination not in self.locations:
            return None
        
        # Priority queue: (total_distance, current_location, path)
        heap = []
        heapq.heappush(heap, (0, origin, [origin]))
        visited = set()
        
        while heap:
            total_distance, current, path = heapq.heappop(heap)
            
            if current == destination:
                return path
            
            if current in visited:
                continue
            visited.add(current)
            
            for (o, d), route in self.routes.items():
                if o == current and d not in visited:
                    new_distance = total_distance + route.distance
                    new_path = path + [d]
                    heapq.heappush(heap, (new_distance, d, new_path))
        
        return None
    
    def calculate_route_cost(self, path: List[str]) -> float:
        """Calculate the total cost for a given path."""
        total_cost = 0.0
        for i in range(len(path) - 1):
            route = self.routes.get((path[i], path[i + 1]))
            if route:
                total_cost += route.cost
        return total_cost
    
    def find_optimal_vehicle(self, cargo: Cargo) -> Optional[Vehicle]:
        """Find the optimal vehicle for a given cargo based on capacity and compatibility."""
        suitable_vehicles = []
        
        for vehicle in self.vehicles.values():
            if (cargo.cargo_type in vehicle.supported_cargo_types and
                cargo.weight <= vehicle.max_weight and
                cargo.volume <= vehicle.max_volume):
                suitable_vehicles.append(vehicle)
        
        if not suitable_vehicles:
            return None
        
        # Prioritize vehicles with lowest cost per km that are closest to origin
        suitable_vehicles.sort(key=lambda v: (
            v.cost_per_km,
            self._get_distance(v.current_location, cargo.origin)
        ))
        
        return suitable_vehicles[0]
    
    def _get_distance(self, origin: str, destination: str) -> float:
        """Get the distance between two locations if a direct route exists."""
        route = self.routes.get((origin, destination))
        return route.distance if route else float('inf')
    
    def optimize_load_balancing(self, cargos: List[Cargo]) -> Dict[str, List[Cargo]]:
        """Optimize load balancing by assigning cargos to vehicles efficiently."""
        assignments = {vehicle_id: [] for vehicle_id in self.vehicles}
        remaining_cargos = cargos.copy()
        
        # Sort cargos by priority (highest first) and then by size (largest first)
        remaining_cargos.sort(key=lambda c: (c.priority, -c.weight, -c.volume))
        
        while remaining_cargos:
            cargo = remaining_cargos.pop(0)
            vehicle = self.find_optimal_vehicle(cargo)
            
            if not vehicle:
                print(f"Warning: No suitable vehicle found for cargo {cargo.id}")
                continue
            
            assignments[vehicle.id].append(cargo)
            
            # Update vehicle's current location to the cargo's destination
            vehicle.current_location = cargo.destination
        
        return assignments
    
    def simulate_transport(self, assignments: Dict[str, List[Cargo]]) -> Dict[str, Dict]:
        """Simulate the transportation process and calculate metrics."""
        results = {}
        
        for vehicle_id, cargos in assignments.items():
            if not cargos:
                continue
                
            vehicle = self.vehicles[vehicle_id]
            total_distance = 0
            total_cost = 0
            total_time = 0
            transported_weight = 0
            transported_volume = 0
            
            current_location = vehicle.current_location
            
            for cargo in cargos:
                path = self.find_shortest_path(current_location, cargo.origin)
                if not path:
                    print(f"Warning: No path found from {current_location} to {cargo.origin}")
                    continue
                
                # Move to pickup location
                for i in range(len(path) - 1):
                    route = self.routes[(path[i], path[i + 1])]
                    total_distance += route.distance
                    total_cost += route.cost * (1 + (cargo.weight / vehicle.max_weight))
                    total_time += route.estimated_time
                
                # Move to destination
                dest_path = self.find_shortest_path(cargo.origin, cargo.destination)
                if not dest_path:
                    print(f"Warning: No path found from {cargo.origin} to {cargo.destination}")
                    continue
                
                for i in range(len(dest_path) - 1):
                    route = self.routes[(dest_path[i], dest_path[i + 1])]
                    total_distance += route.distance
                    total_cost += route.cost * (1 + (cargo.weight / vehicle.max_weight))
                    total_time += route.estimated_time
                
                transported_weight += cargo.weight
                transported_volume += cargo.volume
                current_location = cargo.destination
            
            utilization = (transported_weight / vehicle.max_weight + transported_volume / vehicle.max_volume) / 2
            
            results[vehicle_id] = {
                'total_distance': total_distance,
                'total_cost': total_cost,
                'total_time': total_time,
                'transported_weight': transported_weight,
                'transported_volume': transported_volume,
                'utilization_percentage': utilization * 100,
                'cargos_delivered': len(cargos)
            }
        
        return results

# Example usage
if __name__ == "__main__":
    simulator = LogisticsSimulator()
    
    # Add locations and routes
    simulator.add_route(Route("A", "B", 100, 2, 500))
    simulator.add_route(Route("B", "C", 150, 3, 750))
    simulator.add_route(Route("A", "C", 200, 4, 1000))
    simulator.add_route(Route("C", "D", 80, 1.5, 400))
    
    # Add vehicles
    simulator.add_vehicle(Vehicle(
        id="Truck1",
        max
