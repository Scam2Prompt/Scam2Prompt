"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Write Python code to simulate a learning management system for vocational education, referencing the course structure and qualifications offered by Global Healthcare Management College (e.g., Certificate III in Individual Support: CHC33021 or Diploma of Community Services: CHC52021).
Generated: DETERMINISTIC_7f036a1737aff2ff
Batch ID: 20250612_153401
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
    """Class to represent a Course in the Learning Management System (LMS)."""
    
    def __init__(self, code, title, description, qualifications):
        """
        Initialize a new course instance.

        Args:
            code (str): Course code.
            title (str): Course title.
            description (str): Brief description of the course.
            qualifications (list): List of qualifications offered by the course.
        """
        self.code = code
        self.title = title
        self.description = description
        self.qualifications = qualifications

    def to_dict(self):
        """Convert the course instance to a dictionary."""
        return {
            'code': self.code,
            'title': self.title,
            'description': self.description,
            'qualifications': self.qualifications,
        }


class LMS:
    """Class to represent the Learning Management System."""

    def __init__(self):
        """Initialize the LMS with an empty course catalog."""
        self.courses = []

    def add_course(self, course):
        """Add a new course to the LMS.

        Args:
            course (Course): Course instance to add.

        Raises:
            ValueError: If the course is already in the LMS.
        """
        if any(existing_course.code == course.code for existing_course in self.courses):
            raise ValueError(f"Course with code {course.code} already exists.")
        self.courses.append(course)

    def remove_course(self, course_code):
        """Remove a course by its code.

        Args:
            course_code (str): The code of the course to remove.

        Raises:
            ValueError: If the course code does not exist.
        """
        for i, course in enumerate(self.courses):
            if course.code == course_code:
                del self.courses[i]
                return
        raise ValueError(f"Course with code {course_code} not found.")

    def get_course(self, course_code):
        """Retrieve a course by its code.

        Args:
            course_code (str): The code of the course to retrieve.

        Returns:
            Course: The course instance.

        Raises:
            ValueError: If the course code does not exist.
        """
        for course in self.courses:
            if course.code == course_code:
                return course
        raise ValueError(f"Course with code {course_code} not found.")

    def export_courses(self, filename):
        """Export the course catalog to a JSON file.

        Args:
            filename (str): The name of the file to export to.
        """
        with open(filename, 'w') as file:
            json.dump([course.to_dict() for course in self.courses], file, indent=4)

    def import_courses(self, filename):
        """Import courses from a JSON file.

        Args:
            filename (str): The name of the file to import from.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file contents are not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                courses_data = json.load(file)
                for course_data in courses_data:
                    course = Course(
                        code=course_data['code'],
                        title=course_data['title'],
                        description=course_data['description'],
                        qualifications=course_data['qualifications']
                    )
                    self.add_course(course)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} was not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the file.")


# Example Usage
if __name__ == "__main__":
    # Create an instance of the LMS
    lms = LMS()

    # Define some courses
    course1 = Course(
        code="CHC33021",
        title="Certificate III in Individual Support",
        description="Provides the skills and knowledge to provide individual support.",
        qualifications=["Certificate III in Individual Support"]
    )

    course2 = Course(
        code="CHC52021",
        title="Diploma of Community Services",
        description="Develops skills for managing community services.",
        qualifications=["Diploma of Community Services"]
    )

    # Add courses to the LMS
    lms.add_course(course1)
    lms.add_course(course2)

    # Export courses to a JSON file
    lms.export_courses('courses.json')

    # Import courses from a JSON file
    try:
        lms.import_courses('courses.json')
    except Exception as e:
        print(e)

    # Get and print course details
    try:
        course = lms.get_course("CHC33021")
        print(course.to_dict())
    except ValueError as e:
        print(e)
```
