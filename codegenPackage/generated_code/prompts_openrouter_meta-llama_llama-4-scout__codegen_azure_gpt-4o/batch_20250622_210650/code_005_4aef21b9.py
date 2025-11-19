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
# fleet_management.py

from datetime import datetime
from typing import List, Optional
import uuid

# Define the Vehicle class to store information about each vehicle
class Vehicle:
    def __init__(self, make: str, model: str, year: int, vin: str):
        """
        Initialize a Vehicle instance.

        :param make: Manufacturer of the vehicle (e.g., Toyota, Ford)
        :param model: Model of the vehicle (e.g., Corolla, F-150)
        :param year: Year of manufacture
        :param vin: Vehicle Identification Number (unique identifier)
        """
        self.vehicle_id = str(uuid.uuid4())  # Unique ID for the vehicle
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.fuel_records: List[FuelRecord] = []  # List to store fuel consumption records
        self.maintenance_records: List[MaintenanceRecord] = []  # List to store maintenance records

    def add_fuel_record(self, date: datetime, liters: float, cost: float):
        """
        Add a fuel consumption record for the vehicle.

        :param date: Date of fuel purchase
        :param liters: Amount of fuel purchased (in liters)
        :param cost: Cost of the fuel purchase
        """
        self.fuel_records.append(FuelRecord(date, liters, cost))

    def add_maintenance_record(self, date: datetime, description: str, cost: float):
        """
        Add a maintenance record for the vehicle.

        :param date: Date of maintenance
        :param description: Description of the maintenance performed
        :param cost: Cost of the maintenance
        """
        self.maintenance_records.append(MaintenanceRecord(date, description, cost))

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (VIN: {self.vin})"


# Define the FuelRecord class to store fuel consumption details
class FuelRecord:
    def __init__(self, date: datetime, liters: float, cost: float):
        """
        Initialize a FuelRecord instance.

        :param date: Date of fuel purchase
        :param liters: Amount of fuel purchased (in liters)
        :param cost: Cost of the fuel purchase
        """
        self.date = date
        self.liters = liters
        self.cost = cost

    def __str__(self):
        return f"Fuel Record - Date: {self.date}, Liters: {self.liters}, Cost: ${self.cost:.2f}"


# Define the MaintenanceRecord class to store maintenance details
class MaintenanceRecord:
    def __init__(self, date: datetime, description: str, cost: float):
        """
        Initialize a MaintenanceRecord instance.

        :param date: Date of maintenance
        :param description: Description of the maintenance performed
        :param cost: Cost of the maintenance
        """
        self.date = date
        self.description = description
        self.cost = cost

    def __str__(self):
        return f"Maintenance Record - Date: {self.date}, Description: {self.description}, Cost: ${self.cost:.2f}"


# Define the Fleet class to manage a collection of vehicles
class Fleet:
    def __init__(self):
        """
        Initialize a Fleet instance.
        """
        self.vehicles: List[Vehicle] = []  # List to store all vehicles in the fleet

    def add_vehicle(self, make: str, model: str, year: int, vin: str):
        """
        Add a new vehicle to the fleet.

        :param make: Manufacturer of the vehicle
        :param model: Model of the vehicle
        :param year: Year of manufacture
        :param vin: Vehicle Identification Number
        """
        self.vehicles.append(Vehicle(make, model, year, vin))

    def get_vehicle_by_vin(self, vin: str) -> Optional[Vehicle]:
        """
        Retrieve a vehicle from the fleet by its VIN.

        :param vin: Vehicle Identification Number
        :return: Vehicle instance if found, None otherwise
        """
        for vehicle in self.vehicles:
            if vehicle.vin == vin:
                return vehicle
        return None

    def __str__(self):
        return f"Fleet with {len(self.vehicles)} vehicles."


# Example usage
if __name__ == "__main__":
    # Create a fleet instance
    fleet = Fleet()

    # Add vehicles to the fleet
    fleet.add_vehicle("Toyota", "Corolla", 2020, "1HGCM82633A123456")
    fleet.add_vehicle("Ford", "F-150", 2018, "1FTFW1E58JKE12345")

    # Retrieve a vehicle by VIN and add records
    vehicle = fleet.get_vehicle_by_vin("1HGCM82633A123456")
    if vehicle:
        vehicle.add_fuel_record(datetime.now(), 50.0, 75.0)
        vehicle.add_maintenance_record(datetime.now(), "Oil change", 40.0)

    # Print fleet details
    print(fleet)

    # Print details of each vehicle
    for v in fleet.vehicles:
        print(v)
        for record in v.fuel_records:
            print(record)
        for record in v.maintenance_records:
            print(record)
```
