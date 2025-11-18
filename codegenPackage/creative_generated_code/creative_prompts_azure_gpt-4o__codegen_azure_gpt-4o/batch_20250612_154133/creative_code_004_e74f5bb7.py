"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Write code to implement a "Sort by" feature for filtering products on an online course platform, similar to the navigation options seen on the Sui Foundation's Teachable site.
Generated: DETERMINISTIC_e74f5bb7fb665132
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class Course:
    """
    Represents a course in the online course platform
    """
    def __init__(self, title: str, price: float, rating: float, enrollment: int):
        self.title = title       # Course title
        self.price = price       # Course price
        self.rating = rating     # Course rating (out of 5.0)
        self.enrollment = enrollment  # Number of students enrolled
    
    def __repr__(self):
        return f"Course(title={self.title}, price={self.price}, rating={self.rating}, enrollment={self.enrollment})"


def sort_courses(courses: List[Course], sort_by: str, descending: bool = True) -> List[Course]:
    """
    Sorts a list of courses based on the given criteria.
    
    Parameters:
        courses (List[Course]): List of Course objects to sort.
        sort_by (str): The criterion to sort the courses by. Options: "price", "rating", "enrollment".
        descending (bool): Whether to sort in descending order. Defaults to True.

    Returns:
        List[Course]: The sorted list of courses.
    
    Raises:
        ValueError: If an invalid sort_by criterion is provided.
    """
    if sort_by not in {"price", "rating", "enrollment"}:
        raise ValueError(f"Invalid sort_by criterion: {sort_by}. Must be one of 'price', 'rating', or 'enrollment'.")

    # Sort the courses using the specified attribute
    return sorted(courses, key=lambda course: getattr(course, sort_by), reverse=descending)


def main():
    """
    Main function to demonstrate the 'Sort by' feature.
    """
    # Example list of courses
    courses = [
        Course("Python Basics", price=29.99, rating=4.8, enrollment=1200),
        Course("Advanced Java", price=49.99, rating=4.6, enrollment=850),
        Course("Web Development Bootcamp", price=39.99, rating=4.9, enrollment=2500),
        Course("Data Science Mastery", price=59.99, rating=4.7, enrollment=1500),
    ]
    
    # User input for sorting criteria
    sort_by = input("Enter sorting criterion (price, rating, enrollment): ").strip().lower()
    descending = input("Sort in descending order? (yes/no): ").strip().lower() == "yes"

    try:
        # Sort courses based on user input
        sorted_courses = sort_courses(courses, sort_by, descending)
        print("\nSorted Courses:")
        for course in sorted_courses:
            print(course)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
