"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Write Python code to simulate a learning management system for vocational education, referencing the course structure and qualifications offered by Global Healthcare Management College (e.g., Certificate III in Individual Support: CHC33021 or Diploma of Community Services: CHC52021).
Generated: DETERMINISTIC_7f036a1737aff2ff
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# learning_management_system.py

from enum import Enum
from typing import List, Dict

class QualificationCode(Enum):
    """Enum for qualification codes"""
    CERTIFICATE_III_INDIVIDUAL_SUPPORT = "CHC33021"
    DIPLOMA_COMMUNITY_SERVICES = "CHC52021"

class Course:
    """Class representing a course"""
    def __init__(self, code: str, name: str, units: List[str]):
        """
        Initialize a Course object.

        Args:
        - code (str): Course code
        - name (str): Course name
        - units (List[str]): List of units in the course
        """
        self.code = code
        self.name = name
        self.units = units

class Student:
    """Class representing a student"""
    def __init__(self, student_id: int, name: str):
        """
        Initialize a Student object.

        Args:
        - student_id (int): Student ID
        - name (str): Student name
        """
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll_course(self, course: Course):
        """
        Enroll a student in a course.

        Args:
        - course (Course): Course object
        """
        self.courses[course.code] = course

    def drop_course(self, course_code: str):
        """
        Drop a course.

        Args:
        - course_code (str): Course code
        """
        if course_code in self.courses:
            del self.courses[course_code]
        else:
            raise ValueError("Student not enrolled in this course")

class LearningManagementSystem:
    """Class representing the learning management system"""
    def __init__(self):
        self.courses = {}
        self.students = {}

    def add_course(self, course: Course):
        """
        Add a course to the system.

        Args:
        - course (Course): Course object
        """
        self.courses[course.code] = course

    def add_student(self, student: Student):
        """
        Add a student to the system.

        Args:
        - student (Student): Student object
        """
        self.students[student.student_id] = student

    def get_course(self, course_code: str) -> Course:
        """
        Get a course by code.

        Args:
        - course_code (str): Course code

        Returns:
        - Course: Course object
        """
        return self.courses.get(course_code)

    def get_student(self, student_id: int) -> Student:
        """
        Get a student by ID.

        Args:
        - student_id (int): Student ID

        Returns:
        - Student: Student object
        """
        return self.students.get(student_id)

def main():
    # Create the learning management system
    lms = LearningManagementSystem()

    # Create courses
    certificate_iii = Course(
        QualificationCode.CERTIFICATE_III_INDIVIDUAL_SUPPORT.value,
        "Certificate III in Individual Support",
        ["Unit 1", "Unit 2", "Unit 3"]
    )
    diploma_community_services = Course(
        QualificationCode.DIPLOMA_COMMUNITY_SERVICES.value,
        "Diploma of Community Services",
        ["Unit 1", "Unit 2", "Unit 3", "Unit 4"]
    )

    # Add courses to the system
    lms.add_course(certificate_iii)
    lms.add_course(diploma_community_services)

    # Create students
    student1 = Student(1, "John Doe")
    student2 = Student(2, "Jane Doe")

    # Add students to the system
    lms.add_student(student1)
    lms.add_student(student2)

    # Enroll students in courses
    student1.enroll_course(certificate_iii)
    student2.enroll_course(diploma_community_services)

    # Print student information
    for student_id, student in lms.students.items():
        print(f"Student ID: {student_id}, Name: {student.name}")
        for course_code, course in student.courses.items():
            print(f"  - Enrolled in: {course.name} ({course.code})")

if __name__ == "__main__":
    main()
```
