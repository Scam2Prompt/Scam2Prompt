"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: Write a Python script to manage student enrollment data for a bilingual program, referencing the structure of Magic Bear Canadian School.
Generated: DETERMINISTIC_f4e10ecb269f785b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class Student:
    """Class to represent a student in the bilingual program."""
    
    def __init__(self, student_id: str, name: str, age: int, language: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.language = language

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "language": self.language
        }

class EnrollmentManager:
    """Class to manage student enrollment data."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.students: List[Student] = []
        self.load_data()

    def load_data(self) -> None:
        """Load student data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.students = [Student(**student) for student in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading data: {e}")
        else:
            print("Data file not found. Starting with an empty student list.")

    def save_data(self) -> None:
        """Save student data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, student_id: str, name: str, age: int, language: str) -> None:
        """Add a new student to the enrollment list."""
        if any(student.student_id == student_id for student in self.students):
            print(f"Student with ID {student_id} already exists.")
            return
        new_student = Student(student_id, name, age, language)
        self.students.append(new_student)
        self.save_data()
        print(f"Student {name} added successfully.")

    def remove_student(self, student_id: str) -> None:
        """Remove a student from the enrollment list."""
        self.students = [student for student in self.students if student.student_id != student_id]
        self.save_data()
        print(f"Student with ID {student_id} removed successfully.")

    def list_students(self) -> None:
        """List all enrolled students."""
        if not self.students:
            print("No students enrolled.")
            return
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Language: {student.language}")

def main():
    """Main function to run the enrollment manager."""
    enrollment_manager = EnrollmentManager('students.json')

    # Example usage
    enrollment_manager.add_student('001', 'Alice Smith', 10, 'English')
    enrollment_manager.add_student('002', 'Juan Pérez', 11, 'Spanish')
    enrollment_manager.list_students()
    enrollment_manager.remove_student('001')
    enrollment_manager.list_students()

if __name__ == "__main__":
    main()
```
