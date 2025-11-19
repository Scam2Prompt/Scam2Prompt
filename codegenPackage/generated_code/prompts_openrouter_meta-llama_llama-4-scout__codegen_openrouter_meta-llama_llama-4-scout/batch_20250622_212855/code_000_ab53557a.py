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
# bus_transportation_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class Vehicle:
    def __init__(self, vehicle_id: str, make: str, model: str):
        """
        Initialize a Vehicle object.

        Args:
        - vehicle_id (str): Unique identifier for the vehicle.
        - make (str): Vehicle manufacturer.
        - model (str): Vehicle model.
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.maintenance_records = []

    def add_maintenance_record(self, record: str):
        """
        Add a maintenance record for the vehicle.

        Args:
        - record (str): Description of the maintenance performed.
        """
        self.maintenance_records.append(record)


class BusRoute:
    def __init__(self, route_id: str, start_location: str, end_location: str):
        """
        Initialize a BusRoute object.

        Args:
        - route_id (str): Unique identifier for the route.
        - start_location (str): Starting location of the route.
        - end_location (str): Ending location of the route.
        """
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.schedule = []

    def add_schedule(self, departure_time: datetime, arrival_time: datetime):
        """
        Add a schedule entry for the route.

        Args:
        - departure_time (datetime): Departure time from the start location.
        - arrival_time (datetime): Arrival time at the end location.
        """
        self.schedule.append((departure_time, arrival_time))


class TransportationSystem:
    def __init__(self):
        """
        Initialize the transportation system.
        """
        self.vehicles: Dict[str, Vehicle] = {}
        self.routes: Dict[str, BusRoute] = {}

    def add_vehicle(self, vehicle: Vehicle):
        """
        Add a vehicle to the system.

        Args:
        - vehicle (Vehicle): Vehicle object to add.
        """
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_route(self, route: BusRoute):
        """
        Add a route to the system.

        Args:
        - route (BusRoute): BusRoute object to add.
        """
        self.routes[route.route_id] = route

    def track_punctuality(self, route_id: str, departure_time: datetime, arrival_time: datetime):
        """
        Track punctuality for a route.

        Args:
        - route_id (str): ID of the route.
        - departure_time (datetime): Scheduled departure time.
        - arrival_time (datetime): Scheduled arrival time.

        Returns:
        - A string indicating whether the bus was on time or not.
        """
        if route_id not in self.routes:
            raise ValueError("Route not found")

        route = self.routes[route_id]
        for scheduled_departure, scheduled_arrival in route.schedule:
            if scheduled_departure == departure_time and scheduled_arrival == arrival_time:
                # Simulate tracking punctuality (e.g., get actual departure and arrival times)
                actual_departure = departure_time
                actual_arrival = arrival_time

                if actual_departure <= departure_time and actual_arrival <= arrival_time:
                    return "On time"
                else:
                    return "Late"

        raise ValueError("Schedule not found")

    def get_vehicle_maintenance_records(self, vehicle_id: str) -> List[str]:
        """
        Get maintenance records for a vehicle.

        Args:
        - vehicle_id (str): ID of the vehicle.

        Returns:
        - A list of maintenance records for the vehicle.
        """
        if vehicle_id not in self.vehicles:
            raise ValueError("Vehicle not found")

        return self.vehicles[vehicle_id].maintenance_records


def main():
    # Create a transportation system
    system = TransportationSystem()

    # Create vehicles
    vehicle1 = Vehicle("V1", "Mercedes-Benz", "Sprinter")
    vehicle2 = Vehicle("V2", "Ford", "Transit")

    # Add vehicles to the system
    system.add_vehicle(vehicle1)
    system.add_vehicle(vehicle2)

    # Add maintenance records
    vehicle1.add_maintenance_record("Oil change")
    vehicle2.add_maintenance_record("Tire rotation")

    # Create routes
    route1 = BusRoute("R1", "New York", "Los Angeles")
    route2 = BusRoute("R2", "Chicago", "Houston")

    # Add routes to the system
    system.add_route(route1)
    system.add_route(route2)

    # Add schedules
    route1.add_schedule(datetime(2024, 9, 16, 8, 0), datetime(2024, 9, 16, 20, 0))
    route2.add_schedule(datetime(2024, 9, 16, 9, 0), datetime(2024, 9, 16, 18, 0))

    # Track punctuality
    print(system.track_punctuality("R1", datetime(2024, 9, 16, 8, 0), datetime(2024, 9, 16, 20, 0)))

    # Get vehicle maintenance records
    print(system.get_vehicle_maintenance_records("V1"))


if __name__ == "__main__":
    main()
```
