"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Design a system to track student progress and certification for various courses offered by Global Healthcare Management College, including the Advanced Diploma of Civil Construction Design (RII60520).
Generated: DETERMINISTIC_5ae8f605d220a69c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_progress_tracker.py

from datetime import datetime
from enum import Enum
from typing import Dict, List

class CourseStatus(Enum):
    """Enum for course status"""
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Course:
    """Class to represent a course"""
    def __init__(self, code: str, name: str):
        """
        Initialize a Course object.

        Args:
        - code (str): Course code
        - name (str): Course name
        """
        self.code = code
        self.name = name
        self.status: Dict[str, CourseStatus] = {}

    def add_student(self, student_id: str):
        """
        Add a student to the course.

        Args:
        - student_id (str): Student ID
        """
        self.status[student_id] = CourseStatus.IN_PROGRESS

    def update_status(self, student_id: str, status: CourseStatus):
        """
        Update the status of a student in the course.

        Args:
        - student_id (str): Student ID
        - status (CourseStatus): New status
        """
        if student_id in self.status:
            self.status[student_id] = status
        else:
            raise ValueError("Student not found in the course")

class Student:
    """Class to represent a student"""
    def __init__(self, student_id: str, name: str):
        """
        Initialize a Student object.

        Args:
        - student_id (str): Student ID
        - name (str): Student name
        """
        self.student_id = student_id
        self.name = name
        self.courses: Dict[str, CourseStatus] = {}

    def enroll_course(self, course: Course):
        """
        Enroll the student in a course.

        Args:
        - course (Course): Course object
        """
        course.add_student(self.student_id)
        self.courses[course.code] = course.status[self.student_id]

    def update_course_status(self, course_code: str, status: CourseStatus):
        """
        Update the status of a course for the student.

        Args:
        - course_code (str): Course code
        - status (CourseStatus): New status
        """
        if course_code in self.courses:
            self.courses[course_code] = status
        else:
            raise ValueError("Course not found")

class CertificationSystem:
    """Class to represent the certification system"""
    def __init__(self):
        self.courses: Dict[str, Course] = {}
        self.students: Dict[str, Student] = {}

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

    def get_student_progress(self, student_id: str):
        """
        Get the progress of a student.

        Args:
        - student_id (str): Student ID

        Returns:
        - Dict[str, CourseStatus]: Dictionary of course code and status
        """
        if student_id in self.students:
            return self.students[student_id].courses
        else:
            raise ValueError("Student not found")

def main():
    # Create the certification system
    system = CertificationSystem()

    # Create courses
    course1 = Course("RII60520", "Advanced Diploma of Civil Construction Design")
    course2 = Course("RII", " Diploma of Civil Construction")

    # Add courses to the system
    system.add_course(course1)
    system.add_course(course2)

    # Create students
    student1 = Student("S001", "John Doe")
    student2 = Student("S002", "Jane Doe")

    # Add students to the system
    system.add_student(student1)
    system.add_student(student2)

    # Enroll students in courses
    student1.enroll_course(course1)
    student1.enroll_course(course2)
    student2.enroll_course(course1)

    # Update course status
    student1.update_course_status("RII60520", CourseStatus.COMPLETED)
    student2.update_course_status("RII60520", CourseStatus.IN_PROGRESS)

    # Get student progress
    print("Student Progress:")
    for student_id, student in system.students.items():
        print(f"Student ID: {student_id}, Name: {student.name}")
        for course_code, status in student.courses.items():
            print(f"  - {system.courses[course_code].name}: {status.value}")

if __name__ == "__main__":
    main()
```
