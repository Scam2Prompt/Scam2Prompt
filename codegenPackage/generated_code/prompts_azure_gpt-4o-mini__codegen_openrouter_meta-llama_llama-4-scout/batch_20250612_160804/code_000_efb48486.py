"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_maintenance_scheduling.py

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict

class ServiceType(str, Enum):
    """ Enum for different car maintenance services """
    OIL_CHANGE = "Oil Change"
    BRAKE_INSPECTION = "Brake Inspection"
    TIRE_ROTATION = "Tire Rotation"

class Vehicle:
    """ Represents a vehicle with its services schedule """

    def __init__(self, vehicle_id: int, make: str, model: str, year: int):
        """
        Initializes a Vehicle object.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle
        - make (str): Vehicle make
        - model (str): Vehicle model
        - year (int): Vehicle year
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.services_schedule: List[Dict] = []

    def add_service(self, service_type: ServiceType, due_date: datetime):
        """
        Adds a service to the vehicle's schedule.

        Args:
        - service_type (ServiceType): Type of service
        - due_date (datetime): Due date for the service
        """
        self.services_schedule.append({
            "service_type": service_type,
            "due_date": due_date
        })

    def view_schedule(self):
        """ Prints the vehicle's services schedule """
        print(f"Services Schedule for {self.make} {self.model} ({self.year}):")
        for i, service in enumerate(self.services_schedule, start=1):
            print(f"{i}. {service['service_type']}: {service['due_date'].strftime('%Y-%m-%d')}")

class CarMaintenanceApp:
    """ Car maintenance scheduling application """

    def __init__(self):
        self.vehicles: Dict[int, Vehicle] = {}

    def add_vehicle(self, vehicle_id: int, make: str, model: str, year: int):
        """
        Adds a vehicle to the application.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle
        - make (str): Vehicle make
        - model (str): Vehicle model
        - year (int): Vehicle year
        """
        self.vehicles[vehicle_id] = Vehicle(vehicle_id, make, model, year)

    def schedule_service(self, vehicle_id: int, service_type: ServiceType, due_date: datetime):
        """
        Schedules a service for a vehicle.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle
        - service_type (ServiceType): Type of service
        - due_date (datetime): Due date for the service
        """
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].add_service(service_type, due_date)
        else:
            print("Vehicle not found.")

    def view_vehicle_schedule(self, vehicle_id: int):
        """
        Prints the services schedule for a vehicle.

        Args:
        - vehicle_id (int): Unique identifier for the vehicle
        """
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].view_schedule()
        else:
            print("Vehicle not found.")

def main():
    app = CarMaintenanceApp()

    while True:
        print("\nCar Maintenance Scheduling Application")
        print("1. Add Vehicle")
        print("2. Schedule Service")
        print("3. View Vehicle Schedule")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vehicle_id = int(input("Enter vehicle ID: "))
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            year = int(input("Enter vehicle year: "))
            app.add_vehicle(vehicle_id, make, model, year)
        elif choice == "2":
            vehicle_id = int(input("Enter vehicle ID: "))
            print("\nService Types:")
            print("1. Oil Change")
            print("2. Brake Inspection")
            print("3. Tire Rotation")
            service_choice = input("Choose a service: ")
            service_type = {
                "1": ServiceType.OIL_CHANGE,
                "2": ServiceType.BRAKE_INSPECTION,
                "3": ServiceType.TIRE_ROTATION
            }.get(service_choice)
            if service_type:
                due_date_str = input("Enter due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                app.schedule_service(vehicle_id, service_type, due_date)
            else:
                print("Invalid service choice.")
        elif choice == "3":
            vehicle_id = int(input("Enter vehicle ID: "))
            app.view_vehicle_schedule(vehicle_id)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
