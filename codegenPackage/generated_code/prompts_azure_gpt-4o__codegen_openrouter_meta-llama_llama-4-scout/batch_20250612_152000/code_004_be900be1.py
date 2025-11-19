"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Develop a Python script to manage a school transportation system, inspired by the transportation service offered by Del Sol Montessori.
Generated: DETERMINISTIC_be900be1f7fbbb95
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_transportation_system.py

class Student:
    """Represents a student in the school transportation system."""

    def __init__(self, student_id, name, pickup_location, dropoff_location):
        """
        Initializes a Student object.

        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
            pickup_location (str): Pickup location of the student.
            dropoff_location (str): Dropoff location of the student.
        """
        self.student_id = student_id
        self.name = name
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Pickup Location: {self.pickup_location}, Dropoff Location: {self.dropoff_location}"


class Bus:
    """Represents a bus in the school transportation system."""

    def __init__(self, bus_id, capacity):
        """
        Initializes a Bus object.

        Args:
            bus_id (int): Unique identifier for the bus.
            capacity (int): Maximum capacity of the bus.
        """
        self.bus_id = bus_id
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        """
        Adds a student to the bus.

        Args:
            student (Student): Student to be added.

        Raises:
            ValueError: If the bus is already at capacity.
        """
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            raise ValueError("Bus is already at capacity.")

    def remove_student(self, student_id):
        """
        Removes a student from the bus.

        Args:
            student_id (int): ID of the student to be removed.

        Raises:
            ValueError: If the student is not found on the bus.
        """
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        raise ValueError("Student not found on the bus.")

    def __str__(self):
        bus_info = f"Bus ID: {self.bus_id}, Capacity: {self.capacity}, Current Students: {len(self.students)}\n"
        student_info = "\n".join([str(student) for student in self.students])
        return bus_info + student_info


class TransportationSystem:
    """Represents the school transportation system."""

    def __init__(self):
        self.buses = []
        self.students = {}

    def add_bus(self, bus):
        """
        Adds a bus to the transportation system.

        Args:
            bus (Bus): Bus to be added.
        """
        self.buses.append(bus)

    def add_student(self, student):
        """
        Adds a student to the transportation system.

        Args:
            student (Student): Student to be added.
        """
        self.students[student.student_id] = student

    def assign_student_to_bus(self, student_id, bus_id):
        """
        Assigns a student to a bus.

        Args:
            student_id (int): ID of the student.
            bus_id (int): ID of the bus.

        Raises:
            ValueError: If the student or bus is not found.
        """
        student = self.students.get(student_id)
        if student is None:
            raise ValueError("Student not found.")
        bus = next((bus for bus in self.buses if bus.bus_id == bus_id), None)
        if bus is None:
            raise ValueError("Bus not found.")
        bus.add_student(student)

    def __str__(self):
        system_info = "School Transportation System:\n"
        bus_info = "\n\n".join([str(bus) for bus in self.buses])
        return system_info + bus_info


def main():
    try:
        # Create transportation system
        system = TransportationSystem()

        # Create buses
        bus1 = Bus(1, 50)
        bus2 = Bus(2, 60)

        # Add buses to system
        system.add_bus(bus1)
        system.add_bus(bus2)

        # Create students
        student1 = Student(1, "John Doe", "Location 1", "Location 2")
        student2 = Student(2, "Jane Doe", "Location 3", "Location 4")

        # Add students to system
        system.add_student(student1)
        system.add_student(student2)

        # Assign students to buses
        system.assign_student_to_bus(1, 1)
        system.assign_student_to_bus(2, 2)

        # Print system information
        print(system)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
