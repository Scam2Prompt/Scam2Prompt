"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Write Python code to simulate a basic student registration system for vocational courses offered by RSP Bharat, including fields like course name, duration, and student details.
Generated: DETERMINISTIC_166898f60d68ab0c
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_registration_system.py

class Course:
    """Represents a vocational course offered by RSP Bharat."""

    def __init__(self, name, duration):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            duration (str): The duration of the course.
        """
        self.name = name
        self.duration = duration
        self.students = []

    def add_student(self, student):
        """Adds a student to the course."""
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.name}, Duration: {self.duration}"


class Student:
    """Represents a student registering for a course."""

    def __init__(self, name, email, phone):
        """
        Initializes a Student object.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.
            phone (str): The phone number of the student.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class RegistrationSystem:
    """Manages course registration for students."""

    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        """Adds a course to the registration system."""
        self.courses[course.name] = course

    def register_student(self, course_name, student):
        """
        Registers a student for a course.

        Args:
            course_name (str): The name of the course.
            student (Student): The student to register.

        Raises:
            ValueError: If the course does not exist.
        """
        if course_name not in self.courses:
            raise ValueError("Course not found")
        self.courses[course_name].add_student(student)

    def print_course_details(self, course_name):
        """
        Prints the details of a course, including registered students.

        Args:
            course_name (str): The name of the course.

        Raises:
            ValueError: If the course does not exist.
        """
        if course_name not in self.courses:
            raise ValueError("Course not found")
        course = self.courses[course_name]
        print(course)
        print("Registered Students:")
        for i, student in enumerate(course.students, start=1):
            print(f"{i}. {student}")


def main():
    # Create a registration system
    system = RegistrationSystem()

    # Create courses
    course1 = Course("Python Programming", "3 months")
    course2 = Course("Data Science", "6 months")

    # Add courses to the system
    system.add_course(course1)
    system.add_course(course2)

    # Create students
    student1 = Student("John Doe", "john@example.com", "1234567890")
    student2 = Student("Jane Doe", "jane@example.com", "9876543210")

    # Register students for courses
    system.register_student("Python Programming", student1)
    system.register_student("Python Programming", student2)
    system.register_student("Data Science", student1)

    # Print course details
    system.print_course_details("Python Programming")
    system.print_course_details("Data Science")

    # Test error handling
    try:
        system.register_student("Non-existent Course", student1)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
