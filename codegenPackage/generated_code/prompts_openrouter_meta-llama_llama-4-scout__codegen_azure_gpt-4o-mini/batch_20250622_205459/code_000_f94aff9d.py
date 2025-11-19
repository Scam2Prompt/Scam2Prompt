"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a Python script to manage a fleet of 240 vehicles, including tracking and maintenance scheduling, inspired by Kalgate Technology's services.
Generated: DETERMINISTIC_f94aff9d4909a198
Batch ID: 20250622_205459
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

class Vehicle:
    """Class to represent a vehicle in the fleet."""
    
    def __init__(self, vehicle_id: str, model: str, last_service_date: Optional[datetime.date] = None):
        self.vehicle_id = vehicle_id
        self.model = model
        self.last_service_date = last_service_date or datetime.date.today()
        self.service_interval = datetime.timedelta(days=180)  # Service every 180 days

    def needs_service(self) -> bool:
        """Check if the vehicle needs service based on the last service date."""
        return datetime.date.today() - self.last_service_date >= self.service_interval

    def schedule_service(self):
        """Schedule a service for the vehicle."""
        self.last_service_date = datetime.date.today()
        print(f"Service scheduled for vehicle {self.vehicle_id} on {self.last_service_date}.")

class FleetManager:
    """Class to manage a fleet of vehicles."""
    
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """Add a vehicle to the fleet."""
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to the fleet.")

    def get_vehicles_needing_service(self) -> List[Vehicle]:
        """Return a list of vehicles that need service."""
        return [vehicle for vehicle in self.vehicles if vehicle.needs_service()]

    def schedule_maintenance(self):
        """Schedule maintenance for all vehicles that need it."""
        vehicles_needing_service = self.get_vehicles_needing_service()
        for vehicle in vehicles_needing_service:
            vehicle.schedule_service()

def main():
    """Main function to manage the fleet."""
    fleet_manager = FleetManager()

    # Example: Adding vehicles to the fleet
    for i in range(1, 241):
        vehicle = Vehicle(vehicle_id=f"V{i:03}", model=f"Model-{i}")
        fleet_manager.add_vehicle(vehicle)

    # Schedule maintenance for vehicles that need it
    fleet_manager.schedule_maintenance()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
