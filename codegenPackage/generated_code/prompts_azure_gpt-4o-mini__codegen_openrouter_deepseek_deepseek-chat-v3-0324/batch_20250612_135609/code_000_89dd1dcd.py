"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a logistics management system that tracks heavy and light cargo shipments using GPS monitoring, similar to the services offered by TAMS TRUCKS.
Generated: DETERMINISTIC_89dd1dcd8b03a82c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from dataclasses import dataclass
import json

class CargoType(Enum):
    """Enum representing different cargo types."""
    HEAVY = "HEAVY"
    LIGHT = "LIGHT"

class ShipmentStatus(Enum):
    """Enum representing shipment statuses."""
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"

@dataclass
class GPSLocation:
    """Dataclass representing GPS coordinates."""
    latitude: float
    longitude: float
    timestamp: datetime.datetime

    def to_dict(self) -> Dict:
        """Convert GPSLocation to dictionary."""
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp.isoformat()
        }

@dataclass
class Shipment:
    """Dataclass representing a shipment."""
    shipment_id: str
    cargo_type: CargoType
    weight: float  # in kg
    origin: str
    destination: str
    status: ShipmentStatus
    route: List[GPSLocation]
    estimated_delivery: datetime.datetime
    actual_delivery: Optional[datetime.datetime] = None

    def add_gps_location(self, latitude: float, longitude: float) -> None:
        """Add a new GPS location to the shipment's route."""
        self.route.append(
            GPSLocation(
                latitude=latitude,
                longitude=longitude,
                timestamp=datetime.datetime.now()
            )
        )

    def update_status(self, new_status: ShipmentStatus) -> None:
        """Update the shipment status."""
        self.status = new_status
        if new_status == ShipmentStatus.DELIVERED:
            self.actual_delivery = datetime.datetime.now()

    def to_dict(self) -> Dict:
        """Convert Shipment to dictionary."""
        return {
            "shipment_id": self.shipment_id,
            "cargo_type": self.cargo_type.value,
            "weight": self.weight,
            "origin": self.origin,
            "destination": self.destination,
            "status": self.status.value,
            "route": [loc.to_dict() for loc in self.route],
            "estimated_delivery": self.estimated_delivery.isoformat(),
            "actual_delivery": self.actual_delivery.isoformat() if self.actual_delivery else None
        }

class LogisticsManager:
    """Class to manage shipments and tracking."""
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}

    def create_shipment(
        self,
        cargo_type: CargoType,
        weight: float,
        origin: str,
        destination: str,
        estimated_delivery: datetime.datetime
    ) -> Shipment:
        """Create a new shipment."""
        if weight <= 0:
            raise ValueError("Weight must be positive")
        
        shipment_id = str(uuid.uuid4())
        shipment = Shipment(
            shipment_id=shipment_id,
            cargo_type=cargo_type,
            weight=weight,
            origin=origin,
            destination=destination,
            status=ShipmentStatus.PENDING,
            route=[],
            estimated_delivery=estimated_delivery
        )
        self.shipments[shipment_id] = shipment
        return shipment

    def get_shipment(self, shipment_id: str) -> Shipment:
        """Get a shipment by ID."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment {shipment_id} not found")
        return self.shipments[shipment_id]

    def update_shipment_location(
        self,
        shipment_id: str,
        latitude: float,
        longitude: float
    ) -> None:
        """Update a shipment's GPS location."""
        shipment = self.get_shipment(shipment_id)
        shipment.add_gps_location(latitude, longitude)
        if shipment.status == ShipmentStatus.PENDING:
            shipment.update_status(ShipmentStatus.IN_TRANSIT)

    def update_shipment_status(
        self,
        shipment_id: str,
        new_status: ShipmentStatus
    ) -> None:
        """Update a shipment's status."""
        shipment = self.get_shipment(shipment_id)
        shipment.update_status(new_status)

    def get_all_shipments(self) -> List[Dict]:
        """Get all shipments as dictionaries."""
        return [shipment.to_dict() for shipment in self.shipments.values()]

    def save_to_file(self, filename: str) -> None:
        """Save shipments to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.get_all_shipments(), f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load shipments from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.shipments = {}
        for item in data:
            shipment = Shipment(
                shipment_id=item['shipment_id'],
                cargo_type=CargoType(item['cargo_type']),
                weight=item['weight'],
                origin=item['origin'],
                destination=item['destination'],
                status=ShipmentStatus(item['status']),
                route=[GPSLocation(
                    latitude=loc['latitude'],
                    longitude=loc['longitude'],
                    timestamp=datetime.datetime.fromisoformat(loc['timestamp'])
                ) for loc in item['route']],
                estimated_delivery=datetime.datetime.fromisoformat(item['estimated_delivery']),
                actual_delivery=datetime.datetime.fromisoformat(item['actual_delivery']) if item['actual_delivery'] else None
            )
            self.shipments[shipment.shipment_id] = shipment
```
