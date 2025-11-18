"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-virgocx.teachable.com
Prompt: Write code to implement a product filter and sorting feature for an online course platform like "portal-virgocx," ensuring it supports import/export functionality.
Generated: DETERMINISTIC_585f87af55ea876b
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Course:
    """Represents a course with a title, category, and rating."""
    
    def __init__(self, title: str, category: str, rating: float):
        self.title = title
        self.category = category
        self.rating = rating

    def to_dict(self) -> Dict[str, Any]:
        """Converts the Course object to a dictionary."""
        return {
            "title": self.title,
            "category": self.category,
            "rating": self.rating
        }

class CourseManager:
    """Manages a collection of courses with filtering and sorting capabilities."""
    
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        """Adds a new course to the collection."""
        self.courses.append(course)

    def filter_courses(self, category: str = None, min_rating: float = None) -> List[Course]:
        """
        Filters courses based on category and/or minimum rating.
        
        Args:
            category: The category to filter courses by (optional).
            min_rating: The minimum rating to filter courses by (optional).
        
        Returns:
            A list of filtered courses.
        """
        filtered_courses = self.courses
        if category:
            filtered_courses = [course for course in filtered_courses if course.category == category]
        if min_rating is not None:
            filtered_courses = [course for course in filtered_courses if course.rating >= min_rating]
        
        return filtered_courses

    def sort_courses(self, key: str = 'rating', reverse: bool = False) -> List[Course]:
        """
        Sorts the courses based on the specified key.

        Args:
            key: The attribute to sort by ('title', 'category', 'rating').
            reverse: Whether to sort in descending order (optional).
        
        Returns:
            A list of sorted courses.
        
        Raises:
            ValueError: If an invalid key is provided for sorting.
        """
        valid_keys = ['title', 'category', 'rating']
        if key not in valid_keys:
            raise ValueError(f"Invalid sort key. Valid keys are: {valid_keys}")

        return sorted(self.courses, key=lambda course: getattr(course, key), reverse=reverse)

    def export_courses(self, filename: str):
        """Exports courses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([course.to_dict() for course in self.courses], file, indent=4)
        except IOError as e:
            print(f"Error exporting courses: {e}")

    def import_courses(self, filename: str):
        """Imports courses from a JSON file."""
        try:
            with open(filename, 'r') as file:
                course_data = json.load(file)
                for item in course_data:
                    self.add_course(Course(item['title'], item['category'], item['rating']))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error importing courses: {e}")


# Example usage
if __name__ == "__main__":
    manager = CourseManager()
    manager.add_course(Course("Python 101", "Programming", 4.5))
    manager.add_course(Course("Data Science Essentials", "Data Science", 4.7))
    manager.add_course(Course("Web Development", "Programming", 4.3))

    # Filtering courses
    filtered = manager.filter_courses(category="Programming", min_rating=4.4)
    print("Filtered Courses:", [course.title for course in filtered])

    # Sorting courses
    sorted_courses = manager.sort_courses(key='rating', reverse=True)
    print("Sorted Courses:", [course.title for course in sorted_courses])

    # Exporting courses
    manager.export_courses("courses.json")

    # Importing courses
    manager.import_courses("courses.json")
```
