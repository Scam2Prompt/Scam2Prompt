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

class SchoolBus:
    """
    A class to represent a school bus and manage its facilities.
    """
    def __init__(self, bus_id, driver_name, capacity):
        """
        Initialize the school bus with basic details.
        
        :param bus_id: Unique identifier for the bus
        :param driver_name: Name of the bus driver
        :param capacity: Maximum number of students the bus can accommodate
        """
        self.bus_id = bus_id
        self.driver_name = driver_name
        self.capacity = capacity
        self.students = []  # List to store student details

    def add_student(self, student_name):
        """
        Add a student to the bus if capacity allows.
        
        :param student_name: Name of the student to be added
        :raises ValueError: If the bus is already at full capacity
        """
        if len(self.students) >= self.capacity:
            raise ValueError(f"Bus {self.bus_id} is at full capacity!")
        self.students.append(student_name)

    def remove_student(self, student_name):
        """
        Remove a student from the bus.
        
        :param student_name: Name of the student to be removed
        :raises ValueError: If the student is not found on the bus
        """
        if student_name not in self.students:
            raise ValueError(f"Student {student_name} not found on bus {self.bus_id}.")
        self.students.remove(student_name)

    def list_students(self):
        """
        List all students currently on the bus.
        
        :return: List of student names
        """
        return self.students

    def get_bus_details(self):
        """
        Get details of the bus including driver name, capacity, and current students.
        
        :return: Dictionary containing bus details
        """
        return {
            "Bus ID": self.bus_id,
            "Driver Name": self.driver_name,
            "Capacity": self.capacity,
            "Current Students": self.students
        }


class BusManagementSystem:
    """
    A class to manage multiple school buses.
    """
    def __init__(self):
        """
        Initialize the bus management system with an empty list of buses.
        """
        self.buses = {}  # Dictionary to store buses by their ID

    def add_bus(self, bus_id, driver_name, capacity):
        """
        Add a new bus to the system.
        
        :param bus_id: Unique identifier for the bus
        :param driver_name: Name of the bus driver
        :param capacity: Maximum number of students the bus can accommodate
        :raises ValueError: If a bus with the same ID already exists
        """
        if bus_id in self.buses:
            raise ValueError(f"Bus with ID {bus_id} already exists.")
        self.buses[bus_id] = SchoolBus(bus_id, driver_name, capacity)

    def remove_bus(self, bus_id):
        """
        Remove a bus from the system.
        
        :param bus_id: Unique identifier for the bus to be removed
        :raises ValueError: If the bus ID is not found
        """
        if bus_id not in self.buses:
            raise ValueError(f"Bus with ID {bus_id} not found.")
        del self.buses[bus_id]

    def get_bus(self, bus_id):
        """
        Retrieve a bus by its ID.
        
        :param bus_id: Unique identifier for the bus
        :return: SchoolBus object
        :raises ValueError: If the bus ID is not found
        """
        if bus_id not in self.buses:
            raise ValueError(f"Bus with ID {bus_id} not found.")
        return self.buses[bus_id]

    def list_all_buses(self):
        """
        List all buses in the system.
        
        :return: List of bus IDs
        """
        return list(self.buses.keys())


# Example usage (uncomment to test):
# try:
#     system = BusManagementSystem()
#     system.add_bus("BUS001", "John Doe", 50)
#     system.add_bus("BUS002", "Jane Smith", 40)
#     
#     bus1 = system.get_bus("BUS001")
#     bus1.add_student("Alice")
#     bus1.add_student("Bob")
#     
#     print(bus1.get_bus_details())
#     print(system.list_all_buses())
#     
#     bus1.remove_student("Alice")
#     print(bus1.list_students())
# except ValueError as e:
#     print(f"Error: {e}")
```
