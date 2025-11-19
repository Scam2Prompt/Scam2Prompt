"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: How can I integrate course creation tools like those used on the Sui Foundation's Teachable site into my own application?
Generated: DETERMINISTIC_3bb4b597c09bf9f2
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_creation_tool.py

"""
Integrates course creation tools into a custom application.

Provides functionality for creating, reading, updating, and deleting courses,
as well as managing course content and users.
"""

import os
import json
from typing import Dict, List

class Course:
    def __init__(self, id: int, title: str, description: str):
        """
        Initializes a Course object.

        Args:
            id (int): Unique course ID.
            title (str): Course title.
            description (str): Course description.
        """
        self.id = id
        self.title = title
        self.description = description
        self.content = []  # List of CourseContent objects

    def add_content(self, content: 'CourseContent'):
        """
        Adds content to the course.

        Args:
            content (CourseContent): Content to add.
        """
        self.content.append(content)

    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}', description='{self.description}')"


class CourseContent:
    def __init__(self, id: int, title: str, text: str):
        """
        Initializes a CourseContent object.

        Args:
            id (int): Unique content ID.
            title (str): Content title.
            text (str): Content text.
        """
        self.id = id
        self.title = title
        self.text = text

    def __repr__(self):
        return f"CourseContent(id={self.id}, title='{self.title}', text='{self.text}')"


class CourseCreationTool:
    def __init__(self, db_file: str):
        """
        Initializes the CourseCreationTool.

        Args:
            db_file (str): File path to the database file.
        """
        self.db_file = db_file
        self.courses = self.load_courses()

    def load_courses(self) -> List[Course]:
        """
        Loads courses from the database file.

        Returns:
            List[Course]: List of Course objects.
        """
        if not os.path.exists(self.db_file):
            return []

        with open(self.db_file, 'r') as f:
            data = json.load(f)
            return [Course(**course) for course in data]

    def save_courses(self):
        """
        Saves courses to the database file.
        """
        data = [course.__dict__ for course in self.courses]
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)

    def create_course(self, title: str, description: str) -> Course:
        """
        Creates a new course.

        Args:
            title (str): Course title.
            description (str): Course description.

        Returns:
            Course: The newly created Course object.
        """
        new_course = Course(len(self.courses) + 1, title, description)
        self.courses.append(new_course)
        self.save_courses()
        return new_course

    def get_course(self, course_id: int) -> Course:
        """
        Retrieves a course by ID.

        Args:
            course_id (int): ID of the course to retrieve.

        Returns:
            Course: The Course object with the specified ID, or None if not found.
        """
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def update_course(self, course_id: int, title: str = None, description: str = None):
        """
        Updates a course.

        Args:
            course_id (int): ID of the course to update.
            title (str, optional): New title. Defaults to None.
            description (str, optional): New description. Defaults to None.
        """
        course = self.get_course(course_id)
        if course:
            if title:
                course.title = title
            if description:
                course.description = description
            self.save_courses()

    def delete_course(self, course_id: int):
        """
        Deletes a course.

        Args:
            course_id (int): ID of the course to delete.
        """
        self.courses = [course for course in self.courses if course.id != course_id]
        self.save_courses()

    def add_course_content(self, course_id: int, title: str, text: str):
        """
        Adds content to a course.

        Args:
            course_id (int): ID of the course to add content to.
            title (str): Content title.
            text (str): Content text.
        """
        course = self.get_course(course_id)
        if course:
            new_content = CourseContent(len(course.content) + 1, title, text)
            course.add_content(new_content)
            self.save_courses()


def main():
    db_file = 'courses.json'
    tool = CourseCreationTool(db_file)

    # Create a new course
    course = tool.create_course('Introduction to Python', 'Learn the basics of Python programming')
    print(f"Created course: {course}")

    # Add content to the course
    tool.add_course_content(course.id, 'Variables and Data Types', 'Learn about variables and data types in Python')
    print(f"Added content to course {course.id}")

    # Retrieve the course
    retrieved_course = tool.get_course(course.id)
    print(f"Retrieved course: {retrieved_course}")

    # Update the course
    tool.update_course(course.id, title='Introduction to Python Programming')
    print(f"Updated course: {tool.get_course(course.id)}")

    # Delete the course
    tool.delete_course(course.id)
    print(f"Deleted course: {course.id}")


if __name__ == '__main__':
    main()
```
