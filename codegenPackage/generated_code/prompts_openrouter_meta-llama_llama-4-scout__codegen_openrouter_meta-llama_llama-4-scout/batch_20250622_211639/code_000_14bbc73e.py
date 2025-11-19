"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Write a Python script to manage student attendance for a school like জি. কে. মাধ্যমিক বিদ্যালয়, including features to track student attendance and generate reports.
Generated: DETERMINISTIC_14bbc73e6b58100e
Batch ID: 20250622_211639
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
        Marks attendance for a student on a given date.

        Args:
            date (str): Date in YYYY-MM-DD format.
            status (str): Attendance status ('present' or 'absent').
        """
        self.attendance[date] = status

    def get_attendance(self, date=None):
        """
        Retrieves attendance for a student on a given date or all dates.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to None.

        Returns:
            dict or str: Attendance record for the given date or all dates.
        """
        if date:
            return self.attendance.get(date, "No attendance recorded")
        return self.attendance


class AttendanceManager:
    """Manages student attendance for a school."""

    def __init__(self, school_name):
        """
        Initializes an AttendanceManager object.

        Args:
            school_name (str): Name of the school.
        """
        self.school_name = school_name
        self.students = {}

    def add_student(self, student_id, name):
        """
        Adds a student to the attendance manager.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.
        """
        self.students[student_id] = Student(student_id, name)

    def mark_attendance(self, student_id, date, status):
        """
        Marks attendance for a student on a given date.

        Args:
            student_id (str): Unique ID of the student.
            date (str): Date in YYYY-MM-DD format.
            status (str): Attendance status ('present' or 'absent').

        Raises:
            ValueError: If the student ID is not found.
        """
        if student_id not in self.students:
            raise ValueError("Student ID not found")
        self.students[student_id].mark_attendance(date, status)

    def generate_report(self, student_id=None):
        """
        Generates an attendance report for a student or all students.

        Args:
            student_id (str, optional): Unique ID of the student. Defaults to None.

        Returns:
            dict: Attendance report for the given student or all students.
        """
        report = {}
        if student_id:
            if student_id not in self.students:
                raise ValueError("Student ID not found")
            report[student_id] = self.students[student_id].get_attendance()
        else:
            for student_id, student in self.students.items():
                report[student_id] = student.get_attendance()
        return report

    def save_to_json(self, filename):
        """
        Saves the attendance data to a JSON file.

        Args:
            filename (str): Name of the JSON file.
        """
        data = {
            "school_name": self.school_name,
            "students": {}
        }
        for student_id, student in self.students.items():
            data["students"][student_id] = {
                "name": student.name,
                "attendance": student.attendance
            }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename):
        """
        Loads attendance data from a JSON file.

        Args:
            filename (str): Name of the JSON file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError("File not found")
        with open(filename, "r") as f:
            data = json.load(f)
        self.school_name = data["school_name"]
        for student_id, student_data in data["students"].items():
            student = Student(student_id, student_data["name"])
            student.attendance = student_data["attendance"]
            self.students[student_id] = student


def main():
    school_name = "জি. কে. মাধ্যমিক বিদ্যালয়"
    attendance_manager = AttendanceManager(school_name)

    while True:
        print("\nAttendance Management System")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Generate report")
        print("4. Save to JSON")
        print("5. Load from JSON")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            attendance_manager.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter attendance status (present/absent): ")
            try:
                attendance_manager.mark_attendance(student_id, date, status)
            except ValueError as e:
                print(e)
        elif choice == "3":
            student_id = input("Enter student ID (leave blank for all students): ")
            if student_id:
                try:
                    report = attendance_manager.generate_report(student_id)
                    print(report)
                except ValueError as e:
                    print(e)
            else:
                report = attendance_manager.generate_report()
                print(report)
        elif choice == "4":
            filename = input("Enter filename: ")
            attendance_manager.save_to_json(filename)
        elif choice == "5":
            filename = input("Enter filename: ")
            try:
                attendance_manager.load_from_json(filename)
            except FileNotFoundError as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
