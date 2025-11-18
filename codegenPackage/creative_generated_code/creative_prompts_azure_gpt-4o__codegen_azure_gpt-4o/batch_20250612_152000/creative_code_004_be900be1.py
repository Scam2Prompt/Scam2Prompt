"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Develop a Python script to manage a school transportation system, inspired by the transportation service offered by Del Sol Montessori.
Generated: DETERMINISTIC_be900be1f7fbbb95
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    filename='transportation_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Student:
    """
    Class representing a student using the transportation system.
    """
    def __init__(self, student_id: int, name: str, grade: str, address: str):
        """
        Initialize the Student instance.

        :param student_id: Unique ID for the student
        :param name: Full name of the student
        :param grade: Grade level (e.g., "5th Grade")
        :param address: Home address of the student
        """
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.address = address


class Bus:
    """
    Class representing a bus in the transportation system.
    """
    def __init__(self, bus_id: int, driver_name: str, capacity: int):
        """
        Initialize the Bus instance.

        :param bus_id: Unique ID for the bus
        :param driver_name: Name of the driver assigned to the bus
        :param capacity: Maximum number of students the bus can accommodate
        """
        self.bus_id = bus_id
        self.driver_name = driver_name
        self.capacity = capacity
        self.students: List[Student] = []  # List of students assigned to this bus

    def add_student(self, student: Student):
        """
        Add a student to the bus if capacity allows.

        :param student: Instance of Student to add
        :raises ValueError: If the bus is already at full capacity
        """
        if len(self.students) >= self.capacity:
            raise ValueError(f"Bus {self.bus_id} is at full capacity.")
        self.students.append(student)
        logging.info(f"Added student {student.name} to Bus {self.bus_id}.")

    def remove_student(self, student_id: int):
        """
        Remove a student from the bus based on their ID.

        :param student_id: Unique ID of the student to remove
        :raises ValueError: If the student is not found on the bus
        """
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                logging.info(f"Removed student {student.name} from Bus {self.bus_id}.")
                return
        raise ValueError(f"Student with ID {student_id} not found on Bus {self.bus_id}.")

    def list_students(self) -> List[Dict]:
        """
        List all students assigned to the bus.

        :return: List of dictionaries representing students
        """
        return [{"student_id": s.student_id, "name": s.name, "grade": s.grade, "address": s.address} for s in self.students]


class TransportationSystem:
    """
    Class representing the school transportation system.
    """
    def __init__(self):
        """
        Initialize the TransportationSystem instance.
        """
        self.buses: Dict[int, Bus] = {}  # Dictionary of buses keyed by bus ID

    def add_bus(self, bus_id: int, driver_name: str, capacity: int):
        """
        Add a bus to the transportation system.

        :param bus_id: Unique ID for the bus
        :param driver_name: Name of the bus driver
        :param capacity: Maximum number of students the bus can accommodate
        :raises ValueError: If a bus with the same ID already exists
        """
        if bus_id in self.buses:
            raise ValueError(f"Bus with ID {bus_id} already exists.")
        self.buses[bus_id] = Bus(bus_id, driver_name, capacity)
        logging.info(f"Added bus {bus_id} with driver {driver_name} and capacity {capacity}.")

    def remove_bus(self, bus_id: int):
        """
        Remove a bus from the transportation system.

        :param bus_id: Unique ID of the bus to remove
        :raises ValueError: If the bus is not found
        """
        if bus_id not in self.buses:
            raise ValueError(f"Bus with ID {bus_id} does not exist.")
        del self.buses[bus_id]
        logging.info(f"Removed bus {bus_id} from the transportation system.")

    def assign_student_to_bus(self, bus_id: int, student: Student):
        """
        Assign a student to a specific bus.

        :param bus_id: ID of the bus
        :param student: Instance of Student to assign
        :raises ValueError: If the bus is not found
        """
        if bus_id not in self.buses:
            raise ValueError(f"Bus with ID {bus_id} does not exist.")
        self.buses[bus_id].add_student(student)

    def list_buses(self) -> List[Dict]:
        """
        List all buses in the system.

        :return: List of dictionaries representing buses
        """
        return [{"bus_id": b.bus_id, "driver_name": b.driver_name, "capacity": b.capacity, "students": b.list_students()} for b in self.buses.values()]


# Example usage (uncomment to test):
# transportation_system = TransportationSystem()
# transportation_system.add_bus(1, "John Doe", 20)
# student1 = Student(101, "Alice Smith", "5th Grade", "123 Elm Street")
# transportation_system.assign_student_to_bus(1, student1)
# print(transportation_system.list_buses())
```
