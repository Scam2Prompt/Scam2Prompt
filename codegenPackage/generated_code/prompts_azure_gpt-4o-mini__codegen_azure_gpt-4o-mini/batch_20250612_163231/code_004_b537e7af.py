"""
Generated Code Metadata:
========================
Original URL: https://infinitiai.in
Prompt: What is the process to create and manage online courses using InfinitiAI's course management system?
Generated: DETERMINISTIC_b537e7af07f0b11a
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any

class Course:
    """
    A class to represent a course in the course management system.
    """

    def __init__(self, title: str, description: str, instructor: str):
        """
        Initializes a new course with a title, description, and instructor.

        :param title: Title of the course
        :param description: Description of the course
        :param instructor: Name of the instructor
        """
        self.title = title
        self.description = description
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student_name: str) -> None:
        """
        Enroll a student in the course.

        :param student_name: Name of the student to enroll
        """
        if student_name not in self.students:
            self.students.append(student_name)
        else:
            raise ValueError(f"Student {student_name} is already enrolled in the course.")

    def get_course_info(self) -> Dict[str, Any]:
        """
        Returns the course information.

        :return: A dictionary containing course details
        """
        return {
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "students": self.students
        }


class CourseManagementSystem:
    """
    A class to manage multiple courses in the course management system.
    """

    def __init__(self):
        """
        Initializes the course management system with an empty course list.
        """
        self.courses = {}

    def create_course(self, title: str, description: str, instructor: str) -> Course:
        """
        Creates a new course and adds it to the system.

        :param title: Title of the course
        :param description: Description of the course
        :param instructor: Name of the instructor
        :return: The created Course object
        """
        if title in self.courses:
            raise ValueError(f"Course with title '{title}' already exists.")
        
        course = Course(title, description, instructor)
        self.courses[title] = course
        return course

    def get_course(self, title: str) -> Course:
        """
        Retrieves a course by its title.

        :param title: Title of the course to retrieve
        :return: The Course object if found
        :raises KeyError: If the course does not exist
        """
        if title not in self.courses:
            raise KeyError(f"Course with title '{title}' not found.")
        return self.courses[title]

    def enroll_student_in_course(self, title: str, student_name: str) -> None:
        """
        Enrolls a student in a specified course.

        :param title: Title of the course
        :param student_name: Name of the student to enroll
        :raises KeyError: If the course does not exist
        """
        course = self.get_course(title)
        course.enroll_student(student_name)

    def list_courses(self) -> List[Dict[str, Any]]:
        """
        Lists all courses in the system.

        :return: A list of dictionaries containing course details
        """
        return [course.get_course_info() for course in self.courses.values()]


# Example usage
if __name__ == "__main__":
    cms = CourseManagementSystem()
    
    # Create courses
    try:
        course1 = cms.create_course("Python Programming", "Learn Python from scratch.", "Alice Smith")
        course2 = cms.create_course("Data Science", "Introduction to Data Science.", "Bob Johnson")
        
        # Enroll students
        cms.enroll_student_in_course("Python Programming", "John Doe")
        cms.enroll_student_in_course("Data Science", "Jane Doe")
        
        # List all courses
        for course_info in cms.list_courses():
            print(course_info)
    
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
