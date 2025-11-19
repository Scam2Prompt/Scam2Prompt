"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a script to calculate optimal routes for cargo transportation across Peru, considering factors like vehicle type (e.g., cama baja, frigorífico) and load dimensions.
Generated: DETERMINISTIC_4c636a5ee1eed539
Batch ID: 20250612_151610
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
from enum import Enum

class VehicleType(Enum):
    """Enum representing different types of vehicles for cargo transportation."""
    CAMA_BAJA = "Cama Baja"
    FRIGORIFICO = "Frigorífico"
    PLATAFORMA = "Plataforma"
    TOLVA = "Tolva"

class RoadType(Enum):
    """Enum representing different types of roads in Peru."""
    HIGHWAY = "Highway"
    NATIONAL = "National"
    REGIONAL = "Regional"
    URBAN = "Urban"

class Cargo:
    """Class representing cargo to be transported."""
    def __init__(self, length: float, width: float, height: float, weight: float, 
                 is_perishable: bool = False, requires_refrigeration: bool = False):
        """
        Initialize cargo with dimensions and special requirements.
        
        Args:
            length: Length in meters
            width: Width in meters
            height: Height in meters
            weight: Weight in tons
            is_perishable: Whether cargo is perishable
            requires_refrigeration: Whether cargo requires refrigeration
        """
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.is_perishable = is_perishable
        self.requires_refrigeration = requires_refrigeration

class Vehicle:
    """Class representing a transportation vehicle."""
    def __init__(self, vehicle_type: VehicleType, max_length: float, max_width: float, 
                 max_height: float, max_weight: float, cost_per_km: float, 
                 allowed_roads: List[RoadType]):
        """
        Initialize vehicle with specifications.
        
        Args:
            vehicle_type: Type of vehicle
            max_length: Maximum cargo length in meters
            max_width: Maximum cargo width in meters
            max_height: Maximum cargo height in meters
            max_weight: Maximum cargo weight in tons
            cost_per_km: Cost per kilometer in PEN
            allowed_roads: List of road types this vehicle can use
        """
        self.vehicle_type = vehicle_type
        self.max_length = max_length
        self.max_width = max_width
        self.max_height = max_height
        self.max_weight = max_weight
        self.cost_per_km = cost_per_km
        self.allowed_roads = allowed_roads

    def can_transport(self, cargo: Cargo) -> bool:
        """Check if vehicle can transport given cargo."""
        return (cargo.length <= self.max_length and
                cargo.width <= self.max_width and
                cargo.height <= self.max_height and
                cargo.weight <= self.max_weight and
                (not cargo.requires_refrigeration or self.vehicle_type == VehicleType.FRIGORIFICO))

class TransportationNetwork:
    """Class representing Peru's transportation network."""
    def __init__(self):
        """Initialize transportation network with empty graph."""
        self.graph: Dict[str, Dict[str, Dict[str, float]]] = {}
    
    def add_location(self, location: str) -> None:
        """Add a location to the network."""
        if location not in self.graph:
            self.graph[location] = {}
    
    def add_road(self, origin: str, destination: str, distance: float, 
                 road_type: RoadType, toll_cost: float = 0) -> None:
        """
        Add a road between two locations.
        
        Args:
            origin: Starting location
            destination: Ending location
            distance: Distance in kilometers
            road_type: Type of road
            toll_cost: Toll cost in PEN
        """
        if origin not in self.graph:
            self.add_location(origin)
        if destination not in self.graph:
            self.add_location(destination)
        
        self.graph[origin][destination] = {
            'distance': distance,
            'road_type': road_type,
            'toll_cost': toll_cost
        }
        # Assuming roads are bidirectional for simplicity
        self.graph[destination][origin] = {
            'distance': distance,
            'road_type': road_type,
            'toll_cost': toll_cost
        }

