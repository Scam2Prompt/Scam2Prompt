"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Create a program to simulate multi-modal transport logistics, including air and sea freight, inspired by Bin Qutab Logistics' proven experience in handling large-scale projects.
Generated: DETERMINISTIC_960384e447f999ae
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class TransportMode(ABC):
    """Abstract base class for different transport modes."""
    
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        """Calculate the cost for transportation."""
        pass
    
    @abstractmethod
    def estimate_delivery_time(self, distance: float) -> timedelta:
        """Estimate the delivery time."""
        pass
    
    @abstractmethod
    def get_capacity(self) -> float:
        """Get the maximum capacity of the transport mode."""
        pass


class AirFreight(TransportMode):
    """Air freight transport mode implementation."""
    
    def __init__(self):
        self.base_cost_per_km = 2.5  # USD per km
        self.speed = 800  # km/h
        self.capacity = 100000  # kg
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        if weight > self.capacity:
            raise ValueError(f"Weight exceeds air freight capacity of {self.capacity} kg")
        return distance * self.base_cost_per_km * (weight / 1000)
    
    def estimate_delivery_time(self, distance: float) -> timedelta:
        flight_time = distance / self.speed
        # Add 4 hours for loading/unloading and customs
        total_hours = flight_time + 4
        return timedelta(hours=total_hours)
    
    def get_capacity(self) -> float:
        return self.capacity


class SeaFreight(TransportMode):
    """Sea freight transport mode implementation."""
    
    def __init__(self):
        self.base_cost_per_km = 0.5  # USD per km
        self.speed = 30  # km/h (average speed for cargo ships)
        self.capacity = 5000000  # kg
    
    def calculate_cost(self, distance: float, weight: float) -> float:
        if weight > self.capacity:
            raise ValueError(f"Weight exceeds sea freight capacity of {self.capacity} kg")
        return distance * self.base_cost_per_km * (weight / 1000)
    
    def estimate_delivery_time(self, distance: float) -> timedelta:
        sailing_time = distance / self.speed
        # Add 48 hours for port operations
        total_hours = sailing_time + 48
        return timedelta(hours=total_hours)
    
    def get_capacity(self) -> float:
        return self.capacity


class Shipment:
    """Class representing a shipment with its details."""
    
    def __init__(self, shipment_id: str, origin: str, destination: str, 
                 weight: float, priority: str = "standard"):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.priority = priority
        self.status = "created"
        self.transport_mode = None
        self.cost = 0.0
        self.estimated_delivery = None
    
    def assign_transport(self, transport: TransportMode, distance: float):
        """Assign a transport mode to the shipment."""
        self.transport_mode = transport.__class__.__name__
        self.cost = transport.calculate_cost(distance, self.weight)
        self.estimated_delivery = datetime.now() + transport.estimate_delivery_time(distance)
        self.status = "assigned"
    
    def update_status(self, new_status: str):
        """Update the shipment status."""
        valid_statuses = ["created", "assigned", "in_transit", "delivered", "cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status
    
    def __str__(self):
        return (f"Shipment {self.shipment_id}: {self.origin} -> {self.destination}, "
                f"Weight: {self.weight}kg, Status: {self.status}")


class LogisticsSimulator:
    """Main class to simulate multi-modal logistics operations."""
    
    def __init__(self):
        self.transport_modes = {
            "air": AirFreight(),
            "sea": SeaFreight()
        }
        self.shipments: Dict[str, Shipment] = {}
        self.distance_cache: Dict[Tuple[str, str], float] = {}
    
    def create_shipment(self, origin: str, destination: str, 
                       weight: float, priority: str = "standard") -> str:
        """Create a new shipment and return its ID."""
        shipment_id = f"SH{random.randint(10000, 99999)}"
        shipment = Shipment(shipment_id, origin, destination, weight, priority)
        self.shipments[shipment_id] = shipment
        return shipment_id
    
    def calculate_distance(self, origin: str, destination: str) -> float:
        """Calculate distance between two locations (simulated)."""
        if (origin, destination) in self.distance_cache:
            return self.distance_cache[(origin, destination)]
        
        # Simulate distance calculation (in real app, use geolocation API)
        distance = random.uniform(500, 15000)
        self.distance_cache[(origin, destination)] = distance
        self.distance_cache[(destination, origin)] = distance
        return distance
    
    def assign_transport_mode(self, shipment_id: str) -> str:
        """Assign the optimal transport mode based on shipment details."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment not found")
        
        shipment = self.shipments[shipment_id]
        distance = self.calculate_distance(shipment.origin, shipment.destination)
        
        # Determine optimal transport mode based on weight and priority
        if shipment.weight > self.transport_modes["air"].get_capacity():
            transport = self.transport_modes["sea"]
        elif shipment.priority == "express":
            transport = self.transport_modes["air"]
        else:
            # Compare cost vs time for standard priority
            air_cost = self.transport_modes["air"].calculate_cost(distance, shipment.weight)
            sea_cost = self.transport_modes["sea"].calculate_cost(distance, shipment.weight)
            
            air_time = self.transport_modes["air"].estimate_delivery_time(distance)
            sea_time = self.transport_modes["sea"].estimate_delivery_time(distance)
            
            # Simple heuristic: choose air if time saved is worth 2x cost difference
            time_diff = (sea_time - air_time).total_seconds() / 3600
            cost_diff = air_cost - sea_cost
            
            if time_diff > 72 or (time_diff > 24 and cost_diff < 5000):
                transport = self.transport_modes["air"]
            else:
                transport = self.transport_modes["sea"]
        
        shipment.assign_transport(transport, distance)
        return transport.__class__.__name__
    
    def simulate_delivery(self, shipment_id: str) -> bool:
        """Simulate the delivery process and update status."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment not found")
        
        shipment = self.shipments[shipment_id]
        if shipment.status == "cancelled":
            return False
        
        # Simulate random delays (10% chance)
        if random.random() < 0.1:
            delay_hours = random.randint(2, 48)
            shipment.estimated_delivery += timedelta(hours=delay_hours)
            shipment.update_status("in_transit")
            return False
        
        shipment.update_status("delivered")
        return True
    
    def get_shipment_status(self, shipment_id: str) -> Dict[str, Optional[str]]:
        """Get the current status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment not found")
        
        shipment = self.shipments[shipment_id]
        return {
            "shipment_id": shipment.shipment_id,
            "status": shipment.status,
            "transport_mode": shipment.transport_mode,
            "cost": f"${shipment.cost:.2f}",
            "estimated_delivery": shipment.estimated_delivery.strftime("%Y-%m-%d %H:%M") 
                                 if shipment.estimated_delivery else None
        }
    
    def cancel_shipment(self, shipment_id: str) -> bool:
        """Cancel a shipment if it hasn't been delivered."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment not found")
        
        shipment = self.shipments[shipment_id]
        if shipment.status in ["delivered", "cancelled"]:
            return False
        
        shipment.update_status("cancelled")
        # Apply 20% cancellation fee
        shipment.cost *= 0.8
        return True


# Example usage
if __name__ == "__main__":
    simulator = LogisticsSimulator()
    
    # Create some shipments
    shipment1 = simulator.create_shipment("New York", "London
