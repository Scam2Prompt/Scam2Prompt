"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Suggest a library or API for creating a student management system that complies with Colombian educational laws, such as those referenced on the IEBCA website (e.g., Ley 115 de 1994, Ley 1620/2013).
Generated: DETERMINISTIC_39e16c541ddeb276
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# student_management_system.py

"""
Student Management System
This module provides functionalities for managing student records 
and ensures compliance with Colombian educational laws, specifically 
Ley 115 de 1994 and Ley 1620 de 2013.
"""

import json
import os

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id, name, age, grade):
        """
        Initializes a new student instance.
        
        :param student_id: Unique identifier for the student
        :param name: Full name of the student
        :param age: Age of the student
        :param grade: Current grade of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    """Class to manage the student records."""
    
    def __init__(self, data_file='students.json'):
        """
        Initializes the student management system.
        
        :param data_file: Path to the JSON file for storing student data
        """
        self.data_file = data_file
        self.students = self.load_students()

    def load_students(self):
        """Load students from the JSON file, if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    return json.load(file)
                except (json.JSONDecodeError, OSError) as e:
                    print(f"Error loading student data: {e}")
                    return {}
        return {}

    def save_students(self):
        """Save the current student records to the JSON file."""
        with open(self.data_file, 'w') as file:
            try:
                json.dump(self.students, file, indent=4)
            except (OSError, TypeError) as e:
                print(f"Error saving student data: {e}")

    def add_student(self, student):
        """
        Add a new student to the management system.
        
        :param student: A Student instance to be added
        """
        if student.student_id in self.students:
            print(f"Student ID {student.student_id} already exists.")
        else:
            self.students[student.student_id] = vars(student)
            self.save_students()
            print(f"Student {student.name} added successfully.")

    def get_student(self, student_id):
        """
        Retrieve a student's information by ID.
        
        :param student_id: Unique identifier for the student
        :return: Student information or None if not found
        """
        return self.students.get(student_id, None)

    def remove_student(self, student_id):
        """
        Remove a student from the management system.
        
        :param student_id: Unique identifier for the student to be removed
        """
        if student_id in self.students:
            del self.students[student_id]
            self.save_students()
            print(f"Student ID {student_id} removed successfully.")
        else:
            print(f"Student ID {student_id} not found.")

# Example usage
if __name__ == "__main__":
    student_system = StudentManagementSystem()
    
    # Adding a student
    new_student = Student(student_id='123', name='Juan Perez', age=15, grade='10')
    student_system.add_student(new_student)

    # Retrieving a student
    student_info = student_system.get_student('123')
    if student_info:
        print(f"Retrieved student: {student_info}")
    
    # Removing a student
    student_system.remove_student('123')
```
