"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write a Python code to manage online courses and e-learning platforms for a non-profit organization like SKI Foundation.
Generated: DETERMINISTIC_5d5ce7fb4821808b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Course:
    """
    Represents a course in the e-learning platform.
    """
    def __init__(self, course_id, title, description, instructor, duration):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration  # Duration in hours

    def to_dict(self):
        """
        Converts the course object to a dictionary for serialization.
        """
        return {
            "course_id": self.course_id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "duration": self.duration
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a course object from a dictionary.
        """
        return Course(
            course_id=data["course_id"],
            title=data["title"],
            description=data["description"],
            instructor=data["instructor"],
            duration=data["duration"]
        )


class ELearningPlatform:
    """
    Manages courses for the e-learning platform.
    """
    def __init__(self, data_file="courses.json"):
        self.data_file = data_file
        self.courses = self.load_courses()

    def load_courses(self):
        """
        Loads courses from a JSON file.
        """
        if not os.path.exists(self.data_file):
            return []

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                return [Course.from_dict(course) for course in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading courses: {e}")
            return []

    def save_courses(self):
        """
        Saves courses to a JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump([course.to_dict() for course in self.courses], file, indent=4)
        except IOError as e:
            print(f"Error saving courses: {e}")

    def add_course(self, course):
        """
        Adds a new course to the platform.
        """
        if any(c.course_id == course.course_id for c in self.courses):
            print(f"Course with ID {course.course_id} already exists.")
            return

        self.courses.append(course)
        self.save_courses()
        print(f"Course '{course.title}' added successfully.")

    def remove_course(self, course_id):
        """
        Removes a course by its ID.
        """
        self.courses = [course for course in self.courses if course.course_id != course_id]
        self.save_courses()
        print(f"Course with ID {course_id} removed successfully.")

    def list_courses(self):
        """
        Lists all available courses.
        """
        if not self.courses:
            print("No courses available.")
            return

        for course in self.courses:
            print(f"ID: {course.course_id}, Title: {course.title}, Instructor: {course.instructor}, Duration: {course.duration} hours")


# Example usage
if __name__ == "__main__":
    platform = ELearningPlatform()

    # Add a new course
    new_course = Course(
        course_id="C101",
        title="Introduction to Python",
        description="Learn the basics of Python programming.",
        instructor="John Doe",
        duration=10
    )
    platform.add_course(new_course)

    # List all courses
    platform.list_courses()

    # Remove a course
    platform.remove_course("C101")

    # List all courses after removal
    platform.list_courses()
```
