"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write Python code to simulate a basic student registration system for vocational courses offered by RSP Bharat, including fields like course name, duration, and student details.
Generated: DETERMINISTIC_166898f60d68ab0c
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class Student:
    """
    Represents a student with details such as name, email, and ID.
    """
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the student
        self.name = name
        self.email = email

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Email: {self.email}"


class Course:
    """
    Represents a vocational course with details such as name, duration, and a list of registered students.
    """
    def __init__(self, name: str, duration: str):
        self.course_id = str(uuid.uuid4())  # Generate a unique ID for the course
        self.name = name
        self.duration = duration
        self.registered_students = []  # List to hold registered students

    def register_student(self, student: Student):
        """
        Registers a student to the course.
        """
        if not isinstance(student, Student):
            raise TypeError("Invalid student object provided.")
        self.registered_students.append(student)

    def list_students(self):
        """
        Returns the list of students registered in the course.
        """
        return self.registered_students

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Duration: {self.duration}, Total Students: {len(self.registered_students)}"


class RegistrationSystem:
    """
    A system to manage student registrations for vocational courses.
    """
    def __init__(self):
        self.courses = {}  # Dictionary to store courses with course_id as key

    def add_course(self, name: str, duration: str):
        """
        Adds a new course to the system.
        """
        course = Course(name, duration)
        self.courses[course.course_id] = course
        return course.course_id

    def register_student_to_course(self, course_id: str, student: Student):
        """
        Registers a student to a course given the course ID.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} not found.")
        course = self.courses[course_id]
        course.register_student(student)

    def list_courses(self):
        """
        Returns all courses in the system.
        """
        return self.courses.values()

    def get_course_details(self, course_id: str):
        """
        Returns the details of a specific course given its ID.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} not found.")
        return self.courses[course_id]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the registration system
        registration_system = RegistrationSystem()

        # Add courses to the system
        course_id_1 = registration_system.add_course("Python Programming", "3 Months")
        course_id_2 = registration_system.add_course("Data Analysis with Excel", "2 Months")

        # Create students
        student_1 = Student("Alice Smith", "alice@example.com")
        student_2 = Student("Bob Johnson", "bob@example.com")

        # Register students to courses
        registration_system.register_student_to_course(course_id_1, student_1)
        registration_system.register_student_to_course(course_id_1, student_2)
        registration_system.register_student_to_course(course_id_2, student_2)

        # List all courses
        print("\nCourses available:")
        for course in registration_system.list_courses():
            print(course)

        # Print details of a specific course
        print("\nDetails of course with ID:", course_id_1)
        course_details = registration_system.get_course_details(course_id_1)
        print(course_details)
        print("Students in this course:")
        for student in course_details.list_students():
            print(student)

    except Exception as e:
        print(f"Error: {e}")
```
