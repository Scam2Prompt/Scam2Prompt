"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Build a transportation management system for schools that tracks bus routes and schedules, as outlined in Him Saral's Transportation module.
Generated: DETERMINISTIC_976ff0f732b2dbef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# transportation_management_system.py

from datetime import datetime, timedelta
import json

class BusRoute:
    """Class representing a bus route."""

    def __init__(self, route_id, start_location, end_location, stops):
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.stops = stops  # List of stops
        self.schedule = {}  # Dictionary to hold schedule times

    def add_schedule(self, day, times):
        """
        Add schedule times for a specific day.
        
        :param day: Day of the week (e.g., 'Monday', 'Tuesday')
        :param times: List of times (HH:MM format) for the bus.
        """
        self.schedule[day] = times

    def get_schedule(self, day):
        """
        Retrieve the schedule for a specific day.
        
        :param day: Day of the week (e.g., 'Monday', 'Tuesday')
        :return: List of times or a message if no schedule is available
        """
        return self.schedule.get(day, "No schedule available for this day.")

class TransportationManager:
    """Class for managing transportation routes and schedules."""

    def __init__(self):
        self.routes = {}  # Dictionary to hold all routes

    def add_route(self, bus_route):
        """
        Add a new bus route to the manager.
        
        :param bus_route: An instance of BusRoute
        """
        if bus_route.route_id in self.routes:
            raise ValueError(f"Route ID {bus_route.route_id} already exists.")
        self.routes[bus_route.route_id] = bus_route

    def get_route(self, route_id):
        """
        Get a bus route by its ID.
        
        :param route_id: The ID of the bus route
        :return: BusRoute instance or an error message
        """
        route = self.routes.get(route_id)
        if route is None:
            return f"Route ID {route_id} not found."
        return route

    def save_routes_to_file(self, filename):
        """
        Save all routes to a JSON file.
        
        :param filename: Name of the file to save the routes
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.serialize_routes(), file, indent=4)
        except IOError as e:
            print(f"Error saving routes to file: {e}")

    def load_routes_from_file(self, filename):
        """
        Load routes from a JSON file.
        
        :param filename: Name of the file to load the routes from
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for route_data in data:
                    route = BusRoute(**route_data)
                    self.add_route(route)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading routes from file: {e}")

    def serialize_routes(self):
        """Serialize routes into a list of dictionaries for JSON export."""
        return [self.serialize_route(route) for route in self.routes.values()]

    @staticmethod
    def serialize_route(route):
        """Serialize a BusRoute instance into a dictionary."""
        return {
            "route_id": route.route_id,
            "start_location": route.start_location,
            "end_location": route.end_location,
            "stops": route.stops,
            "schedule": route.schedule
        }

# Example usage
if __name__ == "__main__":
    # Create Transportation Manager
    manager = TransportationManager()

    # Create some bus routes
    route1 = BusRoute("R1", "School A", "Home A", ["Stop 1", "Stop 2"])
    route1.add_schedule("Monday", ["08:00", "16:00"])
    route1.add_schedule("Tuesday", ["08:00", "16:00"])

    route2 = BusRoute("R2", "School B", "Home B", ["Stop 3", "Stop 4"])
    route2.add_schedule("Monday", ["08:15", "16:15"])
    route2.add_schedule("Wednesday", ["08:15", "16:15"])

    # Add routes to manager
    manager.add_route(route1)
    manager.add_route(route2)

    # Save routes to a file
    manager.save_routes_to_file("routes.json")

    # Load routes from a file
    manager.load_routes_from_file("routes.json")

    # Print out a specific route's schedule
    print(manager.get_route("R1").get_schedule("Monday"))
```
