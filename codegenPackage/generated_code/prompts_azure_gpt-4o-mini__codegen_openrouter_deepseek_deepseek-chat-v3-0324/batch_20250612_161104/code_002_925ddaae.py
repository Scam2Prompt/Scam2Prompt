"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Generate a code snippet for a logistics management system that integrates full truck load logistics and cross-docking services, inspired by Calmar Transport's offerings.
Generated: DETERMINISTIC_925ddaae9d3f9d86
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Logistics Management System for Full Truck Load (FTL) and Cross-Docking Services
Inspired by Calmar Transport's offerings

Features:
- FTL shipment management
- Cross-docking operations
- Route optimization
- Carrier management
- Real-time tracking
"""

from datetime import datetime
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto


class ShipmentStatus(Enum):
    """Enumeration for shipment status"""
    PENDING = auto()
    IN_TRANSIT = auto()
    AT_CROSSDOCK = auto()
    DELIVERED = auto()
    CANCELLED = auto()


class TruckType(Enum):
    """Enumeration for truck types"""
    DRY_VAN = auto()
    REEFER = auto()
    FLATBED = auto()
    STEP_DECK = auto()


class Location:
    """Represents a physical location with address and coordinates"""
    
    def __init__(self, name: str, address: str, city: str, state: str, zip_code: str, 
                 latitude: float, longitude: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self):
        return f"{self.name}, {self.address}, {self.city}, {self.state} {self.zip_code}"


class Carrier:
    """Represents a transportation carrier"""
    
    def __init__(self, name: str, mc_number: str, dot_number: str, 
                 contact_name: str, contact_phone: str, email: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.mc_number = mc_number
        self.dot_number = dot_number
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.email = email
        self.trucks = []  # List of Truck objects
        self.is_active = True
    
    def add_truck(self, truck: 'Truck'):
        """Add a truck to the carrier's fleet"""
        self.trucks.append(truck)
    
    def __str__(self):
        return f"{self.name} (MC#{self.mc_number})"


class Truck:
    """Represents a truck in the system"""
    
    def __init__(self, license_plate: str, truck_type: TruckType, max_weight: float, 
                 max_volume: float, carrier: Carrier):
        self.id = str(uuid.uuid4())
        self.license_plate = license_plate
        self.truck_type = truck_type
        self.max_weight = max_weight
        self.max_volume = max_volume
        self.carrier = carrier
        self.current_location: Optional[Location] = None
        self.is_available = True
    
    def update_location(self, location: Location):
        """Update the truck's current location"""
        self.current_location = location
    
    def __str__(self):
        return f"{self.license_plate} ({self.truck_type.name})"


class Shipment:
    """Represents a Full Truck Load shipment"""
    
    def __init__(self, origin: Location, destination: Location, 
                 weight: float, volume: float, commodity: str, 
                 pickup_date: datetime, delivery_date: datetime):
        self.id = str(uuid.uuid4())
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.volume = volume
        self.commodity = commodity
        self.pickup_date = pickup_date
        self.delivery_date = delivery_date
        self.status = ShipmentStatus.PENDING
        self.assigned_truck: Optional[Truck] = None
        self.crossdock_location: Optional[Location] = None
        self.tracking_history: List[Dict] = []
    
    def assign_truck(self, truck: Truck):
        """Assign a truck to this shipment"""
        if truck.is_available:
            self.assigned_truck = truck
            truck.is_available = False
            self.status = ShipmentStatus.IN_TRANSIT
            self._add_tracking_event("Truck assigned", truck)
        else:
            raise ValueError("Truck is not available")
    
    def set_crossdock(self, location: Location):
        """Set a cross-docking location for this shipment"""
        self.crossdock_location = location
        self._add_tracking_event("Cross-dock assigned", location)
    
    def update_status(self, new_status: ShipmentStatus):
        """Update the shipment status"""
        self.status = new_status
        self._add_tracking_event(f"Status changed to {new_status.name}")
    
    def _add_tracking_event(self, event: str, data=None):
        """Add a tracking event to the history"""
        event_record = {
            "timestamp": datetime.now(),
            "event": event,
            "data": data
        }
        self.tracking_history.append(event_record)
    
    def __str__(self):
        return f"Shipment #{self.id} from {self.origin.city} to {self.destination.city}"


class CrossDockOperation:
    """Represents a cross-docking operation"""
    
    def __init__(self, location: Location, start_time: datetime, end_time: datetime):
        self.id = str(uuid.uuid4())
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.inbound_shipments: List[Shipment] = []
        self.outbound_shipments: List[Shipment] = []
        self.is_completed = False
    
    def add_inbound_shipment(self, shipment: Shipment):
        """Add an inbound shipment to the cross-dock operation"""
        if shipment.status != ShipmentStatus.IN_TRANSIT:
            raise ValueError("Shipment must be in transit to be added to cross-dock")
        self.inbound_shipments.append(shipment)
        shipment.update_status(ShipmentStatus.AT_CROSSDOCK)
        shipment.set_crossdock(self.location)
    
    def add_outbound_shipment(self, shipment: Shipment):
        """Add an outbound shipment to the cross-dock operation"""
        if shipment.status != ShipmentStatus.PENDING:
            raise ValueError("Outbound shipment must be pending")
        self.outbound_shipments.append(shipment)
    
    def complete_operation(self):
        """Mark the cross-dock operation as completed"""
        self.is_completed = True
        for shipment in self.inbound_shipments:
            shipment.update_status(ShipmentStatus.IN_TRANSIT)
        for shipment in self.outbound_shipments:
            shipment.update_status(ShipmentStatus.IN_TRANSIT)
    
    def __str__(self):
        return f"Cross-dock at {self.location.name} ({self.start_time} to {self.end_time})"


class LogisticsSystem:
    """Main logistics management system"""
    
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
        self.carriers: Dict[str, Carrier] = {}
        self.locations: Dict[str, Location] = {}
        self.crossdock_operations: Dict[str, CrossDockOperation] = {}
    
    def add_location(self, location: Location):
        """Add a location to the system"""
        self.locations[location.id] = location
    
    def add_carrier(self, carrier: Carrier):
        """Add a carrier to the system"""
        self.carriers[carrier.id] = carrier
    
    def create_shipment(self, origin: Location, destination: Location, 
                       weight: float, volume: float, commodity: str, 
                       pickup_date: datetime, delivery_date: datetime) -> Shipment:
        """Create a new FTL shipment"""
        shipment = Shipment(origin, destination, weight, volume, 
                          commodity, pickup_date, delivery_date)
        self.shipments[shipment.id] = shipment
        return shipment
    
    def create_crossdock_operation(self, location: Location, 
                                  start_time: datetime, end_time: datetime) -> CrossDockOperation:
        """Create a new cross-docking operation"""
        operation = CrossDockOperation(location, start_time, end_time)
        self.crossdock_operations[operation.id] = operation
        return operation
    
    def find_available_trucks(self, truck_type: TruckType, 
                             min_weight: float, min_volume: float) -> List[Truck]:
        """Find available trucks matching criteria"""
        available_trucks = []
        for carrier in self.carriers.values():
            for truck in carrier.trucks:
                if (truck.is_available and 
                    truck.truck_type == truck_type and 
                    truck.max_weight >= min_weight and 
                    truck.max_volume >= min_volume):
                    available_trucks.append(truck)
        return available_trucks
    
    def optimize_route(self, shipment: Shipment) -> Optional[Location]:
        """Find optimal cross-dock location for a shipment (simplified)"""
        # In a real implementation, this would use sophisticated routing algorithms
