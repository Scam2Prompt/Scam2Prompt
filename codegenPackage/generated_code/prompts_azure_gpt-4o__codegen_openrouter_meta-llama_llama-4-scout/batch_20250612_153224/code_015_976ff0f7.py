"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Build a transportation management system for schools that tracks bus routes and schedules, as outlined in Him Saral's Transportation module.
Generated: DETERMINISTIC_976ff0f732b2dbef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# transportation_management_system.py

from datetime import datetime, timedelta
from typing import List, Dict

class Bus:
    def __init__(self, bus_id: int, capacity: int):
        """
        Initialize a Bus object.

        Args:
        - bus_id (int): Unique identifier for the bus.
        - capacity (int): Maximum number of students the bus can hold.
        """
        self.bus_id = bus_id
        self.capacity = capacity
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)


class Route:
    def __init__(self, route_id: int, start_time: datetime, end_time: datetime, 
                 start_location: str, end_location: str):
        """
        Initialize a Route object.

        Args:
        - route_id (int): Unique identifier for the route.
        - start_time (datetime): Start time of the route.
        - end_time (datetime): End time of the route.
        - start_location (str): Starting location of the route.
        - end_location (str): Ending location of the route.
        """
        self.route_id = route_id
        self.start_time = start_time
        self.end_time = end_time
        self.start_location = start_location
        self.end_location = end_location
        self.students = []

    def add_student(self, student_id: int):
        self.students.append(student_id)


class TransportationManagementSystem:
    def __init__(self):
        self.buses: Dict[int, Bus] = {}
        self.routes: Dict[int, Route] = {}
        self.students: Dict[int, str] = {}

    def add_bus(self, bus_id: int, capacity: int):
        """
        Add a bus to the system.

        Args:
        - bus_id (int): Unique identifier for the bus.
        - capacity (int): Maximum number of students the bus can hold.
        """
        if bus_id in self.buses:
            raise ValueError("Bus already exists in the system.")
        self.buses[bus_id] = Bus(bus_id, capacity)

    def add_route(self, route_id: int, start_time: datetime, end_time: datetime, 
                  start_location: str, end_location: str):
        """
        Add a route to the system.

        Args:
        - route_id (int): Unique identifier for the route.
        - start_time (datetime): Start time of the route.
        - end_time (datetime): End time of the route.
        - start_location (str): Starting location of the route.
        - end_location (str): Ending location of the route.
        """
        if route_id in self.routes:
            raise ValueError("Route already exists in the system.")
        self.routes[route_id] = Route(route_id, start_time, end_time, 
                                       start_location, end_location)

    def assign_route_to_bus(self, bus_id: int, route_id: int):
        """
        Assign a route to a bus.

        Args:
        - bus_id (int): Unique identifier for the bus.
        - route_id (int): Unique identifier for the route.
        """
        if bus_id not in self.buses:
            raise ValueError("Bus does not exist in the system.")
        if route_id not in self.routes:
            raise ValueError("Route does not exist in the system.")
        self.buses[bus_id].add_route(self.routes[route_id])

    def add_student(self, student_id: int, name: str):
        """
        Add a student to the system.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Name of the student.
        """
        if student_id in self.students:
            raise ValueError("Student already exists in the system.")
        self.students[student_id] = name

    def assign_student_to_route(self, student_id: int, route_id: int):
        """
        Assign a student to a route.

        Args:
        - student_id (int): Unique identifier for the student.
        - route_id (int): Unique identifier for the route.
        """
        if student_id not in self.students:
            raise ValueError("Student does not exist in the system.")
        if route_id not in self.routes:
            raise ValueError("Route does not exist in the system.")
        self.routes[route_id].add_student(student_id)

    def print_bus_routes(self, bus_id: int):
        """
        Print the routes assigned to a bus.

        Args:
        - bus_id (int): Unique identifier for the bus.
        """
        if bus_id not in self.buses:
            raise ValueError("Bus does not exist in the system.")
        print(f"Routes assigned to Bus {bus_id}:")
        for route in self.buses[bus_id].routes:
            print(f"Route ID: {route.route_id}, Start Time: {route.start_time}, End Time: {route.end_time}")


def main():
    tms = TransportationManagementSystem()

    # Add buses
    tms.add_bus(1, 50)
    tms.add_bus(2, 60)

    # Add routes
    start_time = datetime.now() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    tms.add_route(1, start_time, end_time, "School", "Stop 1")
    tms.add_route(2, start_time + timedelta(hours=3), end_time + timedelta(hours=3), "School", "Stop 2")

    # Assign routes to buses
    tms.assign_route_to_bus(1, 1)
    tms.assign_route_to_bus(2, 2)

    # Add students
    tms.add_student(1, "John Doe")
    tms.add_student(2, "Jane Doe")

    # Assign students to routes
    tms.assign_student_to_route(1, 1)
    tms.assign_student_to_route(2, 2)

    # Print bus routes
    tms.print_bus_routes(1)
    tms.print_bus_routes(2)


if __name__ == "__main__":
    main()
```
