"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Write a Python script to manage bus routes and schedules for a transportation company like Autocares Cosme, including features for tracking punctuality and vehicle maintenance.
Generated: DETERMINISTIC_ab53557aecbc07f7
Batch ID: 20250622_212855
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


class BusRouteManager:
    """
    A class to manage bus routes, schedules, punctuality tracking, and vehicle maintenance.
    """

    def __init__(self):
        self.routes = {}  # Stores route information
        self.maintenance_records = {}  # Stores vehicle maintenance records
        self.punctuality_records = {}  # Stores punctuality tracking data

    def add_route(self, route_id, start_location, end_location, schedule):
        """
        Add a new bus route.

        :param route_id: Unique identifier for the route
        :param start_location: Starting point of the route
        :param end_location: Ending point of the route
        :param schedule: List of datetime objects representing the schedule
        """
        if route_id in self.routes:
            raise ValueError(f"Route ID {route_id} already exists.")
        self.routes[route_id] = {
            "start_location": start_location,
            "end_location": end_location,
            "schedule": schedule,
        }

    def update_schedule(self, route_id, new_schedule):
        """
        Update the schedule for an existing route.

        :param route_id: Unique identifier for the route
        :param new_schedule: List of datetime objects representing the new schedule
        """
        if route_id not in self.routes:
            raise ValueError(f"Route ID {route_id} does not exist.")
        self.routes[route_id]["schedule"] = new_schedule

    def record_punctuality(self, route_id, timestamp, is_on_time):
        """
        Record punctuality data for a route.

        :param route_id: Unique identifier for the route
        :param timestamp: Datetime object representing the timestamp of the record
        :param is_on_time: Boolean indicating whether the bus was on time
        """
        if route_id not in self.routes:
            raise ValueError(f"Route ID {route_id} does not exist.")
        if route_id not in self.punctuality_records:
            self.punctuality_records[route_id] = []
        self.punctuality_records[route_id].append({"timestamp": timestamp, "on_time": is_on_time})

    def add_maintenance_record(self, vehicle_id, date, description):
        """
        Add a maintenance record for a vehicle.

        :param vehicle_id: Unique identifier for the vehicle
        :param date: Datetime object representing the date of maintenance
        :param description: Description of the maintenance performed
        """
        if vehicle_id not in self.maintenance_records:
            self.maintenance_records[vehicle_id] = []
        self.maintenance_records[vehicle_id].append({"date": date, "description": description})

    def save_data_to_file(self, filename):
        """
        Save all data to a JSON file.

        :param filename: Name of the file to save data to
        """
        data = {
            "routes": self.routes,
            "punctuality_records": self.punctuality_records,
            "maintenance_records": self.maintenance_records,
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, default=str, indent=4)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, filename):
        """
        Load data from a JSON file.

        :param filename: Name of the file to load data from
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.routes = data.get("routes", {})
                self.punctuality_records = data.get("punctuality_records", {})
                self.maintenance_records = data.get("maintenance_records", {})
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = BusRouteManager()

    # Add a route
    manager.add_route(
        route_id="R001",
        start_location="Station A",
        end_location="Station B",
        schedule=[
            datetime.datetime(2023, 10, 1, 8, 0),
            datetime.datetime(2023, 10, 1, 12, 0),
            datetime.datetime(2023, 10, 1, 16, 0),
        ],
    )

    # Record punctuality
    manager.record_punctuality("R001", datetime.datetime(2023, 10, 1, 8, 0), True)

    # Add maintenance record
    manager.add_maintenance_record("Bus001", datetime.datetime(2023, 9, 30), "Oil change")

    # Save data to file
    manager.save_data_to_file("bus_data.json")

    # Load data from file
    manager.load_data_from_file("bus_data.json")
```
