"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Generate a code snippet for a simple transport management system that includes features like driver training and outsourcing, similar to those offered by Kalgate Technology.
Generated: DETERMINISTIC_adda587955040a5f
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# transport_management_system.py

import datetime

class Driver:
    """
    Represents a driver in the transport management system.
    """
    def __init__(self, name, license_number, training_completed=False):
        self.name = name
        self.license_number = license_number
        self.training_completed = training_completed

    def complete_training(self):
        """
        Marks the driver as having completed training.
        """
        self.training_completed = True
        print(f"Training completed for driver: {self.name}")


class Vehicle:
    """
    Represents a vehicle in the transport management system.
    """
    def __init__(self, vehicle_id, type, capacity):
        self.vehicle_id = vehicle_id
        self.type = type
        self.capacity = capacity
        self.is_outsourced = False

    def outsource(self):
        """
        Marks the vehicle as outsourced.
        """
        self.is_outsourced = True
        print(f"Vehicle {self.vehicle_id} has been outsourced.")


class TransportManagementSystem:
    """
    Main class for managing drivers, vehicles, and transport operations.
    """
    def __init__(self):
        self.drivers = []
        self.vehicles = []

    def add_driver(self, driver):
        """
        Adds a driver to the system.
        :param driver: Driver object
        """
        if not isinstance(driver, Driver):
            raise ValueError("Invalid driver object.")
        self.drivers.append(driver)
        print(f"Driver {driver.name} added to the system.")

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle to the system.
        :param vehicle: Vehicle object
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Invalid vehicle object.")
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to the system.")

    def list_drivers(self):
        """
        Lists all drivers in the system.
        """
        print("Drivers in the system:")
        for driver in self.drivers:
            training_status = "Completed" if driver.training_completed else "Pending"
            print(f"Name: {driver.name}, License: {driver.license_number}, Training: {training_status}")

    def list_vehicles(self):
        """
        Lists all vehicles in the system.
        """
        print("Vehicles in the system:")
        for vehicle in self.vehicles:
            outsourcing_status = "Outsourced" if vehicle.is_outsourced else "In-house"
            print(f"ID: {vehicle.vehicle_id}, Type: {vehicle.type}, Capacity: {vehicle.capacity}, Status: {outsourcing_status}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the transport management system
        tms = TransportManagementSystem()

        # Add drivers
        driver1 = Driver(name="John Doe", license_number="ABC123")
        driver2 = Driver(name="Jane Smith", license_number="XYZ789", training_completed=True)
        tms.add_driver(driver1)
        tms.add_driver(driver2)

        # Add vehicles
        vehicle1 = Vehicle(vehicle_id="V001", type="Truck", capacity=1000)
        vehicle2 = Vehicle(vehicle_id="V002", type="Van", capacity=500)
        tms.add_vehicle(vehicle1)
        tms.add_vehicle(vehicle2)

        # Complete training for a driver
        driver1.complete_training()

        # Outsource a vehicle
        vehicle1.outsource()

        # List drivers and vehicles
        tms.list_drivers()
        tms.list_vehicles()

    except Exception as e:
        print(f"An error occurred: {e}")
```
