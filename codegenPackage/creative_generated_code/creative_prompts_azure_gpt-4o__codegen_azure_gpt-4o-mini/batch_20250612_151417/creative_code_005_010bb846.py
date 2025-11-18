"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write a script to automate student admission processes for grades Nursery to Nine, referencing the admission system at Happy Boarding School.
Generated: DETERMINISTIC_010bb8469807a246
Batch ID: 20250612_151417
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
    """
    Class representing a student in the admission process.
    """

    def __init__(self, first_name, last_name, grade, dob, parent_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.dob = dob
        self.parent_contact = parent_contact
        self.admission_status = "Pending"

    def validate(self):
        """
        Validates the student's information before admission.
        :return: True if valid, False otherwise
        """
        if self.grade not in range(1, 10):
            raise ValueError("Grade must be between 1 and 9.")
        if not self.is_valid_contact():
            raise ValueError("Invalid parent contact number.")
        return True

    def is_valid_contact(self):
        """
        Validates the parent's contact number format.
        :return: True if valid, False otherwise
        """
        return isinstance(self.parent_contact, str) and len(self.parent_contact) == 10 and self.parent_contact.isdigit()

class AdmissionSystem:
    """
    Admission system for managing student admissions.
    """

    def __init__(self):
        self.students = []
        self.admission_file = "admissions.json"

    def add_student(self, student):
        """
        Adds a student to the admission list after validation.
        :param student: Instance of the Student class
        """
        try:
            if student.validate():
                self.students.append(student)
                self.save_admissions()
                print(f"Admission request for {student.first_name} {student.last_name} has been added.")
        except Exception as e:
            print(f"Error adding student: {e}")

    def save_admissions(self):
        """
        Saves admission data to a JSON file.
        """
        with open(self.admission_file, 'w') as f:
            json.dump([s.__dict__ for s in self.students], f, default=str)
    
    def load_admissions(self):
        """
        Loads admission data from a JSON file.
        """
        try:
            with open(self.admission_file, 'r') as f:
                data = json.load(f)
                self.students = [Student(**student) for student in data]
        except FileNotFoundError:
            print("No previous admissions found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty list.")
    
    def display_admissions(self):
        """
        Displays all current admissions.
        """
        print("Current Admissions:")
        for student in self.students:
            print(f"{student.first_name} {student.last_name} - Grade: {student.grade} - Status: {student.admission_status}")

def main():
    # Initialize the admission system
    admission_system = AdmissionSystem()
    admission_system.load_admissions()

    # Example of adding students
    try:
        student1 = Student("Alice", "Smith", 1, "2018-04-15", "1234567890")
        admission_system.add_student(student1)

        student2 = Student("Bob", "Johnson", 2, "2017-05-20", "0987654321")
        admission_system.add_student(student2)

        student3 = Student("Charlie", "Brown", 0, "2016-06-10", "12345abcde")  # Invalid grade and contact
        admission_system.add_student(student3)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Display all admissions
    admission_system.display_admissions()

if __name__ == "__main__":
    main()
```
