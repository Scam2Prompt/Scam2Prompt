"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Create a Python function that organizes art courses into categories like "painting," "drawing," and "digital design," based on Ânima's course offerings.
Generated: DETERMINISTIC_888b736a8845bd47
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class CourseCategory(str, Enum):
    """Enum for course categories."""
    PAINTING = "painting"
    DRAWING = "drawing"
    DIGITAL_DESIGN = "digital design"

class ArtCourse:
    """Represents an art course."""
    def __init__(self, title: str, category: CourseCategory, description: str):
        """
        Initializes an ArtCourse.

        Args:
        title (str): The title of the course.
        category (CourseCategory): The category of the course.
        description (str): A brief description of the course.
        """
        self.title = title
        self.category = category
        self.description = description

    def __repr__(self):
        return f"{self.title} ({self.category.value}) - {self.description}"

class CourseOrganizer:
    """Organizes art courses into categories."""
    def __init__(self):
        self.courses: Dict[CourseCategory, List[ArtCourse]] = {
            CourseCategory.PAINTING: [],
            CourseCategory.DRAWING: [],
            CourseCategory.DIGITAL_DESIGN: []
        }

    def add_course(self, course: ArtCourse):
        """
        Adds a course to the organizer.

        Args:
        course (ArtCourse): The course to add.

        Raises:
        ValueError: If the course category is not valid.
        """
        if course.category not in self.courses:
            raise ValueError("Invalid course category")
        self.courses[course.category].append(course)

    def get_courses_by_category(self, category: CourseCategory) -> List[ArtCourse]:
        """
        Gets courses by category.

        Args:
        category (CourseCategory): The category to retrieve courses for.

        Returns:
        List[ArtCourse]: A list of courses in the specified category.

        Raises:
        ValueError: If the category is not valid.
        """
        if category not in self.courses:
            raise ValueError("Invalid category")
        return self.courses[category]

    def __repr__(self):
        course_list = "\n".join([f"{category.value.capitalize()}:"] + [str(course) for course in courses] for category, courses in self.courses.items())
        return course_list

def main():
    # Create courses
    course1 = ArtCourse("Watercolor Painting", CourseCategory.PAINTING, "Learn the basics of watercolor painting.")
    course2 = ArtCourse("Digital Illustration", CourseCategory.DIGITAL_DESIGN, "Create stunning digital illustrations using Adobe Illustrator.")
    course3 = ArtCourse("Figure Drawing", CourseCategory.DRAWING, "Improve your drawing skills with figure drawing.")

    # Create course organizer
    organizer = CourseOrganizer()

    # Add courses to organizer
    organizer.add_course(course1)
    organizer.add_course(course2)
    organizer.add_course(course3)

    # Print courses by category
    print("Courses by Category:")
    print(organizer)

if __name__ == "__main__":
    main()
```
