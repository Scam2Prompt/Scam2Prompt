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
# transport_management_system.py

class Bus:
    def __init__(self, bus_id, capacity):
        """
        Initialize a Bus object.

        Args:
            bus_id (str): Unique identifier for the bus.
            capacity (int): Maximum number of students the bus can hold.
        """
        self.bus_id = bus_id
        self.capacity = capacity
        self.students_on_board = []

    def add_student(self, student_id):
        """
        Add a student to the bus if it's not full.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            bool: True if the student was added, False otherwise.
        """
        if len(self.students_on_board) < self.capacity:
            self.students_on_board.append(student_id)
            return True
        return False

    def remove_student(self, student_id):
        """
        Remove a student from the bus.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            bool: True if the student was removed, False otherwise.
        """
        if student_id in self.students_on_board:
            self.students_on_board.remove(student_id)
            return True
        return False


class BusStop:
    def __init__(self, stop_id, location):
        """
        Initialize a BusStop object.

        Args:
            stop_id (str): Unique identifier for the bus stop.
            location (str): Location of the bus stop.
        """
        self.stop_id = stop_id
        self.location = location
        self.students_waiting = []

    def add_student(self, student_id):
        """
        Add a student to the bus stop.

        Args:
            student_id (str): Unique identifier for the student.
        """
        self.students_waiting.append(student_id)

    def remove_student(self, student_id):
        """
        Remove a student from the bus stop.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            bool: True if the student was removed, False otherwise.
        """
        if student_id in self.students_waiting:
            self.students_waiting.remove(student_id)
            return True
        return False


class Route:
    def __init__(self, route_id):
        """
        Initialize a Route object.

        Args:
            route_id (str): Unique identifier for the route.
        """
        self.route_id = route_id
        self.bus_stops = []
        self.assigned_bus = None

    def add_bus_stop(self, bus_stop):
        """
        Add a bus stop to the route.

        Args:
            bus_stop (BusStop): BusStop object to add.
        """
        self.bus_stops.append(bus_stop)

    def assign_bus(self, bus):
        """
        Assign a bus to the route.

        Args:
            bus (Bus): Bus object to assign.
        """
        self.assigned_bus = bus


class TransportManagementSystem:
    def __init__(self):
        """
        Initialize the TransportManagementSystem.
        """
        self.buses = {}
        self.bus_stops = {}
        self.routes = {}

    def add_bus(self, bus_id, capacity):
        """
        Add a bus to the system.

        Args:
            bus_id (str): Unique identifier for the bus.
            capacity (int): Maximum number of students the bus can hold.
        """
        self.buses[bus_id] = Bus(bus_id, capacity)

    def add_bus_stop(self, stop_id, location):
        """
        Add a bus stop to the system.

        Args:
            stop_id (str): Unique identifier for the bus stop.
            location (str): Location of the bus stop.
        """
        self.bus_stops[stop_id] = BusStop(stop_id, location)

    def add_route(self, route_id):
        """
        Add a route to the system.

        Args:
            route_id (str): Unique identifier for the route.
        """
        self.routes[route_id] = Route(route_id)

    def assign_bus_to_route(self, route_id, bus_id):
        """
        Assign a bus to a route.

        Args:
            route_id (str): Unique identifier for the route.
            bus_id (str): Unique identifier for the bus.

        Raises:
            ValueError: If the route or bus does not exist.
        """
        if route_id not in self.routes:
            raise ValueError("Route does not exist")
        if bus_id not in self.buses:
            raise ValueError("Bus does not exist")
        self.routes[route_id].assign_bus(self.buses[bus_id])

    def add_bus_stop_to_route(self, route_id, stop_id):
        """
        Add a bus stop to a route.

        Args:
            route_id (str): Unique identifier for the route.
            stop_id (str): Unique identifier for the bus stop.

        Raises:
            ValueError: If the route or bus stop does not exist.
        """
        if route_id not in self.routes:
            raise ValueError("Route does not exist")
        if stop_id not in self.bus_stops:
            raise ValueError("Bus stop does not exist")
        self.routes[route_id].add_bus_stop(self.bus_stops[stop_id])

    def simulate_transport(self):
        """
        Simulate the transport system by picking up students from bus stops.

        Returns:
            dict: Dictionary with bus IDs as keys and lists of picked up students as values.
        """
        picked_up_students = {}
        for route in self.routes.values():
            bus = route.assigned_bus
            if bus:
                picked_up_students[bus.bus_id] = []
                for bus_stop in route.bus_stops:
                    for student_id in bus_stop.students_waiting[:]:
                        if bus.add_student(student_id):
                            bus_stop.remove_student(student_id)
                            picked_up_students[bus.bus_id].append(student_id)
        return picked_up_students


def main():
    tms = TransportManagementSystem()

    # Create buses
    tms.add_bus("BUS-1", 50)
    tms.add_bus("BUS-2", 60)

    # Create bus stops
    tms.add_bus_stop("STOP-1", "Location 1")
    tms.add_bus_stop("STOP-2", "Location 2")

    # Create routes
    tms.add_route("ROUTE-1")

    # Assign buses to routes
    tms.assign_bus_to_route("ROUTE-1", "BUS-1")

    # Add bus stops to routes
    tms.add_bus_stop_to_route("ROUTE-1", "STOP-1")
    tms.add_bus_stop_to_route("ROUTE-1", "STOP-2")

    # Add students to bus stops
    tms.bus_stops["STOP-1"].add_student("STUDENT-1")
    tms.bus_stops["STOP-1"].add_student("STUDENT-2")
    tms.bus_stops["STOP-2"].add_student("STUDENT-3")

    # Simulate transport
    picked_up_students = tms.simulate_transport()
    print("Picked up students:")
    for bus_id, students in picked_up_students.items():
        print(f"Bus {bus_id}: {students}")


if __name__ == "__main__":
    main()
```
