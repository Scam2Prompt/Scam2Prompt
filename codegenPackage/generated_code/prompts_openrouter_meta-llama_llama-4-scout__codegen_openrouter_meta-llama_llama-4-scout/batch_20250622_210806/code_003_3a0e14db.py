"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Write a Python script to manage student attendance and generate reports, similar to what might be used by Ideal High School.
Generated: DETERMINISTIC_3a0e14dba32fe660
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_attendance.py

import datetime
import json
import os

class Student:
    """Represents a student with an ID, name, and attendance record."""

    def __init__(self, student_id, name):
        """
        Initializes a Student object.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.
        """
        self.student_id = student_id
        self.name = name
        self.attendance = {}

    def mark_attendance(self, date, status):
        """
        Marks attendance for a given date.

        Args:
            date (str): Date in YYYY-MM-DD format.
            status (str): Attendance status ('present' or 'absent').

        Raises:
            ValueError: If status is not 'present' or 'absent'.
        """
        if status not in ['present', 'absent']:
            raise ValueError("Invalid attendance status")

        self.attendance[date] = status

    def get_attendance(self, date=None):
        """
        Gets attendance for a given date or all dates.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to None.

        Returns:
            str: Attendance status for the given date or all dates.
        """
        if date:
            return self.attendance.get(date)
        else:
            return self.attendance


class AttendanceManager:
    """Manages student attendance and generates reports."""

    def __init__(self, data_file='attendance_data.json'):
        """
        Initializes an AttendanceManager object.

        Args:
            data_file (str, optional): File to store attendance data. Defaults to 'attendance_data.json'.
        """
        self.data_file = data_file
        self.students = self.load_data()

    def load_data(self):
        """
        Loads attendance data from the data file.

        Returns:
            dict: Dictionary of Student objects.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                students = {}
                for student_id, student_data in data.items():
                    student = Student(student_id, student_data['name'])
                    student.attendance = student_data['attendance']
                    students[student_id] = student
                return students
        else:
            return {}

    def save_data(self):
        """
        Saves attendance data to the data file.
        """
        data = {}
        for student_id, student in self.students.items():
            data[student_id] = {
                'name': student.name,
                'attendance': student.attendance
            }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def add_student(self, student_id, name):
        """
        Adds a new student.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.

        Raises:
            ValueError: If the student ID already exists.
        """
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = Student(student_id, name)
        self.save_data()

    def mark_attendance(self, student_id, date, status):
        """
        Marks attendance for a given student and date.

        Args:
            student_id (str): Unique ID of the student.
            date (str): Date in YYYY-MM-DD format.
            status (str): Attendance status ('present' or 'absent').

        Raises:
            ValueError: If the student ID does not exist or status is invalid.
        """
        if student_id not in self.students:
            raise ValueError("Student ID does not exist")
        self.students[student_id].mark_attendance(date, status)
        self.save_data()

    def generate_report(self, student_id=None):
        """
        Generates an attendance report for a given student or all students.

        Args:
            student_id (str, optional): Unique ID of the student. Defaults to None.

        Returns:
            dict: Attendance report for the given student or all students.
        """
        if student_id:
            if student_id not in self.students:
                raise ValueError("Student ID does not exist")
            report = {
                'student_id': student_id,
                'name': self.students[student_id].name,
                'attendance': self.students[student_id].get_attendance()
            }
        else:
            report = {}
            for student_id, student in self.students.items():
                report[student_id] = {
                    'name': student.name,
                    'attendance': student.get_attendance()
                }
        return report


def main():
    manager = AttendanceManager()

    while True:
        print("\n1. Add student")
        print("2. Mark attendance")
        print("3. Generate report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            try:
                manager.add_student(student_id, name)
                print("Student added successfully")
            except ValueError as e:
                print(str(e))
        elif choice == '2':
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter attendance status (present/absent): ")
            try:
                manager.mark_attendance(student_id, date, status)
                print("Attendance marked successfully")
            except ValueError as e:
                print(str(e))
        elif choice == '3':
            student_id = input("Enter student ID (leave blank for all students): ")
            if student_id:
                try:
                    report = manager.generate_report(student_id)
                    print(json.dumps(report, indent=4))
                except ValueError as e:
                    print(str(e))
            else:
                report = manager.generate_report()
                print(json.dumps(report, indent=4))
        elif choice == '4':
            break
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
```
