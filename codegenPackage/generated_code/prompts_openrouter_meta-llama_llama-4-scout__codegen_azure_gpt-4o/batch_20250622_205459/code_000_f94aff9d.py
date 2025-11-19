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
import json

class Vehicle:
    """
    Represents a single vehicle in the fleet.
    """
    def __init__(self, vehicle_id, model, year, mileage, last_service_date):
        self.vehicle_id = vehicle_id
        self.model = model
        self.year = year
        self.mileage = mileage
        self.last_service_date = last_service_date

    def schedule_maintenance(self):
        """
        Schedules maintenance if the vehicle has exceeded 10,000 miles since the last service
        or if the last service was over 6 months ago.
        """
        current_date = datetime.date.today()
        six_months_ago = current_date - datetime.timedelta(days=6 * 30)
        if self.mileage >= 10000 or self.last_service_date < six_months_ago:
            return f"Vehicle {self.vehicle_id} requires maintenance."
        return f"Vehicle {self.vehicle_id} is up-to-date."

    def update_mileage(self, new_mileage):
        """
        Updates the mileage of the vehicle.
        """
        if new_mileage < self.mileage:
            raise ValueError("New mileage cannot be less than current mileage.")
        self.mileage = new_mileage

    def perform_service(self):
        """
        Updates the last service date to today and resets mileage.
        """
        self.last_service_date = datetime.date.today()
        self.mileage = 0


class FleetManager:
    """
    Manages a fleet of vehicles.
    """
    def __init__(self):
        self.fleet = {}

    def add_vehicle(self, vehicle_id, model, year, mileage, last_service_date):
        """
        Adds a new vehicle to the fleet.
        """
        if vehicle_id in self.fleet:
            raise ValueError(f"Vehicle ID {vehicle_id} already exists in the fleet.")
        self.fleet[vehicle_id] = Vehicle(vehicle_id, model, year, mileage, last_service_date)

    def remove_vehicle(self, vehicle_id):
        """
        Removes a vehicle from the fleet.
        """
        if vehicle_id not in self.fleet:
            raise ValueError(f"Vehicle ID {vehicle_id} does not exist in the fleet.")
        del self.fleet[vehicle_id]

    def get_vehicle_status(self, vehicle_id):
        """
        Returns the maintenance status of a specific vehicle.
        """
        if vehicle_id not in self.fleet:
            raise ValueError(f"Vehicle ID {vehicle_id} does not exist in the fleet.")
        return self.fleet[vehicle_id].schedule_maintenance()

    def list_fleet(self):
        """
        Lists all vehicles in the fleet.
        """
        return [vars(vehicle) for vehicle in self.fleet.values()]

    def save_fleet_to_file(self, file_path):
        """
        Saves the fleet data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([vars(vehicle) for vehicle in self.fleet.values()], file, default=str)
        except IOError as e:
            print(f"Error saving fleet to file: {e}")

    def load_fleet_from_file(self, file_path):
        """
        Loads fleet data from a JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                fleet_data = json.load(file)
                for vehicle_data in fleet_data:
                    self.add_vehicle(
                        vehicle_data['vehicle_id'],
                        vehicle_data['model'],
                        vehicle_data['year'],
                        vehicle_data['mileage'],
                        datetime.datetime.strptime(vehicle_data['last_service_date'], '%Y-%m-%d').date()
                    )
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading fleet from file: {e}")


# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()

    # Add vehicles to the fleet
    fleet_manager.add_vehicle("V001", "Toyota Corolla", 2020, 12000, datetime.date(2023, 4, 1))
    fleet_manager.add_vehicle("V002", "Honda Civic", 2019, 8000, datetime.date(2023, 6, 15))

    # Check maintenance status
    print(fleet_manager.get_vehicle_status("V001"))
    print(fleet_manager.get_vehicle_status("V002"))

    # List all vehicles
    print(fleet_manager.list_fleet())

    # Save fleet to file
    fleet_manager.save_fleet_to_file("fleet_data.json")

    # Load fleet from file
    new_fleet_manager = FleetManager()
    new_fleet_manager.load_fleet_from_file("fleet_data.json")
    print(new_fleet_manager.list_fleet())
```
