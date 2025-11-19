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
import json
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import random
import uuid


class BusStatus(Enum):
    """Enum representing the status of a bus."""
    ACTIVE = auto()
    INACTIVE = auto()
    MAINTENANCE = auto()


@dataclass
class BusStop:
    """Represents a bus stop with name and location."""
    name: str
    latitude: float
    longitude: float
    students: Set[str] = field(default_factory=set)  # Set of student IDs

    def add_student(self, student_id: str) -> None:
        """Add a student to this bus stop."""
        self.students.add(student_id)

    def remove_student(self, student_id: str) -> None:
        """Remove a student from this bus stop."""
        self.students.discard(student_id)


@dataclass
class BusRoute:
    """Represents a bus route with ordered stops."""
    name: str
    stops: List[BusStop] = field(default_factory=list)
    bus_ids: Set[str] = field(default_factory=set)  # Set of bus IDs assigned to this route

    def add_stop(self, stop: BusStop) -> None:
        """Add a stop to the route."""
        self.stops.append(stop)

    def remove_stop(self, stop_name: str) -> bool:
        """Remove a stop from the route by name. Returns True if removed."""
        for i, stop in enumerate(self.stops):
            if stop.name == stop_name:
                self.stops.pop(i)
                return True
        return False

    def assign_bus(self, bus_id: str) -> None:
        """Assign a bus to this route."""
        self.bus_ids.add(bus_id)

    def unassign_bus(self, bus_id: str) -> None:
        """Unassign a bus from this route."""
        self.bus_ids.discard(bus_id)


@dataclass
class Bus:
    """Represents a school bus."""
    bus_id: str
    capacity: int
    status: BusStatus = BusStatus.ACTIVE
    current_route: Optional[str] = None
    current_stop: Optional[str] = None
    passengers: Set[str] = field(default_factory=set)  # Set of student IDs

    def board_student(self, student_id: str) -> bool:
        """Board a student if capacity allows. Returns success status."""
        if len(self.passengers) < self.capacity:
            self.passengers.add(student_id)
            return True
        return False

    def alight_student(self, student_id: str) -> None:
        """Alight a student from the bus."""
        self.passengers.discard(student_id)

    def update_status(self, status: BusStatus) -> None:
        """Update the bus status."""
        self.status = status


class TransportManager:
    """Manages the school's transport system including routes, stops, and buses."""

    def __init__(self):
        self.routes: Dict[str, BusRoute] = {}  # route_name -> BusRoute
        self.stops: Dict[str, BusStop] = {}  # stop_name -> BusStop
        self.buses: Dict[str, Bus] = {}  # bus_id -> Bus
        self.student_assignments: Dict[str, str] = {}  # student_id -> stop_name

    def add_route(self, route_name: str) -> bool:
        """Add a new route. Returns False if route already exists."""
        if route_name in self.routes:
            return False
        self.routes[route_name] = BusRoute(route_name)
        return True

    def remove_route(self, route_name: str) -> bool:
        """Remove a route. Returns False if route doesn't exist."""
        if route_name not in self.routes:
            return False
        # Unassign all buses from this route
        for bus_id in list(self.routes[route_name].bus_ids):
            self.unassign_bus_from_route(bus_id, route_name)
        del self.routes[route_name]
        return True

    def add_stop(self, stop_name: str, latitude: float, longitude: float) -> bool:
        """Add a new stop. Returns False if stop already exists."""
        if stop_name in self.stops:
            return False
        self.stops[stop_name] = BusStop(stop_name, latitude, longitude)
        return True

    def remove_stop(self, stop_name: str) -> bool:
        """Remove a stop. Returns False if stop doesn't exist."""
        if stop_name not in self.stops:
            return False
        
        # Remove from all routes
        for route in self.routes.values():
            route.remove_stop(stop_name)
        
        # Unassign all students from this stop
        for student_id in list(self.stops[stop_name].students):
            self.unassign_student_from_stop(student_id, stop_name)
        
        del self.stops[stop_name]
        return True

    def add_stop_to_route(self, stop_name: str, route_name: str) -> bool:
        """Add a stop to a route. Returns False if stop or route doesn't exist."""
        if stop_name not in self.stops or route_name not in self.routes:
            return False
        self.routes[route_name].add_stop(self.stops[stop_name])
        return True

    def add_bus(self, capacity: int) -> str:
        """Add a new bus and return its ID."""
        bus_id = str(uuid.uuid4())
        self.buses[bus_id] = Bus(bus_id, capacity)
        return bus_id

    def remove_bus(self, bus_id: str) -> bool:
        """Remove a bus. Returns False if bus doesn't exist."""
        if bus_id not in self.buses:
            return False
        
        # Unassign from all routes
        for route in self.routes.values():
            if bus_id in route.bus_ids:
                route.unassign_bus(bus_id)
        
        del self.buses[bus_id]
        return True

    def assign_bus_to_route(self, bus_id: str, route_name: str) -> bool:
        """Assign a bus to a route. Returns False if bus or route doesn't exist."""
        if bus_id not in self.buses or route_name not in self.routes:
            return False
        self.routes[route_name].assign_bus(bus_id)
        self.buses[bus_id].current_route = route_name
        return True

    def unassign_bus_from_route(self, bus_id: str, route_name: str) -> bool:
        """Unassign a bus from a route. Returns False if bus or route doesn't exist."""
        if bus_id not in self.buses or route_name not in self.routes:
            return False
        if bus_id not in self.routes[route_name].bus_ids:
            return False
        self.routes[route_name].unassign_bus(bus_id)
        self.buses[bus_id].current_route = None
        self.buses[bus_id].current_stop = None
        return True

    def assign_student_to_stop(self, student_id: str, stop_name: str) -> bool:
        """Assign a student to a stop. Returns False if stop doesn't exist."""
        if stop_name not in self.stops:
            return False
        self.stops[stop_name].add_student(student_id)
        self.student_assignments[student_id] = stop_name
        return True

    def unassign_student_from_stop(self, student_id: str, stop_name: str) -> bool:
        """Unassign a student from a stop. Returns False if stop doesn't exist or student not assigned."""
        if stop_name not in self.stops or student_id not in self.student_assignments:
            return False
        self.stops[stop_name].remove_student(student_id)
        del self.student_assignments[student_id]
        return True

    def move_bus_to_next_stop(self, bus_id: str) -> bool:
        """Move a bus to its next stop on the route. Returns False if bus not on a route."""
        if bus_id not in self.buses:
            return False
        
        bus = self.buses[bus_id]
        if not bus.current_route:
            return False
        
        route = self.routes[bus.current_route]
        if not route.stops:
            return False
        
        # If bus is not at any stop, start at first stop
        if not bus.current_stop:
            bus.current_stop = route.stops[0].name
            return True
        
        # Find current stop index
        current_index = None
        for i, stop in enumerate(route.stops):
            if stop.name == bus.current_stop:
                current_index = i
                break
        
        if current_index is None:
            return False
        
        # Move to next stop (circular route)
        next_index = (current_index + 1) % len(route.stops)
        bus.current_st
