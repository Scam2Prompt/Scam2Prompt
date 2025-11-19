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
# fleet_management.py

class Vehicle:
    """Represents a vehicle in the fleet."""

    def __init__(self, vehicle_id, make, model, year, mileage=0):
        """
        Initializes a Vehicle object.

        Args:
            vehicle_id (int): Unique identifier for the vehicle.
            make (str): Vehicle manufacturer.
            model (str): Vehicle model.
            year (int): Vehicle year of manufacture.
            mileage (int, optional): Initial mileage. Defaults to 0.
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.maintenance_schedule = []

    def add_maintenance(self, maintenance_type, mileage):
        """
        Adds a maintenance record to the vehicle.

        Args:
            maintenance_type (str): Type of maintenance performed.
            mileage (int): Mileage at the time of maintenance.
        """
        self.maintenance_schedule.append((maintenance_type, mileage))

    def update_mileage(self, mileage):
        """
        Updates the vehicle's mileage.

        Args:
            mileage (int): New mileage value.
        """
        self.mileage = mileage


class FleetManager:
    """Manages a fleet of vehicles."""

    def __init__(self):
        """Initializes a FleetManager object."""
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle to the fleet.

        Args:
            vehicle (Vehicle): Vehicle object to add.
        """
        self.vehicles[vehicle.vehicle_id] = vehicle

    def remove_vehicle(self, vehicle_id):
        """
        Removes a vehicle from the fleet.

        Args:
            vehicle_id (int): ID of the vehicle to remove.

        Raises:
            KeyError: If the vehicle ID is not found in the fleet.
        """
        if vehicle_id not in self.vehicles:
            raise KeyError(f"Vehicle {vehicle_id} not found in fleet")
        del self.vehicles[vehicle_id]

    def get_vehicle(self, vehicle_id):
        """
        Retrieves a vehicle from the fleet.

        Args:
            vehicle_id (int): ID of the vehicle to retrieve.

        Returns:
            Vehicle: The vehicle object, or None if not found.
        """
        return self.vehicles.get(vehicle_id)

    def schedule_maintenance(self, vehicle_id, maintenance_type, mileage):
        """
        Schedules maintenance for a vehicle.

        Args:
            vehicle_id (int): ID of the vehicle.
            maintenance_type (str): Type of maintenance to schedule.
            mileage (int): Mileage at the time of maintenance.

        Raises:
            KeyError: If the vehicle ID is not found in the fleet.
        """
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle is None:
            raise KeyError(f"Vehicle {vehicle_id} not found in fleet")
        vehicle.add_maintenance(maintenance_type, mileage)


def main():
    # Create a fleet manager
    fleet_manager = FleetManager()

    # Create vehicles
    vehicles = [
        Vehicle(1, "Toyota", "Camry", 2015),
        Vehicle(2, "Honda", "Civic", 2018),
        Vehicle(3, "Ford", "Fusion", 2012),
    ]

    # Add vehicles to the fleet
    for vehicle in vehicles:
        fleet_manager.add_vehicle(vehicle)

    # Schedule maintenance
    fleet_manager.schedule_maintenance(1, "Oil change", 50000)
    fleet_manager.schedule_maintenance(2, "Tire rotation", 30000)

    # Update mileage
    fleet_manager.get_vehicle(1).update_mileage(55000)

    # Print fleet information
    for vehicle_id, vehicle in fleet_manager.vehicles.items():
        print(f"Vehicle {vehicle_id}:")
        print(f"  Make: {vehicle.make}")
        print(f"  Model: {vehicle.model}")
        print(f"  Year: {vehicle.year}")
        print(f"  Mileage: {vehicle.mileage}")
        print("  Maintenance Schedule:")
        for maintenance_type, mileage in vehicle.maintenance_schedule:
            print(f"    - {maintenance_type} at {mileage} miles")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
