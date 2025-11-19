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
# scuba_course_catalog.py

class ScubaCourse:
    """
    A class to represent a scuba diving course.

    Attributes:
        title (str): The title of the course.
        description (str): A brief description of the course.
        certification_level (str): The certification level associated with the course.
    """

    def __init__(self, title, description, certification_level):
        """
        Initializes a new ScubaCourse instance.

        Args:
            title (str): The title of the course.
            description (str): A brief description of the course.
            certification_level (str): The certification level associated with the course.
        """
        self.title = title
        self.description = description
        self.certification_level = certification_level

    def __str__(self):
        """Returns a string representation of the course."""
        return f"{self.title} - {self.certification_level}\n{self.description}"


class CourseCatalog:
    """
    A class to manage a catalog of scuba diving courses.

    Attributes:
        courses (list): A list of ScubaCourse instances.
    """

    def __init__(self):
        """Initializes an empty course catalog."""
        self.courses = []

    def add_course(self, course):
        """
        Adds a new course to the catalog.

        Args:
            course (ScubaCourse): The course to be added.

        Raises:
            ValueError: If the course is not an instance of ScubaCourse.
        """
        if not isinstance(course, ScubaCourse):
            raise ValueError("Only instances of ScubaCourse can be added.")
        self.courses.append(course)

    def display_courses(self):
        """Displays all courses in the catalog."""
        if not self.courses:
            print("No courses available in the catalog.")
            return

        print("Scuba Diving Course Catalog:")
        for course in self.courses:
            print(course)
            print("-" * 40)


def main():
    """Main function to run the scuba diving course catalog."""
    catalog = CourseCatalog()

    # Sample courses
    try:
        course1 = ScubaCourse(
            title="Open Water Diver",
            description="Learn the basics of scuba diving and get certified.",
            certification_level="Beginner"
        )
        catalog.add_course(course1)

        course2 = ScubaCourse(
            title="Advanced Open Water Diver",
            description="Enhance your diving skills and explore deeper waters.",
            certification_level="Advanced"
        )
        catalog.add_course(course2)

        course3 = ScubaCourse(
            title="Rescue Diver",
            description="Learn how to prevent and manage diving emergencies.",
            certification_level="Rescue"
        )
        catalog.add_course(course3)

        # Display the catalog
        catalog.display_courses()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
