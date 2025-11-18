"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write Python code to simulate a Smart School Bus tracking system for Happy Boarding School, incorporating GPS location updates and student attendance tracking.
Generated: DETERMINISTIC_eb88036bb4bb6de5
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from datetime import datetime

class Student:
    """Class to represent a student."""
    
    def __init__(self, id, name):
        """
        Initializes a Student object.

        Args:
            id (str): Unique identifier for the student.
            name (str): Name of the student.
        """
        self.id = id
        self.name = name
        self.is_present = False

class SchoolBus:
    """Class to represent the school bus."""
    
    def __init__(self, bus_id):
        """
        Initializes a SchoolBus object.

        Args:
            bus_id (str): Unique identifier for the bus.
        """
        self.bus_id = bus_id
        self.current_location = (0.0, 0.0)  # GPS coordinates (latitude, longitude)
        self.students = {}
        self.attendance_log = []

    def add_student(self, student):
        """
        Adds a student to the bus.

        Args:
            student (Student): A Student object to be added to the bus.
        """
        self.students[student.id] = student

    def update_location(self, latitude, longitude):
        """
        Updates the bus current location.

        Args:
            latitude (float): The new latitude.
            longitude (float): The new longitude.
        """
        self.current_location = (latitude, longitude)
        print(f"Bus {self.bus_id} location updated to: {self.current_location}")

    def mark_attendance(self, student_id):
        """
        Marks a student as present and logs the attendance.

        Args:
            student_id (str): The ID of the student to mark as present.
        """
        if student_id in self.students:
            self.students[student_id].is_present = True
            self.attendance_log.append((student_id, datetime.now()))
            print(f"Attendance marked for student ID: {student_id}")
        else:
            print(f"Error: Student ID {student_id} not found on bus {self.bus_id}")

class SmartSchoolBusTrackingSystem:
    """Main class to handle the school bus tracking system."""
    
    def __init__(self):
        """
        Initializes the SmartSchoolBusTrackingSystem object.
        """
        self.buses = {}

    def add_bus(self, bus):
        """
        Adds a bus to the tracking system.

        Args:
            bus (SchoolBus): The SchoolBus object to be added to the system.
        """
        self.buses[bus.bus_id] = bus

    def update_bus_location(self, bus_id, latitude, longitude):
        """
        Updates the location of a specific bus.

        Args:
            bus_id (str): Unique bus identifier.
            latitude (float): New latitude.
            longitude (float): New longitude.
        """
        if bus_id in self.buses:
            self.buses[bus_id].update_location(latitude, longitude)
        else:
            print(f"Error: Bus ID {bus_id} not found.")

    def mark_student_attendance(self, bus_id, student_id):
        """
        Marks attendance for a student on a specific bus.

        Args:
            bus_id (str): Unique bus identifier.
            student_id (str): Unique student identifier.
        """
        if bus_id in self.buses:
            self.buses[bus_id].mark_attendance(student_id)
        else:
            print(f"Error: Bus ID {bus_id} not found.")

# Example usage
if __name__ == "__main__":
    # Create a tracking system instance
    tracking_system = SmartSchoolBusTrackingSystem()

    # Create a bus and add it to the tracking system
    bus_101 = SchoolBus(bus_id="101")
    tracking_system.add_bus(bus_101)

    # Create students and add them to the bus
    student1 = Student(id="S001", name="John Doe")
    student2 = Student(id="S002", name="Jane Smith")
    bus_101.add_student(student1)
    bus_101.add_student(student2)

    # Simulate GPS location updates
    for _ in range(3):
        lat = random.uniform(-90, 90)  # Random latitude
        lon = random.uniform(-180, 180)  # Random longitude
        tracking_system.update_bus_location(bus_id="101", latitude=lat, longitude=lon)
        time.sleep(1)  # Simulate delay

    # Mark attendance for students
    tracking_system.mark_student_attendance(bus_id="101", student_id="S001")
    tracking_system.mark_student_attendance(bus_id="101", student_id="S002")
    # Attempt to mark attendance for a non-existent student
    tracking_system.mark_student_attendance(bus_id="101", student_id="S003")
```
