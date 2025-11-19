"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Generate a Python script to create a comprehensive school management system that includes student records, attendance tracking, and fee submission, as described by the Canadian Tech-Institute for Academic Research.
Generated: DETERMINISTIC_8d8cd4a9410699b7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}
        self.fees_paid = False

    def mark_attendance(self, date, present=True):
        """Mark attendance for the student."""
        self.attendance[date] = present

    def pay_fees(self):
        """Mark fees as paid."""
        self.fees_paid = True


class SchoolManagementSystem:
    """Class to manage the school system."""
    
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        self.students[student_id] = Student(student_id, name)

    def mark_student_attendance(self, student_id, date, present=True):
        """Mark attendance for a specific student."""
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        self.students[student_id].mark_attendance(date, present)

    def submit_fee(self, student_id):
        """Submit fee for a specific student."""
        if student_id not in self.students:
            raise ValueError("Student ID not found.")
        self.students[student_id].pay_fees()

    def save_records(self, filename):
        """Save student records to JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self._serialize_students(), file, indent=4)
        except IOError as e:
            print(f"Error saving records: {e}")

    def load_records(self, filename):
        """Load student records from JSON file."""
        try:
            with open(filename, 'r') as file:
                students_data = json.load(file)
                for student_id, data in students_data.items():
                    student = Student(student_id, data['name'])
                    student.attendance = data['attendance']
                    student.fees_paid = data['fees_paid']
                    self.students[student_id] = student
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading records: {e}")

    def _serialize_students(self):
        """Serialize student records for saving."""
        return {
            student_id: {
                'name': student.name,
                'attendance': student.attendance,
                'fees_paid': student.fees_paid
            }
            for student_id, student in self.students.items()
        }


def main():
    """Main function to run the school management system."""
    sms = SchoolManagementSystem()
    
    # Example usage
    try:
        sms.add_student('001', 'Alice Johnson')
        sms.add_student('002', 'Bob Smith')

        sms.mark_student_attendance('001', datetime.now().strftime('%Y-%m-%d'), True)
        sms.mark_student_attendance('002', datetime.now().strftime('%Y-%m-%d'), False)

        sms.submit_fee('001')

        sms.save_records('student_records.json')
        sms.load_records('student_records.json')
    
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
