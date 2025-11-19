"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: How can I implement attendance tracking in a school management system similar to Him Saral's features?
Generated: DETERMINISTIC_9a24181c89c1a3c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Attendance Tracking System**
================================

### Models

```python
# models.py
from datetime import datetime
from typing import Optional

class Student:
    def __init__(self, student_id: int, name: str):
        """
        Initialize a Student object.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Name of the student.
        """
        self.student_id = student_id
        self.name = name

class Attendance:
    def __init__(self, student: Student, date: datetime, status: str):
        """
        Initialize an Attendance object.

        Args:
        - student (Student): Student object associated with the attendance record.
        - date (datetime): Date of the attendance record.
        - status (str): Attendance status (e.g., "present", "absent").
        """
        self.student = student
        self.date = date
        self.status = status

class AttendanceRecord:
    def __init__(self):
        """
        Initialize an AttendanceRecord object.
        """
        self.attendance_records = []

    def add_attendance(self, attendance: Attendance):
        """
        Add an attendance record.

        Args:
        - attendance (Attendance): Attendance object to add.
        """
        self.attendance_records.append(attendance)

    def get_attendance(self, student: Student, date: Optional[datetime] = None):
        """
        Get attendance records for a student.

        Args:
        - student (Student): Student object to retrieve attendance records for.
        - date (datetime, optional): Date to filter attendance records by. Defaults to None.

        Returns:
        - list[Attendance]: List of attendance records for the student.
        """
        if date:
            return [record for record in self.attendance_records if record.student.student_id == student.student_id and record.date.date() == date.date()]
        else:
            return [record for record in self.attendance_records if record.student.student_id == student.student_id]
```

### Services

```python
# services.py
from models import Student, Attendance, AttendanceRecord

class AttendanceService:
    def __init__(self, attendance_record: AttendanceRecord):
        """
        Initialize an AttendanceService object.

        Args:
        - attendance_record (AttendanceRecord): AttendanceRecord object to use.
        """
        self.attendance_record = attendance_record

    def mark_attendance(self, student: Student, status: str):
        """
        Mark attendance for a student.

        Args:
        - student (Student): Student object to mark attendance for.
        - status (str): Attendance status (e.g., "present", "absent").
        """
        attendance = Attendance(student, datetime.now(), status)
        self.attendance_record.add_attendance(attendance)

    def get_student_attendance(self, student: Student):
        """
        Get attendance records for a student.

        Args:
        - student (Student): Student object to retrieve attendance records for.

        Returns:
        - list[Attendance]: List of attendance records for the student.
        """
        return self.attendance_record.get_attendance(student)
```

### Controllers

```python
# controllers.py
from services import AttendanceService
from models import Student, AttendanceRecord

class AttendanceController:
    def __init__(self):
        """
        Initialize an AttendanceController object.
        """
        self.attendance_record = AttendanceRecord()
        self.attendance_service = AttendanceService(self.attendance_record)

    def mark_attendance(self, student_id: int, name: str, status: str):
        """
        Mark attendance for a student.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Name of the student.
        - status (str): Attendance status (e.g., "present", "absent").
        """
        try:
            student = Student(student_id, name)
            self.attendance_service.mark_attendance(student, status)
            print("Attendance marked successfully.")
        except Exception as e:
            print(f"Error marking attendance: {str(e)}")

    def get_student_attendance(self, student_id: int, name: str):
        """
        Get attendance records for a student.

        Args:
        - student_id (int): Unique identifier for the student.
        - name (str): Name of the student.
        """
        try:
            student = Student(student_id, name)
            attendance_records = self.attendance_service.get_student_attendance(student)
            for record in attendance_records:
                print(f"Date: {record.date}, Status: {record.status}")
        except Exception as e:
            print(f"Error retrieving attendance: {str(e)}")
```

### Example Usage

```python
# main.py
from controllers import AttendanceController

def main():
    attendance_controller = AttendanceController()
    while True:
        print("1. Mark Attendance")
        print("2. Get Student Attendance")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            status = input("Enter attendance status (present/absent): ")
            attendance_controller.mark_attendance(student_id, name, status)
        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            attendance_controller.get_student_attendance(student_id, name)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
