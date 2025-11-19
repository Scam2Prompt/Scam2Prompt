"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Create a program to manage freight forwarding services that include air-sea and sea-air transportation, incorporating features like door-to-door delivery and consolidation services as highlighted by Daimon Logistics BD.
Generated: DETERMINISTIC_61b7a00b28541c26
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Freight Forwarding Management System
This program manages freight forwarding services including air-sea and sea-air transportation,
door-to-door delivery, and consolidation services.
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
import json
import uuid


class TransportMode(Enum):
    """Enumeration for transport modes"""
    AIR = "Air"
    SEA = "Sea"
    AIR_SEA = "Air-Sea"
    SEA_AIR = "Sea-Air"


class ServiceType(Enum):
    """Enumeration for service types"""
    DOOR_TO_DOOR = "Door-to-Door"
    CONSOLIDATION = "Consolidation"
    STANDARD = "Standard"


class ShipmentStatus(Enum):
    """Enumeration for shipment statuses"""
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class Address:
    """Class representing a physical address"""
    def __init__(self, street: str, city: str, country: str, postal_code: str):
        self.street = street
        self.city = city
        self.country = country
        self.postal_code = postal_code

    def to_dict(self) -> Dict:
        """Convert address to dictionary"""
        return {
            "street": self.street,
            "city": self.city,
            "country": self.country,
            "postal_code": self.postal_code
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Address':
        """Create address from dictionary"""
        return cls(
            street=data["street"],
            city=data["city"],
            country=data["country"],
            postal_code=data["postal_code"]
        )


class CargoItem:
    """Class representing a cargo item"""
    def __init__(self, description: str, weight: float, volume: float, quantity: int):
        self.description = description
        self.weight = weight
        self.volume = volume
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """Convert cargo item to dictionary"""
        return {
            "description": self.description,
            "weight": self.weight,
            "volume": self.volume,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CargoItem':
        """Create cargo item from dictionary"""
        return cls(
            description=data["description"],
            weight=data["weight"],
            volume=data["volume"],
            quantity=data["quantity"]
        )


class Shipment:
    """Class representing a shipment"""
    def __init__(
        self,
        shipment_id: str,
        origin: Address,
        destination: Address,
        transport_mode: TransportMode,
        service_type: ServiceType,
        cargo_items: List[CargoItem],
        status: ShipmentStatus = ShipmentStatus.PENDING,
        created_at: Optional[datetime.datetime] = None
    ):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.transport_mode = transport_mode
        self.service_type = service_type
        self.cargo_items = cargo_items
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.history = []

    def add_history_event(self, event: str):
        """Add an event to shipment history"""
        timestamp = datetime.datetime.now()
        self.history.append({"timestamp": timestamp, "event": event})

    def update_status(self, new_status: ShipmentStatus):
        """Update shipment status"""
        self.status = new_status
        self.add_history_event(f"Status changed to {new_status.value}")

    def calculate_total_weight(self) -> float:
        """Calculate total weight of all cargo items"""
        return sum(item.weight * item.quantity for item in self.cargo_items)

    def calculate_total_volume(self) -> float:
        """Calculate total volume of all cargo items"""
        return sum(item.volume * item.quantity for item in self.cargo_items)

    def to_dict(self) -> Dict:
        """Convert shipment to dictionary"""
        return {
            "shipment_id": self.shipment_id,
            "origin": self.origin.to_dict(),
            "destination": self.destination.to_dict(),
            "transport_mode": self.transport_mode.value,
            "service_type": self.service_type.value,
            "cargo_items": [item.to_dict() for item in self.cargo_items],
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "history": self.history
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Shipment':
        """Create shipment from dictionary"""
        return cls(
            shipment_id=data["shipment_id"],
            origin=Address.from_dict(data["origin"]),
            destination=Address.from_dict(data["destination"]),
            transport_mode=TransportMode(data["transport_mode"]),
            service_type=ServiceType(data["service_type"]),
            cargo_items=[CargoItem.from_dict(item) for item in data["cargo_items"]],
            status=ShipmentStatus(data["status"]),
            created_at=datetime.datetime.fromisoformat(data["created_at"])
        )


class FreightForwardingSystem:
    """Main class for freight forwarding management system"""
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}

    def create_shipment(
        self,
        origin: Address,
        destination: Address,
        transport_mode: TransportMode,
        service_type: ServiceType,
        cargo_items: List[CargoItem]
    ) -> Shipment:
        """Create a new shipment"""
        shipment_id = str(uuid.uuid4())
        shipment = Shipment(
            shipment_id=shipment_id,
            origin=origin,
            destination=destination,
            transport_mode=transport_mode,
            service_type=service_type,
            cargo_items=cargo_items
        )
        self.shipments[shipment_id] = shipment
        shipment.add_history_event("Shipment created")
        return shipment

    def get_shipment(self, shipment_id: str) -> Optional[Shipment]:
        """Get shipment by ID"""
        return self.shipments.get(shipment_id)

    def update_shipment_status(self, shipment_id: str, new_status: ShipmentStatus) -> bool:
        """Update shipment status"""
        shipment = self.get_shipment(shipment_id)
        if not shipment:
            return False
        shipment.update_status(new_status)
        return True

    def get_all_shipments(self) -> List[Shipment]:
        """Get all shipments"""
        return list(self.shipments.values())

    def save_to_file(self, filename: str):
        """Save shipments to file"""
        data = {
            "shipments": [shipment.to_dict() for shipment in self.shipments.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str):
        """Load shipments from file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.shipments = {
                    shipment_data["shipment_id"]: Shipment.from_dict(shipment_data)
                    for shipment_data in data["shipments"]
                }
        except FileNotFoundError:
            self.shipments = {}


def main():
    """Main function to demonstrate the system"""
    system = FreightForwardingSystem()

    # Create addresses
    origin = Address(
        street="123 Main St",
        city="Dhaka",
        country="Bangladesh",
        postal_code="1000"
    )
    destination = Address(
        street="456 Broadway",
        city="New York",
        country="USA",
        postal_code="10001"
    )

    # Create cargo items
    cargo_items = [
        CargoItem(
            description="Electronics",
            weight=10.5,
            volume=2.3,
            quantity=5
        ),
        CargoItem(
            description="Textiles",
            weight=15.0,
            volume=5.0,
            quantity=10
        )
    ]

    # Create a shipment
    shipment = system.create_shipment(
        origin=origin,
        destination=destination,
        transport_mode=TransportMode.AIR_SEA,
        service_type=ServiceType.DOOR_TO_DOOR,
        cargo_items=cargo_items
    )

    # Update shipment status
    system.update_shipment_status(shipment.shipment_id, ShipmentStatus.IN_TRANSIT)

    # Save to file
    system.save_to_file("shipments.json")

    # Print shipment details
    print(f"Shipment ID: {shipment.shipment_id}")
    print(f"Status: {shipment.status.value}")
    print(f"Total Weight: {shipment.calculate_total_weight()} kg")
    print(f"Total Volume: {shipment.calculate_total_volume()} m³")


if __name__ == "__main__":
    main()
```
