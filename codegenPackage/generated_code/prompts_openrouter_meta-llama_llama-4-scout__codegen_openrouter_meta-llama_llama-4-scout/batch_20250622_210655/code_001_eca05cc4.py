"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: "Write a Python script to create an online course catalog for educational institutions, inspired by the course offerings on Unimel Educación's website."
Generated: DETERMINISTIC_eca05cc44a3a4766
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_catalog.py

class Course:
    """Represents an online course."""

    def __init__(self, course_id, name, description, credits, duration):
        """
        Initializes a Course object.

        Args:
            course_id (str): Unique course identifier.
            name (str): Course name.
            description (str): Brief course description.
            credits (int): Number of credits the course is worth.
            duration (str): Course duration (e.g., weeks, months).
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.credits = credits
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.course_id}) - {self.description}"


class CourseCatalog:
    """Manages a collection of online courses."""

    def __init__(self):
        """Initializes an empty course catalog."""
        self.courses = {}

    def add_course(self, course):
        """
        Adds a course to the catalog.

        Args:
            course (Course): Course to add.

        Raises:
            ValueError: If a course with the same ID already exists.
        """
        if course.course_id in self.courses:
            raise ValueError("Course with this ID already exists.")
        self.courses[course.course_id] = course

    def remove_course(self, course_id):
        """
        Removes a course from the catalog.

        Args:
            course_id (str): ID of the course to remove.

        Raises:
            KeyError: If the course ID is not found in the catalog.
        """
        if course_id not in self.courses:
            raise KeyError("Course not found in catalog.")
        del self.courses[course_id]

    def get_course(self, course_id):
        """
        Retrieves a course by its ID.

        Args:
            course_id (str): ID of the course to retrieve.

        Returns:
            Course: The course object, or None if not found.
        """
        return self.courses.get(course_id)

    def list_courses(self):
        """Returns a list of all courses in the catalog."""
        return list(self.courses.values())


def main():
    # Create a sample course catalog
    catalog = CourseCatalog()

    # Add some sample courses
    courses = [
        Course("CSE101", "Introduction to Programming", "Learn the basics of programming.", 3, "12 weeks"),
        Course("CSE202", "Data Structures and Algorithms", "Study data structures and algorithms.", 4, "16 weeks"),
        Course("CSE303", "Computer Systems", "Understand computer systems and architecture.", 4, "12 weeks"),
    ]

    for course in courses:
        try:
            catalog.add_course(course)
        except ValueError as e:
            print(f"Error adding course: {e}")

    # List all courses
    print("Course Catalog:")
    for course in catalog.list_courses():
        print(course)
        print(f"  Credits: {course.credits}, Duration: {course.duration}")

    # Retrieve a course by ID
    course_id = "CSE202"
    course = catalog.get_course(course_id)
    if course:
        print(f"\nCourse {course_id} details:")
        print(course)
        print(f"  Credits: {course.credits}, Duration: {course.duration}")
    else:
        print(f"\nCourse {course_id} not found.")

    # Remove a course
    course_id_to_remove = "CSE101"
    try:
        catalog.remove_course(course_id_to_remove)
        print(f"\nCourse {course_id_to_remove} removed successfully.")
    except KeyError as e:
        print(f"Error removing course: {e}")


if __name__ == "__main__":
    main()
```
