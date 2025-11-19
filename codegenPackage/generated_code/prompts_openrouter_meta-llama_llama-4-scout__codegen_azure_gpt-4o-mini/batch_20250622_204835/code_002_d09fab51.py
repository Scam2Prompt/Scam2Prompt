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
from typing import List, Dict, Optional

class Boat:
    """Class representing a boat in the fleet."""
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.location: Optional[str] = None
        self.maintenance_schedule: List[datetime.date] = []
        self.reservations: List[Dict] = []

    def update_location(self, new_location: str):
        """Update the boat's current location."""
        self.location = new_location

    def schedule_maintenance(self, date: datetime.date):
        """Schedule maintenance for the boat."""
        if date not in self.maintenance_schedule:
            self.maintenance_schedule.append(date)
        else:
            raise ValueError("Maintenance date already scheduled.")

    def add_reservation(self, customer_name: str, start_date: datetime.date, end_date: datetime.date):
        """Add a reservation for the boat."""
        reservation = {
            "customer_name": customer_name,
            "start_date": start_date,
            "end_date": end_date
        }
        self.reservations.append(reservation)

class FleetManager:
    """Class to manage a fleet of boats."""
    
    def __init__(self):
        self.boats: Dict[str, Boat] = {}

    def add_boat(self, boat: Boat):
        """Add a new boat to the fleet."""
        if boat.id in self.boats:
            raise ValueError("Boat with this ID already exists.")
        self.boats[boat.id] = boat

    def get_boat(self, boat_id: str) -> Optional[Boat]:
        """Retrieve a boat by its ID."""
        return self.boats.get(boat_id)

    def track_boat_location(self, boat_id: str) -> Optional[str]:
        """Track the current location of a boat."""
        boat = self.get_boat(boat_id)
        if boat:
            return boat.location
        else:
            raise ValueError("Boat not found.")

    def get_maintenance_schedule(self, boat_id: str) -> List[datetime.date]:
        """Get the maintenance schedule for a boat."""
        boat = self.get_boat(boat_id)
        if boat:
            return boat.maintenance_schedule
        else:
            raise ValueError("Boat not found.")

    def get_reservations(self, boat_id: str) -> List[Dict]:
        """Get the reservations for a boat."""
        boat = self.get_boat(boat_id)
        if boat:
            return boat.reservations
        else:
            raise ValueError("Boat not found.")

# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()
    
    # Create and add boats to the fleet
    boat1 = Boat(id="B001", name="Wave Rider")
    fleet_manager.add_boat(boat1)

    # Update location
    boat1.update_location("Marina Bay")

    # Schedule maintenance
    try:
        boat1.schedule_maintenance(datetime.date(2023, 10, 15))
    except ValueError as e:
        print(e)

    # Add a reservation
    boat1.add_reservation("John Doe", datetime.date(2023, 10, 20), datetime.date(2023, 10, 22))

    # Track boat location
    print(f"Current location of {boat1.name}: {fleet_manager.track_boat_location('B001')}")

    # Get maintenance schedule
    print(f"Maintenance schedule for {boat1.name}: {fleet_manager.get_maintenance_schedule('B001')}")

    # Get reservations
    print(f"Reservations for {boat1.name}: {fleet_manager.get_reservations('B001')}")
```
