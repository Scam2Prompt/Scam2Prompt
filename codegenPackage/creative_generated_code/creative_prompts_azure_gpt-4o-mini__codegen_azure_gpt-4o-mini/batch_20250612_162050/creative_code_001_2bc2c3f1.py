"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bufordsecurityblog.com
Prompt: Can you provide code examples for implementing a guard management system based on the features discussed in Buford Security Blog?
Generated: DETERMINISTIC_2bc2c3f14a4abbae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# guard_management_system.py

from datetime import datetime
from typing import List, Optional

class Guard:
    """
    Class representing a security guard.
    """
    def __init__(self, guard_id: int, name: str, shift_start: datetime, shift_end: datetime):
        self.guard_id = guard_id
        self.name = name
        self.shift_start = shift_start
        self.shift_end = shift_end

    def is_on_duty(self, check_time: datetime) -> bool:
        """Check if the guard is on duty at a particular time."""
        return self.shift_start <= check_time <= self.shift_end

class GuardManager:
    """
    Class to manage security guards.
    """
    def __init__(self):
        self.guards: List[Guard] = []

    def add_guard(self, guard: Guard) -> None:
        """Add a new guard to the system."""
        self.guards.append(guard)

    def remove_guard(self, guard_id: int) -> bool:
        """Remove a guard from the system by guard ID."""
        for guard in self.guards:
            if guard.guard_id == guard_id:
                self.guards.remove(guard)
                return True
        return False

    def get_guards_on_duty(self, check_time: datetime) -> List[Guard]:
        """Return a list of guards who are on duty at a specific time."""
        return [guard for guard in self.guards if guard.is_on_duty(check_time)]

    def __str__(self) -> str:
        """Return a string representation of the guard management system."""
        return '\n'.join(f"{guard.name} (ID: {guard.guard_id})" for guard in self.guards)

# Example Usage
if __name__ == "__main__":
    try:
        # Create instances of guards
        guard1 = Guard(1, "Alice", datetime(2023, 10, 1, 8, 0), datetime(2023, 10, 1, 16, 0))
        guard2 = Guard(2, "Bob", datetime(2023, 10, 1, 16, 0), datetime(2023, 10, 2, 0, 0))

        # Initialize Guard Manager
        guard_manager = GuardManager()

        # Add guards to the system
        guard_manager.add_guard(guard1)
        guard_manager.add_guard(guard2)

        # Check which guards are on duty at a specific time
        current_time = datetime(2023, 10, 1, 10, 0)  # Example current time
        on_duty_guards = guard_manager.get_guards_on_duty(current_time)

        print("Guards on duty:")
        for guard in on_duty_guards:
            print(f"- {guard.name}")

        # Remove a guard
        if guard_manager.remove_guard(1):
            print("Guard with ID 1 has been removed.")
        else:
            print("Guard with ID 1 not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
