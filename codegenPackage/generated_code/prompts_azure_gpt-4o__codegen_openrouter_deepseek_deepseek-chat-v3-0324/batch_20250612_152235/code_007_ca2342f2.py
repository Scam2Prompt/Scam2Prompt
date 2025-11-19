"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a program to calculate freight costs dynamically, incorporating Bin Qutab Logistics' ability to match freight with the right vehicle and route while offering flexibility.
Generated: DETERMINISTIC_ca2342f25bfa4bfe
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
import math

class VehicleType(Enum):
    """Enum representing different types of vehicles available for freight."""
    TRUCK_SMALL = "Small Truck"
    TRUCK_MEDIUM = "Medium Truck"
    TRUCK_LARGE = "Large Truck"
    VAN = "Van"
    TRAILER = "Trailer"

class RouteType(Enum):
    """Enum representing different types of routes."""
    HIGHWAY = "Highway"
    URBAN = "Urban"
    RURAL = "Rural"
    MOUNTAIN = "Mountain"

class Freight:
    """Class representing a freight item."""
    def __init__(self, weight: float, volume: float, fragility: float, 
                 perishable: bool, hazardous: bool):
        """
        Initialize a freight item.
        
        Args:
            weight: Weight of the freight in kg.
            volume: Volume of the freight in cubic meters.
            fragility: Fragility level (0-1, where 1 is most fragile).
            perishable: Whether the freight is perishable.
            hazardous: Whether the freight is hazardous.
        """
        self.weight = weight
        self.volume = volume
        self.fragility = fragility
        self.perishable = perishable
        self.hazardous = hazardous

class Vehicle:
    """Class representing a vehicle for freight transport."""
    def __init__(self, vehicle_type: VehicleType, max_weight: float, 
                 max_volume: float, base_cost_per_km: float, 
                 suitable_route_types: List[RouteType], 
                 can_transport_hazardous: bool, 
                 can_transport_perishable: bool):
        """
        Initialize a vehicle.
        
        Args:
            vehicle_type: Type of the vehicle.
            max_weight: Maximum weight capacity in kg.
            max_volume: Maximum volume capacity in cubic meters.
            base_cost_per_km: Base cost per kilometer in USD.
            suitable_route_types: List of route types suitable for this vehicle.
            can_transport_hazardous: Whether it can transport hazardous freight.
            can_transport_perishable: Whether it can transport perishable freight.
        """
        self.vehicle_type = vehicle_type
        self.max_weight = max_weight
        self.max_volume = max_volume
        self.base_cost_per_km = base_cost_per_km
        self.suitable_route_types = suitable_route_types
        self.can_transport_hazardous = can_transport_hazardous
        self.can_transport_perishable = can_transport_perishable

class Route:
    """Class representing a transport route."""
    def __init__(self, route_type: RouteType, distance: float, 
                 traffic_factor: float = 1.0, terrain_factor: float = 1.0):
        """
        Initialize a route.
        
        Args:
            route_type: Type of the route.
            distance: Distance in kilometers.
            traffic_factor: Traffic multiplier (default 1.0).
            terrain_factor: Terrain difficulty multiplier (default 1.0).
        """
        self.route_type = route_type
        self.distance = distance
        self.traffic_factor = traffic_factor
        self.terrain_factor = terrain_factor