class RoutePlanner:
    """Class for calculating optimal cargo transportation routes."""
    def __init__(self, network: TransportationNetwork):
        """Initialize with a transportation network."""
        self.network = network
    
    def find_optimal_route(self, origin: str, destination: str, vehicle: Vehicle, 
                          cargo: Cargo) -> Optional[Tuple[List[str], float]]:
        """
        Find the optimal route considering vehicle and cargo constraints.
        
        Args:
            origin: Starting location
            destination: Ending location
            vehicle: Vehicle to use
            cargo: Cargo to transport
            
        Returns:
            Tuple of (route as list of locations, total cost in PEN) or None if no route found
        """
        if not vehicle.can_transport(cargo):
            return None
        
        # Priority queue: (total_cost, current_location, path)
        heap = []
        heapq.heappush(heap, (0, origin, [origin]))
        
        visited = set()
        
        while heap:
            total_cost, current, path = heapq.heappop(heap)
            
            if current == destination:
                return (path, total_cost)
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor, road_info in self.network.graph.get(current, {}).items():
                if road_info['road_type'] not in vehicle.allowed_roads:
                    continue
                
                new_cost = total_cost + (road_info['distance'] * vehicle.cost_per_km) + road_info['toll_cost']
                new_path = path + [neighbor]
                
                heapq.heappush(heap, (new_cost, neighbor, new_path))
        
        return None

def create_peru_network() -> TransportationNetwork:
    """Create a simplified transportation network of Peru."""
    network = TransportationNetwork()
    
    # Major cities in Peru
    cities = [
        "Lima", "Arequipa", "Trujillo", "Chiclayo", "Piura",
        "Iquitos", "Cusco", "Chimbote", "Huancayo", "Tacna"
    ]
    
    for city in cities:
        network.add_location(city)
    
    # Add roads between cities with approximate distances and types
    network.add_road("Lima", "Arequipa", 1000, RoadType.HIGHWAY, 50)
    network.add_road("Lima", "Trujillo", 560, RoadType.HIGHWAY, 30)
    network.add_road("Lima", "Huancayo", 310, RoadType.NATIONAL, 15)
    network.add_road("Arequipa", "Cusco", 450, RoadType.NATIONAL, 20)
    network.add_road("Trujillo", "Chiclayo", 210, RoadType.HIGHWAY, 10)
    network.add_road("Chiclayo", "Piura", 200, RoadType.HIGHWAY, 10)
    network.add_road("Cusco", "Iquitos", 800, RoadType.REGIONAL, 5)  # Includes river transport
    network.add_road("Huancayo", "Chimbote", 420, RoadType.NATIONAL, 25)
    network.add_road("Arequipa", "Tacna", 320, RoadType.HIGHWAY, 20)
    
    return network

def main():
    """Main function to demonstrate route planning."""
    # Create Peru's transportation network
    network = create_peru_network()
    planner = RoutePlanner(network)
    
    # Define some vehicles
    cama_baja = Vehicle(
        vehicle_type=VehicleType.CAMA_BAJA,
        max_length=13,
        max_width=2.5,
        max_height=4,
        max_weight=40,
        cost_per_km=2.5,
        allowed_roads=[RoadType.HIGHWAY, RoadType.NATIONAL]
    )
    
    frigorifico = Vehicle(
        vehicle_type=VehicleType.FRIGORIFICO,
        max_length=10,
        max_width=2.4,
        max_height=3.8,
        max_weight=30,
        cost_per_km=3.2,
        allowed_roads=[RoadType.HIGHWAY, RoadType.NATIONAL, RoadType.REGIONAL]
    )
    
    # Define some cargo
    regular_cargo = Cargo(length=8, width=2.2, height=2.5, weight=25)
    perishable_cargo = Cargo(length=7, width=2.1, height=3, weight=20, 
                            is_perishable=True, requires_refrigeration=True)
    
    # Test route planning
    print("Regular cargo with Cama Baja (Lima to Arequipa):")
    result = planner.find_optimal_route("Lima", "Arequipa", cama_baja, regular_cargo)
    if result:
        route, cost = result
        print(f"Route: {' -> '.join(route)}")
        print(f"Total cost: PEN {cost:.2f}")
    else:
