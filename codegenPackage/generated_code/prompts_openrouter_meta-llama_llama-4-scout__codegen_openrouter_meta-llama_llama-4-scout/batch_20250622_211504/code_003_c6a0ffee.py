"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Design a system for online course management, inspired by the online education programs at ISIV, including Análisis de Sistemas and Negocios Digitales."
Generated: DETERMINISTIC_c6a0ffee1ae3f1c6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_management_system.py

from typing import List, Dict
from enum import Enum
from datetime import datetime

class CourseStatus(str, Enum):
    """Course status enumeration"""
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Course:
    """Represents an online course"""
    def __init__(self, id: int, name: str, description: str, status: CourseStatus):
        """
        Initializes a Course object

        Args:
        id (int): Unique course identifier
        name (str): Course name
        description (str): Course description
        status (CourseStatus): Course status
        """
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.students: List[Student] = []

    def add_student(self, student: 'Student'):
        """Adds a student to the course"""
        self.students.append(student)

    def __str__(self):
        return f"Course {self.id}: {self.name} - {self.status.value}"

class Student:
    """Represents a student"""
    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Student object

        Args:
        id (int): Unique student identifier
        name (str): Student name
        email (str): Student email
        """
        self.id = id
        self.name = name
        self.email = email
        self.courses: List[Course] = []

    def enroll_course(self, course: Course):
        """Enrolls the student in a course"""
        self.courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"Student {self.id}: {self.name} - {self.email}"

class CourseManagementSystem:
    """Manages online courses and students"""
    def __init__(self):
        self.courses: Dict[int, Course] = {}
        self.students: Dict[int, Student] = {}

    def create_course(self, id: int, name: str, description: str, status: CourseStatus):
        """
        Creates a new course

        Args:
        id (int): Unique course identifier
        name (str): Course name
        description (str): Course description
        status (CourseStatus): Course status

        Raises:
        ValueError: If a course with the same ID already exists
        """
        if id in self.courses:
            raise ValueError("Course with the same ID already exists")
        course = Course(id, name, description, status)
        self.courses[id] = course
        return course

    def create_student(self, id: int, name: str, email: str):
        """
        Creates a new student

        Args:
        id (int): Unique student identifier
        name (str): Student name
        email (str): Student email

        Raises:
        ValueError: If a student with the same ID already exists
        """
        if id in self.students:
            raise ValueError("Student with the same ID already exists")
        student = Student(id, name, email)
        self.students[id] = student
        return student

    def get_course(self, id: int) -> Course:
        """
        Retrieves a course by ID

        Args:
        id (int): Unique course identifier

        Returns:
        Course: The course object or None if not found
        """
        return self.courses.get(id)

    def get_student(self, id: int) -> Student:
        """
        Retrieves a student by ID

        Args:
        id (int): Unique student identifier

        Returns:
        Student: The student object or None if not found
        """
        return self.students.get(id)

def main():
    # Example usage
    system = CourseManagementSystem()

    try:
        course1 = system.create_course(1, "Análisis de Sistemas", "Course description", CourseStatus.AVAILABLE)
        course2 = system.create_course(2, "Negocios Digitales", "Course description", CourseStatus.AVAILABLE)

        student1 = system.create_student(1, "John Doe", "john@example.com")
        student2 = system.create_student(2, "Jane Doe", "jane@example.com")

        student1.enroll_course(course1)
        student2.enroll_course(course2)
        student1.enroll_course(course2)

        print("Courses:")
        for course in system.courses.values():
            print(course)
            print(f"  Students: {[student.name for student in course.students]}")

        print("\nStudents:")
        for student in system.students.values():
            print(student)
            print(f"  Courses: {[course.name for course in student.courses]}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
