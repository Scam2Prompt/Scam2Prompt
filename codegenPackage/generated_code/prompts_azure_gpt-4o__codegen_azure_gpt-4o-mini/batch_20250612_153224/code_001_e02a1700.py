"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Recommend a system design for developing an integrated school management system for public institutions, as described in Licitare's "Solução em T.I" services.
Generated: DETERMINISTIC_e02a1700811e553e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_management_system.py

"""
School Management System

This module provides a basic structure for an integrated school management system
for public institutions. It includes classes for managing students, teachers, courses,
and enrollments. The system is designed to be extensible and maintainable.
"""

class Student:
    """Class representing a student in the school management system."""
    
    def __init__(self, student_id, name, age):
        """
        Initialize a new student.

        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param age: Age of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age})"


class Teacher:
    """Class representing a teacher in the school management system."""
    
    def __init__(self, teacher_id, name, subject):
        """
        Initialize a new teacher.

        :param teacher_id: Unique identifier for the teacher
        :param name: Name of the teacher
        :param subject: Subject taught by the teacher
        """
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        """Return a string representation of the teacher."""
        return f"Teacher(ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject})"


class Course:
    """Class representing a course in the school management system."""
    
    def __init__(self, course_id, title, teacher):
        """
        Initialize a new course.

        :param course_id: Unique identifier for the course
        :param title: Title of the course
        :param teacher: Teacher assigned to the course
        """
        self.course_id = course_id
        self.title = title
        self.teacher = teacher

    def __str__(self):
        """Return a string representation of the course."""
        return f"Course(ID: {self.course_id}, Title: {self.title}, Teacher: {self.teacher.name})"


class Enrollment:
    """Class representing an enrollment of a student in a course."""
    
    def __init__(self, student, course):
        """
        Initialize a new enrollment.

        :param student: Student being enrolled
        :param course: Course in which the student is enrolled
        """
        self.student = student
        self.course = course

    def __str__(self):
        """Return a string representation of the enrollment."""
        return f"Enrollment(Student: {self.student.name}, Course: {self.course.title})"


class SchoolManagementSystem:
    """Class representing the school management system."""
    
    def __init__(self):
        """Initialize the school management system with empty lists."""
        self.students = []
        self.teachers = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student):
        """Add a student to the system."""
        self.students.append(student)

    def add_teacher(self, teacher):
        """Add a teacher to the system."""
        self.teachers.append(teacher)

    def add_course(self, course):
        """Add a course to the system."""
        self.courses.append(course)

    def enroll_student(self, student, course):
        """Enroll a student in a course."""
        if student not in self.students:
            raise ValueError("Student not found in the system.")
        if course not in self.courses:
            raise ValueError("Course not found in the system.")
        
        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)

    def get_enrollments(self):
        """Return a list of all enrollments."""
        return self.enrollments


# Example usage
if __name__ == "__main__":
    # Create the school management system
    sms = SchoolManagementSystem()

    # Create and add students
    student1 = Student(1, "Alice", 14)
    student2 = Student(2, "Bob", 15)
    sms.add_student(student1)
    sms.add_student(student2)

    # Create and add teachers
    teacher1 = Teacher(1, "Mr. Smith", "Mathematics")
    sms.add_teacher(teacher1)

    # Create and add courses
    course1 = Course(1, "Algebra", teacher1)
    sms.add_course(course1)

    # Enroll students in courses
    sms.enroll_student(student1, course1)
    sms.enroll_student(student2, course1)

    # Print all enrollments
    for enrollment in sms.get_enrollments():
        print(enrollment)
```
