"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevmtrustline.info
Prompt: Design a library in Python that helps manage student records for an elementary school, focusing on features like enrollment tracking and academic performance, similar to the academic focus of Excellence Elementary School.
Generated: DETERMINISTIC_f927ae61f27ce586
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Student:
    """Class representing a student record."""
    
    def __init__(self, student_id: int, name: str, age: int):
        """Initialize a new student record."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.enrollment_status = False  # False indicates not enrolled
        self.grades: List[Dict[str, Any]] = []  # List to hold subjects and grades

    def enroll(self):
        """Enroll the student."""
        self.enrollment_status = True

    def unenroll(self):
        """Unenroll the student."""
        self.enrollment_status = False

    def add_grade(self, subject: str, grade: float):
        """Add a grade for a specific subject."""
        if self.enrollment_status:
            self.grades.append({"subject": subject, "grade": grade})
        else:
            raise ValueError(f"Student {self.name} is not enrolled. Cannot add grade.")

    def get_average_grade(self) -> float:
        """Calculate and return the average grade of the student."""
        if not self.grades:
            return 0.0
        total = sum(grade['grade'] for grade in self.grades)
        return total / len(self.grades)


class StudentManager:
    """Class to manage student records."""
    
    def __init__(self):
        """Initialize a new student manager with an empty student list."""
        self.students: Dict[int, Student] = {}

    def add_student(self, student: Student):
        """Add a new student to the records."""
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists.")
        self.students[student.student_id] = student

    def remove_student(self, student_id: int):
        """Remove a student from the records."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        del self.students[student_id]

    def get_student(self, student_id: int) -> Student:
        """Retrieve a student record by ID."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        return self.students[student_id]

    def get_all_students(self) -> List[Student]:
        """Retrieve all student records."""
        return list(self.students.values())

    def save_to_file(self, filename: str):
        """Save student records to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({student_id: student.__dict__ for student_id, student in self.students.items()}, file)

    def load_from_file(self, filename: str):
        """Load student records from a JSON file."""
        try:
            with open(filename, 'r') as file:
                student_data = json.load(file)
                for student_id, data in student_data.items():
                    student = Student(data['student_id'], data['name'], data['age'])
                    student.enrollment_status = data['enrollment_status']
                    student.grades = data['grades']
                    self.students[student_id] = student
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the file.")
```
