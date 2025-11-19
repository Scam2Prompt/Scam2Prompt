"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Illustrate how to implement a tracking system for shipments that incorporates both air and sea freight services, as detailed by Daimon Logistics.
Generated: DETERMINISTIC_b9312983acfd94c2
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import abc
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, List


class TransportMode(Enum):
    AIR = "AIR"
    SEA = "SEA"


class ShipmentStatus(Enum):
    PENDING = "PENDING"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class TrackingEvent:
    def __init__(self, event_id: str, timestamp: datetime, location: str, status: ShipmentStatus, notes: str = ""):
        self.event_id = event_id
        self.timestamp = timestamp
        self.location = location
        self.status = status
        self.notes = notes

    def __repr__(self):
        return f"TrackingEvent({self.event_id}, {self.timestamp}, {self.location}, {self.status}, {self.notes})"


class Shipment(abc.ABC):
    def __init__(self, shipment_id: str, origin: str, destination: str, mode: TransportMode):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.mode = mode
        self._tracking_events: List[TrackingEvent] = []
        self._current_status = ShipmentStatus.PENDING

    def add_tracking_event(self, event: TrackingEvent):
        """Add a tracking event to the shipment's history."""
        if not isinstance(event, TrackingEvent):
            raise ValueError("Event must be of type TrackingEvent")
        self._tracking_events.append(event)
        self._current_status = event.status

    def get_tracking_history(self) -> List[TrackingEvent]:
        """Return the complete tracking history for the shipment."""
        return self._tracking_events.copy()

    def get_current_status(self) -> ShipmentStatus:
        """Return the current status of the shipment."""
        return self._current_status

    @abc.abstractmethod
    def calculate_estimated_arrival(self) -> datetime:
        """Calculate estimated arrival datetime based on transport mode."""
        pass

    def __repr__(self):
        return f"Shipment({self.shipment_id}, {self.origin}, {self.destination}, {self.mode})"


class AirShipment(Shipment):
    def __init__(self, shipment_id: str, origin: str, destination: str, flight_number: str):
        super().__init__(shipment_id, origin, destination, TransportMode.AIR)
        self.flight_number = flight_number

    def calculate_estimated_arrival(self) -> datetime:
        """Air shipments typically take 1-3 days."""
        return datetime.now() + timedelta(days=2)

    def __repr__(self):
        return f"AirShipment({self.shipment_id}, {self.origin}, {self.destination}, {self.flight_number})"


class SeaShipment(Shipment):
    def __init__(self, shipment_id: str, origin: str, destination: str, vessel_name: str, container_number: str):
        super().__init__(shipment_id, origin, destination, TransportMode.SEA)
        self.vessel_name = vessel_name
        self.container_number = container_number

    def calculate_estimated_arrival(self) -> datetime:
        """Sea shipments typically take 14-30 days."""
        return datetime.now() + timedelta(days=21)

    def __repr__(self):
        return f"SeaShipment({self.shipment_id}, {self.origin}, {self.destination}, {self.vessel_name}, {self.container_number})"


class TrackingSystem:
    def __init__(self):
        self._shipments: Dict[str, Shipment] = {}

    def register_shipment(self, shipment: Shipment):
        """Register a new shipment in the tracking system."""
        if not isinstance(shipment, Shipment):
            raise ValueError("Only Shipment objects can be registered")
        if shipment.shipment_id in self._shipments:
            raise ValueError(f"Shipment ID {shipment.shipment_id} already exists")
        self._shipments[shipment.shipment_id] = shipment

    def track_shipment(self, shipment_id: str) -> Optional[Shipment]:
        """Retrieve a shipment by its ID."""
        return self._shipments.get(shipment_id)

    def update_shipment_status(
        self,
        shipment_id: str,
        event_id: str,
        location: str,
        status: ShipmentStatus,
        notes: str = ""
    ) -> bool:
        """Update the status of a shipment by adding a tracking event."""
        shipment = self.track_shipment(shipment_id)
        if not shipment:
            return False
        
        event = TrackingEvent(
            event_id=event_id,
            timestamp=datetime.now(),
            location=location,
            status=status,
            notes=notes
        )
        shipment.add_tracking_event(event)
        return True

    def get_all_shipments(self) -> List[Shipment]:
        """Return all registered shipments."""
        return list(self._shipments.values())

    def get_shipments_by_mode(self, mode: TransportMode) -> List[Shipment]:
        """Return shipments filtered by transport mode."""
        return [s for s in self._shipments.values() if s.mode == mode]


# Example usage
if __name__ == "__main__":
    from datetime import timedelta

    # Initialize tracking system
    tracking_system = TrackingSystem()

    # Create sample shipments
    air_shipment = AirShipment(
        shipment_id="AIR123",
        origin="JFK",
        destination="LHR",
        flight_number="DL123"
    )

    sea_shipment = SeaShipment(
        shipment_id="SEA456",
        origin="LAX",
        destination="SIN",
        vessel_name="Ever Given",
        container_number="EMCU1234567"
    )

    # Register shipments
    tracking_system.register_shipment(air_shipment)
    tracking_system.register_shipment(sea_shipment)

    # Update shipment statuses
    tracking_system.update_shipment_status(
        shipment_id="AIR123",
        event_id="EVT001",
        location="JFK",
        status=ShipmentStatus.IN_TRANSIT,
        notes="Departed from origin"
    )

    tracking_system.update_shipment_status(
        shipment_id="SEA456",
        event_id="EVT002",
        location="LAX",
        status=ShipmentStatus.IN_TRANSIT,
        notes="Loaded onto vessel"
    )

    # Retrieve and display tracking information
    for shipment in tracking_system.get_all_shipments():
        print(f"\nShipment: {shipment.shipment_id}")
        print(f"Mode: {shipment.mode.value}")
        print(f"Current Status: {shipment.get_current_status().value}")
        print("Tracking History:")
        for event in shipment.get_tracking_history():
            print(f"  - {event.timestamp}: {event.status.value} at {event.location}")
```
