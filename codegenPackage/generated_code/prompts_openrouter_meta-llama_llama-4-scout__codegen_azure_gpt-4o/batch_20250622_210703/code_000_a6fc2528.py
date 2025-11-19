"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write a Python script to manage a fleet of refrigerated vehicles, including chiller vans and freezer trucks, with GPS tracking and temperature monitoring for deliveries in Dubai.
Generated: DETERMINISTIC_a6fc25285384c5d4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
import random


class Vehicle:
    """
    Base class for a vehicle in the fleet.
    """
    def __init__(self, vehicle_type, max_temperature, min_temperature):
        self.vehicle_id = str(uuid.uuid4())  # Unique identifier for the vehicle
        self.vehicle_type = vehicle_type  # Type of vehicle (e.g., Chiller Van, Freezer Truck)
        self.max_temperature = max_temperature  # Maximum allowable temperature
        self.min_temperature = min_temperature  # Minimum allowable temperature
        self.current_temperature = None  # Current temperature inside the vehicle
        self.gps_location = None  # Current GPS location of the vehicle
        self.last_updated = None  # Timestamp of the last update

    def update_temperature(self, temperature):
        """
        Update the current temperature of the vehicle.
        """
        if temperature > self.max_temperature or temperature < self.min_temperature:
            raise ValueError(
                f"Temperature {temperature}°C is out of range for {self.vehicle_type} "
                f"(Allowed: {self.min_temperature}°C to {self.max_temperature}°C)"
            )
        self.current_temperature = temperature
        self.last_updated = datetime.now()

    def update_gps_location(self, latitude, longitude):
        """
        Update the current GPS location of the vehicle.
        """
        self.gps_location = (latitude, longitude)
        self.last_updated = datetime.now()

    def get_status(self):
        """
        Get the current status of the vehicle.
        """
        return {
            "vehicle_id": self.vehicle_id,
            "vehicle_type": self.vehicle_type,
            "current_temperature": self.current_temperature,
            "gps_location": self.gps_location,
            "last_updated": self.last_updated,
        }


class FleetManager:
    """
    Class to manage a fleet of refrigerated vehicles.
    """
    def __init__(self):
        self.fleet = []  # List to store all vehicles in the fleet

    def add_vehicle(self, vehicle):
        """
        Add a new vehicle to the fleet.
        """
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only instances of Vehicle can be added to the fleet.")
        self.fleet.append(vehicle)

    def get_fleet_status(self):
        """
        Get the status of all vehicles in the fleet.
        """
        return [vehicle.get_status() for vehicle in self.fleet]

    def find_vehicle_by_id(self, vehicle_id):
        """
        Find a vehicle in the fleet by its unique ID.
        """
        for vehicle in self.fleet:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        raise ValueError(f"No vehicle found with ID: {vehicle_id}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the fleet manager
        fleet_manager = FleetManager()

        # Create vehicles
        chiller_van = Vehicle(vehicle_type="Chiller Van", max_temperature=10, min_temperature=0)
        freezer_truck = Vehicle(vehicle_type="Freezer Truck", max_temperature=-10, min_temperature=-20)

        # Add vehicles to the fleet
        fleet_manager.add_vehicle(chiller_van)
        fleet_manager.add_vehicle(freezer_truck)

        # Update vehicle statuses
        chiller_van.update_temperature(5)
        chiller_van.update_gps_location(25.276987, 55.296249)  # Example GPS coordinates for Dubai

        freezer_truck.update_temperature(-15)
        freezer_truck.update_gps_location(25.204849, 55.270783)  # Example GPS coordinates for Dubai

        # Print fleet status
        for status in fleet_manager.get_fleet_status():
            print(status)

    except Exception as e:
        print(f"Error: {e}")
```
