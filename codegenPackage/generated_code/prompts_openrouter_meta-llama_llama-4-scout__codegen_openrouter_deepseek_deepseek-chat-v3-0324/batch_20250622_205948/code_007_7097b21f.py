"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Write a script to calculate costs and optimize logistics for dry load services, taking into account factors like distance, weight, and delivery time for a company like Calmar Transport."
Generated: DETERMINISTIC_7097b21fd39c6687
Batch ID: 20250622_205948
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
from typing import List, Optional
from enum import Enum, auto
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VehicleType(Enum):
    """Enum representing different types of vehicles available for transport."""
    VAN = auto()
    SPRINTER = auto()
    STRAIGHT_TRUCK = auto()
    LARGE_STRAIGHT = auto()
    MEGA_TRUCK = auto()

@dataclass
class Vehicle:
    """Class representing a transport vehicle."""
    type: VehicleType
    max_weight: float  # in kg
    base_cost_per_km: float
    speed: float  # km/h
    availability: bool = True

@dataclass
class Location:
    """Class representing a geographical location."""
    city: str
    state: str
    latitude: float
    longitude: float

@dataclass
class Shipment:
    """Class representing a shipment to be transported."""
    origin: Location
    destination: Location
    weight: float  # in kg
    delivery_deadline: datetime
    special_requirements: Optional[List[str]] = None

@dataclass
class Route:
    """Class representing a transport route."""
    origin: Location
    destination: Location
    distance: float  # in km
    estimated_time: timedelta  # in hours

@dataclass
class TransportCost:
    """Class representing transport cost details."""
    base_cost: float
    fuel_surcharge: float
    time_surcharge: float
    total_cost: float

