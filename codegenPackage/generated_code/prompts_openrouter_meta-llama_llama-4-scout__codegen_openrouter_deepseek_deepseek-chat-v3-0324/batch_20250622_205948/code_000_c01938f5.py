"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Write a Python script to manage logistics and track shipments for a transportation company like Calmar Transport, including features for trailer drop services and cross-docking."
Generated: DETERMINISTIC_c01938f5abeef640
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Union
from enum import Enum


class ShipmentStatus(Enum):
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class TrailerType(Enum):
    DRY_VAN = "Dry Van"
    REEFER = "Reefer"
    FLATBED = "Flatbed"
    STEP_DECK = "Step Deck"


class Shipment:
    def __init__(
        self,
        shipment_id: str,
        origin: str,
        destination: str,
        trailer_type: TrailerType,
        weight: float,
        expected_delivery: datetime.date,
        status: ShipmentStatus = ShipmentStatus.PENDING,
    ):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.trailer_type = trailer_type
        self.weight = weight
        self.expected_delivery = expected_delivery
        self.status = status
        self.actual_delivery: Optional[datetime.date] = None
        self.history: List[Dict[str, Union[str, datetime.datetime]]] = []
        self._add_history_entry("Shipment created")

    def update_status(self, new_status: ShipmentStatus) -> None:
        """Update the status of the shipment and record the change."""
        self.status = new_status
        self._add_history_entry(f"Status changed to {new_status.value}")

        if new_status == ShipmentStatus.DELIVERED:
            self.actual_delivery = datetime.date.today()

    def _add_history_entry(self, description: str) -> None:
        """Add an entry to the shipment history."""
        entry = {
            "timestamp": datetime.datetime.now(),
            "description": description,
        }
        self.history.append(entry)

    def to_dict(self) -> Dict:
        """Convert the shipment object to a dictionary for serialization."""
        return {
            "shipment_id": self.shipment_id,
            "origin": self.origin,
            "destination": self.destination,
            "trailer_type": self.trailer_type.value,
            "weight": self.weight,
            "expected_delivery": self.expected_delivery.isoformat(),
            "status": self.status.value,
            "actual_delivery": self.actual_delivery.isoformat() if self.actual_delivery else None,
            "history": [
                {
                    "timestamp": entry["timestamp"].isoformat(),
                    "description": entry["description"],
                }
                for entry in self.history
            ],
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Shipment":
        """Create a Shipment object from a dictionary."""
        shipment = cls(
            shipment_id=data["shipment_id"],
            origin=data["origin"],
            destination=data["destination"],
            trailer_type=TrailerType(data["trailer_type"]),
            weight=data["weight"],
            expected_delivery=datetime.date.fromisoformat(data["expected_delivery"]),
            status=ShipmentStatus(data["status"]),
        )
        if data["actual_delivery"]:
            shipment.actual_delivery = datetime.date.fromisoformat(data["actual_delivery"])
        
        shipment.history = [
            {
                "timestamp": datetime.datetime.fromisoformat(entry["timestamp"]),
                "description": entry["description"],
            }
            for entry in data["history"]
        ]
        return shipment


class TrailerDrop:
    def __init__(self, drop_id: str, location: str, trailer_type: TrailerType, available_from: datetime.date):
        self.drop_id = drop_id
        self.location = location
        self.trailer_type = trailer_type
        self.available_from = available_from
        self.available_until: Optional[datetime.date] = None
        self.is_occupied = False

    def to_dict(self) -> Dict:
        """Convert the trailer drop object to a dictionary for serialization."""
        return {
            "drop_id": self.drop_id,
            "location": self.location,
            "trailer_type": self.trailer_type.value,
            "available_from": self.available_from.isoformat(),
            "available_until": self.available_until.isoformat() if self.available_until else None,
            "is_occupied": self.is_occupied,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "TrailerDrop":
        """Create a TrailerDrop object from a dictionary."""
        drop = cls(
            drop_id=data["drop_id"],
            location=data["location"],
            trailer_type=TrailerType(data["trailer_type"]),
            available_from=datetime.date.fromisoformat(data["available_from"]),
        )
        if data["available_until"]:
            drop.available_until = datetime.date.fromisoformat(data["available_until"])
        drop.is_occupied = data["is_occupied"]
        return drop


class CrossDockOperation:
    def __init__(self, operation_id: str, location: str, start_time: datetime.datetime):
        self.operation_id = operation_id
        self.location = location
        self.start_time = start_time
        self.end_time: Optional[datetime.datetime] = None
        self.shipments: List[str] = []  # List of shipment IDs
        self.is_complete = False

    def add_shipment(self, shipment_id: str) -> None:
        """Add a shipment to the cross-dock operation."""
        if shipment_id not in self.shipments:
            self.shipments.append(shipment_id)

    def complete_operation(self) -> None:
        """Mark the cross-dock operation as complete."""
        self.is_complete = True
        self.end_time = datetime.datetime.now()

    def to_dict(self) -> Dict:
        """Convert the cross-dock operation object to a dictionary for serialization."""
        return {
            "operation_id": self.operation_id,
            "location": self.location,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "shipments": self.shipments,
            "is_complete": self.is_complete,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "CrossDockOperation":
        """Create a CrossDockOperation object from a dictionary."""
        operation = cls(
            operation_id=data["operation_id"],
            location=data["location"],
            start_time=datetime.datetime.fromisoformat(data["start_time"]),
        )
        if data["end_time"]:
            operation.end_time = datetime.datetime.fromisoformat(data["end_time"])
        operation.shipments = data["shipments"]
        operation.is_complete = data["is_complete"]
        return operation


class LogisticsManager:
    def __init__(self, data_file: str = "logistics_data.json"):
        self.data_file = data_file
        self.shipments: Dict[str, Shipment] = {}
        self.trailer_drops: Dict[str, TrailerDrop] = {}
        self.cross_dock_operations: Dict[str, CrossDockOperation] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load data from the JSON file."""
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.shipments = {
                    shipment_id: Shipment.from_dict(shipment_data)
                    for shipment_id, shipment_data in data.get("shipments", {}).items()
                }
                self.trailer_drops = {
                    drop_id: TrailerDrop.from_dict(drop_data)
                    for drop_id, drop_data in data.get("trailer_drops", {}).items()
                }
                self.cross_dock_operations = {
                    op_id: CrossDockOperation.from_dict(op_data)
                    for op_id, op_data in data.get("cross_dock_operations", {}).items()
                }
        except FileNotFoundError:
            # File doesn't exist yet, start with empty data
            pass
        except json.JSONDecodeError:
            raise ValueError("Data file is corrupted")

    def _save_data(self) -> None:
        """Save data to the JSON file."""
        data = {
            "shipments": {
                shipment_id: shipment.to_dict()
                for shipment_id, shipment in self.shipments.items()
            },
            "trailer_drops": {
                drop_id: drop.to_dict()
                for drop_id, drop in self.trailer_drops.items()
            },
            "cross_dock_operations": {
                op_id: op.to_dict()
                for op_id, op in self.cross_dock_operations.items()
            },
        }
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=2)

    def create_shipment(
        self,
        origin: str,
        destination: str,
        trailer_type: TrailerType,
        weight: float,
        expected_delivery: datetime.date,
    ) -> str:
        """Create a new shipment and return its ID."""
        shipment_id = f"SH{datetime.datetime
