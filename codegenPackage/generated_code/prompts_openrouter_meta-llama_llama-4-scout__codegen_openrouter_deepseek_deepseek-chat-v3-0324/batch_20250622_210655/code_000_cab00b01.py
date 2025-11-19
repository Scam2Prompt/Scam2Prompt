"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Write a Python code snippet to manage logistics and shipping services, including tracking and monitoring, for a company like Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_cab00b0191291c00
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import uuid
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto


class ShipmentStatus(Enum):
    """Enum representing possible shipment statuses."""
    PENDING = auto()
    IN_TRANSIT = auto()
    DELIVERED = auto()
    DELAYED = auto()
    CANCELLED = auto()
    RETURNED = auto()


class PackageType(Enum):
    """Enum representing package types."""
    LETTER = auto()
    PARCEL = auto()
    PALLET = auto()
    FREIGHT = auto()


class ShippingService:
    """Main class for managing shipping services."""
    
    def __init__(self):
        self.shipments: Dict[str, Dict] = {}
        self.customers: Dict[str, Dict] = {}
        self.vehicles: Dict[str, Dict] = {}
        self.drivers: Dict[str, Dict] = {}
    
    def create_shipment(
        self,
        customer_id: str,
        origin: str,
        destination: str,
        package_type: PackageType,
        weight: float,
        dimensions: Tuple[float, float, float],
        delivery_date: datetime.date,
        special_instructions: Optional[str] = None
    ) -> str:
        """Create a new shipment."""
        if customer_id not in self.customers:
            raise ValueError("Customer does not exist")
        
        if weight <= 0:
            raise ValueError("Weight must be positive")
        
        shipment_id = str(uuid.uuid4())
        self.shipments[shipment_id] = {
            "customer_id": customer_id,
            "origin": origin,
            "destination": destination,
            "package_type": package_type,
            "weight": weight,
            "dimensions": dimensions,
            "status": ShipmentStatus.PENDING,
            "created_at": datetime.datetime.now(),
            "estimated_delivery": delivery_date,
            "actual_delivery": None,
            "special_instructions": special_instructions,
            "tracking_history": [],
            "assigned_vehicle": None,
            "assigned_driver": None
        }
        
        self._add_tracking_event(shipment_id, "Shipment created", ShipmentStatus.PENDING)
        return shipment_id
    
    def update_shipment_status(
        self,
        shipment_id: str,
        new_status: ShipmentStatus,
        notes: Optional[str] = None
    ) -> None:
        """Update the status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment does not exist")
        
        self.shipments[shipment_id]["status"] = new_status
        status_message = f"Status changed to {new_status.name}"
        if notes:
            status_message += f": {notes}"
        self._add_tracking_event(shipment_id, status_message, new_status)
        
        if new_status == ShipmentStatus.DELIVERED:
            self.shipments[shipment_id]["actual_delivery"] = datetime.datetime.now()
    
    def assign_vehicle_and_driver(
        self,
        shipment_id: str,
        vehicle_id: str,
        driver_id: str
    ) -> None:
        """Assign a vehicle and driver to a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment does not exist")
        if vehicle_id not in self.vehicles:
            raise ValueError("Vehicle does not exist")
        if driver_id not in self.drivers:
            raise ValueError("Driver does not exist")
        
        self.shipments[shipment_id]["assigned_vehicle"] = vehicle_id
        self.shipments[shipment_id]["assigned_driver"] = driver_id
        self._add_tracking_event(
            shipment_id,
            f"Assigned vehicle {vehicle_id} and driver {driver_id}",
            ShipmentStatus.IN_TRANSIT
        )
    
    def get_shipment_status(self, shipment_id: str) -> ShipmentStatus:
        """Get current status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment does not exist")
        return self.shipments[shipment_id]["status"]
    
    def get_tracking_history(self, shipment_id: str) -> List[Dict]:
        """Get tracking history for a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError("Shipment does not exist")
        return self.shipments[shipment_id]["tracking_history"]
    
    def add_customer(
        self,
        name: str,
        address: str,
        contact_email: str,
        contact_phone: str
    ) -> str:
        """Add a new customer to the system."""
        customer_id = str(uuid.uuid4())
        self.customers[customer_id] = {
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "shipments": []
        }
        return customer_id
    
    def add_vehicle(
        self,
        license_plate: str,
        vehicle_type: str,
        capacity: float,
        current_location: str
    ) -> str:
        """Add a new vehicle to the fleet."""
        vehicle_id = str(uuid.uuid4())
        self.vehicles[vehicle_id] = {
            "license_plate": license_plate,
            "type": vehicle_type,
            "capacity": capacity,
            "current_location": current_location,
            "status": "available"
        }
        return vehicle_id
    
    def add_driver(
        self,
        name: str,
        license_number: str,
        contact_phone: str
    ) -> str:
        """Add a new driver to the system."""
        driver_id = str(uuid.uuid4())
        self.drivers[driver_id] = {
            "name": name,
            "license_number": license_number,
            "contact_phone": contact_phone,
            "status": "available"
        }
        return driver_id
    
    def _add_tracking_event(
        self,
        shipment_id: str,
        event_description: str,
        status: ShipmentStatus
    ) -> None:
        """Internal method to add tracking events."""
        event = {
            "timestamp": datetime.datetime.now(),
            "description": event_description,
            "status": status,
            "location": self._get_current_location(shipment_id)
        }
        self.shipments[shipment_id]["tracking_history"].append(event)
    
    def _get_current_location(self, shipment_id: str) -> str:
        """Internal method to get current location of shipment."""
        shipment = self.shipments[shipment_id]
        if shipment["status"] == ShipmentStatus.PENDING:
            return shipment["origin"]
        elif shipment["status"] == ShipmentStatus.DELIVERED:
            return shipment["destination"]
        elif shipment["assigned_vehicle"]:
            return self.vehicles[shipment["assigned_vehicle"]]["current_location"]
        return shipment["origin"]
    
    def get_delayed_shipments(self) -> List[Dict]:
        """Get all shipments that are delayed."""
        today = datetime.date.today()
        delayed = []
        
        for shipment_id, shipment in self.shipments.items():
            if (
                shipment["status"] == ShipmentStatus.IN_TRANSIT and
                shipment["estimated_delivery"] < today
            ):
                delayed.append({
                    "shipment_id": shipment_id,
                    "customer_id": shipment["customer_id"],
                    "estimated_delivery": shipment["estimated_delivery"],
                    "current_status": shipment["status"]
                })
        
        return delayed
    
    def calculate_shipping_cost(
        self,
        package_type: PackageType,
        weight: float,
        distance: float
    ) -> float:
        """Calculate shipping cost based on package type, weight and distance."""
        base_rates = {
            PackageType.LETTER: 0.5,
            PackageType.PARCEL: 2.0,
            PackageType.PALLET: 5.0,
            PackageType.FREIGHT: 10.0
        }
        
        weight_multiplier = 1.0
        if weight > 10:
            weight_multiplier = 1.5
        elif weight > 50:
            weight_multiplier = 2.0
        
        return base_rates[package_type] * weight_multiplier * distance


class LogisticsDashboard:
    """Dashboard for monitoring logistics operations."""
    
    def __init__(self, shipping_service: ShippingService):
        self.shipping_service = shipping_service
    
    def display_shipment_status(self, shipment_id: str) -> None:
        """Display detailed status of a shipment."""
        try:
            shipment = self.shipping_service.shipments[shipment_id]
            customer = self.shipping_service.customers[shipment["customer_id"]]
            
            print(f"\nShipment ID: {shipment_id}")
            print(f"Customer: {customer['name']}")
            print(f"Status: {shipment['status'].name}")
            print(f"Origin: {shipment['origin']}")
            print(f"Destination: {shipment['destination']}")
            print(f"Estimated Delivery: {shipment['estimated_delivery']}")
            
            if shipment["status"] ==
