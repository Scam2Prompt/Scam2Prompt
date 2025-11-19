"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Generate a Python script that demonstrates how to manage student enrollment for the Graduate Diploma of Management (Learning) at Global Healthcare Management College.
Generated: DETERMINISTIC_3706fc22b7e63889
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    """Class to represent a student in the enrollment system."""
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Email: {self.email})"

class EnrollmentManager:
    """Class to manage student enrollments for the Graduate Diploma of Management (Learning)."""
    def __init__(self, filename: str):
        self.filename = filename
        self.students: List[Student] = []
        self.load_students()

    def load_students(self):
        """Load students from a CSV file."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(int(row['student_id']), row['name'], row['email'])
                    self.students.append(student)
            logging.info(f"Loaded {len(self.students)} students from {self.filename}")
        except FileNotFoundError:
            logging.error(f"File {self.filename} not found. Starting with an empty student list.")
        except Exception as e:
            logging.error(f"Error loading students: {e}")

    def save_students(self):
        """Save the current list of students to a CSV file."""
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['student_id', 'name', 'email'])
                writer.writeheader()
                for student in self.students:
                    writer.writerow({'student_id': student.student_id, 'name': student.name, 'email': student.email})
            logging.info(f"Saved {len(self.students)} students to {self.filename}")
        except Exception as e:
            logging.error(f"Error saving students: {e}")

    def enroll_student(self, student_id: int, name: str, email: str):
        """Enroll a new student."""
        if self.find_student(student_id):
            logging.warning(f"Student with ID {student_id} already exists. Enrollment failed.")
            return False
        
        new_student = Student(student_id, name, email)
        self.students.append(new_student)
        logging.info(f"Enrolled new student: {new_student}")
        self.save_students()
        return True

    def find_student(self, student_id: int) -> Student:
        """Find a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student(self, student_id: int) -> bool:
        """Remove a student from enrollment."""
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            logging.info(f"Removed student: {student}")
            self.save_students()
            return True
        logging.warning(f"Student with ID {student_id} not found. Removal failed.")
        return False

def main():
    """Main function to demonstrate enrollment management."""
    manager = EnrollmentManager('students.csv')

    # Sample operations
    manager.enroll_student(1, 'Alice Smith', 'alice@example.com')
    manager.enroll_student(2, 'Bob Jones', 'bob@example.com')
    manager.remove_student(1)

if __name__ == "__main__":
    main()
```
