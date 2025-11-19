"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write Python code to simulate a Smart School Bus tracking system for Happy Boarding School, incorporating GPS location updates and student attendance tracking.
Generated: DETERMINISTIC_eb88036bb4bb6de5
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_school_bus.py

import datetime
import random
import time
from typing import Dict, List

class Student:
    """Represents a student with an ID and name."""

    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.attended = False

    def mark_attendance(self):
        """Mark the student as attended."""
        self.attended = True


class Bus:
    """Represents a school bus with an ID, current location, and students."""

    def __init__(self, bus_id: int):
        self.bus_id = bus_id
        self.location = (0.0, 0.0)  # Initialize with dummy location
        self.students: List[Student] = []

    def update_location(self, latitude: float, longitude: float):
        """Update the bus location using GPS coordinates."""
        self.location = (latitude, longitude)

    def add_student(self, student: Student):
        """Add a student to the bus."""
        self.students.append(student)

    def get_attendance(self) -> Dict[int, bool]:
        """Get the attendance status of all students on the bus."""
        return {student.student_id: student.attended for student in self.students}


class SmartSchoolBusSystem:
    """Simulates a smart school bus tracking system."""

    def __init__(self):
        self.buses: Dict[int, Bus] = {}

    def add_bus(self, bus: Bus):
        """Add a bus to the system."""
        self.buses[bus.bus_id] = bus

    def get_bus_location(self, bus_id: int) -> tuple:
        """Get the location of a bus by its ID."""
        if bus_id in self.buses:
            return self.buses[bus_id].location
        else:
            raise ValueError("Bus not found")

    def update_bus_location(self, bus_id: int, latitude: float, longitude: float):
        """Update the location of a bus by its ID."""
        if bus_id in self.buses:
            self.buses[bus_id].update_location(latitude, longitude)
        else:
            raise ValueError("Bus not found")

    def mark_student_attendance(self, bus_id: int, student_id: int):
        """Mark a student's attendance by bus ID and student ID."""
        if bus_id in self.buses:
            bus = self.buses[bus_id]
            for student in bus.students:
                if student.student_id == student_id:
                    student.mark_attendance()
                    return
            raise ValueError("Student not found on bus")
        else:
            raise ValueError("Bus not found")


def simulate_gps_updates(bus: Bus):
    """Simulate GPS location updates for a bus."""
    while True:
        # Generate random GPS coordinates
        latitude = random.uniform(37.0, 38.0)
        longitude = random.uniform(-122.0, -121.0)
        bus.update_location(latitude, longitude)
        print(f"Bus {bus.bus_id} location updated to ({latitude}, {longitude})")
        time.sleep(5)  # Update every 5 seconds


def main():
    # Create a smart school bus system
    system = SmartSchoolBusSystem()

    # Create buses
    bus1 = Bus(1)
    bus2 = Bus(2)

    # Add buses to the system
    system.add_bus(bus1)
    system.add_bus(bus2)

    # Create students
    student1 = Student(1, "John Doe")
    student2 = Student(2, "Jane Doe")

    # Add students to buses
    bus1.add_student(student1)
    bus2.add_student(student2)

    # Simulate GPS location updates for buses
    import threading
    threading.Thread(target=simulate_gps_updates, args=(bus1,)).start()
    threading.Thread(target=simulate_gps_updates, args=(bus2,)).start()

    # Mark student attendance
    system.mark_student_attendance(1, 1)
    print(f"Student {student1.student_id} attendance: {system.get_bus_location(1)} - {bus1.get_attendance()}")

    try:
        while True:
            # Get bus location
            print(f"Bus 1 location: {system.get_bus_location(1)}")
            print(f"Bus 2 location: {system.get_bus_location(2)}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
```
