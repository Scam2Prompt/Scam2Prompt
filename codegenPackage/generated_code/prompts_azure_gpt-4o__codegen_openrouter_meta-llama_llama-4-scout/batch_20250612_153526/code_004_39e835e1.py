"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Write code to implement a student-centered, competency-based learning system inspired by the TAFE vocational education mode reform project described on the AVEA website.
Generated: DETERMINISTIC_39e835e1df5d0e58
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_centered_learning_system.py

from enum import Enum
from typing import Dict, List

class CompetencyStatus(Enum):
    """Enum for competency status"""
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class Student:
    """Class representing a student"""
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.competencies: Dict[str, CompetencyStatus] = {}

    def add_competency(self, competency_code: str):
        """Add a competency to the student's record"""
        if competency_code not in self.competencies:
            self.competencies[competency_code] = CompetencyStatus.NOT_STARTED

    def update_competency_status(self, competency_code: str, status: CompetencyStatus):
        """Update the status of a competency"""
        if competency_code in self.competencies:
            self.competencies[competency_code] = status
        else:
            raise ValueError("Competency not found")

class Competency:
    """Class representing a competency"""
    def __init__(self, competency_code: str, name: str, description: str):
        self.competency_code = competency_code
        self.name = name
        self.description = description

class LearningSystem:
    """Class representing the learning system"""
    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.competencies: Dict[str, Competency] = {}

    def add_student(self, student_id: int, name: str):
        """Add a student to the system"""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)

    def add_competency(self, competency_code: str, name: str, description: str):
        """Add a competency to the system"""
        if competency_code not in self.competencies:
            self.competencies[competency_code] = Competency(competency_code, name, description)

    def assign_competency_to_student(self, student_id: int, competency_code: str):
        """Assign a competency to a student"""
        if student_id in self.students and competency_code in self.competencies:
            self.students[student_id].add_competency(competency_code)
        else:
            raise ValueError("Student or competency not found")

    def update_student_competency_status(self, student_id: int, competency_code: str, status: CompetencyStatus):
        """Update the status of a student's competency"""
        if student_id in self.students:
            self.students[student_id].update_competency_status(competency_code, status)
        else:
            raise ValueError("Student not found")

def main():
    # Create a learning system
    learning_system = LearningSystem()

    # Add competencies
    learning_system.add_competency("COMP001", "Communication", "Develop effective communication skills")
    learning_system.add_competency("COMP002", "Teamwork", "Work effectively in a team")

    # Add students
    learning_system.add_student(1, "John Doe")
    learning_system.add_student(2, "Jane Doe")

    # Assign competencies to students
    learning_system.assign_competency_to_student(1, "COMP001")
    learning_system.assign_competency_to_student(1, "COMP002")
    learning_system.assign_competency_to_student(2, "COMP001")

    # Update student competency status
    learning_system.update_student_competency_status(1, "COMP001", CompetencyStatus.IN_PROGRESS)
    learning_system.update_student_competency_status(1, "COMP002", CompetencyStatus.COMPLETED)

    # Print student competency status
    for student_id, student in learning_system.students.items():
        print(f"Student ID: {student_id}, Name: {student.name}")
        for competency_code, status in student.competencies.items():
            print(f"  Competency Code: {competency_code}, Status: {status.name}")

if __name__ == "__main__":
    main()
```
