"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Generate a Python script to manage student enrollment for admission exam preparation courses, including personalized classes and flexible scheduling."
Generated: DETERMINISTIC_8a5787cc828bd2ea
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Student:
    """Class representing a student."""
    
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses: List[str] = []

    def enroll(self, course_name: str):
        """Enroll the student in a course."""
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
        else:
            raise ValueError(f"Student is already enrolled in {course_name}.")

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.email}, {self.enrolled_courses})"


class Course:
    """Class representing a course."""
    
    def __init__(self, course_name: str, schedule: List[str]):
        self.course_name = course_name
        self.schedule = schedule

    def __repr__(self):
        return f"Course({self.course_name}, {self.schedule})"


class EnrollmentManager:
    """Class to manage student enrollment in courses."""
    
    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.courses: Dict[str, Course] = {}

    def add_student(self, student_id: int, name: str, email: str):
        """Add a new student to the enrollment system."""
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name, email)

    def add_course(self, course_name: str, schedule: List[str]):
        """Add a new course to the enrollment system."""
        if course_name in self.courses:
            raise ValueError(f"Course {course_name} already exists.")
        self.courses[course_name] = Course(course_name, schedule)

    def enroll_student_in_course(self, student_id: int, course_name: str):
        """Enroll a student in a specified course."""
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} does not exist.")
        if course_name not in self.courses:
            raise ValueError(f"Course {course_name} does not exist.")
        
        student = self.students[student_id]
        student.enroll(course_name)

    def save_data(self, filename: str):
        """Save the current state of students and courses to a JSON file."""
        data = {
            "students": {student_id: student.__dict__ for student_id, student in self.students.items()},
            "courses": {course_name: course.__dict__ for course_name, course in self.courses.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str):
        """Load students and courses from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.students = {int(student_id): Student(**student) for student_id, student in data['students'].items()}
                self.courses = {course_name: Course(**course) for course_name, course in data['courses'].items()}
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty enrollment system.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Please check the file format.")

# Example usage
if __name__ == "__main__":
    manager = EnrollmentManager()
    
    # Adding students
    manager.add_student(1, "Alice Smith", "alice@example.com")
    manager.add_student(2, "Bob Johnson", "bob@example.com")
    
    # Adding courses
    manager.add_course("Math Preparation", ["Monday 10 AM", "Wednesday 2 PM"])
    manager.add_course("Science Preparation", ["Tuesday 1 PM", "Thursday 3 PM"])
    
    # Enrolling students in courses
    manager.enroll_student_in_course(1, "Math Preparation")
    manager.enroll_student_in_course(2, "Science Preparation")
    
    # Saving data to a file
    manager.save_data("enrollment_data.json")
    
    # Loading data from a file
    manager.load_data("enrollment_data.json")
    
    # Print current state
    print(manager.students)
    print(manager.courses)
```
