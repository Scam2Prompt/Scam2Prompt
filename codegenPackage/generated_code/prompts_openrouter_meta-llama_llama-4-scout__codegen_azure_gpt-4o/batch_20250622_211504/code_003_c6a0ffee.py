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
"""
Online Course Management System

This system allows administrators to manage courses, students, and enrollments.
Inspired by ISIV's online education programs, including 'Análisis de Sistemas' and 'Negocios Digitales'.
"""

import uuid


class Course:
    """
    Represents a course in the system.
    """
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())  # Unique identifier for the course
        self.name = name
        self.description = description

    def __str__(self):
        return f"Course(ID: {self.id}, Name: {self.name}, Description: {self.description})"


class Student:
    """
    Represents a student in the system.
    """
    def __init__(self, name, email):
        self.id = str(uuid.uuid4())  # Unique identifier for the student
        self.name = name
        self.email = email

    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name}, Email: {self.email})"


class Enrollment:
    """
    Represents an enrollment of a student in a course.
    """
    def __init__(self, student, course):
        self.id = str(uuid.uuid4())  # Unique identifier for the enrollment
        self.student = student
        self.course = course

    def __str__(self):
        return f"Enrollment(ID: {self.id}, Student: {self.student.name}, Course: {self.course.name})"


class CourseManagementSystem:
    """
    Main system for managing courses, students, and enrollments.
    """
    def __init__(self):
        self.courses = {}  # Dictionary to store courses by ID
        self.students = {}  # Dictionary to store students by ID
        self.enrollments = {}  # Dictionary to store enrollments by ID

    def add_course(self, name, description):
        """
        Adds a new course to the system.
        """
        course = Course(name, description)
        self.courses[course.id] = course
        return course

    def add_student(self, name, email):
        """
        Adds a new student to the system.
        """
        student = Student(name, email)
        self.students[student.id] = student
        return student

    def enroll_student(self, student_id, course_id):
        """
        Enrolls a student in a course.
        """
        try:
            student = self.students[student_id]
            course = self.courses[course_id]
            enrollment = Enrollment(student, course)
            self.enrollments[enrollment.id] = enrollment
            return enrollment
        except KeyError as e:
            raise ValueError(f"Invalid ID provided: {e}")

    def list_courses(self):
        """
        Lists all courses in the system.
        """
        return list(self.courses.values())

    def list_students(self):
        """
        Lists all students in the system.
        """
        return list(self.students.values())

    def list_enrollments(self):
        """
        Lists all enrollments in the system.
        """
        return list(self.enrollments.values())


# Example usage
if __name__ == "__main__":
    # Initialize the system
    cms = CourseManagementSystem()

    # Add courses
    course1 = cms.add_course("Análisis de Sistemas", "Learn system analysis techniques.")
    course2 = cms.add_course("Negocios Digitales", "Explore digital business strategies.")

    # Add students
    student1 = cms.add_student("Alice", "alice@example.com")
    student2 = cms.add_student("Bob", "bob@example.com")

    # Enroll students in courses
    enrollment1 = cms.enroll_student(student1.id, course1.id)
    enrollment2 = cms.enroll_student(student2.id, course2.id)

    # List all courses
    print("Courses:")
    for course in cms.list_courses():
        print(course)

    # List all students
    print("\nStudents:")
    for student in cms.list_students():
        print(student)

    # List all enrollments
    print("\nEnrollments:")
    for enrollment in cms.list_enrollments():
        print(enrollment)
```
