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

import datetime

class BusRoute:
    """
    Class to represent a Bus Route.
    Tracks the route number, stops, and assigned driver.
    """
    def __init__(self, route_number, stops, driver_name):
        self.route_number = route_number  # Unique identifier for the bus route
        self.stops = stops  # List of stops for the route
        self.driver_name = driver_name  # Name of the driver assigned to the route

    def display_route_info(self):
        """
        Display the details of the bus route.
        """
        print(f"Route Number: {self.route_number}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Stops: {', '.join(self.stops)}")


class BusSchedule:
    """
    Class to represent a Bus Schedule.
    Tracks the schedule for each route (time and date).
    """
    def __init__(self):
        self.schedules = {}  # Dictionary to track route schedules

    def add_schedule(self, route_number, start_time, end_time):
        """
        Add a schedule for a bus route.
        """
        if route_number in self.schedules:
            print(f"Error: Schedule for route {route_number} already exists.")
            return
        self.schedules[route_number] = {
            "start_time": start_time,
            "end_time": end_time
        }

    def display_schedule(self, route_number):
        """
        Display the schedule for a given route.
        """
        if route_number not in self.schedules:
            print(f"No schedule found for route {route_number}.")
            return
        
        schedule = self.schedules[route_number]
        print(f"Route Number: {route_number}")
        print(f"Start Time: {schedule['start_time'].strftime('%H:%M:%S')}")
        print(f"End Time: {schedule['end_time'].strftime('%H:%M:%S')}")


class TransportationManagementSystem:
    """
    Main class to manage the transportation system.
    Integrates routes and schedules.
    """
    def __init__(self):
        self.routes = {}  # Dictionary to store bus routes
        self.schedule = BusSchedule()  # Schedule manager instance

    def add_route(self, route_number, stops, driver_name):
        """
        Add a bus route to the system.
        """
        if route_number in self.routes:
            print(f"Error: Route {route_number} already exists.")
            return

        new_route = BusRoute(route_number, stops, driver_name)
        self.routes[route_number] = new_route
        print(f"Route {route_number} added successfully.")

    def add_schedule(self, route_number, start_time, end_time):
        """
        Add a schedule for an existing route.
        """
        if route_number not in self.routes:
            print(f"Error: Route {route_number} does not exist.")
            return

        self.schedule.add_schedule(route_number, start_time, end_time)

    def display_route_details(self, route_number):
        """
        Display details of a specific route along with its schedule.
        """
        if route_number not in self.routes:
            print(f"Error: Route {route_number} does not exist.")
            return
        
        print("Route Information:")
        self.routes[route_number].display_route_info()
        
        print("\nSchedule Information:")
        self.schedule.display_schedule(route_number)


# Example Usage
if __name__ == "__main__":
    try:
        # Create the transportation system instance
        tms = TransportationManagementSystem()

        # Add routes
        tms.add_route("101", ["School A", "Stop 1", "Stop 2"], "John Doe")
        tms.add_route("102", ["School B", "Stop 3", "Stop 4"], "Jane Smith")

        # Add schedules
        start_time_101 = datetime.datetime.strptime("07:30:00", "%H:%M:%S")
        end_time_101 = datetime.datetime.strptime("08:30:00", "%H:%M:%S")
        tms.add_schedule("101", start_time_101, end_time_101)

        start_time_102 = datetime.datetime.strptime("08:00:00", "%H:%M:%S")
        end_time_102 = datetime.datetime.strptime("09:00:00", "%H:%M:%S")
        tms.add_schedule("102", start_time_102, end_time_102)

        # Display route and schedule details
        tms.display_route_details("101")
        print("\n")
        tms.display_route_details("102")
    except Exception as e:
        print(f"An error occurred: {e}")
```