class FreightCalculator:
    """Main class for calculating freight costs."""
    def __init__(self):
        """Initialize the freight calculator with default vehicles."""
        self.vehicles = self._initialize_vehicles()
    
    def _initialize_vehicles(self) -> List[Vehicle]:
        """Initialize and return a list of available vehicles."""
        return [
            Vehicle(
                VehicleType.TRUCK_SMALL,
                max_weight=5000,
                max_volume=20,
                base_cost_per_km=1.5,
                suitable_route_types=[RouteType.HIGHWAY, RouteType.URBAN, RouteType.RURAL],
                can_transport_hazardous=False,
                can_transport_perishable=True
            ),
            Vehicle(
                VehicleType.TRUCK_MEDIUM,
                max_weight=10000,
                max_volume=40,
                base_cost_per_km=2.0,
                suitable_route_types=[RouteType.HIGHWAY, RouteType.URBAN, RouteType.RURAL],
                can_transport_hazardous=True,
                can_transport_perishable=True
            ),
            Vehicle(
                VehicleType.TRUCK_LARGE,
                max_weight=20000,
                max_volume=80,
                base_cost_per_km=3.0,
                suitable_route_types=[RouteType.HIGHWAY, RouteType.RURAL],
                can_transport_hazardous=True,
                can_transport_perishable=False
            ),
            Vehicle(
                VehicleType.VAN,
                max_weight=2000,
                max_volume=10,
                base_cost_per_km=1.0,
                suitable_route_types=[RouteType.URBAN, RouteType.RURAL],
                can_transport_hazardous=False,
                can_transport_perishable=True
            ),
            Vehicle(
                VehicleType.TRAILER,
                max_weight=30000,
                max_volume=120,
                base_cost_per_km=4.0,
                suitable_route_types=[RouteType.HIGHWAY, RouteType.RURAL],
                can_transport_hazardous=True,
                can_transport_perishable=False
            )
        ]
    
    def _is_vehicle_suitable(self, vehicle: Vehicle, freight: Freight, route: Route) -> bool:
        """
        Check if a vehicle is suitable for given freight and route.
        
        Args:
            vehicle: Vehicle to check.
            freight: Freight to transport.
            route: Route to take.
            
        Returns:
            bool: True if vehicle is suitable, False otherwise.
        """
        # Check weight and volume capacity
        if freight.weight > vehicle.max_weight or freight.volume > vehicle.max_volume:
            return False
        
        # Check hazardous and perishable compatibility
        if freight.hazardous and not vehicle.can_transport_hazardous:
            return False
        if freight.perishable and not vehicle.can_transport_perishable:
            return False
        
        # Check route compatibility
        if route.route_type not in vehicle.suitable_route_types:
            return False
        
        return True
    
    def _calculate_vehicle_cost(self, vehicle: Vehicle, freight: Freight, route: Route) -> float:
        """
        Calculate the cost for a specific vehicle to transport freight on a route.
        
        Args:
            vehicle: Vehicle to use.
            freight: Freight to transport.
            route: Route to take.
            
        Returns:
            float: Total cost for this vehicle.
        """
        base_cost = vehicle.base_cost_per_km * route.distance
        
        # Apply traffic factor
        cost = base_cost * route.traffic_factor
        
        # Apply terrain factor
        cost *= route.terrain_factor
        
        # Apply fragility multiplier (more fragile = more careful handling)
        cost *= (1 + freight.fragility * 0.5)
        
        return cost
    
    def calculate_freight_cost(self, freight: Freight, route: Route) -> Dict[str, float]:
        """
        Calculate freight costs for all suitable vehicles.
        
        Args:
            freight: Freight to transport.
            route: Route to take.
            
        Returns:
            Dict[str, float]: Dictionary mapping vehicle types to their costs.
        """
        costs = {}
        
        for vehicle in self.vehicles:
            if self._is_vehicle_suitable(vehicle, freight, route):
                cost = self._calculate_vehicle_cost(vehicle, freight, route)
                costs[vehicle.vehicle_type.value] = round(cost, 2)
        
        return costs
    
    def get_optimal_vehicle(self, freight: Freight, route: Route) -> Tuple[Optional[str], Optional[float]]:
        """
        Get the optimal vehicle and cost for given freight and route.
        
        Args:
            freight: Freight to transport.
            route: Route to take.
            
        Returns:
            Tuple[Optional[str], Optional[float]]: (vehicle_type, cost) or (None, None) if no suitable vehicle.
        """
        costs = self.calculate_freight_cost(freight, route)
        
        if not costs:
            return None, None
        
        optimal_vehicle = min(costs.items(), key=lambda x: x[1])
        return optimal_vehicle

# Example usage
if __name__ == "__main__":
    calculator = FreightCalculator()
    
    # Create a sample freight
    freight = Freight(
        weight=8000,  # 8 tons
        volume=30,    # 30 cubic meters
        fragility=0.3,  # Moderately fragile
        perishable=True,
        hazardous=False
    )
    
    # Create a sample route
    route = Route(
        route_type=RouteType.HIGHWAY,
        distance=300,  # 300 km
        traffic_factor=1.2,  # 20% more due to traffic
        terrain_factor=1.0   # Normal terrain
    )
    
    # Calculate all possible options
    all_costs = calculator.calculate_freight_cost(freight, route)
    print("All available options:")
    for vehicle, cost in all
