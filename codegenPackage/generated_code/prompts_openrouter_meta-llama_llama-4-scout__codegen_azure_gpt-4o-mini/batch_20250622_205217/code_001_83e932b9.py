"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Write a Python code to manage student information for a university with programs like BBS, B Ed, and MBS.
Generated: DETERMINISTIC_83e932b9094201fa
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Student:
    """Class to represent a student."""
    
    def __init__(self, student_id: int, name: str, program: str):
        """
        Initialize a new student.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param program: Program the student is enrolled in
        """
        self.student_id = student_id
        self.name = name
        self.program = program

    def to_dict(self) -> Dict[str, Any]:
        """Convert student information to a dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'program': self.program
        }

class StudentManager:
    """Class to manage student information."""
    
    def __init__(self, filename: str):
        """
        Initialize the student manager.

        :param filename: The file to store student data
        """
        self.filename = filename
        self.students: List[Student] = []
        self.load_students()

    def load_students(self):
        """Load students from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                student_data = json.load(file)
                self.students = [Student(**data) for data in student_data]
        except FileNotFoundError:
            # If the file does not exist, we start with an empty list
            self.students = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file.")
            self.students = []

    def save_students(self):
        """Save students to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([student.to_dict() for student in self.students], file, indent=4)
        except IOError as e:
            print(f"Error: Could not write to file. {e}")

    def add_student(self, student_id: int, name: str, program: str):
        """Add a new student to the list."""
        if any(student.student_id == student_id for student in self.students):
            print(f"Error: Student with ID {student_id} already exists.")
            return
        new_student = Student(student_id, name, program)
        self.students.append(new_student)
        self.save_students()

    def get_students(self) -> List[Dict[str, Any]]:
        """Get a list of all students."""
        return [student.to_dict() for student in self.students]

    def find_student(self, student_id: int) -> Dict[str, Any]:
        """Find a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student.to_dict()
        print(f"Error: Student with ID {student_id} not found.")
        return {}

# Example usage
if __name__ == "__main__":
    manager = StudentManager('students.json')
    
    # Adding students
    manager.add_student(1, 'Alice Smith', 'BBS')
    manager.add_student(2, 'Bob Johnson', 'B Ed')
    manager.add_student(3, 'Charlie Brown', 'MBS')

    # Retrieving all students
    all_students = manager.get_students()
    print("All Students:", all_students)

    # Finding a specific student
    student_info = manager.find_student(1)
    print("Student Info:", student_info)
```
