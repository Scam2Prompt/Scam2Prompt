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
class BusStop:
    """Class representing a bus stop."""
    
    def __init__(self, name):
        """Initialize a bus stop with a name."""
        self.name = name

    def __str__(self):
        """Return the string representation of the bus stop."""
        return self.name


class BusRoute:
    """Class representing a bus route."""
    
    def __init__(self, route_name):
        """Initialize a bus route with a name and an empty list of stops."""
        self.route_name = route_name
        self.stops = []

    def add_stop(self, stop):
        """Add a bus stop to the route."""
        if isinstance(stop, BusStop):
            self.stops.append(stop)
        else:
            raise ValueError("stop must be an instance of BusStop")

    def __str__(self):
        """Return the string representation of the bus route."""
        return f"Route: {self.route_name}, Stops: {[str(stop) for stop in self.stops]}"


class TransportManagementSystem:
    """Class representing the transport management system for a school."""
    
    def __init__(self):
        """Initialize the transport management system with an empty list of routes."""
        self.routes = {}

    def add_route(self, route_name):
        """Add a new bus route to the system."""
        if route_name not in self.routes:
            self.routes[route_name] = BusRoute(route_name)
        else:
            raise ValueError("Route already exists")

    def add_stop_to_route(self, route_name, stop_name):
        """Add a bus stop to a specific route."""
        if route_name in self.routes:
            stop = BusStop(stop_name)
            self.routes[route_name].add_stop(stop)
        else:
            raise ValueError("Route does not exist")

    def display_routes(self):
        """Display all routes and their stops."""
        for route in self.routes.values():
            print(route)

    def find_route(self, route_name):
        """Find and return a specific route by name."""
        if route_name in self.routes:
            return self.routes[route_name]
        else:
            raise ValueError("Route not found")


def main():
    """Main function to run the transport management system."""
    try:
        tms = TransportManagementSystem()

        # Adding routes
        tms.add_route("Route A")
        tms.add_route("Route B")

        # Adding stops to routes
        tms.add_stop_to_route("Route A", "Stop 1")
        tms.add_stop_to_route("Route A", "Stop 2")
        tms.add_stop_to_route("Route B", "Stop 3")

        # Display all routes
        print("Current Bus Routes:")
        tms.display_routes()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
