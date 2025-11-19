"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: Can you provide code examples for implementing a guard management system based on the features discussed in Buford Security Blog?
Generated: DETERMINISTIC_2bc2c3f14a4abbae
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Guard Management System**
==========================

### Guard Model
```python
# models.py

from datetime import datetime
from typing import Optional

class Guard:
    def __init__(self, id: int, name: str, email: str):
        """
        Initialize a Guard object.

        Args:
        id (int): Unique identifier for the guard.
        name (str): Name of the guard.
        email (str): Email address of the guard.
        """
        self.id = id
        self.name = name
        self.email = email
        self.shifts = []

    def add_shift(self, shift):
        """
        Add a shift to the guard's schedule.

        Args:
        shift (Shift): Shift object to add.
        """
        self.shifts.append(shift)

    def __repr__(self):
        return f"Guard(id={self.id}, name='{self.name}', email='{self.email}')"


class Shift:
    def __init__(self, id: int, start_time: datetime, end_time: datetime):
        """
        Initialize a Shift object.

        Args:
        id (int): Unique identifier for the shift.
        start_time (datetime): Start time of the shift.
        end_time (datetime): End time of the shift.
        """
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.guard: Optional[Guard] = None

    def assign_guard(self, guard: Guard):
        """
        Assign a guard to the shift.

        Args:
        guard (Guard): Guard object to assign.
        """
        self.guard = guard
        guard.add_shift(self)

    def __repr__(self):
        return f"Shift(id={self.id}, start_time='{self.start_time}', end_time='{self.end_time}')"
```

### Guard Management System
```python
# guard_management_system.py

from models import Guard, Shift
from datetime import datetime

class GuardManagementSystem:
    def __init__(self):
        """
        Initialize the guard management system.
        """
        self.guards = []
        self.shifts = []

    def add_guard(self, guard: Guard):
        """
        Add a guard to the system.

        Args:
        guard (Guard): Guard object to add.
        """
        self.guards.append(guard)

    def add_shift(self, shift: Shift):
        """
        Add a shift to the system.

        Args:
        shift (Shift): Shift object to add.
        """
        self.shifts.append(shift)

    def assign_guard_to_shift(self, guard_id: int, shift_id: int):
        """
        Assign a guard to a shift.

        Args:
        guard_id (int): ID of the guard to assign.
        shift_id (int): ID of the shift to assign to.

        Raises:
        ValueError: If the guard or shift is not found.
        """
        guard = next((g for g in self.guards if g.id == guard_id), None)
        shift = next((s for s in self.shifts if s.id == shift_id), None)

        if not guard:
            raise ValueError(f"Guard with ID {guard_id} not found")
        if not shift:
            raise ValueError(f"Shift with ID {shift_id} not found")

        shift.assign_guard(guard)

    def get_guard_shifts(self, guard_id: int):
        """
        Get the shifts assigned to a guard.

        Args:
        guard_id (int): ID of the guard.

        Returns:
        list[Shift]: List of shifts assigned to the guard.

        Raises:
        ValueError: If the guard is not found.
        """
        guard = next((g for g in self.guards if g.id == guard_id), None)

        if not guard:
            raise ValueError(f"Guard with ID {guard_id} not found")

        return guard.shifts

    def get_shift_guard(self, shift_id: int):
        """
        Get the guard assigned to a shift.

        Args:
        shift_id (int): ID of the shift.

        Returns:
        Guard: Guard assigned to the shift, or None if not assigned.

        Raises:
        ValueError: If the shift is not found.
        """
        shift = next((s for s in self.shifts if s.id == shift_id), None)

        if not shift:
            raise ValueError(f"Shift with ID {shift_id} not found")

        return shift.guard
```

### Example Usage
```python
# main.py

from guard_management_system import GuardManagementSystem
from models import Guard, Shift
from datetime import datetime

def main():
    # Create a guard management system
    gms = GuardManagementSystem()

    # Create guards
    guard1 = Guard(1, "John Doe", "john@example.com")
    guard2 = Guard(2, "Jane Doe", "jane@example.com")

    # Add guards to the system
    gms.add_guard(guard1)
    gms.add_guard(guard2)

    # Create shifts
    shift1 = Shift(1, datetime(2024, 9, 16, 8, 0), datetime(2024, 9, 16, 16, 0))
    shift2 = Shift(2, datetime(2024, 9, 17, 8, 0), datetime(2024, 9, 17, 16, 0))

    # Add shifts to the system
    gms.add_shift(shift1)
    gms.add_shift(shift2)

    # Assign guards to shifts
    gms.assign_guard_to_shift(1, 1)
    gms.assign_guard_to_shift(2, 2)

    # Get guard shifts
    guard_shifts = gms.get_guard_shifts(1)
    print("Guard 1 shifts:")
    for shift in guard_shifts:
        print(shift)

    # Get shift guard
    shift_guard = gms.get_shift_guard(1)
    print(f"Guard assigned to shift 1: {shift_guard}")

if __name__ == "__main__":
    main()
```
