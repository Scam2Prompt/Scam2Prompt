"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebenezerbandeira.com.br
Prompt: Write a code snippet that integrates course registration functionality for Ebenézer Bandeira’s family medicine courses.
Generated: DETERMINISTIC_b16637bb1a1940d6
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# course_registration.py

from typing import List, Dict, Optional

class Course:
    """Represents a course in the family medicine program."""

    def __init__(self, course_id: str, title: str, capacity: int):
        """
        Initializes a new Course instance.

        Args:
            course_id (str): Unique identifier for the course.
            title (str): Title of the course.
            capacity (int): Maximum number of students that can enroll.
        """
        self.course_id = course_id
        self.title = title
        self.capacity = capacity
        self.enrolled_students: List[str] = []

    def register_student(self, student_id: str) -> bool:
        """
        Registers a student for the course if there is capacity.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            bool: True if registration was successful, False otherwise.
        """
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_id)
            return True
        return False

class CourseRegistrationSystem:
    """Manages course registrations for family medicine courses."""

    def __init__(self):
        """Initializes the course registration system with an empty course list."""
        self.courses: Dict[str, Course] = {}

    def add_course(self, course: Course) -> None:
        """
        Adds a new course to the registration system.

        Args:
            course (Course): The course to be added.
        """
        if course.course_id in self.courses:
            raise ValueError(f"Course with ID {course.course_id} already exists.")
        self.courses[course.course_id] = course

    def register_student_for_course(self, course_id: str, student_id: str) -> bool:
        """
        Registers a student for a given course.

        Args:
            course_id (str): The ID of the course.
            student_id (str): The ID of the student.

        Returns:
            bool: True if registration was successful, False if course is full or does not exist.
        """
        course = self.courses.get(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        if course.register_student(student_id):
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Create a course registration system
    registration_system = CourseRegistrationSystem()

    # Create some courses
    course1 = Course(course_id="FM101", title="Introduction to Family Medicine", capacity=2)
    course2 = Course(course_id="FM102", title="Advanced Family Medicine", capacity=3)

    # Add courses to the system
    registration_system.add_course(course1)
    registration_system.add_course(course2)

    # Register students for courses
    try:
        print(registration_system.register_student_for_course("FM101", "student_1"))  # Expected: True
        print(registration_system.register_student_for_course("FM101", "student_2"))  # Expected: True
        print(registration_system.register_student_for_course("FM101", "student_3"))  # Expected: False
    except ValueError as e:
        print(f"Error: {e}")
```
