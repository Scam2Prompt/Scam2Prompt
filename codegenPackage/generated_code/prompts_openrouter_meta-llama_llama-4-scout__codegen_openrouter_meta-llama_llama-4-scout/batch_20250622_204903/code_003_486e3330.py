"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Design a school management system using a library or framework, incorporating features like air-conditioned computer labs and American-style management systems, as seen in Happy Boarding School.
Generated: DETERMINISTIC_486e3330d92c6de6
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

from typing import List, Dict
from enum import Enum
from datetime import datetime

class LabStatus(str, Enum):
    """Status of a computer lab."""
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    MAINTENANCE = "maintenance"

class Student:
    """Represents a student."""
    def __init__(self, student_id: int, name: str, grade: int):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class ComputerLab:
    """Represents a computer lab."""
    def __init__(self, lab_id: int, capacity: int):
        self.lab_id = lab_id
        self.capacity = capacity
        self.status: LabStatus = LabStatus.AVAILABLE
        self.students: List[Student] = []

    def add_student(self, student: Student):
        """Add a student to the lab."""
        if self.status == LabStatus.AVAILABLE:
            self.students.append(student)
            self.status = LabStatus.OCCUPIED
            print(f"Student {student.name} added to lab {self.lab_id}.")
        else:
            print(f"Lab {self.lab_id} is not available.")

    def remove_student(self, student: Student):
        """Remove a student from the lab."""
        if student in self.students:
            self.students.remove(student)
            if not self.students:
                self.status = LabStatus.AVAILABLE
            print(f"Student {student.name} removed from lab {self.lab_id}.")
        else:
            print(f"Student {student.name} not found in lab {self.lab_id}.")

class School:
    """Represents a school."""
    def __init__(self, name: str):
        self.name = name
        self.labs: Dict[int, ComputerLab] = {}
        self.students: Dict[int, Student] = {}

    def add_lab(self, lab: ComputerLab):
        """Add a computer lab to the school."""
        self.labs[lab.lab_id] = lab

    def add_student(self, student: Student):
        """Add a student to the school."""
        self.students[student.student_id] = student

    def assign_student_to_lab(self, student_id: int, lab_id: int):
        """Assign a student to a lab."""
        if student_id in self.students and lab_id in self.labs:
            student = self.students[student_id]
            lab = self.labs[lab_id]
            lab.add_student(student)
        else:
            print("Student or lab not found.")

def main():
    school = School("Happy Boarding School")

    lab1 = ComputerLab(1, 30)
    lab2 = ComputerLab(2, 40)

    school.add_lab(lab1)
    school.add_lab(lab2)

    student1 = Student(1, "John Doe", 10)
    student2 = Student(2, "Jane Doe", 11)

    school.add_student(student1)
    school.add_student(student2)

    school.assign_student_to_lab(1, 1)
    school.assign_student_to_lab(2, 1)

    # Try to add another student to an occupied lab
    student3 = Student(3, "Bob Smith", 9)
    school.add_student(student3)
    school.assign_student_to_lab(3, 1)

    # Remove a student from a lab
    lab1.remove_student(student1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
