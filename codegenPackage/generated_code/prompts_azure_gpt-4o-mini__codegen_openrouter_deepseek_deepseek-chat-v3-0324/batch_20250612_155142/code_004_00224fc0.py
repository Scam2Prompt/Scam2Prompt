"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Illustrate how to implement a tracking system for shipments that ensures timely delivery, in line with the logistics strategies of Fealty Worldwide.
Generated: DETERMINISTIC_00224fc030cb17c9
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
import uuid


class ShipmentStatus(Enum):
    """Enum representing possible shipment statuses."""
    CREATED = "Created"
    IN_TRANSIT = "In Transit"
    DELAYED = "Delayed"
    OUT_FOR_DELIVERY = "Out for Delivery"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


@dataclass
class Location:
    """Represents a geographical location."""
    latitude: float
    longitude: float
    address: str
    city: str
    country: str
    postal_code: str


@dataclass
class ShipmentEvent:
    """Represents an event in the shipment's lifecycle."""
    event_id: str
    timestamp: datetime.datetime
    status: ShipmentStatus
    location: Optional[Location] = None
    notes: Optional[str] = None


@dataclass
class Shipment:
    """Represents a shipment with tracking information."""
    shipment_id: str
    tracking_number: str
    origin: Location
    destination: Location
    estimated_delivery: datetime.datetime
    events: List[ShipmentEvent]
    current_status: ShipmentStatus
    carrier: str
    customer_id: str


class ShipmentTracker:
    """Core class for tracking shipments and ensuring timely delivery."""
    
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
    
    def create_shipment(
        self,
        origin: Location,
        destination: Location,
        estimated_delivery: datetime.datetime,
        carrier: str,
        customer_id: str
    ) -> Shipment:
        """Creates a new shipment with initial tracking information."""
        shipment_id = str(uuid.uuid4())
        tracking_number = f"FWT-{uuid.uuid4().hex[:8].upper()}"
        
        initial_event = ShipmentEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.datetime.now(),
            status=ShipmentStatus.CREATED,
            location=origin
        )
        
        shipment = Shipment(
            shipment_id=shipment_id,
            tracking_number=tracking_number,
            origin=origin,
            destination=destination,
            estimated_delivery=estimated_delivery,
            events=[initial_event],
            current_status=ShipmentStatus.CREATED,
            carrier=carrier,
            customer_id=customer_id
        )
        
        self.shipments[shipment_id] = shipment
        return shipment
    
    def update_shipment_status(
        self,
        shipment_id: str,
        new_status: ShipmentStatus,
        location: Optional[Location] = None,
        notes: Optional[str] = None
    ) -> Shipment:
        """Updates the status of a shipment and logs the event."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment {shipment_id} not found")
        
        shipment = self.shipments[shipment_id]
        
        event = ShipmentEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.datetime.now(),
            status=new_status,
            location=location,
            notes=notes
        )
        
        shipment.events.append(event)
        shipment.current_status = new_status
        
        # Check for delays if status is IN_TRANSIT
        if new_status == ShipmentStatus.IN_TRANSIT:
            self._check_for_delays(shipment)
        
        return shipment
    
    def _check_for_delays(self, shipment: Shipment) -> None:
        """Internal method to check for potential delays."""
        current_time = datetime.datetime.now()
        if current_time > shipment.estimated_delivery:
            self.update_shipment_status(
                shipment.shipment_id,
                ShipmentStatus.DELAYED,
                notes="Estimated delivery time has passed"
            )
    
    def get_shipment_status(self, shipment_id: str) -> ShipmentStatus:
        """Returns the current status of a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment {shipment_id} not found")
        return self.shipments[shipment_id].current_status
    
    def get_shipment_events(self, shipment_id: str) -> List[ShipmentEvent]:
        """Returns all tracking events for a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment {shipment_id} not found")
        return self.shipments[shipment_id].events
    
    def get_shipment_eta(self, shipment_id: str) -> datetime.datetime:
        """Returns the estimated time of arrival for a shipment."""
        if shipment_id not in self.shipments:
            raise ValueError(f"Shipment {shipment_id} not found")
        return self.shipments[shipment_id].estimated_delivery
    
    def get_all_shipments(self) -> List[Shipment]:
        """Returns all shipments being tracked."""
        return list(self.shipments.values())
    
    def get_shipments_by_status(self, status: ShipmentStatus) -> List[Shipment]:
        """Returns shipments filtered by status."""
        return [s for s in self.shipments.values() if s.current_status == status]
    
    def get_delayed_shipments(self) -> List[Shipment]:
        """Returns all shipments that are delayed."""
        return self.get_shipments_by_status(ShipmentStatus.DELAYED)
```
