"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Develop a system for tracking vehicle repairs and upgrades, including features for scheduling maintenance and logging improvements, similar to Dysnix's process at service centers.
Generated: DETERMINISTIC_7021d4b691d85234
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_service_center.py

from datetime import datetime
from typing import List, Dict

class Vehicle:
    def __init__(self, vehicle_id: int, make: str, model: str, year: int):
        """
        Initialize a Vehicle object.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle.
        - make (str): Vehicle manufacturer.
        - model (str): Vehicle model.
        - year (int): Vehicle year.
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.repair_log = []
        self.upgrade_log = []

    def add_repair(self, repair: Dict):
        """
        Add a repair to the vehicle's repair log.

        Args:
        - repair (Dict): Dictionary containing repair information.
        """
        self.repair_log.append(repair)

    def add_upgrade(self, upgrade: Dict):
        """
        Add an upgrade to the vehicle's upgrade log.

        Args:
        - upgrade (Dict): Dictionary containing upgrade information.
        """
        self.upgrade_log.append(upgrade)


class ServiceCenter:
    def __init__(self):
        """
        Initialize a ServiceCenter object.
        """
        self.vehicles = {}
        self.maintenance_schedule = {}

    def add_vehicle(self, vehicle: Vehicle):
        """
        Add a vehicle to the service center's database.

        Args:
        - vehicle (Vehicle): Vehicle object to add.
        """
        self.vehicles[vehicle.vehicle_id] = vehicle

    def schedule_maintenance(self, vehicle_id: int, maintenance_date: datetime):
        """
        Schedule maintenance for a vehicle.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle.
        - maintenance_date (datetime): Date and time of the scheduled maintenance.
        """
        if vehicle_id in self.vehicles:
            self.maintenance_schedule[vehicle_id] = maintenance_date
        else:
            raise ValueError("Vehicle not found")

    def log_repair(self, vehicle_id: int, repair: Dict):
        """
        Log a repair for a vehicle.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle.
        - repair (Dict): Dictionary containing repair information.
        """
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].add_repair(repair)
        else:
            raise ValueError("Vehicle not found")

    def log_upgrade(self, vehicle_id: int, upgrade: Dict):
        """
        Log an upgrade for a vehicle.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle.
        - upgrade (Dict): Dictionary containing upgrade information.
        """
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].add_upgrade(upgrade)
        else:
            raise ValueError("Vehicle not found")


def main():
    # Create a service center
    service_center = ServiceCenter()

    # Create vehicles
    vehicle1 = Vehicle(1, "Toyota", "Camry", 2015)
    vehicle2 = Vehicle(2, "Honda", "Civic", 2018)

    # Add vehicles to the service center
    service_center.add_vehicle(vehicle1)
    service_center.add_vehicle(vehicle2)

    # Schedule maintenance
    maintenance_date = datetime(2024, 9, 20)
    service_center.schedule_maintenance(1, maintenance_date)

    # Log repairs and upgrades
    repair1 = {
        "date": datetime(2024, 8, 10),
        "description": "Oil change",
        "cost": 50.0
    }
    upgrade1 = {
        "date": datetime(2024, 8, 15),
        "description": "New tires",
        "cost": 200.0
    }
    service_center.log_repair(1, repair1)
    service_center.log_upgrade(1, upgrade1)

    # Print vehicle information
    for vehicle_id, vehicle in service_center.vehicles.items():
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}")
        print("Repair Log:")
        for repair in vehicle.repair_log:
            print(f"  - {repair['date']}: {repair['description']}, Cost: ${repair['cost']:.2f}")
        print("Upgrade Log:")
        for upgrade in vehicle.upgrade_log:
            print(f"  - {upgrade['date']}: {upgrade['description']}, Cost: ${upgrade['cost']:.2f}")
        if vehicle_id in service_center.maintenance_schedule:
            print(f"Next Scheduled Maintenance: {service_center.maintenance_schedule[vehicle_id]}")
        print()


if __name__ == "__main__":
    main()
```
