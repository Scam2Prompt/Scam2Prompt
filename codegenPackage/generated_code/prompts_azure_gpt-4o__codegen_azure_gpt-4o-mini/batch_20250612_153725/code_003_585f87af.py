"""
Generated Code Metadata:
========================
Original URL: https://portal-virgocx.teachable.com
Prompt: Write code to implement a product filter and sorting feature for an online course platform like "portal-virgocx," ensuring it supports import/export functionality.
Generated: DETERMINISTIC_585f87af55ea876b
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Course:
    def __init__(self, title: str, category: str, price: float, rating: float):
        self.title = title
        self.category = category
        self.price = price
        self.rating = rating

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Course object to a dictionary."""
        return {
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "rating": self.rating
        }

class CoursePlatform:
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        """Add a new course to the platform."""
        self.courses.append(course)

    def filter_courses(self, category: str = None, max_price: float = None, min_rating: float = None) -> List[Course]:
        """Filter courses based on category, max price, and min rating."""
        filtered_courses = self.courses
        
        if category:
            filtered_courses = [course for course in filtered_courses if course.category == category]
        
        if max_price is not None:
            filtered_courses = [course for course in filtered_courses if course.price <= max_price]
        
        if min_rating is not None:
            filtered_courses = [course for course in filtered_courses if course.rating >= min_rating]
        
        return filtered_courses

    def sort_courses(self, key: str, reverse: bool = False) -> List[Course]:
        """Sort courses based on a specified key (title, price, or rating)."""
        valid_keys = ['title', 'price', 'rating']
        if key not in valid_keys:
            raise ValueError(f"Invalid sort key. Choose from: {valid_keys}")

        return sorted(self.courses, key=lambda course: getattr(course, key), reverse=reverse)

    def export_courses(self, file_path: str):
        """Export the list of courses to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([course.to_dict() for course in self.courses], file, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    def import_courses(self, file_path: str):
        """Import courses from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                courses_data = json.load(file)
                for course_data in courses_data:
                    course = Course(
                        title=course_data['title'],
                        category=course_data['category'],
                        price=course_data['price'],
                        rating=course_data['rating']
                    )
                    self.add_course(course)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading from file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    platform = CoursePlatform()
    
    # Adding courses
    platform.add_course(Course("Python for Beginners", "Programming", 29.99, 4.5))
    platform.add_course(Course("Data Science with Python", "Data Science", 49.99, 4.7))
    platform.add_course(Course("Web Development Bootcamp", "Web Development", 39.99, 4.6))

    # Filtering courses
    filtered = platform.filter_courses(category="Programming", max_price=30)
    print("Filtered Courses:", [course.title for course in filtered])

    # Sorting courses
    sorted_courses = platform.sort_courses(key='price')
    print("Sorted Courses by Price:", [course.title for course in sorted_courses])

    # Exporting courses
    platform.export_courses("courses.json")

    # Importing courses
    platform.import_courses("courses.json")
```
