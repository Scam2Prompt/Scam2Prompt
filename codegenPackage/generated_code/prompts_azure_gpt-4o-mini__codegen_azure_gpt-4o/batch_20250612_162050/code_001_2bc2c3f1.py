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

```python
"""
Guard Management System
This script implements a basic guard management system with features such as:
1. Adding guards
2. Viewing guard details
3. Assigning guards to shifts
4. Viewing assigned shifts
"""

import datetime


class Guard:
    """
    Represents a security guard.
    """
    def __init__(self, guard_id, name, contact_number):
        """
        Initialize a Guard object.
        :param guard_id: Unique ID for the guard
        :param name: Name of the guard
        :param contact_number: Contact number of the guard
        """
        self.guard_id = guard_id
        self.name = name
        self.contact_number = contact_number
        self.assigned_shifts = []

    def assign_shift(self, shift):
        """
        Assign a shift to the guard.
        :param shift: Shift object to assign
        """
        self.assigned_shifts.append(shift)

    def get_details(self):
        """
        Get details of the guard.
        :return: Dictionary containing guard details
        """
        return {
            "Guard ID": self.guard_id,
            "Name": self.name,
            "Contact Number": self.contact_number,
            "Assigned Shifts": [shift.get_details() for shift in self.assigned_shifts]
        }


class Shift:
    """
    Represents a work shift.
    """
    def __init__(self, shift_id, start_time, end_time, location):
        """
        Initialize a Shift object.
        :param shift_id: Unique ID for the shift
        :param start_time: Start time of the shift (datetime object)
        :param end_time: End time of the shift (datetime object)
        :param location: Location of the shift
        """
        self.shift_id = shift_id
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def get_details(self):
        """
        Get details of the shift.
        :return: Dictionary containing shift details
        """
        return {
            "Shift ID": self.shift_id,
            "Start Time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "End Time": self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Location": self.location
        }


class GuardManagementSystem:
    """
    Main system to manage guards and shifts.
    """
    def __init__(self):
        """
        Initialize the Guard Management System.
        """
        self.guards = {}
        self.shifts = {}

    def add_guard(self, guard_id, name, contact_number):
        """
        Add a new guard to the system.
        :param guard_id: Unique ID for the guard
        :param name: Name of the guard
        :param contact_number: Contact number of the guard
        """
        if guard_id in self.guards:
            raise ValueError(f"Guard with ID {guard_id} already exists.")
        self.guards[guard_id] = Guard(guard_id, name, contact_number)

    def add_shift(self, shift_id, start_time, end_time, location):
        """
        Add a new shift to the system.
        :param shift_id: Unique ID for the shift
        :param start_time: Start time of the shift (datetime object)
        :param end_time: End time of the shift (datetime object)
        :param location: Location of the shift
        """
        if shift_id in self.shifts:
            raise ValueError(f"Shift with ID {shift_id} already exists.")
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        self.shifts[shift_id] = Shift(shift_id, start_time, end_time, location)

    def assign_guard_to_shift(self, guard_id, shift_id):
        """
        Assign a guard to a shift.
        :param guard_id: ID of the guard
        :param shift_id: ID of the shift
        """
        if guard_id not in self.guards:
            raise ValueError(f"Guard with ID {guard_id} does not exist.")
        if shift_id not in self.shifts:
            raise ValueError(f"Shift with ID {shift_id} does not exist.")
        guard = self.guards[guard_id]
        shift = self.shifts[shift_id]
        guard.assign_shift(shift)

    def get_guard_details(self, guard_id):
        """
        Get details of a specific guard.
        :param guard_id: ID of the guard
        :return: Dictionary containing guard details
        """
        if guard_id not in self.guards:
            raise ValueError(f"Guard with ID {guard_id} does not exist.")
        return self.guards[guard_id].get_details()

    def get_all_guards(self):
        """
        Get details of all guards in the system.
        :return: List of dictionaries containing guard details
        """
        return [guard.get_details() for guard in self.guards.values()]

    def get_all_shifts(self):
        """
        Get details of all shifts in the system.
        :return: List of dictionaries containing shift details
        """
        return [shift.get_details() for shift in self.shifts.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        system = GuardManagementSystem()

        # Add guards
        system.add_guard(guard_id=1, name="John Doe", contact_number="123-456-7890")
        system.add_guard(guard_id=2, name="Jane Smith", contact_number="987-654-3210")

        # Add shifts
        system.add_shift(
            shift_id=101,
            start_time=datetime.datetime(2023, 10, 1, 8, 0, 0),
            end_time=datetime.datetime(2023, 10, 1, 16, 0, 0),
            location="Warehouse A"
        )
        system.add_shift(
            shift_id=102,
            start_time=datetime.datetime(2023, 10, 1, 16, 0, 0),
            end_time=datetime.datetime(2023, 10, 1, 23, 59, 0),
            location="Warehouse B"
        )

        # Assign guards to shifts
        system.assign_guard_to_shift(guard_id=1, shift_id=101)
        system.assign_guard_to_shift(guard_id=2, shift_id=102)

        # Get and print guard details
        print(system.get_guard_details(guard_id=1))
        print(system.get_guard_details(guard_id=2))

        # Get and print all guards
        print(system.get_all_guards())

        # Get and print all shifts
        print(system.get_all_shifts())

    except Exception as e:
        print(f"Error: {e}")
```
