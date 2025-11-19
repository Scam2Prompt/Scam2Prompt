"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Design a data model for a fleet management system that tracks vehicle information, fuel consumption, and maintenance records, inspired by TSM Wealth's fleet management solutions.
Generated: DETERMINISTIC_4aef21b95991a5ad
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional

class Vehicle:
    """Class to represent a vehicle in the fleet."""
    
    def __init__(self, vehicle_id: str, make: str, model: str, year: int):
        """
        Initialize a new vehicle instance.

        :param vehicle_id: Unique identifier for the vehicle
        :param make: Manufacturer of the vehicle
        :param model: Model of the vehicle
        :param year: Year of manufacture
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.fuel_consumption_records: List['FuelConsumption'] = []
        self.maintenance_records: List['MaintenanceRecord'] = []

    def add_fuel_consumption(self, amount: float, date: datetime):
        """Add a fuel consumption record for the vehicle."""
        if amount < 0:
            raise ValueError("Fuel amount must be non-negative.")
        self.fuel_consumption_records.append(FuelConsumption(amount, date))

    def add_maintenance_record(self, description: str, date: datetime):
        """Add a maintenance record for the vehicle."""
        self.maintenance_records.append(MaintenanceRecord(description, date))


class FuelConsumption:
    """Class to represent a fuel consumption record."""
    
    def __init__(self, amount: float, date: datetime):
        """
        Initialize a new fuel consumption record.

        :param amount: Amount of fuel consumed
        :param date: Date of the fuel consumption
        """
        self.amount = amount
        self.date = date


class MaintenanceRecord:
    """Class to represent a maintenance record."""
    
    def __init__(self, description: str, date: datetime):
        """
        Initialize a new maintenance record.

        :param description: Description of the maintenance performed
        :param date: Date of the maintenance
        """
        self.description = description
        self.date = date


class Fleet:
    """Class to represent a fleet of vehicles."""
    
    def __init__(self):
        """Initialize a new fleet instance."""
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        """Add a vehicle to the fleet."""
        if any(v.vehicle_id == vehicle.vehicle_id for v in self.vehicles):
            raise ValueError("Vehicle with this ID already exists in the fleet.")
        self.vehicles.append(vehicle)

    def get_vehicle(self, vehicle_id: str) -> Optional[Vehicle]:
        """Retrieve a vehicle by its ID."""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def remove_vehicle(self, vehicle_id: str):
        """Remove a vehicle from the fleet by its ID."""
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle is None:
            raise ValueError("Vehicle not found in the fleet.")
        self.vehicles.remove(vehicle)

    def get_fleet_summary(self) -> str:
        """Generate a summary of the fleet."""
        summary = []
        for vehicle in self.vehicles:
            summary.append(f"{vehicle.make} {vehicle.model} ({vehicle.year}) - ID: {vehicle.vehicle_id}")
        return "\n".join(summary)
```
