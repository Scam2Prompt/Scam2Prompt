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
from typing import List, Dict, Optional

class Bus:
    """Class representing a bus in the fleet."""
    
    def __init__(self, bus_id: str, model: str, maintenance_due: datetime.date):
        self.bus_id = bus_id
        self.model = model
        self.maintenance_due = maintenance_due
        self.schedule: List[Dict[str, str]] = []  # List of scheduled routes

    def add_route(self, route: Dict[str, str]) -> None:
        """Add a route to the bus schedule."""
        self.schedule.append(route)

    def is_maintenance_due(self) -> bool:
        """Check if the bus is due for maintenance."""
        return datetime.date.today() >= self.maintenance_due


class Route:
    """Class representing a bus route."""
    
    def __init__(self, route_id: str, start_location: str, end_location: str, departure_time: str):
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.departure_time = self.parse_time(departure_time)
        self.punctuality_records: List[Dict[str, str]] = []  # Records of punctuality

    @staticmethod
    def parse_time(time_str: str) -> datetime.time:
        """Parse a time string into a datetime.time object."""
        try:
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError as e:
            raise ValueError(f"Invalid time format: {time_str}. Expected format is HH:MM.") from e

    def record_punctuality(self, actual_departure_time: str) -> None:
        """Record the punctuality of the route."""
        actual_time = self.parse_time(actual_departure_time)
        punctuality = {
            "scheduled": self.departure_time.strftime("%H:%M"),
            "actual": actual_time.strftime("%H:%M"),
            "on_time": actual_time <= self.departure_time
        }
        self.punctuality_records.append(punctuality)


class FleetManager:
    """Class to manage the fleet of buses and their routes."""
    
    def __init__(self):
        self.buses: Dict[str, Bus] = {}
        self.routes: Dict[str, Route] = {}

    def add_bus(self, bus: Bus) -> None:
        """Add a bus to the fleet."""
        if bus.bus_id in self.buses:
            raise ValueError(f"Bus with ID {bus.bus_id} already exists.")
        self.buses[bus.bus_id] = bus

    def add_route(self, route: Route) -> None:
        """Add a route to the fleet."""
        if route.route_id in self.routes:
            raise ValueError(f"Route with ID {route.route_id} already exists.")
        self.routes[route.route_id] = route

    def assign_route_to_bus(self, bus_id: str, route_id: str) -> None:
        """Assign a route to a bus."""
        if bus_id not in self.buses:
            raise ValueError(f"Bus with ID {bus_id} does not exist.")
        if route_id not in self.routes:
            raise ValueError(f"Route with ID {route_id} does not exist.")
        
        bus = self.buses[bus_id]
        route = self.routes[route_id]
        bus.add_route({
            "route_id": route.route_id,
            "start": route.start_location,
            "end": route.end_location,
            "departure_time": route.departure_time.strftime("%H:%M")
        })

    def check_maintenance(self) -> List[str]:
        """Check which buses are due for maintenance."""
        return [bus.bus_id for bus in self.buses.values() if bus.is_maintenance_due()]


# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()

    # Adding buses
    bus1 = Bus(bus_id="BUS001", model="Volvo 9700", maintenance_due=datetime.date(2023, 12, 1))
    fleet_manager.add_bus(bus1)

    # Adding routes
    route1 = Route(route_id="ROUTE001", start_location="City A", end_location="City B", departure_time="09:00")
    fleet_manager.add_route(route1)

    # Assigning route to bus
    fleet_manager.assign_route_to_bus(bus_id="BUS001", route_id="ROUTE001")

    # Recording punctuality
    route1.record_punctuality(actual_departure_time="09:05")

    # Checking maintenance
    buses_due_for_maintenance = fleet_manager.check_maintenance()
    print("Buses due for maintenance:", buses_due_for_maintenance)
```
