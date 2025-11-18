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
import json

class Course:
    """Class to represent a vocational course."""

    def __init__(self, name, duration):
        """
        Initialize a new Course.

        Args:
            name (str): The name of the course.
            duration (str): The duration of the course.
        """
        self.name = name
        self.duration = duration

    def to_dict(self):
        """Convert Course object to dictionary."""
        return {
            'name': self.name,
            'duration': self.duration
        }


class Student:
    """Class to represent a student."""

    def __init__(self, name, age, course):
        """
        Initialize a new Student.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            course (Course): The course the student is enrolling in.
        """
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        """Convert Student object to dictionary."""
        return {
            'name': self.name,
            'age': self.age,
            'course': self.course.to_dict()
        }


class RegistrationSystem:
    """Class to manage student registrations."""

    def __init__(self):
        """Initialize the registration system with an empty list of students."""
        self.students = []

    def register_student(self, name, age, course_name, course_duration):
        """
        Register a new student.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            course_name (str): The name of the course.
            course_duration (str): The duration of the course.

        Raises:
            ValueError: If the student age is not a positive integer.
        """
        if age <= 0:
            raise ValueError("Age must be a positive integer.")

        course = Course(course_name, course_duration)
        student = Student(name, age, course)
        self.students.append(student)

    def save_to_file(self, filename):
        """
        Save registered students to a JSON file.

        Args:
            filename (str): The name of the file to save the data.

        Raises:
            IOError: If the file cannot be written or opened.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([student.to_dict() for student in self.students], f, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        """
        Load registered students from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If the file cannot be read or opened.
        """
        try:
            with open(filename, 'r') as f:
                students_data = json.load(f)
                for student_data in students_data:
                    course = Course(student_data['course']['name'], student_data['course']['duration'])
                    student = Student(student_data['name'], student_data['age'], course)
                    self.students.append(student)
        except IOError as e:
            print(f"Error loading from file {filename}: {e}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {filename}.")

    def display_students(self):
        """Display the list of registered students."""
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Course: {student.course.name}, Duration: {student.course.duration}")


if __name__ == "__main__":
    # Create a registration system instance
    reg_system = RegistrationSystem()

    # Register some students
    try:
        reg_system.register_student("Alice", 25, "Plumbing", "6 months")
        reg_system.register_student("Bob", 22, "Electrical", "4 months")
    except ValueError as e:
        print(e)

    # Display registered students
    reg_system.display_students()

    # Save registered students to a file
    reg_system.save_to_file("students.json")

    # Load students from a file (if needed)
    # reg_system.load_from_file("students.json")
```
