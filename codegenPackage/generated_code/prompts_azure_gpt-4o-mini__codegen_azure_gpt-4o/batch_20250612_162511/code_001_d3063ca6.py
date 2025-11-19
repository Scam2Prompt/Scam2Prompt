"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Write a Python script that simulates the transport management system for a school, considering the constraints mentioned by Param Gyan Niketan regarding bus routes and stops.
Generated: DETERMINISTIC_d3063ca6458e34b2
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Transport Management System for Param Gyan Niketan School

This script simulates a transport management system for a school, considering bus routes and stops.
It allows for adding buses, defining routes, assigning students to stops, and checking bus capacity constraints.
"""

import sys

class Bus:
    """
    Represents a school bus with a unique ID, capacity, and assigned route.
    """
    def __init__(self, bus_id, capacity):
        self.bus_id = bus_id
        self.capacity = capacity
        self.route = []
        self.students = []

    def assign_route(self, route):
        """
        Assigns a route to the bus.
        :param route: List of stops (strings) representing the route.
        """
        self.route = route

    def add_student(self, student_name, stop):
        """
        Adds a student to the bus if the stop is on the route and capacity allows.
        :param student_name: Name of the student.
        :param stop: Stop where the student boards the bus.
        :raises ValueError: If the stop is not on the route or the bus is full.
        """
        if stop not in self.route:
            raise ValueError(f"Stop '{stop}' is not on the route for bus {self.bus_id}.")
        if len(self.students) >= self.capacity:
            raise ValueError(f"Bus {self.bus_id} is full. Cannot add more students.")
        self.students.append({"name": student_name, "stop": stop})

    def __str__(self):
        """
        Returns a string representation of the bus details.
        """
        return f"Bus ID: {self.bus_id}, Capacity: {self.capacity}, Route: {self.route}, Students: {self.students}"


class TransportManagementSystem:
    """
    Manages buses, routes, and student assignments for the school.
    """
    def __init__(self):
        self.buses = {}

    def add_bus(self, bus_id, capacity):
        """
        Adds a new bus to the system.
        :param bus_id: Unique identifier for the bus.
        :param capacity: Maximum number of students the bus can carry.
        """
        if bus_id in self.buses:
            raise ValueError(f"Bus with ID {bus_id} already exists.")
        self.buses[bus_id] = Bus(bus_id, capacity)

    def assign_route_to_bus(self, bus_id, route):
        """
        Assigns a route to a specific bus.
        :param bus_id: ID of the bus.
        :param route: List of stops (strings) representing the route.
        :raises KeyError: If the bus ID does not exist.
        """
        if bus_id not in self.buses:
            raise KeyError(f"Bus with ID {bus_id} does not exist.")
        self.buses[bus_id].assign_route(route)

    def add_student_to_bus(self, bus_id, student_name, stop):
        """
        Adds a student to a specific bus at a specific stop.
        :param bus_id: ID of the bus.
        :param student_name: Name of the student.
        :param stop: Stop where the student boards the bus.
        :raises KeyError: If the bus ID does not exist.
        """
        if bus_id not in self.buses:
            raise KeyError(f"Bus with ID {bus_id} does not exist.")
        self.buses[bus_id].add_student(student_name, stop)

    def display_bus_details(self, bus_id):
        """
        Displays details of a specific bus.
        :param bus_id: ID of the bus.
        :raises KeyError: If the bus ID does not exist.
        """
        if bus_id not in self.buses:
            raise KeyError(f"Bus with ID {bus_id} does not exist.")
        print(self.buses[bus_id])

    def display_all_buses(self):
        """
        Displays details of all buses in the system.
        """
        for bus in self.buses.values():
            print(bus)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the transport management system
        tms = TransportManagementSystem()

        # Add buses
        tms.add_bus("Bus1", 50)
        tms.add_bus("Bus2", 40)

        # Assign routes to buses
        tms.assign_route_to_bus("Bus1", ["Stop1", "Stop2", "Stop3", "Stop4"])
        tms.assign_route_to_bus("Bus2", ["StopA", "StopB", "StopC"])

        # Add students to buses
        tms.add_student_to_bus("Bus1", "Alice", "Stop1")
        tms.add_student_to_bus("Bus1", "Bob", "Stop2")
        tms.add_student_to_bus("Bus2", "Charlie", "StopA")

        # Display bus details
        tms.display_bus_details("Bus1")
        tms.display_bus_details("Bus2")

        # Display all buses
        print("\nAll Buses:")
        tms.display_all_buses()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
