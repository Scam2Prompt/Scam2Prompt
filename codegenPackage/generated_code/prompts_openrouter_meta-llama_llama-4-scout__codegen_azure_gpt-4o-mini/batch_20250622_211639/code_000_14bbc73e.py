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
import csv
from datetime import datetime

class AttendanceManager:
    def __init__(self, filename='attendance.csv'):
        """
        Initializes the AttendanceManager with a specified CSV filename.
        :param filename: The name of the CSV file to store attendance records.
        """
        self.filename = filename
        self.attendance_data = self.load_attendance()

    def load_attendance(self):
        """
        Loads attendance data from the CSV file.
        :return: A dictionary with student IDs as keys and their attendance records as values.
        """
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                return {row['student_id']: row for row in reader}
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading attendance data: {e}")
            return {}

    def mark_attendance(self, student_id, date, status):
        """
        Marks the attendance for a student on a specific date.
        :param student_id: The ID of the student.
        :param date: The date of attendance.
        :param status: The attendance status ('Present' or 'Absent').
        """
        if student_id not in self.attendance_data:
            self.attendance_data[student_id] = {'student_id': student_id, 'attendance': {}}
        
        self.attendance_data[student_id]['attendance'][date] = status
        self.save_attendance()

    def save_attendance(self):
        """
        Saves the current attendance data to the CSV file.
        """
        try:
            with open(self.filename, mode='w', newline='') as file:
                fieldnames = ['student_id', 'attendance']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student_id, data in self.attendance_data.items():
                    writer.writerow({
                        'student_id': student_id,
                        'attendance': str(data['attendance'])
                    })
        except Exception as e:
            print(f"Error saving attendance data: {e}")

    def generate_report(self):
        """
        Generates a report of attendance for all students.
        :return: A string representation of the attendance report.
        """
        report = "Attendance Report\n"
        report += "Student ID | Attendance\n"
        report += "-" * 30 + "\n"
        
        for student_id, data in self.attendance_data.items():
            report += f"{student_id} | {data['attendance']}\n"
        
        return report

def main():
    manager = AttendanceManager()
    
    # Example usage
    while True:
        print("\n1. Mark Attendance")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter status (Present/Absent): ")
            manager.mark_attendance(student_id, date, status)
            print("Attendance marked successfully.")
        elif choice == '2':
            report = manager.generate_report()
            print(report)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
