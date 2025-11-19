"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write a Python code snippet to manage school bus facilities, similar to Happy Boarding School's SMART SCHOOL BUS system.
Generated: DETERMINISTIC_1f57b98c7ba7173e
Batch ID: 20250622_204903
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
    """Class representing a school bus."""
    
    def __init__(self, bus_id: str, capacity: int):
        """
        Initialize a new Bus instance.

        :param bus_id: Unique identifier for the bus
        :param capacity: Maximum number of students the bus can carry
        """
        self.bus_id = bus_id
        self.capacity = capacity
        self.students: List[str] = []

    def add_student(self, student_name: str) -> bool:
        """
        Add a student to the bus if there is capacity.

        :param student_name: Name of the student to add
        :return: True if the student was added, False if the bus is full
        """
        if len(self.students) < self.capacity:
            self.students.append(student_name)
            return True
        return False

    def remove_student(self, student_name: str) -> bool:
        """
        Remove a student from the bus.

        :param student_name: Name of the student to remove
        :return: True if the student was removed, False if the student was not found
        """
        try:
            self.students.remove(student_name)
            return True
        except ValueError:
            return False

    def get_student_list(self) -> List[str]:
        """Return the list of students currently on the bus."""
        return self.students

class BusManager:
    """Class to manage multiple buses and their operations."""
    
    def __init__(self):
        """Initialize the BusManager with an empty bus list."""
        self.buses: Dict[str, Bus] = {}

    def add_bus(self, bus_id: str, capacity: int) -> None:
        """
        Add a new bus to the manager.

        :param bus_id: Unique identifier for the bus
        :param capacity: Maximum number of students the bus can carry
        """
        if bus_id in self.buses:
            raise ValueError(f"Bus with ID {bus_id} already exists.")
        self.buses[bus_id] = Bus(bus_id, capacity)

    def remove_bus(self, bus_id: str) -> bool:
        """
        Remove a bus from the manager.

        :param bus_id: Unique identifier for the bus
        :return: True if the bus was removed, False if the bus was not found
        """
        return self.buses.pop(bus_id, None) is not None

    def get_bus(self, bus_id: str) -> Optional[Bus]:
        """
        Retrieve a bus by its ID.

        :param bus_id: Unique identifier for the bus
        :return: Bus object if found, None otherwise
        """
        return self.buses.get(bus_id)

    def list_buses(self) -> List[str]:
        """Return a list of all bus IDs managed by the BusManager."""
        return list(self.buses.keys())

# Example usage
if __name__ == "__main__":
    try:
        bus_manager = BusManager()
        bus_manager.add_bus("Bus101", 30)
        bus_manager.add_bus("Bus102", 25)

        bus = bus_manager.get_bus("Bus101")
        if bus:
            bus.add_student("Alice")
            bus.add_student("Bob")
            print(f"Students on {bus.bus_id}: {bus.get_student_list()}")

        bus.remove_student("Alice")
        print(f"Students on {bus.bus_id} after removal: {bus.get_student_list()}")

        print(f"All buses managed: {bus_manager.list_buses()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
