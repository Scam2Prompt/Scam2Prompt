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
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class SecurityGuard:
    """Class to represent a security guard."""
    
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.schedule: List[Dict[str, str]] = []  # List to hold scheduled shifts

    def add_shift(self, start_time: str, end_time: str) -> None:
        """Add a shift to the guard's schedule."""
        self.schedule.append({
            'start_time': start_time,
            'end_time': end_time
        })

    def get_schedule(self) -> List[Dict[str, str]]:
        """Return the guard's schedule."""
        return self.schedule


class PatrolRoute:
    """Class to represent a patrol route."""
    
    def __init__(self, route_name: str):
        self.route_name = route_name
        self.checkpoints: List[str] = []  # List to hold route checkpoints

    def add_checkpoint(self, checkpoint: str) -> None:
        """Add a checkpoint to the patrol route."""
        self.checkpoints.append(checkpoint)

    def get_route(self) -> List[str]:
        """Return the patrol route checkpoints."""
        return self.checkpoints


class SecurityScheduleManager:
    """Class to manage security guard schedules and patrol routes."""
    
    def __init__(self):
        self.guards: Dict[int, SecurityGuard] = {}  # Dictionary to hold guards by ID
        self.routes: Dict[str, PatrolRoute] = {}  # Dictionary to hold routes by name

    def add_guard(self, name: str, id: int) -> None:
        """Add a new security guard."""
        if id in self.guards:
            raise ValueError(f"Guard with ID {id} already exists.")
        self.guards[id] = SecurityGuard(name, id)

    def add_route(self, route_name: str) -> None:
        """Add a new patrol route."""
        if route_name in self.routes:
            raise ValueError(f"Route '{route_name}' already exists.")
        self.routes[route_name] = PatrolRoute(route_name)

    def assign_shift(self, guard_id: int, start_time: str, end_time: str) -> None:
        """Assign a shift to a guard."""
        if guard_id not in self.guards:
            raise ValueError(f"Guard with ID {guard_id} does not exist.")
        self.guards[guard_id].add_shift(start_time, end_time)

    def assign_route(self, route_name: str, guard_id: int) -> None:
        """Assign a patrol route to a guard."""
        if route_name not in self.routes:
            raise ValueError(f"Route '{route_name}' does not exist.")
        if guard_id not in self.guards:
            raise ValueError(f"Guard with ID {guard_id} does not exist.")
        # Here you could implement logic to associate a route with a guard

    def save_to_file(self, filename: str) -> None:
        """Save the current schedule and routes to a JSON file."""
        data = {
            'guards': {guard_id: guard.get_schedule() for guard_id, guard in self.guards.items()},
            'routes': {route_name: route.get_route() for route_name, route in self.routes.items()}
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load the schedule and routes from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for guard_id, shifts in data['guards'].items():
                    self.guards[int(guard_id)] = SecurityGuard(name=f"Guard {guard_id}", id=int(guard_id))
                    for shift in shifts:
                        self.guards[int(guard_id)].add_shift(shift['start_time'], shift['end_time'])
                for route_name, checkpoints in data['routes'].items():
                    self.routes[route_name] = PatrolRoute(route_name)
                    for checkpoint in checkpoints:
                        self.routes[route_name].add_checkpoint(checkpoint)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    manager = SecurityScheduleManager()
    
    # Adding guards
    manager.add_guard("Alice", 1)
    manager.add_guard("Bob", 2)

    # Adding patrol routes
    manager.add_route("Main Entrance")
    manager.add_route("Parking Lot")

    # Assigning shifts
    manager.assign_shift(1, "2023-10-01T08:00:00", "2023-10-01T16:00:00")
    manager.assign_shift(2, "2023-10-01T16:00:00", "2023-10-02T00:00:00")

    # Assigning routes (this is a placeholder for future implementation)
    manager.assign_route("Main Entrance", 1)
    manager.assign_route("Parking Lot", 2)

    # Saving to file
    manager.save_to_file("security_schedule.json")

    # Loading from file
    manager.load_from_file("security_schedule.json")
```
