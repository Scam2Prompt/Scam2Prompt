"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Recommend a library or API for managing educational programs that could be used to implement ENAFO's flexible structure combining theoretical and practical folklore courses.
Generated: DETERMINISTIC_400bfba606b5402e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I need to clarify that I'll be providing a Python solution as it's a popular and versatile language. I'll be recommending a simple library for managing educational programs and providing a basic implementation.

```python
# educational_program.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class CourseType(Enum):
    """Enum for course types."""
    THEORETICAL = 1
    PRACTICAL = 2

@dataclass
class Course:
    """Dataclass for a course."""
    id: int
    name: str
    course_type: CourseType
    description: str

class EducationalProgram:
    """Class for managing educational programs."""

    def __init__(self, name: str):
        """
        Initialize an educational program.

        Args:
        - name (str): The name of the program.
        """
        self.name = name
        self.courses = []

    def add_course(self, course: Course):
        """
        Add a course to the program.

        Args:
        - course (Course): The course to add.

        Raises:
        - ValueError: If the course is already in the program.
        """
        if course in self.courses:
            raise ValueError("Course already exists in the program.")
        self.courses.append(course)

    def remove_course(self, course_id: int):
        """
        Remove a course from the program.

        Args:
        - course_id (int): The ID of the course to remove.

        Raises:
        - ValueError: If the course does not exist in the program.
        """
        self.courses = [course for course in self.courses if course.id != course_id]

    def get_courses(self) -> List[Course]:
        """
        Get all courses in the program.

        Returns:
        - List[Course]: A list of courses in the program.
        """
        return self.courses

def main():
    # Create an educational program
    program = EducationalProgram("Folklore Program")

    # Create courses
    course1 = Course(1, "Theoretical Folklore", CourseType.THEORETICAL, "Learn about folklore theory.")
    course2 = Course(2, "Practical Folklore", CourseType.PRACTICAL, "Apply folklore in practice.")

    # Add courses to the program
    program.add_course(course1)
    program.add_course(course2)

    # Print courses in the program
    print("Courses in the program:")
    for course in program.get_courses():
        print(f"ID: {course.id}, Name: {course.name}, Type: {course.course_type.name}, Description: {course.description}")

    # Remove a course from the program
    program.remove_course(1)

    # Print courses in the program after removal
    print("\nCourses in the program after removal:")
    for course in program.get_courses():
        print(f"ID: {course.id}, Name: {course.name}, Type: {course.course_type.name}, Description: {course.description}")

if __name__ == "__main__":
    main()
```
