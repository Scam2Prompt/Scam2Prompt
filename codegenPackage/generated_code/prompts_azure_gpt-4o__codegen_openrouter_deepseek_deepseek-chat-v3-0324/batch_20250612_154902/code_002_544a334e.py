"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Generate code to simulate multimodal transportation combining air freight and ocean freight, optimizing cost savings as described by Uniair Cargo.
Generated: DETERMINISTIC_544a334e1c7aae27
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Tuple

class TransportMode(Enum):
    """Enum representing different transportation modes."""
    AIR = auto()
    OCEAN = auto()

@dataclass
class TransportLeg:
    """Represents a single leg of the transportation journey."""
    mode: TransportMode
    cost: float
    duration_days: float
    origin: str
    destination: str

@dataclass
class Shipment:
    """Represents a shipment with its details."""
    weight_kg: float
    volume_cbm: float
    origin: str
    destination: str
    max_transit_days: Optional[float] = None
    max_cost: Optional[float] = None

class TransportationOptimizer:
    """Optimizes multimodal transportation combining air and ocean freight."""
    
    def __init__(self, air_cost_per_kg: float, ocean_cost_per_kg: float, 
                 air_cost_per_cbm: float, ocean_cost_per_cbm: float,
                 air_speed_days_per_1000km: float, ocean_speed_days_per_1000km: float):
        """
        Initialize the optimizer with cost and speed parameters.
        
        Args:
            air_cost_per_kg: Cost per kg for air freight
            ocean_cost_per_kg: Cost per kg for ocean freight
            air_cost_per_cbm: Cost per cubic meter for air freight
            ocean_cost_per_cbm: Cost per cubic meter for ocean freight
            air_speed_days_per_1000km: Days per 1000km for air transport
            ocean_speed_days_per_1000km: Days per 1000km for ocean transport
        """
        self.air_cost_per_kg = air_cost_per_kg
        self.ocean_cost_per_kg = ocean_cost_per_kg
        self.air_cost_per_cbm = air_cost_per_cbm
        self.ocean_cost_per_cbm = ocean_cost_per_cbm
        self.air_speed = air_speed_days_per_1000km
        self.ocean_speed = ocean_speed_days_per_1000km
    
    def calculate_distance(self, origin: str, destination: str) -> float:
        """
        Calculate approximate distance between two locations (simplified).
        In a real implementation, this would use a proper geolocation API.
        
        Args:
            origin: Origin location code
            destination: Destination location code
            
        Returns:
            Distance in kilometers
        """
        # Simplified distance calculation (would use proper API in production)
        return 5000.0  # Example fixed distance for demo purposes
    
    def calculate_leg_cost(self, mode: TransportMode, shipment: Shipment) -> float:
        """Calculate cost for a transportation leg."""
        distance = self.calculate_distance(shipment.origin, shipment.destination)
        
        if mode == TransportMode.AIR:
            weight_cost = shipment.weight_kg * self.air_cost_per_kg
            volume_cost = shipment.volume_cbm * self.air_cost_per_cbm
        else:
            weight_cost = shipment.weight_kg * self.ocean_cost_per_kg
            volume_cost = shipment.volume_cbm * self.ocean_cost_per_cbm
            
        return max(weight_cost, volume_cost) * (distance / 1000)
    
    def calculate_leg_duration(self, mode: TransportMode, shipment: Shipment) -> float:
        """Calculate duration for a transportation leg in days."""
        distance = self.calculate_distance(shipment.origin, shipment.destination)
        
        if mode == TransportMode.AIR:
            return distance * self.air_speed / 1000
        else:
            return distance * self.ocean_speed / 1000
    
    def generate_possible_routes(self, shipment: Shipment) -> List[List[TransportLeg]]:
        """Generate all possible transportation routes for the shipment."""
        routes = []
        
        # Pure air route
        air_cost = self.calculate_leg_cost(TransportMode.AIR, shipment)
        air_duration = self.calculate_leg_duration(TransportMode.AIR, shipment)
        pure_air = [
            TransportLeg(
                mode=TransportMode.AIR,
                cost=air_cost,
                duration_days=air_duration,
                origin=shipment.origin,
                destination=shipment.destination
            )
        ]
        routes.append(pure_air)
        
        # Pure ocean route
        ocean_cost = self.calculate_leg_cost(TransportMode.OCEAN, shipment)
        ocean_duration = self.calculate_leg_duration(TransportMode.OCEAN, shipment)
        pure_ocean = [
            TransportLeg(
                mode=TransportMode.OCEAN,
                cost=ocean_cost,
                duration_days=ocean_duration,
                origin=shipment.origin,
                destination=shipment.destination
            )
        ]
        routes.append(pure_ocean)
        
        # Multimodal routes (example: air to major hub, then ocean)
        # In production, this would use actual hub locations
        multimodal_1 = [
            TransportLeg(
                mode=TransportMode.AIR,
                cost=self.calculate_leg_cost(TransportMode.AIR, 
                    Shipment(shipment.weight_kg, shipment.volume_cbm, 
                             shipment.origin, "HUB")),
                duration_days=self.calculate_leg_duration(TransportMode.AIR, 
                    Shipment(shipment.weight_kg, shipment.volume_cbm, 
                             shipment.origin, "HUB")),
                origin=shipment.origin,
                destination="HUB"
            ),
            TransportLeg(
                mode=TransportMode.OCEAN,
                cost=self.calculate_leg_cost(TransportMode.OCEAN, 
                    Shipment(shipment.weight_kg, shipment.volume_cbm, 
                             "HUB", shipment.destination)),
                duration_days=self.calculate_leg_duration(TransportMode.OCEAN, 
                    Shipment(shipment.weight_kg, shipment.volume_cbm, 
                             "HUB", shipment.destination)),
                origin="HUB",
                destination=shipment.destination
            )
        ]
        routes.append(multimodal_1)
        
        return routes
    
    def optimize_route(self, shipment: Shipment) -> Tuple[List[TransportLeg], float, float]:
        """
        Find the optimal transportation route considering cost and time constraints.
        
        Args:
            shipment: The shipment details
            
        Returns:
            Tuple of (best_route, total_cost, total_duration)
        """
        possible_routes = self.generate_possible_routes(shipment)
        best_route = None
        min_cost = float('inf')
        best_duration = 0
        
        for route in possible_routes:
            total_cost = sum(leg.cost for leg in route)
            total_duration = sum(leg.duration_days for leg in route)
            
            # Check constraints
            if shipment.max_transit_days is not None and total_duration > shipment.max_transit_days:
                continue
            if shipment.max_cost is not None and total_cost > shipment.max_cost:
                continue
                
            if total_cost < min_cost:
                min_cost = total_cost
                best_route = route
                best_duration = total_duration
                
        if best_route is None:
            raise ValueError("No feasible route found within given constraints")
            
        return best_route, min_cost, best_duration

# Example usage
if __name__ == "__main__":
    # Initialize with example rates (would come from configuration in production)
    optimizer = TransportationOptimizer(
        air_cost_per_kg=5.0,
        ocean_cost_per_kg=1.0,
        air_cost_per_cbm=5000.0,
        ocean_cost_per_cbm=1000.0,
        air_speed_days_per_1000km=0.5,
        ocean_speed_days_per_1000km=2.0
    )
    
    # Example shipment
    shipment = Shipment(
        weight_kg=1000,
        volume_cbm=5,
        origin="JFK",
        destination="HKG",
        max_transit_days=10,
        max_cost=15000
    )
    
    try:
        best_route, total_cost, total_duration = optimizer.optimize_route(shipment)
        print(f"Optimal route found with cost ${total_cost:.2f} and duration {total_duration:.1f} days")
        for i, leg in enumerate(best_route, 1):
            print(f"Leg {i}: {leg.mode.name} from {leg.origin} to {leg.destination} "
                  f"(Cost: ${leg.cost:.2f}, Duration: {leg.duration_days:.1f} days)")
    except ValueError as e:
        print(f"Error: {e}")
```
