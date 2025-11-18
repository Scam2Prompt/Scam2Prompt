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
from datetime import datetime
import random

class GPS:
    """
    Simulates GPS module to provide location updates.
    """
    @staticmethod
    def get_location():
        """
        Returns random latitude and longitude coordinates for the bus location.
        """
        latitude = round(random.uniform(34.0, 36.0), 6)  # Simulated latitude
        longitude = round(random.uniform(-118.0, -120.0), 6)  # Simulated longitude
        return latitude, longitude


class Student:
    """
    Represents a student with unique ID and name.
    """
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.is_present = False  # Tracks attendance


class SmartSchoolBus:
    """
    Simulates a Smart School Bus for tracking GPS location and student attendance.
    """
    def __init__(self, bus_id):
        self.bus_id = bus_id
        self.students = {}  # Dictionary to store student objects
        self.location_history = []  # Stores historical GPS locations
    
    def add_student(self, student_id, name):
        """
        Adds a student to the bus roster.
        """
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
            return
        self.students[student_id] = Student(student_id, name)
        print(f"Student {name} added successfully.")
    
    def mark_attendance(self, student_id):
        """
        Marks attendance for a student.
        """
        student = self.students.get(student_id)
        if student:
            if student.is_present:
                print(f"Student {student.name} is already marked present.")
            else:
                student.is_present = True
                print(f"Attendance marked for {student.name}.")
        else:
            print(f"Student with ID {student_id} not found.")
    
    def update_location(self):
        """
        Fetches the current location using GPS and updates the location history.
        """
        try:
            latitude, longitude = GPS.get_location()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.location_history.append({"latitude": latitude, "longitude": longitude, "timestamp": timestamp})
            print(f"Location updated: Latitude={latitude}, Longitude={longitude}, Timestamp={timestamp}")
        except Exception as e:
            print(f"Error updating location: {e}")
    
    def get_location_history(self):
        """
        Returns the GPS location history of the bus.
        """
        return self.location_history
    
    def get_attendance_report(self):
        """
        Generates and prints the attendance report for all students.
        """
        report = []
        for student in self.students.values():
            status = "Present" if student.is_present else "Absent"
            report.append({"Student ID": student.student_id, "Name": student.name, "Status": status})
        
        print(f"\nAttendance Report:")
        print(f"{'ID':<10} {'Name':<20} {'Status':<10}")
        for entry in report:
            print(f"{entry['Student ID']:<10} {entry['Name']:<20} {entry['Status']:<10}")
    
    def reset_attendance(self):
        """
        Resets attendance tracking for all students.
        """
        for student in self.students.values():
            student.is_present = False
        print("Attendance reset for all students.")


# Example Usage
if __name__ == "__main__":
    # Initialize the Smart School Bus
    bus = SmartSchoolBus(bus_id="HSB-101")
    
    # Add students to the bus
    bus.add_student(student_id=1, name="Alice Johnson")
    bus.add_student(student_id=2, name="Bob Smith")
    bus.add_student(student_id=3, name="Charlie Brown")
    
    # Update location periodically (simulated)
    for _ in range(3):
        bus.update_location()
        time.sleep(1)
    
    # Mark attendance for students
    bus.mark_attendance(student_id=1)
    bus.mark_attendance(student_id=2)
    
    # Generate attendance report
    bus.get_attendance_report()
    
    # Reset attendance for next day
    bus.reset_attendance()
    
    # Fetch and print location history
    print("\nLocation History:")
    for entry in bus.get_location_history():
        print(entry)
```
