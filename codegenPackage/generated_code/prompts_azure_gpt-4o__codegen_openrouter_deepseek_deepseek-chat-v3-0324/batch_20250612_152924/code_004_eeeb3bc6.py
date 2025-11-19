"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Write code to model the logistics of transporting oversized cargo using a fleet of vehicles, incorporating OPC S.A.S.'s approach to handling extra-dimensional loads.
Generated: DETERMINISTIC_eeeb3bc6ef5d67a7
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import List, Dict, Optional, Tuple

class VehicleType(Enum):
    """Enum representing different types of vehicles for oversized cargo transport."""
    FLATBED = "Flatbed"
    LOWBOY = "Lowboy"
    STEP_DECK = "Step Deck"
    EXTENDABLE = "Extendable"
    MODULAR = "Modular"

class Cargo:
    """Class representing oversized cargo to be transported."""
    
    def __init__(self, 
                 cargo_id: str, 
                 length: float, 
                 width: float, 
                 height: float, 
                 weight: float,
                 special_requirements: List[str] = None):
        """
        Initialize cargo with dimensions and requirements.
        
        Args:
            cargo_id: Unique identifier for the cargo
            length: Length in meters
            width: Width in meters
            height: Height in meters
            weight: Weight in tons
            special_requirements: List of special handling requirements
        """
        self.cargo_id = cargo_id
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.special_requirements = special_requirements if special_requirements else []
    
    def get_volume(self) -> float:
        """Calculate the volume of the cargo in cubic meters."""
        return self.length * self.width * self.height
    
    def __str__(self) -> str:
        return f"Cargo {self.cargo_id}: {self.length}m x {self.width}m x {self.height}m, {self.weight} tons"

class Vehicle:
    """Class representing a transport vehicle."""
    
    def __init__(self, 
                 vehicle_id: str, 
                 vehicle_type: VehicleType,
                 max_length: float,
                 max_width: float,
                 max_height: float,
                 max_weight: float,
                 special_capabilities: List[str] = None):
        """
        Initialize vehicle with transport capabilities.
        
        Args:
            vehicle_id: Unique identifier for the vehicle
            vehicle_type: Type of vehicle from VehicleType enum
            max_length: Maximum cargo length in meters
            max_width: Maximum cargo width in meters
            max_height: Maximum cargo height in meters
            max_weight: Maximum cargo weight in tons
            special_capabilities: List of special capabilities (e.g., 'hydraulic', 'extendable')
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.max_length = max_length
        self.max_width = max_width
        self.max_height = max_height
        self.max_weight = max_weight
        self.special_capabilities = special_capabilities if special_capabilities else []
        self.current_cargo: Optional[Cargo] = None
    
    def can_transport(self, cargo: Cargo) -> Tuple[bool, str]:
        """
        Check if vehicle can transport given cargo.
        
        Args:
            cargo: Cargo object to check
            
        Returns:
            Tuple of (can_transport: bool, reason: str)
        """
        if cargo.length > self.max_length:
            return (False, f"Length {cargo.length}m exceeds max {self.max_length}m")
        if cargo.width > self.max_width:
            return (False, f"Width {cargo.width}m exceeds max {self.max_width}m")
        if cargo.height > self.max_height:
            return (False, f"Height {cargo.height}m exceeds max {self.max_height}m")
        if cargo.weight > self.max_weight:
            return (False, f"Weight {cargo.weight} tons exceeds max {self.max_weight} tons")
        
        # Check special requirements
        for req in cargo.special_requirements:
            if req not in self.special_capabilities:
                return (False, f"Missing required capability: {req}")
        
        return (True, "Can transport")
    
    def load_cargo(self, cargo: Cargo) -> bool:
        """
        Load cargo onto vehicle if possible.
        
        Args:
            cargo: Cargo to load
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        can_load, reason = self.can_transport(cargo)
        if not can_load:
            print(f"Cannot load cargo: {reason}")
            return False
        
        if self.current_cargo is not None:
            print(f"Vehicle {self.vehicle_id} already has cargo loaded")
            return False
            
        self.current_cargo = cargo
        print(f"Loaded {cargo.cargo_id} onto {self.vehicle_id}")
        return True
    
    def unload_cargo(self) -> Optional[Cargo]:
        """
        Unload cargo from vehicle.
        
        Returns:
            The unloaded cargo or None if no cargo was loaded
        """
        if self.current_cargo is None:
            print(f"No cargo to unload from {self.vehicle_id}")
            return None
            
        cargo = self.current_cargo
        self.current_cargo = None
        print(f"Unloaded {cargo.cargo_id} from {self.vehicle_id}")
        return cargo
    
    def __str__(self) -> str:
        status = f"Vehicle {self.vehicle_id} ({self.vehicle_type.value})"
        if self.current_cargo:
            status += f" carrying {self.current_cargo.cargo_id}"
        return status