class LogisticsOptimizer:
    """Class to optimize logistics and calculate costs for dry load services."""
    
    def __init__(self):
        self.vehicles = self._initialize_vehicles()
        self.fuel_cost_per_liter = 1.20  # current fuel cost
        self.fuel_consumption_rate = 0.35  # liters per km
    
    def _initialize_vehicles(self) -> List[Vehicle]:
        """Initialize available vehicles with their specifications."""
        return [
            Vehicle(VehicleType.VAN, 1500, 0.50, 80),
            Vehicle(VehicleType.SPRINTER, 2500, 0.60, 85),
            Vehicle(VehicleType.STRAIGHT_TRUCK, 10000, 0.80, 75),
            Vehicle(VehicleType.LARGE_STRAIGHT, 15000, 1.00, 70),
            Vehicle(VehicleType.MEGA_TRUCK, 20000, 1.20, 65)
        ]
    
    def calculate_distance(self, origin: Location, destination: Location) -> float:
        """
        Calculate distance between two locations using Haversine formula.
        
        Args:
            origin: Starting location
            destination: Ending location
            
        Returns:
            Distance in kilometers
        """
        lat1, lon1 = math.radians(origin.latitude), math.radians(origin.longitude)
        lat2, lon2 = math.radians(destination.latitude), math.radians(destination.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return 6371 * c  # Earth radius in km
    
    def calculate_route(self, origin: Location, destination: Location) -> Route:
        """
        Calculate route details between two locations.
        
        Args:
            origin: Starting location
            destination: Ending location
            
        Returns:
            Route object containing distance and estimated time
        """
        distance = self.calculate_distance(origin, destination)
        vehicle = self.select_optimal_vehicle(distance, 0)  # Default weight for route calculation
        estimated_time = timedelta(hours=distance / vehicle.speed)
        
        return Route(origin, destination, distance, estimated_time)
    
    def select_optimal_vehicle(self, distance: float, weight: float) -> Vehicle:
        """
        Select the optimal vehicle for a shipment based on weight and distance.
        
        Args:
            distance: Distance in km
            weight: Weight in kg
            
        Returns:
            Optimal vehicle for the shipment
            
        Raises:
            ValueError: If no suitable vehicle is found
        """
        suitable_vehicles = [v for v in self.vehicles 
                           if v.max_weight >= weight and v.availability]
        
        if not suitable_vehicles:
            logger.error("No suitable vehicles available for weight: %s kg", weight)
            raise ValueError("No suitable vehicles available")
        
        # Select vehicle with lowest cost that can handle the weight
        optimal_vehicle = min(suitable_vehicles, 
                             key=lambda v: v.base_cost_per_km * distance)
        
        return optimal_vehicle
    
    def calculate_transport_cost(self, shipment: Shipment) -> TransportCost:
        """
        Calculate total transport cost for a shipment.
        
        Args:
            shipment: Shipment details
            
        Returns:
            TransportCost object with cost breakdown
            
        Raises:
            ValueError: If no suitable vehicle is found
        """
        try:
            route = self.calculate_route(shipment.origin, shipment.destination)
            vehicle = self.select_optimal_vehicle(route.distance, shipment.weight)
            
            base_cost = route.distance * vehicle.base_cost_per_km
            fuel_surcharge = route.distance * self.fuel_consumption_rate * self.fuel_cost_per_liter
            
            # Time surcharge if delivery is urgent
            current_time = datetime.now()
            time_available = (shipment.delivery_deadline - current_time).total_seconds() / 3600
            time_needed = route.estimated_time.total_seconds() / 3600
            
            time_surcharge = 0
            if time_needed > time_available * 0.9:  # If we need more than 90% of available time
                time_surcharge = base_cost * 0.2  # 20% surcharge
            
            total_cost = base_cost + fuel_surcharge + time_surcharge
            
            return TransportCost(
                base_cost=base_cost,
                fuel_surcharge=fuel_surcharge,
                time_surcharge=time_surcharge,
                total_cost=total_cost
            )
        except Exception as e:
            logger.error("Error calculating transport cost: %s", str(e))
            raise
    
    def optimize_schedule(self, shipments: List[Shipment]) -> List[Shipment]:
        """
        Optimize shipment schedule based on delivery deadlines and routes.
        
        Args:
            shipments: List of shipments to optimize
            
        Returns:
            List of optimized shipments in schedule order
        """
        # Sort shipments by deadline (earliest first)
        shipments.sort(key=lambda s: s.delivery_deadline)
        
        # Simple optimization: group shipments going to nearby locations
        optimized_shipments = []
        processed_shipments = set()
        
        for i, shipment in enumerate(shipments):
            if i in processed_shipments:
                continue
                
            # Find shipments with similar destination
            similar_shipments = [shipment]
            for j, other_shipment in enumerate(shipments[i+1:], start=i+1):
                if j in processed_shipments:
                    continue
                    
                route = self.calculate_route(shipment.destination, other_shipment.destination)
                if route.distance < 50:  # Within 50 km considered similar
                    similar_shipments.append(other_shipment)
                    processed_shipments.add(j)
            
            optimized_shipments.extend(similar_shipments)
        
        return optimized_shipments

# Example usage
if __name__ == "__main__":
    optimizer = LogisticsOptimizer()
    
    # Create sample locations
    toronto = Location("Toronto", "ON", 43.6532, -79.3832)
    montreal = Location("Montreal", "QC", 45.5017, -73.5673)
    ottawa = Location("Ottawa", "ON", 45.4215, -75.6972)
    
    # Create sample shipments
    shipments = [
        Shipment(
            origin=toronto,
            destination=montreal,
            weight=5000,
            delivery_deadline=datetime.now() + timedelta(days=2)
        ),
        Shipment(
            origin=toronto,
            destination=ottawa,
            weight=3000,
            delivery_deadline=datetime.now() + timedelta(days=1)
        ),
        Shipment(
            origin=montreal,
            destination=ottawa,
            weight=2000,
            delivery_deadline=datetime.now() + timedelta(days=3)
        )
    ]
    
    # Calculate costs and optimize
    try:
        for shipment in shipments:
            cost = optimizer.c
