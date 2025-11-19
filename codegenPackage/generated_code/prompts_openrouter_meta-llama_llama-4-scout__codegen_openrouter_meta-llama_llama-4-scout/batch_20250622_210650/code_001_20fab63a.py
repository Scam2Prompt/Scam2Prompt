"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "Write a Python script to manage security guard schedules and patrol routes."
Generated: DETERMINISTIC_20fab63a397fbf20
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_guard_scheduler.py

from datetime import datetime, timedelta
from typing import List, Dict

class SecurityGuard:
    """Represents a security guard with a name and a unique ID."""

    def __init__(self, guard_id: int, name: str):
        """
        Initializes a SecurityGuard object.

        Args:
            guard_id (int): Unique ID for the guard.
            name (str): Name of the guard.
        """
        self.guard_id = guard_id
        self.name = name

class PatrolRoute:
    """Represents a patrol route with a name and a list of locations."""

    def __init__(self, route_id: int, name: str, locations: List[str]):
        """
        Initializes a PatrolRoute object.

        Args:
            route_id (int): Unique ID for the route.
            name (str): Name of the route.
            locations (List[str]): List of locations in the route.
        """
        self.route_id = route_id
        self.name = name
        self.locations = locations

class Schedule:
    """Represents a schedule for a security guard."""

    def __init__(self, schedule_id: int, guard: SecurityGuard, route: PatrolRoute, start_time: datetime, end_time: datetime):
        """
        Initializes a Schedule object.

        Args:
            schedule_id (int): Unique ID for the schedule.
            guard (SecurityGuard): Security guard assigned to the schedule.
            route (PatrolRoute): Patrol route assigned to the schedule.
            start_time (datetime): Start time of the schedule.
            end_time (datetime): End time of the schedule.
        """
        self.schedule_id = schedule_id
        self.guard = guard
        self.route = route
        self.start_time = start_time
        self.end_time = end_time

class SecurityGuardScheduler:
    """Manages security guard schedules and patrol routes."""

    def __init__(self):
        self.guards: Dict[int, SecurityGuard] = {}
        self.routes: Dict[int, PatrolRoute] = {}
        self.schedules: Dict[int, Schedule] = {}

    def add_guard(self, guard_id: int, name: str):
        """
        Adds a security guard to the scheduler.

        Args:
            guard_id (int): Unique ID for the guard.
            name (str): Name of the guard.
        """
        self.guards[guard_id] = SecurityGuard(guard_id, name)

    def add_route(self, route_id: int, name: str, locations: List[str]):
        """
        Adds a patrol route to the scheduler.

        Args:
            route_id (int): Unique ID for the route.
            name (str): Name of the route.
            locations (List[str]): List of locations in the route.
        """
        self.routes[route_id] = PatrolRoute(route_id, name, locations)

    def add_schedule(self, schedule_id: int, guard_id: int, route_id: int, start_time: str, end_time: str):
        """
        Adds a schedule to the scheduler.

        Args:
            schedule_id (int): Unique ID for the schedule.
            guard_id (int): ID of the guard assigned to the schedule.
            route_id (int): ID of the patrol route assigned to the schedule.
            start_time (str): Start time of the schedule in YYYY-MM-DD HH:MM format.
            end_time (str): End time of the schedule in YYYY-MM-DD HH:MM format.

        Raises:
            ValueError: If the guard or route ID is not found.
        """
        if guard_id not in self.guards:
            raise ValueError(f"Guard with ID {guard_id} not found")
        if route_id not in self.routes:
            raise ValueError(f"Route with ID {route_id} not found")

        guard = self.guards[guard_id]
        route = self.routes[route_id]
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

        self.schedules[schedule_id] = Schedule(schedule_id, guard, route, start_time, end_time)

    def print_schedules(self):
        """Prints all schedules."""
        for schedule in self.schedules.values():
            print(f"Schedule ID: {schedule.schedule_id}")
            print(f"Guard: {schedule.guard.name}")
            print(f"Route: {schedule.route.name}")
            print(f"Start Time: {schedule.start_time.strftime('%Y-%m-%d %H:%M')}")
            print(f"End Time: {schedule.end_time.strftime('%Y-%m-%d %H:%M')}")
            print("Locations:")
            for location in schedule.route.locations:
                print(f"- {location}")
            print()

def main():
    scheduler = SecurityGuardScheduler()

    # Add guards
    scheduler.add_guard(1, "John Doe")
    scheduler.add_guard(2, "Jane Smith")

    # Add routes
    scheduler.add_route(1, "Route 1", ["Location 1", "Location 2", "Location 3"])
    scheduler.add_route(2, "Route 2", ["Location 4", "Location 5", "Location 6"])

    # Add schedules
    scheduler.add_schedule(1, 1, 1, "2024-09-16 08:00", "2024-09-16 16:00")
    scheduler.add_schedule(2, 2, 2, "2024-09-16 09:00", "2024-09-16 17:00")

    # Print schedules
    scheduler.print_schedules()

if __name__ == "__main__":
    main()
```
