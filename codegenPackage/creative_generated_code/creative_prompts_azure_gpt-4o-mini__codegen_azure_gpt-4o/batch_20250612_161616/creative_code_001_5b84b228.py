"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Write a code snippet to manage student registrations for the various aesthetic medicine courses available at Academia Medicina Estética.
Generated: DETERMINISTIC_5b84b228770de2b9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Student:
    """Class representing a student."""
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}, Email: {self.email})"


class Course:
    """Class representing a course."""
    def __init__(self, course_id, name, max_capacity):
        self.course_id = course_id
        self.name = name
        self.max_capacity = max_capacity
        self.students = []

    def register_student(self, student):
        """Register a student for this course."""
        if len(self.students) >= self.max_capacity:
            raise ValueError(f"Course '{self.name}' is already at maximum capacity.")
        self.students.append(student)

    def list_students(self):
        """List all registered students."""
        return self.students

    def __str__(self):
        return f"{self.name} (ID: {self.course_id}, Capacity: {self.max_capacity})"


class RegistrationSystem:
    """Class to manage course registrations."""
    def __init__(self):
        self.students = {}  # Dictionary to store students by ID
        self.courses = {}   # Dictionary to store courses by ID

    def add_student(self, student_id, name, email):
        """Add a new student to the system."""
        if student_id in self.students:
            raise ValueError(f"Student ID '{student_id}' is already registered.")
        student = Student(student_id, name, email)
        self.students[student_id] = student

    def add_course(self, course_id, name, max_capacity):
        """Add a new course to the system."""
        if course_id in self.courses:
            raise ValueError(f"Course ID '{course_id}' already exists.")
        course = Course(course_id, name, max_capacity)
        self.courses[course_id] = course

    def register_student_to_course(self, student_id, course_id):
        """Register a student to a course."""
        if student_id not in self.students:
            raise ValueError(f"Student ID '{student_id}' not found.")
        if course_id not in self.courses:
            raise ValueError(f"Course ID '{course_id}' not found.")
        student = self.students[student_id]
        course = self.courses[course_id]
        course.register_student(student)

    def list_course_students(self, course_id):
        """List students registered in a specific course."""
        if course_id not in self.courses:
            raise ValueError(f"Course ID '{course_id}' not found.")
        course = self.courses[course_id]
        return course.list_students()

    def __str__(self):
        return f"Registration System: {len(self.students)} students, {len(self.courses)} courses."


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the registration system
        reg_system = RegistrationSystem()

        # Add sample students
        reg_system.add_student(student_id="S001", name="Alice Johnson", email="alice@example.com")
        reg_system.add_student(student_id="S002", name="Bob Smith", email="bob@example.com")

        # Add sample courses
        reg_system.add_course(course_id="C001", name="Botox Masterclass", max_capacity=2)
        reg_system.add_course(course_id="C002", name="Dermal Fillers Workshop", max_capacity=3)

        # Register students to courses
        reg_system.register_student_to_course(student_id="S001", course_id="C001")
        reg_system.register_student_to_course(student_id="S002", course_id="C002")

        # List students in a course
        botox_students = reg_system.list_course_students(course_id="C001")
        print(f"Students in Botox Masterclass: {[str(student) for student in botox_students]}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
```
