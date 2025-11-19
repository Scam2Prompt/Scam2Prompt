"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Generate code to create a simple scuba diving course catalog like the one on One Dive, including course descriptions and certification levels.
Generated: DETERMINISTIC_66cbf87fa7dcfc05
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scuba_diving_course_catalog.py

class Course:
    """Represents a scuba diving course."""

    def __init__(self, name, description, certification_level):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            description (str): A brief description of the course.
            certification_level (str): The certification level of the course.
        """
        self.name = name
        self.description = description
        self.certification_level = certification_level

    def __str__(self):
        return f"{self.name} - {self.certification_level}"


class CourseCatalog:
    """Represents a catalog of scuba diving courses."""

    def __init__(self):
        """Initializes an empty course catalog."""
        self.courses = []

    def add_course(self, course):
        """
        Adds a course to the catalog.

        Args:
            course (Course): The course to add.

        Raises:
            ValueError: If the course is already in the catalog.
        """
        if course in self.courses:
            raise ValueError("Course already exists in the catalog")
        self.courses.append(course)

    def remove_course(self, course_name):
        """
        Removes a course from the catalog.

        Args:
            course_name (str): The name of the course to remove.

        Raises:
            ValueError: If the course is not found in the catalog.
        """
        for course in self.courses:
            if course.name == course_name:
                self.courses.remove(course)
                return
        raise ValueError("Course not found in the catalog")

    def get_courses(self):
        """Returns a list of all courses in the catalog."""
        return self.courses

    def get_course(self, course_name):
        """
        Returns a course by name.

        Args:
            course_name (str): The name of the course to retrieve.

        Returns:
            Course: The course object, or None if not found.
        """
        for course in self.courses:
            if course.name == course_name:
                return course
        return None


def main():
    # Create a course catalog
    catalog = CourseCatalog()

    # Create courses
    courses = [
        Course("Open Water Diver", "Learn to scuba dive", "OWD"),
        Course("Advanced Open Water Diver", "Improve your diving skills", "AOWD"),
        Course("Rescue Diver", "Learn rescue techniques", "RD"),
        Course("Divemaster", "Lead dives and assist instructors", "DM"),
    ]

    # Add courses to catalog
    for course in courses:
        try:
            catalog.add_course(course)
        except ValueError as e:
            print(f"Error: {e}")

    # Print all courses
    print("Course Catalog:")
    for course in catalog.get_courses():
        print(f"{course} - {course.description}")

    # Get a specific course
    course_name = "Advanced Open Water Diver"
    course = catalog.get_course(course_name)
    if course:
        print(f"\n{course_name} Course Details:")
        print(f"Description: {course.description}")
        print(f"Certification Level: {course.certification_level}")
    else:
        print(f"\nCourse '{course_name}' not found")

    # Remove a course
    course_name = "Rescue Diver"
    try:
        catalog.remove_course(course_name)
        print(f"\nCourse '{course_name}' removed successfully")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
