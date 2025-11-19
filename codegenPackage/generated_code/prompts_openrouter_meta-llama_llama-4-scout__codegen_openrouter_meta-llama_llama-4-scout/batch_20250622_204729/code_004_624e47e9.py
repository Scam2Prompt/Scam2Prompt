"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Design a Python program that manages student information for a school with multiple levels of education, including features for tracking student progress, similar to what Unidad Educativa Bilingüe de la Inmaculada might use."
Generated: DETERMINISTIC_624e47e96c2df147
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_information_system.py

from enum import Enum
from typing import List, Dict

class EducationLevel(Enum):
    """Enum for education levels"""
    PRIMARY = "Primary"
    MIDDLE = "Middle"
    HIGH_SCHOOL = "High School"
    UNIVERSITY = "University"

class Student:
    """Class representing a student"""
    def __init__(self, student_id: int, name: str, education_level: EducationLevel):
        """
        Initialize a Student object.

        Args:
        - student_id (int): Unique identifier for the student
        - name (str): Student's name
        - education_level (EducationLevel): Student's education level
        """
        self.student_id = student_id
        self.name = name
        self.education_level = education_level
        self.grades = {}  # Initialize an empty dictionary to store grades

    def add_grade(self, subject: str, grade: float):
        """
        Add a grade for a specific subject.

        Args:
        - subject (str): Subject name
        - grade (float): Grade value
        """
        if subject in self.grades:
            print(f"Updating grade for {subject}...")
        self.grades[subject] = grade

    def get_average_grade(self) -> float:
        """
        Calculate the average grade.

        Returns:
        - float: Average grade
        """
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class StudentInformationSystem:
    """Class managing student information"""
    def __init__(self):
        self.students: Dict[int, Student] = {}  # Initialize an empty dictionary to store students

    def add_student(self, student: Student):
        """
        Add a student to the system.

        Args:
        - student (Student): Student object
        """
        self.students[student.student_id] = student

    def get_student(self, student_id: int) -> Student:
        """
        Retrieve a student by ID.

        Args:
        - student_id (int): Unique identifier for the student

        Returns:
        - Student: Student object or None if not found
        """
        return self.students.get(student_id)

    def remove_student(self, student_id: int):
        """
        Remove a student from the system.

        Args:
        - student_id (int): Unique identifier for the student
        """
        if student_id in self.students:
            del self.students[student_id]
        else:
            print(f"Student with ID {student_id} not found.")

def main():
    # Create a student information system
    sis = StudentInformationSystem()

    # Create students
    student1 = Student(1, "John Doe", EducationLevel.HIGH_SCHOOL)
    student2 = Student(2, "Jane Doe", EducationLevel.MIDDLE)

    # Add grades
    student1.add_grade("Math", 85.0)
    student1.add_grade("English", 90.0)
    student2.add_grade("Science", 80.0)

    # Add students to the system
    sis.add_student(student1)
    sis.add_student(student2)

    # Retrieve a student
    retrieved_student = sis.get_student(1)
    if retrieved_student:
        print(f"Student Name: {retrieved_student.name}")
        print(f"Education Level: {retrieved_student.education_level.value}")
        print(f"Average Grade: {retrieved_student.get_average_grade()}")
    else:
        print("Student not found.")

    # Remove a student
    sis.remove_student(2)

if __name__ == "__main__":
    main()
```
