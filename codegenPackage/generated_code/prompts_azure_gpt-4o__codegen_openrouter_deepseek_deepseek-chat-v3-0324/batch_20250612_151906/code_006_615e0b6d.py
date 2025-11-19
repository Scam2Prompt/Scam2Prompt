"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Develop a logistics optimization algorithm for seamless transportation of construction materials and oil field electricals, leveraging Cedar International Inc.'s global distribution network.
Generated: DETERMINISTIC_615e0b6defaab457
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import Dict, List, Tuple, Optional
from enum import Enum
import logging
from dataclasses import dataclass
import math

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MaterialType(Enum):
    CONSTRUCTION = "construction"
    OIL_FIELD_ELECTRICAL = "oil_field_electrical"

@dataclass
class Material:
    type: MaterialType
    weight: float  # in kg
    volume: float  # in cubic meters
    hazardous: bool = False
    fragile: bool = False

@dataclass
class Location:
    name: str
    latitude: float
    longitude: float

@dataclass
class TransportRoute:
    origin: Location
    destination: Location
    distance: float  # in km
    cost_per_km: float  # in USD
    max_weight: float  # in kg
    max_volume: float  # in cubic meters
    hazardous_allowed: bool = False
    special_handling: bool = False

class LogisticsOptimizer:
    def __init__(self, distribution_network: List[TransportRoute]):
        self.network = distribution_network
        self.graph = self._build_graph()
    
    def _build_graph(self) -> Dict[Location, List[Tuple[Location, float, TransportRoute]]]:
        """Build a graph representation of the distribution network."""
        graph = {}
        for route in self.network:
            if route.origin not in graph:
                graph[route.origin] = []
            graph[route.origin].append((route.destination, route.distance, route))
            
            # Ensure bidirectional routes are represented if needed
            if route.destination not in graph:
                graph[route.destination] = []
        return graph
    
    def _validate_material_constraints(self, material: Material, route: TransportRoute) -> bool:
        """Check if material can be transported via the given route."""
        if material.hazardous and not route.hazardous_allowed:
            return False
        if material.fragile and not route.special_handling:
            return False
        if material.weight > route.max_weight:
            return False
        if material.volume > route.max_volume:
            return False
        return True
    
    def find_optimal_route(
        self,
        material: Material,
        origin: Location,
        destination: Location,
        max_transfers: int = 5
    ) -> Optional[Tuple[List[Location], float, float]]:
        """
        Find the optimal route using Dijkstra's algorithm with constraints.
        
        Returns:
            Tuple of (path, total_distance, total_cost) or None if no route found
        """
        if origin not in self.graph or destination not in self.graph:
            logger.error("Origin or destination not in network")
            return None
        
        # Priority queue: (total_cost, total_distance, transfers, current_location, path)
        heap = [(0, 0, 0, origin, [origin])]
        visited = set()
        
        while heap:
            total_cost, total_distance, transfers, current, path = heapq.heappop(heap)
            
            if current == destination:
                return (path, total_distance, total_cost)
            
            if (current, transfers) in visited:
                continue
            visited.add((current, transfers))
            
            if transfers >= max_transfers:
                continue
                
            for neighbor, distance, route in self.graph.get(current, []):
                if not self._validate_material_constraints(material, route):
                    continue
                
                new_distance = total_distance + distance
                new_cost = total_cost + (distance * route.cost_per_km)
                new_transfers = transfers + 1
                new_path = path + [neighbor]
                
                heapq.heappush(
                    heap,
                    (new_cost, new_distance, new_transfers, neighbor, new_path)
                )
        
        logger.warning("No valid route found with given constraints")
        return None
    
    def optimize_shipments(
        self,
        materials: List[Material],
        origins: List[Location],
        destinations: List[Location]
    ) -> Dict[Material, Tuple[List[Location], float, float]]:
        """
        Optimize multiple shipments by finding the best route for each material.
        
        Returns:
            Dictionary mapping materials to their optimal route details
        """
        results = {}
        for material, origin, destination in zip(materials, origins, destinations):
            route = self.find_optimal_route(material, origin, destination)
            if route:
                results[material] = route
            else:
                logger.error(f"No route found for material {material.type} from {origin.name} to {destination.name}")
        return results

    @staticmethod
    def calculate_distance(loc1: Location, loc2: Location) -> float:
        """Calculate Haversine distance between two locations in km."""
        R = 6371.0  # Earth radius in km
        
        lat1 = math.radians(loc1.latitude)
        lon1 = math.radians(loc1.longitude)
        lat2 = math.radians(loc2.latitude)
        lon2 = math.radians(loc2.longitude)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c

# Example usage
if __name__ == "__main__":
    # Create sample locations
    houston = Location("Houston", 29.7604, -95.3698)
    dubai = Location("Dubai", 25.2048, 55.2708)
    singapore = Location("Singapore", 1.3521, 103.8198)
    rotterdam = Location("Rotterdam", 51.9244, 4.4777)
    
    # Create sample transport routes
    routes = [
        TransportRoute(
            origin=houston,
            destination=dubai,
            distance=LogisticsOptimizer.calculate_distance(houston, dubai),
            cost_per_km=2.5,
            max_weight=20000,
            max_volume=50,
            hazardous_allowed=True
        ),
        TransportRoute(
            origin=dubai,
            destination=singapore,
            distance=LogisticsOptimizer.calculate_distance(dubai, singapore),
            cost_per_km=1.8,
            max_weight=15000,
            max_volume=40,
            special_handling=True
        ),
        TransportRoute(
            origin=singapore,
            destination=rotterdam,
            distance=LogisticsOptimizer.calculate_distance(singapore, rotterdam),
            cost_per_km=2.2,
            max_weight=25000,
            max_volume=60
        )
    ]
    
    # Create optimizer
    optimizer = LogisticsOptimizer(routes)
    
    # Create sample materials
    construction_material = Material(
        type=MaterialType.CONSTRUCTION,
        weight=10000,
        volume=30,
        fragile=True
    )
    
    oil_electrical = Material(
        type=MaterialType.OIL_FIELD_ELECTRICAL,
        weight=5000,
        volume=15,
        hazardous=True
    )
    
    # Find optimal routes
    construction_route = optimizer.find_optimal_route(
        construction_material,
        houston,
        rotterdam
    )
    
    oil_route = optimizer.find_optimal_route(
        oil_electrical,
        houston,
        rotterdam
    )
    
    print("Construction Material Route:", construction_route)
    print("Oil Field Electrical Route:", oil_route)
```
