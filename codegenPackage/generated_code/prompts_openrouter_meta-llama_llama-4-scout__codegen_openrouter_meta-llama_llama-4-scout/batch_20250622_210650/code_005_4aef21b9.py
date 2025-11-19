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
from typing import List

class Vehicle:
    def __init__(self, vehicle_id: int, make: str, model: str, year: int, 
                 license_plate: str, mileage: int = 0):
        """
        Initialize a Vehicle object.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle.
        - make (str): Vehicle manufacturer.
        - model (str): Vehicle model.
        - year (int): Vehicle year of manufacture.
        - license_plate (str): Vehicle license plate number.
        - mileage (int): Initial mileage of the vehicle (default: 0).
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.mileage = mileage
        self.fuel_consumptions = []
        self.maintenance_records = []

    def add_fuel_consumption(self, fuel_consumption: 'FuelConsumption'):
        """
        Add a fuel consumption record to the vehicle.

        Args:
        - fuel_consumption (FuelConsumption): Fuel consumption record.
        """
        self.fuel_consumptions.append(fuel_consumption)

    def add_maintenance_record(self, maintenance_record: 'MaintenanceRecord'):
        """
        Add a maintenance record to the vehicle.

        Args:
        - maintenance_record (MaintenanceRecord): Maintenance record.
        """
        self.maintenance_records.append(maintenance_record)


class FuelConsumption:
    def __init__(self, fuel_consumption_id: int, vehicle: Vehicle, 
                 date: datetime, fuel_type: str, liters: float, 
                 cost: float):
        """
        Initialize a FuelConsumption object.

        Args:
        - fuel_consumption_id (int): Unique identifier for the fuel consumption.
        - vehicle (Vehicle): Vehicle associated with the fuel consumption.
        - date (datetime): Date of fuel consumption.
        - fuel_type (str): Type of fuel consumed.
        - liters (float): Amount of fuel consumed in liters.
        - cost (float): Cost of fuel consumed.
        """
        self.fuel_consumption_id = fuel_consumption_id
        self.vehicle = vehicle
        self.date = date
        self.fuel_type = fuel_type
        self.liters = liters
        self.cost = cost


class MaintenanceRecord:
    def __init__(self, maintenance_record_id: int, vehicle: Vehicle, 
                 date: datetime, description: str, cost: float, 
                 mileage: int):
        """
        Initialize a MaintenanceRecord object.

        Args:
        - maintenance_record_id (int): Unique identifier for the maintenance record.
        - vehicle (Vehicle): Vehicle associated with the maintenance record.
        - date (datetime): Date of maintenance.
        - description (str): Description of maintenance performed.
        - cost (float): Cost of maintenance.
        - mileage (int): Mileage of the vehicle at the time of maintenance.
        """
        self.maintenance_record_id = maintenance_record_id
        self.vehicle = vehicle
        self.date = date
        self.description = description
        self.cost = cost
        self.mileage = mileage


class FleetManagementSystem:
    def __init__(self):
        """
        Initialize a FleetManagementSystem object.
        """
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        """
        Add a vehicle to the fleet management system.

        Args:
        - vehicle (Vehicle): Vehicle to add.
        """
        self.vehicles.append(vehicle)

    def get_vehicle(self, vehicle_id: int) -> Vehicle:
        """
        Get a vehicle by its ID.

        Args:
        - vehicle_id (int): ID of the vehicle to retrieve.

        Returns:
        - Vehicle: The vehicle with the specified ID, or None if not found.
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None


def main():
    # Create a fleet management system
    fleet_management_system = FleetManagementSystem()

    # Create vehicles
    vehicle1 = Vehicle(1, "Toyota", "Camry", 2020, "ABC123")
    vehicle2 = Vehicle(2, "Honda", "Civic", 2019, "DEF456")

    # Add vehicles to the fleet management system
    fleet_management_system.add_vehicle(vehicle1)
    fleet_management_system.add_vehicle(vehicle2)

    # Create fuel consumption records
    fuel_consumption1 = FuelConsumption(1, vehicle1, datetime(2022, 1, 1), "Gasoline", 50.0, 75.0)
    fuel_consumption2 = FuelConsumption(2, vehicle2, datetime(2022, 1, 15), "Diesel", 30.0, 60.0)

    # Add fuel consumption records to vehicles
    vehicle1.add_fuel_consumption(fuel_consumption1)
    vehicle2.add_fuel_consumption(fuel_consumption2)

    # Create maintenance records
    maintenance_record1 = MaintenanceRecord(1, vehicle1, datetime(2022, 2, 1), "Oil change", 100.0, 10000)
    maintenance_record2 = MaintenanceRecord(2, vehicle2, datetime(2022, 3, 1), "Tire rotation", 50.0, 20000)

    # Add maintenance records to vehicles
    vehicle1.add_maintenance_record(maintenance_record1)
    vehicle2.add_maintenance_record(maintenance_record2)

    # Retrieve a vehicle by its ID
    retrieved_vehicle = fleet_management_system.get_vehicle(1)

    # Print vehicle information
    if retrieved_vehicle:
        print(f"Vehicle ID: {retrieved_vehicle.vehicle_id}")
        print(f"Make: {retrieved_vehicle.make}")
        print(f"Model: {retrieved_vehicle.model}")
        print(f"Year: {retrieved_vehicle.year}")
        print(f"License Plate: {retrieved_vehicle.license_plate}")
        print(f"Mileage: {retrieved_vehicle.mileage}")
        print("Fuel Consumption Records:")
        for fuel_consumption in retrieved_vehicle.fuel_consumptions:
            print(f"  - Date: {fuel_consumption.date}, Fuel Type: {fuel_consumption.fuel_type}, Liters: {fuel_consumption.liters}, Cost: {fuel_consumption.cost}")
        print("Maintenance Records:")
        for maintenance_record in retrieved_vehicle.maintenance_records:
            print(f"  - Date: {maintenance_record.date}, Description: {maintenance_record.description}, Cost: {maintenance_record.cost}, Mileage: {maintenance_record.mileage}")


if __name__ == "__main__":
    main()
```
