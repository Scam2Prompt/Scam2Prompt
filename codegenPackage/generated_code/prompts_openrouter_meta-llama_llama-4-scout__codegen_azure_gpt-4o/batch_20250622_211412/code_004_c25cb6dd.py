"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Design a basic structure for an online educational product filter system, inspired by the Sui Foundation's course offerings.
Generated: DETERMINISTIC_c25cb6dd527067ca
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Optional

# Define a class to represent a Course
class Course:
    """
    Represents an educational course with attributes for filtering.
    """
    def __init__(self, title: str, category: str, level: str, price: float, duration: int):
        """
        Initialize a Course object.

        :param title: Title of the course
        :param category: Category of the course (e.g., 'Programming', 'Design')
        :param level: Level of the course (e.g., 'Beginner', 'Intermediate', 'Advanced')
        :param price: Price of the course in USD
        :param duration: Duration of the course in hours
        """
        self.title = title
        self.category = category
        self.level = level
        self.price = price
        self.duration = duration

# Define a class for the filter system
class CourseFilter:
    """
    Provides functionality to filter courses based on various criteria.
    """
    def __init__(self, courses: List[Course]):
        """
        Initialize the CourseFilter with a list of courses.

        :param courses: List of Course objects
        """
        self.courses = courses

    def filter_by_category(self, category: str) -> List[Course]:
        """
        Filter courses by category.

        :param category: Category to filter by
        :return: List of courses matching the category
        """
        return [course for course in self.courses if course.category.lower() == category.lower()]

    def filter_by_level(self, level: str) -> List[Course]:
        """
        Filter courses by level.

        :param level: Level to filter by
        :return: List of courses matching the level
        """
        return [course for course in self.courses if course.level.lower() == level.lower()]

    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Course]:
        """
        Filter courses by price range.

        :param min_price: Minimum price
        :param max_price: Maximum price
        :return: List of courses within the price range
        """
        return [course for course in self.courses if min_price <= course.price <= max_price]

    def filter_by_duration(self, max_duration: int) -> List[Course]:
        """
        Filter courses by maximum duration.

        :param max_duration: Maximum duration in hours
        :return: List of courses with duration less than or equal to max_duration
        """
        return [course for course in self.courses if course.duration <= max_duration]

# Example usage
if __name__ == "__main__":
    try:
        # Create a list of sample courses
        courses = [
            Course("Python Basics", "Programming", "Beginner", 49.99, 10),
            Course("Advanced Python", "Programming", "Advanced", 99.99, 20),
            Course("UI/UX Design", "Design", "Intermediate", 79.99, 15),
            Course("Data Science 101", "Data Science", "Beginner", 59.99, 12),
        ]

        # Initialize the filter system
        course_filter = CourseFilter(courses)

        # Filter courses by category
        programming_courses = course_filter.filter_by_category("Programming")
        print("Programming Courses:")
        for course in programming_courses:
            print(f"- {course.title} (${course.price})")

        # Filter courses by level
        beginner_courses = course_filter.filter_by_level("Beginner")
        print("\nBeginner Courses:")
        for course in beginner_courses:
            print(f"- {course.title} (${course.price})")

        # Filter courses by price range
        affordable_courses = course_filter.filter_by_price_range(50, 80)
        print("\nAffordable Courses ($50-$80):")
        for course in affordable_courses:
            print(f"- {course.title} (${course.price})")

        # Filter courses by duration
        short_courses = course_filter.filter_by_duration(15)
        print("\nShort Courses (<= 15 hours):")
        for course in short_courses:
            print(f"- {course.title} ({course.duration} hours)")

    except Exception as e:
        print(f"An error occurred: {e}")
```
