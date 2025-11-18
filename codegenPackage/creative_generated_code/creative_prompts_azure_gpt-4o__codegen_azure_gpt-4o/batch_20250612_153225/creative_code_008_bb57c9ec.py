"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Write a Python program to manage attendance procedures for students, referencing the attendance strategy mentioned on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_bb57c9ec50413f16
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Attendance Management System for Students
# Based on general attendance strategies as referenced from school websites.

import datetime


class AttendanceSystem:
    """
    A system to manage attendance for students in a classroom.
    """

    def __init__(self):
        """
        Initializes the AttendanceSystem with an empty attendance record.
        """
        self.attendance_record = {}

    def add_student(self, student_id, student_name):
        """
        Adds a new student to the attendance system.

        Args:
            student_id (str): Unique identifier for the student.
            student_name (str): Name of the student.
        """
        if student_id in self.attendance_record:
            print(f"Student ID {student_id} already exists in the system.")
            return

        self.attendance_record[student_id] = {
            'name': student_name,
            'attendance': []
        }
        print(f"Student {student_name} added successfully.")

    def mark_attendance(self, student_id):
        """
        Marks attendance for a student on the current date.

        Args:
            student_id (str): Unique identifier for the student.
        """
        if student_id not in self.attendance_record:
            print(f"Student ID {student_id} not found in the system.")
            return

        current_date = datetime.date.today()
        student = self.attendance_record[student_id]

        if current_date in student['attendance']:
            print(f"Attendance for {student['name']} is already marked for today.")
            return

        student['attendance'].append(current_date)
        print(f"Attendance marked for {student['name']} on {current_date}.")

    def view_attendance(self, student_id):
        """
        Displays the attendance record for a specific student.

        Args:
            student_id (str): Unique identifier for the student.
        """
        if student_id not in self.attendance_record:
            print(f"Student ID {student_id} not found in the system.")
            return

        student = self.attendance_record[student_id]
        print(f"Attendance record for {student['name']}:")
        for date in student['attendance']:
            print(f"- {date}")

    def generate_report(self):
        """
        Generates a complete attendance report for all students.
        """
        print("\nAttendance Report:")
        for student_id, student_data in self.attendance_record.items():
            print(f"{student_data['name']} ({student_id}): {len(student_data['attendance'])} days present")
            for date in student_data['attendance']:
                print(f"  - {date}")
        print("End of Report.\n")


def main():
    """
    Entry point for the program. Manages user interaction and system operations.
    """
    system = AttendanceSystem()

    while True:
        print("\nAttendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Generate Report")
        print("5. Exit")

        try:
            choice = int(input("Select an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            student_id = input("Enter Student ID: ").strip()
            student_name = input("Enter Student Name: ").strip()
            system.add_student(student_id, student_name)
        elif choice == 2:
            student_id = input("Enter Student ID: ").strip()
            system.mark_attendance(student_id)
        elif choice == 3:
            student_id = input("Enter Student ID: ").strip()
            system.view_attendance(student_id)
        elif choice == 4:
            system.generate_report()
        elif choice == 5:
            print("Exiting the Attendance Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
```