class TransportFleet:
    """Class representing a fleet of vehicles for oversized cargo transport."""
    
    def __init__(self):
        """Initialize an empty fleet."""
        self.vehicles: Dict[str, Vehicle] = {}
    
    def add_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Add a vehicle to the fleet.
        
        Args:
            vehicle: Vehicle to add
            
        Returns:
            bool: True if added successfully, False if vehicle ID already exists
        """
        if vehicle.vehicle_id in self.vehicles:
            print(f"Vehicle with ID {vehicle.vehicle_id} already exists in fleet")
            return False
        self.vehicles[vehicle.vehicle_id] = vehicle
        return True
    
    def remove_vehicle(self, vehicle_id: str) -> bool:
        """
        Remove a vehicle from the fleet.
        
        Args:
            vehicle_id: ID of vehicle to remove
            
        Returns:
            bool: True if removed successfully, False if vehicle not found
        """
        if vehicle_id not in self.vehicles:
            print(f"Vehicle with ID {vehicle_id} not found in fleet")
            return False
        del self.vehicles[vehicle_id]
        return True
    
    def find_available_vehicle(self, cargo: Cargo) -> Optional[Vehicle]:
        """
        Find a vehicle capable of transporting the given cargo.
        
        Args:
            cargo: Cargo to transport
            
        Returns:
            Vehicle: First available vehicle that can transport the cargo, or None
        """
        for vehicle in self.vehicles.values():
            if vehicle.current_cargo is None:
                can_transport, _ = vehicle.can_transport(cargo)
                if can_transport:
                    return vehicle
        return None
    
    def transport_cargo(self, cargo: Cargo, destination: str) -> bool:
        """
        Transport cargo to destination using available fleet vehicles.
        
        Args:
            cargo: Cargo to transport
            destination: Destination location
            
        Returns:
            bool: True if transport was successful, False otherwise
        """
        vehicle = self.find_available_vehicle(cargo)
        if not vehicle:
            print(f"No available vehicle can transport {cargo.cargo_id}")
            return False
        
        if not vehicle.load_cargo(cargo):
            return False
        
        # Simulate transport process
        print(f"Transporting {cargo.cargo_id} to {destination} using {vehicle.vehicle_id}")
        
        vehicle.unload_cargo()
        print(f"Successfully delivered {cargo.cargo_id} to {destination}")
        return True
    
    def get_fleet_status(self) -> Dict[str, int]:
        """
        Get current fleet status.
        
        Returns:
            Dict with counts of total vehicles and available vehicles
        """
        total = len(self.vehicles)
        available = sum(1 for v in self.vehicles.values() if v.current_cargo is None)
        return {
            "total_vehicles": total,
            "available_vehicles": available,
            "utilized_vehicles": total - available
        }

class RoutePlanner:
    """Class for planning routes for oversized cargo transport."""
    
    def __init__(self):
        """Initialize route planner."""
        self.route_cache: Dict[Tuple[str, str], Dict] = {}
    
    def calculate_route(self, origin: str, destination: str) -> Dict:
        """
        Calculate optimal route for oversized cargo transport.
        
        Args:
            origin: Starting location
            destination: Destination location
            
        Returns:
            Dict with route details including distance, estimated time, and special considerations
        """
        cache_key = (origin, destination)
        if cache_key in self.route_cache:
            return self.route_cache[cache_key]
        
        # Simulate route calculation with special considerations for oversized cargo
        route = {
            "distance_km": self._estimate_distance(origin, destination),
            "estimated_hours": self._estimate_time(origin, destination),
            "special_considerations": self._get_special_considerations(origin,
