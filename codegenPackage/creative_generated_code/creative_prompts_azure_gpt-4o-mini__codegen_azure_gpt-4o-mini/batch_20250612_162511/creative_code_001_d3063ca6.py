"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Write a Python script that simulates the transport management system for a school, considering the constraints mentioned by Param Gyan Niketan regarding bus routes and stops.
Generated: DETERMINISTIC_d3063ca6458e34b2
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Bus:
    """
    Represents a bus in the transport management system.
    Attributes:
        bus_id (str): Unique identifier for the bus.
        capacity (int): Maximum number of students that the bus can carry.
        current_passengers (list): List of students currently on the bus.
    """
    
    def __init__(self, bus_id: str, capacity: int):
        """
        Initializes a new Bus instance.

        Args:
            bus_id (str): Unique identifier for the bus.
            capacity (int): Maximum capacity of the bus.
        """
        self.bus_id = bus_id
        self.capacity = capacity
        self.current_passengers = []

    def board_student(self, student: str) -> bool:
        """
        Boards a student onto the bus if there is capacity.

        Args:
            student (str): The name of the student to board.

        Returns:
            bool: True if the student boarded successfully, False otherwise.
        """
        if len(self.current_passengers) < self.capacity:
            self.current_passengers.append(student)
            return True
        return False

    def disembark_student(self, student: str) -> bool:
        """
        Disembarks a student from the bus.

        Args:
            student (str): The name of the student to disembark.

        Returns:
            bool: True if the student disembarked successfully, False if not found.
        """
        try:
            self.current_passengers.remove(student)
            return True
        except ValueError:
            return False

    def get_passenger_list(self) -> list:
        """
        Returns a list of current passengers.

        Returns:
            list: List of students currently on the bus.
        """
        return self.current_passengers.copy()


class Route:
    """
    Represents a bus route in the transport management system.
    Attributes:
        route_id (str): Unique identifier for the route.
        stops (list): List of stops on the route.
        buses (list): List of buses assigned to the route.
    """
    
    def __init__(self, route_id: str, stops: list):
        """
        Initializes a new Route instance.

        Args:
            route_id (str): Unique identifier for the route.
            stops (list): List of stops on the route.
        """
        self.route_id = route_id
        self.stops = stops
        self.buses = []

    def add_bus(self, bus: Bus):
        """
        Adds a bus to the route.

        Args:
            bus (Bus): The bus to be added to the route.
        """
        self.buses.append(bus)

    def get_buses(self) -> list:
        """
        Returns a list of buses assigned to the route.

        Returns:
            list: List of buses for the route.
        """
        return self.buses.copy()


class TransportManagementSystem:
    """
    Represents the transport management system for the school.
    Attributes:
        routes (dict): Dictionary of routes managed by the system.
    """
    
    def __init__(self):
        """
        Initializes the transport management system with no routes.
        """
        self.routes = {}

    def add_route(self, route: Route):
        """
        Adds a new route to the system.

        Args:
            route (Route): The route to be added.
        """
        if route.route_id in self.routes:
            raise ValueError(f"Route with ID {route.route_id} already exists.")
        self.routes[route.route_id] = route

    def get_route(self, route_id: str) -> Route:
        """
        Retrieves a route from the system by its ID.

        Args:
            route_id (str): The unique ID of the route.

        Raises:
            KeyError: If the route ID does not exist.

        Returns:
            Route: The requested route.
        """
        if route_id not in self.routes:
            raise KeyError(f"Route with ID {route_id} does not exist.")
        return self.routes[route_id]


# Example usage of the Transport Management System
if __name__ == "__main__":
    # Initialize the transport management system
    tms = TransportManagementSystem()

    # Create a new route with defined stops
    route1 = Route(route_id="Route101", stops=["Stop A", "Stop B", "Stop C"])
    
    # Add route to the system
    tms.add_route(route1)

    # Create a bus and add it to the route
    bus1 = Bus(bus_id="Bus001", capacity=30)
    route1.add_bus(bus1)

    # Board students onto the bus
    students = ["Alice", "Bob", "Charlie"]
    for student in students:
        if not bus1.board_student(student):
            print(f"Could not board {student}, bus is full.")
    
    # Print current passengers
    print("Current Passengers on Bus001:", bus1.get_passenger_list())
    
    # Disembark a student
    bus1.disembark_student("Bob")
    print("After Bob disembarks:", bus1.get_passenger_list())
```
