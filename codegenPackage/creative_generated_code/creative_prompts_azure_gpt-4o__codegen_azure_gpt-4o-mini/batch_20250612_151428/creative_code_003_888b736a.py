"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Create a Python function that organizes art courses into categories like "painting," "drawing," and "digital design," based on Ânima's course offerings.
Generated: DETERMINISTIC_888b736a8845bd47
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class CourseOrganizer:
    """
    A class to organize art courses into categories based on their offerings.
    """

    def __init__(self):
        """
        Initializes the CourseOrganizer with an empty course catalog.
        """
        self.course_catalog: Dict[str, List[str]] = {
            'painting': [],
            'drawing': [],
            'digital design': []
        }

    def add_course(self, category: str, course_name: str) -> None:
        """
        Adds a course to the specified category.

        :param category: The category to which the course belongs.
        :param course_name: The name of the course to add.
        :raises ValueError: If the category is not recognized.
        """
        if category not in self.course_catalog:
            raise ValueError(f"Unrecognized category: {category}. Please use one of the following: {', '.join(self.course_catalog.keys())}")

        self.course_catalog[category].append(course_name)

    def organize_courses(self, courses: List[Dict[str, Any]]) -> None:
        """
        Organizes a list of courses into categories.

        :param courses: A list of dictionaries containing course information.
        """
        for course in courses:
            try:
                category = course['category']
                course_name = course['name']
                self.add_course(category, course_name)
            except KeyError as e:
                print(f"Error: Missing key {e} in course data: {course}")
            except ValueError as e:
                print(e)

    def get_courses(self) -> Dict[str, List[str]]:
        """
        Returns the organized course catalog.

        :return: A dictionary containing the organized course categories and their respective courses.
        """
        return self.course_catalog


# Example usage
if __name__ == "__main__":
    organizer = CourseOrganizer()

    # Example input data for courses
    courses_data = [
        {'name': 'Acrylic Painting Basics', 'category': 'painting'},
        {'name': 'Charcoal Drawing Techniques', 'category': 'drawing'},
        {'name': 'Digital Illustration with Photoshop', 'category': 'digital design'},
        {'name': 'Watercolor Techniques', 'category': 'painting'},
        {'name': 'Figure Drawing', 'category': 'drawing'},
        {'name': '3D Modeling Basics', 'category': 'digital design'},
        {'name': 'Abstract Art', 'category': 'unknown'}  # This will raise an error
    ]

    # Organize the courses
    organizer.organize_courses(courses_data)

    # Print organized courses
    print(organizer.get_courses())
```
