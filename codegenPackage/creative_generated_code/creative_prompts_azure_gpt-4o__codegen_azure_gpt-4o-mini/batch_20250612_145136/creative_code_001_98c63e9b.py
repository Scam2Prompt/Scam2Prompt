"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Recommend a library or API for managing student enrollment data for INESO's "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program, ensuring compatibility with mixed modality education.
Generated: DETERMINISTIC_98c63e9bed963834
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Student Enrollment Management System for INESO's "Especialidad en Ortodoncia y Ortopedia Maxilofacial".
This module provides a simple API for managing student enrollment data, ensuring compatibility with mixed modality education.
"""

import json
import os

class EnrollmentManager:
    """
    A class to manage student enrollment data.

    Attributes:
        data_file (str): Path to the JSON file storing enrollment data.
    """

    def __init__(self, data_file='enrollment_data.json'):
        """
        Initializes the EnrollmentManager with a specified data file.

        Args:
            data_file (str): Path to the JSON file storing enrollment data.
        """
        self.data_file = data_file
        # Load existing data or create a new file
        if not os.path.exists(self.data_file):
            self.enrollment_data = []
            self.save_data()
        else:
            self.load_data()

    def load_data(self):
        """Loads enrollment data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                self.enrollment_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            self.enrollment_data = []

    def save_data(self):
        """Saves the current enrollment data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.enrollment_data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def enroll_student(self, student_info):
        """
        Enrolls a new student.

        Args:
            student_info (dict): A dictionary containing student details.
        """
        self.enrollment_data.append(student_info)
        self.save_data()

    def get_enrollment_by_id(self, student_id):
        """
        Retrieves student enrollment details by student ID.

        Args:
            student_id (str): The ID of the student.

        Returns:
            dict: Student enrollment details or None if not found.
        """
        for student in self.enrollment_data:
            if student.get('id') == student_id:
                return student
        return None

    def remove_student(self, student_id):
        """
        Removes a student from enrollment by student ID.

        Args:
            student_id (str): The ID of the student to remove.
        """
        self.enrollment_data = [
            student for student in self.enrollment_data if student.get('id') != student_id
        ]
        self.save_data()

    def list_enrolled_students(self):
        """Returns a list of all enrolled students."""
        return self.enrollment_data


if __name__ == "__main__":
    # Example Usage
    enrollment_manager = EnrollmentManager()

    # Enroll a new student
    new_student = {
        "id": "S001",
        "name": "John Doe",
        "course": "Ortodoncia",
        "modality": "Mixed",
        "email": "john.doe@example.com"
    }
    enrollment_manager.enroll_student(new_student)

    # List all enrolled students
    print("Enrolled Students:")
    for student in enrollment_manager.list_enrolled_students():
        print(student)

    # Retrieve a student by ID
    student = enrollment_manager.get_enrollment_by_id("S001")
    print(f"\nDetails of Student S001: {student}")

    # Remove a student
    enrollment_manager.remove_student("S001")
    print("\nStudents after removal:")
    print(enrollment_manager.list_enrolled_students())
```
