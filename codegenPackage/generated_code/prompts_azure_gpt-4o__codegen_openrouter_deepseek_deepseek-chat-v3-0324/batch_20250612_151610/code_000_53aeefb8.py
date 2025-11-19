"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write Python code to simulate a logistics system for managing cargo transportation, including features for tracking shipments, monitoring vehicle locations via GPS, and handling refrigerated cargo requirements.
Generated: DETERMINISTIC_53aeefb88e56fd67
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
import random
import json

class CargoType(Enum):
    """Enumeration of cargo types."""
    GENERAL = auto()
    REFRIGERATED = auto()
    HAZARDOUS = auto()
    PERISHABLE = auto()

class VehicleType(Enum):
    """Enumeration of vehicle types."""
    TRUCK = auto()
    VAN = auto()
    SHIP = auto()
    PLANE = auto()

class ShipmentStatus(Enum):
    """Enumeration of shipment statuses."""
    PENDING = auto()
    IN_TRANSIT = auto()
    DELIVERED = auto()
    CANCELLED = auto()
    DELAYED = auto()

class GPSLocation:
    """Class representing GPS coordinates."""
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude
    
    def to_dict(self) -> Dict:
        """Convert GPSLocation to dictionary."""
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'GPSLocation':
        """Create GPSLocation from dictionary."""
        return cls(data['latitude'], data['longitude'])

class Cargo:
    """Class representing a cargo item."""
    def __init__(self, cargo_id: str, weight: float, cargo_type: CargoType, 
                 description: str, temperature_control: Optional[float] = None):
        self.cargo_id = cargo_id
        self.weight = weight
        self.cargo_type = cargo_type
        self.description = description
        self.temperature_control = temperature_control
    
    def to_dict(self) -> Dict:
        """Convert Cargo to dictionary."""
        return {
            'cargo_id': self.cargo_id,
            'weight': self.weight,
            'cargo_type': self.cargo_type.name,
            'description': self.description,
            'temperature_control': self.temperature_control
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Cargo':
        """Create Cargo from dictionary."""
        return cls(
            data['cargo_id'],
            data['weight'],
            CargoType[data['cargo_type']],
            data['description'],
            data.get('temperature_control')
        )

class Vehicle:
    """Class representing a transportation vehicle."""
    def __init__(self, vehicle_id: str, vehicle_type: VehicleType, 
                 capacity: float, current_location: GPSLocation):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.current_location = current_location
        self.current_load = 0.0
    
    def can_load(self, cargo: Cargo) -> bool:
        """Check if vehicle can load the cargo."""
        return self.current_load + cargo.weight <= self.capacity
    
    def load_cargo(self, cargo: Cargo) -> bool:
        """Load cargo onto the vehicle."""
        if self.can_load(cargo):
            self.current_load += cargo.weight
            return True
        return False
    
    def unload_cargo(self, cargo: Cargo) -> bool:
        """Unload cargo from the vehicle."""
        if self.current_load >= cargo.weight:
            self.current_load -= cargo.weight
            return True
        return False
    
    def update_location(self, new_location: GPSLocation) -> None:
        """Update vehicle's current location."""
        self.current_location = new_location
    
    def to_dict(self) -> Dict:
        """Convert Vehicle to dictionary."""
        return {
            'vehicle_id': self.vehicle_id,
            'vehicle_type': self.vehicle_type.name,
            'capacity': self.capacity,
            'current_load': self.current_load,
            'current_location': self.current_location.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Vehicle':
        """Create Vehicle from dictionary."""
        return cls(
            data['vehicle_id'],
            VehicleType[data['vehicle_type']],
            data['capacity'],
            GPSLocation.from_dict(data['current_location'])
        )

class Shipment:
    """Class representing a shipment."""
    def __init__(self, shipment_id: str, origin: GPSLocation, 
                 destination: GPSLocation, cargo_list: List[Cargo], 
                 vehicle: Vehicle, status: ShipmentStatus = ShipmentStatus.PENDING):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.cargo_list = cargo_list
        self.vehicle = vehicle
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_status(self, new_status: ShipmentStatus) -> None:
        """Update shipment status."""
        self.status = new_status
        self.updated_at = datetime.now()
    
    def check_temperature_requirements(self) -> bool:
        """Check if all refrigerated cargo meets temperature requirements."""
        for cargo in self.cargo_list:
            if cargo.cargo_type == CargoType.REFRIGERATED and cargo.temperature_control is None:
                return False
        return True
    
    def to_dict(self) -> Dict:
        """Convert Shipment to dictionary."""
        return {
            'shipment_id': self.shipment_id,
            'origin': self.origin.to_dict(),
            'destination': self.destination.to_dict(),
            'cargo_list': [cargo.to_dict() for cargo in self.cargo_list],
            'vehicle': self.vehicle.to_dict(),
            'status': self.status.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Shipment':
        """Create Shipment from dictionary."""
        return cls(
            data['shipment_id'],
            GPSLocation.from_dict(data['origin']),
            GPSLocation.from_dict(data['destination']),
            [Cargo.from_dict(cargo) for cargo in data['cargo_list']],
            Vehicle.from_dict(data['vehicle']),
            ShipmentStatus[data['status']]
        )

class LogisticsSystem:
    """Class representing the logistics system."""
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
        self.vehicles: Dict[str, Vehicle] = {}
    
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the system."""
        if vehicle.vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle.vehicle_id} already exists.")
        self.vehicles[vehicle.vehicle_id] = vehicle
    
    def create_shipment(self, origin: GPSLocation, destination: GPSLocation, 
                       cargo_list: List[Cargo], vehicle_id: str) -> Shipment:
        """Create a new shipment."""
        if not cargo_list:
            raise ValueError("Cargo list cannot be empty.")
        
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle_id} not found.")
        
        vehicle = self.vehicles[vehicle_id]
        
        # Check if vehicle can carry all cargo
        total_weight = sum(cargo.weight for cargo in cargo_list)
        if total_weight > vehicle.capacity:
            raise ValueError("Total cargo weight exceeds vehicle capacity.")
        
        # Check refrigerated cargo requirements
        for cargo in cargo_list:
            if cargo.cargo_type == CargoType.REFRIGERATED and cargo.temperature_control is None:
                raise ValueError("Refrigerated cargo must have temperature control specified.")
        
        shipment_id = str(uuid.uuid4())
        shipment = Shipment(shipment_id, origin, destination, cargo_list, vehicle)
        self.shipments[shipment_id] = shipment
        
        # Load cargo onto vehicle
        for cargo in cargo_list:
            if not vehicle.load_cargo(cargo):
                raise RuntimeError(f"Failed to load cargo {cargo.cargo_id} onto vehicle {vehicle_id}")
        
        return shipment
    
    def update_shipment_status(self, shipment_id: str, new_status: ShipmentStatus) -> None:
        """Update the status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment with ID {shipment_id} not found.")
        self.shipments[shipment_id].update_status(new_status)
    
    def update_vehicle_location(self, vehicle_id: str, new_location: GPSLocation) -> None:
        """Update the location of a vehicle."""
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle_id} not found.")
        self.vehicles[vehicle_id].update_location(new_location)
    
    def get_shipment_status(self, shipment_id: str) -> ShipmentStatus:
        """Get the status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment with ID {shipment_id} not found.")
        return self.shipments[shipment_id].status
    
    def get_vehicle_location(self, vehicle_id: str) -> GPSLocation:
        """
