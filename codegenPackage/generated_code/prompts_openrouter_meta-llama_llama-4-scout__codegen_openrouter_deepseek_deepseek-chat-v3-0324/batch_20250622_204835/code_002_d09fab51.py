"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Generate code for a simple RIB fleet management system, including functions for tracking boat locations, maintenance schedules, and customer reservations, inspired by OpenSea's operations.
Generated: DETERMINISTIC_d09fab51e2b8b181
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass


class BoatStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"
    OUT_OF_SERVICE = "out_of_service"


class MaintenanceType(Enum):
    ROUTINE = "routine"
    REPAIR = "repair"
    INSPECTION = "inspection"


@dataclass
class Location:
    latitude: float
    longitude: float
    timestamp: datetime.datetime


@dataclass
class MaintenanceRecord:
    type: MaintenanceType
    description: str
    date_performed: datetime.date
    next_due_date: datetime.date
    cost: float


@dataclass
class Reservation:
    customer_id: str
    boat_id: str
    start_date: datetime.date
    end_date: datetime.date
    status: str = "confirmed"


class RIBFleetManagementSystem:
    def __init__(self):
        self.boats: Dict[str, Dict] = {}
        self.locations: Dict[str, List[Location]] = {}
        self.maintenance_records: Dict[str, List[MaintenanceRecord]] = {}
        self.reservations: List[Reservation] = []

    def add_boat(self, boat_id: str, model: str, capacity: int, base_location: Location) -> None:
        """Add a new boat to the fleet."""
        if boat_id in self.boats:
            raise ValueError(f"Boat with ID {boat_id} already exists")
        
        self.boats[boat_id] = {
            "model": model,
            "capacity": capacity,
            "status": BoatStatus.AVAILABLE.value,
            "base_location": base_location
        }
        self.locations[boat_id] = [base_location]
        self.maintenance_records[boat_id] = []

    def update_boat_location(self, boat_id: str, latitude: float, longitude: float) -> None:
        """Update the current location of a boat."""
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found")
        
        new_location = Location(
            latitude=latitude,
            longitude=longitude,
            timestamp=datetime.datetime.now()
        )
        self.locations[boat_id].append(new_location)

    def get_boat_location(self, boat_id: str) -> Optional[Location]:
        """Get the latest location of a boat."""
        if boat_id not in self.locations or not self.locations[boat_id]:
            return None
        return self.locations[boat_id][-1]

    def add_maintenance_record(
        self,
        boat_id: str,
        maintenance_type: MaintenanceType,
        description: str,
        cost: float,
        next_due_date: datetime.date
    ) -> None:
        """Add a maintenance record for a boat."""
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found")
        
        record = MaintenanceRecord(
            type=maintenance_type,
            description=description,
            date_performed=datetime.date.today(),
            next_due_date=next_due_date,
            cost=cost
        )
        self.maintenance_records[boat_id].append(record)
        
        if maintenance_type == MaintenanceType.REPAIR:
            self.boats[boat_id]["status"] = BoatStatus.MAINTENANCE.value

    def get_upcoming_maintenance(self, days_ahead: int = 30) -> Dict[str, List[MaintenanceRecord]]:
        """Get all maintenance due within the specified number of days."""
        upcoming = {}
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        
        for boat_id, records in self.maintenance_records.items():
            boat_upcoming = [
                record for record in records
                if today <= record.next_due_date <= end_date
            ]
            if boat_upcoming:
                upcoming[boat_id] = boat_upcoming
                
        return upcoming

    def create_reservation(
        self,
        customer_id: str,
        boat_id: str,
        start_date: datetime.date,
        end_date: datetime.date
    ) -> Reservation:
        """Create a new reservation for a boat."""
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found")
        
        if self.boats[boat_id]["status"] != BoatStatus.AVAILABLE.value:
            raise ValueError(f"Boat with ID {boat_id} is not available for reservation")
        
        # Check for overlapping reservations
        for reservation in self.reservations:
            if reservation.boat_id == boat_id:
                if not (end_date < reservation.start_date or start_date > reservation.end_date):
                    raise ValueError("Boat already reserved for the selected dates")
        
        reservation = Reservation(
            customer_id=customer_id,
            boat_id=boat_id,
            start_date=start_date,
            end_date=end_date
        )
        self.reservations.append(reservation)
        self.boats[boat_id]["status"] = BoatStatus.RESERVED.value
        return reservation

    def cancel_reservation(self, reservation_id: str) -> None:
        """Cancel an existing reservation."""
        reservation = next(
            (r for r in self.reservations if r.customer_id == reservation_id),
            None
        )
        if not reservation:
            raise ValueError(f"Reservation with ID {reservation_id} not found")
        
        self.reservations.remove(reservation)
        self.boats[reservation.boat_id]["status"] = BoatStatus.AVAILABLE.value

    def get_available_boats(
        self,
        start_date: datetime.date,
        end_date: datetime.date,
        min_capacity: Optional[int] = None
    ) -> List[Dict]:
        """Get all boats available for the specified date range."""
        available_boats = []
        
        for boat_id, boat in self.boats.items():
            if boat["status"] != BoatStatus.AVAILABLE.value:
                continue
                
            if min_capacity and boat["capacity"] < min_capacity:
                continue
                
            # Check reservations
            is_available = True
            for reservation in self.reservations:
                if reservation.boat_id == boat_id:
                    if not (end_date < reservation.start_date or start_date > reservation.end_date):
                        is_available = False
                        break
            
            if is_available:
                available_boats.append({
                    "boat_id": boat_id,
                    "model": boat["model"],
                    "capacity": boat["capacity"],
                    "location": self.get_boat_location(boat_id)
                })
                
        return available_boats

    def get_boat_status(self, boat_id: str) -> str:
        """Get the current status of a boat."""
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found")
        return self.boats[boat_id]["status"]

    def set_boat_status(self, boat_id: str, status: BoatStatus) -> None:
        """Set the status of a boat."""
        if boat_id not in self.boats:
            raise ValueError(f"Boat with ID {boat_id} not found")
        self.boats[boat_id]["status"] = status.value
```
