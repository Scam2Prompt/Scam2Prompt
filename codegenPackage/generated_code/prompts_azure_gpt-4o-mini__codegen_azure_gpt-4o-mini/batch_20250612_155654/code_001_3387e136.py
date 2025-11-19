"""
Generated Code Metadata:
========================
Original URL: https://rabbi-apps.teachable.com
Prompt: What features does rabbi-apps offer for course creation and management?
Generated: DETERMINISTIC_3387e1366ea16229
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
rabbi_apps.py

This module provides a class for managing course creation and management features
offered by the rabbi-apps platform. It includes methods for creating, updating,
deleting, and retrieving courses, along with error handling and data validation.
"""

class Course:
    """
    A class to represent a course.

    Attributes:
        title (str): The title of the course.
        description (str): A brief description of the course.
        instructor (str): The name of the instructor.
        course_id (int): A unique identifier for the course.
    """

    def __init__(self, title, description, instructor, course_id):
        """
        Initializes a new course instance.

        Args:
            title (str): The title of the course.
            description (str): A brief description of the course.
            instructor (str): The name of the instructor.
            course_id (int): A unique identifier for the course.
        """
        self.title = title
        self.description = description
        self.instructor = instructor
        self.course_id = course_id

    def __str__(self):
        """Returns a string representation of the course."""
        return f"Course ID: {self.course_id}, Title: {self.title}, Instructor: {self.instructor}"


class CourseManager:
    """
    A class to manage a collection of courses.

    Attributes:
        courses (dict): A dictionary to store courses with course_id as the key.
    """

    def __init__(self):
        """Initializes the CourseManager with an empty course collection."""
        self.courses = {}

    def add_course(self, course):
        """
        Adds a new course to the collection.

        Args:
            course (Course): The course to be added.

        Raises:
            ValueError: If the course_id already exists.
        """
        if course.course_id in self.courses:
            raise ValueError(f"Course ID {course.course_id} already exists.")
        self.courses[course.course_id] = course

    def update_course(self, course_id, title=None, description=None, instructor=None):
        """
        Updates an existing course's details.

        Args:
            course_id (int): The ID of the course to update.
            title (str, optional): The new title of the course.
            description (str, optional): The new description of the course.
            instructor (str, optional): The new instructor of the course.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID {course_id} does not exist.")
        
        course = self.courses[course_id]
        if title:
            course.title = title
        if description:
            course.description = description
        if instructor:
            course.instructor = instructor

    def delete_course(self, course_id):
        """
        Deletes a course from the collection.

        Args:
            course_id (int): The ID of the course to delete.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID {course_id} does not exist.")
        del self.courses[course_id]

    def get_course(self, course_id):
        """
        Retrieves a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The course object.

        Raises:
            KeyError: If the course_id does not exist.
        """
        if course_id not in self.courses:
            raise KeyError(f"Course ID {course_id} does not exist.")
        return self.courses[course_id]

    def list_courses(self):
        """Returns a list of all courses in the collection."""
        return list(self.courses.values())


# Example usage
if __name__ == "__main__":
    manager = CourseManager()
    
    # Create courses
    course1 = Course("Python Programming", "Learn Python from scratch", "John Doe", 1)
    course2 = Course("Data Science", "Introduction to Data Science", "Jane Smith", 2)

    # Add courses
    manager.add_course(course1)
    manager.add_course(course2)

    # List courses
    for course in manager.list_courses():
        print(course)

    # Update a course
    manager.update_course(1, instructor="Johnathan Doe")

    # Retrieve a specific course
    print(manager.get_course(1))

    # Delete a course
    manager.delete_course(2)

    # List courses after deletion
    for course in manager.list_courses():
        print(course)
```
