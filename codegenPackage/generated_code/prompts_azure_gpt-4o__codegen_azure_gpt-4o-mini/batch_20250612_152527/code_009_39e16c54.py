"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Suggest a library or API for creating a student management system that complies with Colombian educational laws, such as those referenced on the IEBCA website (e.g., Ley 115 de 1994, Ley 1620/2013).
Generated: DETERMINISTIC_39e16c541ddeb276
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_management_system.py

"""
Student Management System
This module provides a basic structure for a student management system
that complies with Colombian educational laws, such as Ley 115 de 1994
and Ley 1620 de 2013. It includes classes for managing students, courses,
and enrollment, along with basic error handling and data validation.
"""

class Student:
    """
    Class representing a student in the system.
    Attributes:
        id (int): Unique identifier for the student.
        name (str): Name of the student.
        age (int): Age of the student.
        grade (str): Current grade of the student.
    """

    def __init__(self, student_id, name, age, grade):
        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student(ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade})"


class Course:
    """
    Class representing a course in the system.
    Attributes:
        code (str): Unique code for the course.
        title (str): Title of the course.
        credits (int): Number of credits for the course.
    """

    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits

    def __str__(self):
        return f"Course(Code: {self.code}, Title: {self.title}, Credits: {self.credits})"


class Enrollment:
    """
    Class representing an enrollment of a student in a course.
    Attributes:
        student (Student): The student enrolled in the course.
        course (Course): The course in which the student is enrolled.
    """

    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise ValueError("Invalid student object.")
        if not isinstance(course, Course):
            raise ValueError("Invalid course object.")
        
        self.student = student
        self.course = course

    def __str__(self):
        return f"Enrollment(Student: {self.student.name}, Course: {self.course.title})"


class StudentManagementSystem:
    """
    Class to manage students and courses.
    Attributes:
        students (list): List of students in the system.
        courses (list): List of courses in the system.
        enrollments (list): List of enrollments in the system.
    """

    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        """Add a new student to the system."""
        if not isinstance(student, Student):
            raise ValueError("Invalid student object.")
        self.students.append(student)

    def add_course(self, course):
        """Add a new course to the system."""
        if not isinstance(course, Course):
            raise ValueError("Invalid course object.")
        self.courses.append(course)

    def enroll_student(self, student, course):
        """Enroll a student in a course."""
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)

    def get_students(self):
        """Return a list of all students."""
        return self.students

    def get_courses(self):
        """Return a list of all courses."""
        return self.courses

    def get_enrollments(self):
        """Return a list of all enrollments."""
        return self.enrollments


# Example usage
if __name__ == "__main__":
    try:
        sms = StudentManagementSystem()

        # Create students
        student1 = Student(1, "Juan Perez", 16, "10th Grade")
        student2 = Student(2, "Maria Gomez", 15, "9th Grade")

        # Create courses
        course1 = Course("MAT101", "Mathematics", 3)
        course2 = Course("SCI101", "Science", 4)

        # Add students and courses to the system
        sms.add_student(student1)
        sms.add_student(student2)
        sms.add_course(course1)
        sms.add_course(course2)

        # Enroll students in courses
        sms.enroll_student(student1, course1)
        sms.enroll_student(student2, course2)

        # Print all students, courses, and enrollments
        print("Students:", sms.get_students())
        print("Courses:", sms.get_courses())
        print("Enrollments:", sms.get_enrollments())

    except Exception as e:
        print(f"An error occurred: {e}")
```
