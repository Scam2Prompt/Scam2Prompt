"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: "Write a Python script to manage a fleet of vehicles using telematics, including GPS tracking and vehicle diagnostics."
Generated: DETERMINISTIC_f2a2675d9c303b45
Batch ID: 20250622_205459
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


class Vehicle:
    """
    Represents a vehicle in the fleet.
    Attributes:
        vehicle_id (str): Unique identifier for the vehicle.
        make (str): Manufacturer of the vehicle.
        model (str): Model of the vehicle.
        year (int): Year of manufacture.
        gps_location (tuple): Current GPS location (latitude, longitude).
        diagnostics (dict): Diagnostic data (e.g., fuel level, engine status).
    """

    def __init__(self, make, model, year):
        self.vehicle_id = str(uuid.uuid4())  # Generate a unique ID for the vehicle
        self.make = make
        self.model = model
        self.year = year
        self.gps_location = (0.0, 0.0)  # Default GPS location
        self.diagnostics = {
            "fuel_level": 100,  # Percentage
            "engine_status": "OK",  # Engine status
        }

    def update_gps_location(self, latitude, longitude):
        """
        Updates the GPS location of the vehicle.
        Args:
            latitude (float): Latitude of the new location.
            longitude (float): Longitude of the new location.
        """
        self.gps_location = (latitude, longitude)

    def update_diagnostics(self, key, value):
        """
        Updates a specific diagnostic parameter for the vehicle.
        Args:
            key (str): Diagnostic parameter to update.
            value: New value for the diagnostic parameter.
        """
        if key in self.diagnostics:
            self.diagnostics[key] = value
        else:
            raise KeyError(f"Invalid diagnostic key: {key}")

    def __str__(self):
        """
        Returns a string representation of the vehicle.
        """
        return f"Vehicle ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}"


class FleetManager:
    """
    Manages a fleet of vehicles.
    Attributes:
        fleet (dict): Dictionary of vehicles, keyed by vehicle ID.
    """

    def __init__(self):
        self.fleet = {}

    def add_vehicle(self, make, model, year):
        """
        Adds a new vehicle to the fleet.
        Args:
            make (str): Manufacturer of the vehicle.
            model (str): Model of the vehicle.
            year (int): Year of manufacture.
        Returns:
            Vehicle: The newly added vehicle.
        """
        vehicle = Vehicle(make, model, year)
        self.fleet[vehicle.vehicle_id] = vehicle
        return vehicle

    def remove_vehicle(self, vehicle_id):
        """
        Removes a vehicle from the fleet.
        Args:
            vehicle_id (str): ID of the vehicle to remove.
        """
        if vehicle_id in self.fleet:
            del self.fleet[vehicle_id]
        else:
            raise KeyError(f"Vehicle ID {vehicle_id} not found in fleet.")

    def get_vehicle(self, vehicle_id):
        """
        Retrieves a vehicle from the fleet.
        Args:
            vehicle_id (str): ID of the vehicle to retrieve.
        Returns:
            Vehicle: The requested vehicle.
        """
        if vehicle_id in self.fleet:
            return self.fleet[vehicle_id]
        else:
            raise KeyError(f"Vehicle ID {vehicle_id} not found in fleet.")

    def list_vehicles(self):
        """
        Lists all vehicles in the fleet.
        Returns:
            list: List of all vehicles in the fleet.
        """
        return list(self.fleet.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the fleet manager
        fleet_manager = FleetManager()

        # Add vehicles to the fleet
        vehicle1 = fleet_manager.add_vehicle("Toyota", "Camry", 2020)
        vehicle2 = fleet_manager.add_vehicle("Ford", "F-150", 2019)

        # Update GPS location for a vehicle
        vehicle1.update_gps_location(37.7749, -122.4194)

        # Update diagnostics for a vehicle
        vehicle2.update_diagnostics("fuel_level", 75)

        # List all vehicles in the fleet
        print("Fleet Vehicles:")
        for vehicle in fleet_manager.list_vehicles():
            print(vehicle)

        # Retrieve a specific vehicle
        retrieved_vehicle = fleet_manager.get_vehicle(vehicle1.vehicle_id)
        print("\nRetrieved Vehicle:")
        print(retrieved_vehicle)

        # Remove a vehicle from the fleet
        fleet_manager.remove_vehicle(vehicle2.vehicle_id)
        print("\nVehicle removed successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
