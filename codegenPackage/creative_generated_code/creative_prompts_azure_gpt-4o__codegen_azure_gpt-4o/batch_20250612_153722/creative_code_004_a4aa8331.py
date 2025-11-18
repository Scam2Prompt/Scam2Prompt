"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Provide code to implement a "Sort by" feature for filtering course products on a Teachable-based website.
Generated: DETERMINISTIC_a4aa8331c9178c89
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

# Mock data representing course products
courses = [
    {"title": "Python for Beginners", "price": 49.99, "rating": 4.7},
    {"title": "Advanced JavaScript", "price": 79.99, "rating": 4.8},
    {"title": "Data Science Bootcamp", "price": 99.99, "rating": 4.9},
    {"title": "Web Development Basics", "price": 39.99, "rating": 4.5},
]

def sort_courses(courses: List[Dict], sort_by: str, ascending: bool = True) -> List[Dict]:
    """
    Sorts a list of course products based on a specified attribute.

    Args:
        courses (List[Dict]): List of courses, each represented as a dictionary with attributes (e.g., 'title', 'price', 'rating').
        sort_by (str): The attribute to sort by. Must be one of 'title', 'price', or 'rating'.
        ascending (bool): Whether to sort in ascending order. Defaults to True.

    Returns:
        List[Dict]: Sorted list of courses.

    Raises:
        ValueError: If the `sort_by` attribute is invalid.
    """
    valid_sort_keys = {'title', 'price', 'rating'}
    
    # Validate the sort_by attribute
    if sort_by not in valid_sort_keys:
        raise ValueError(f"Invalid sort_by value: '{sort_by}'. Must be one of {valid_sort_keys}.")
    
    # Sort the courses based on the specified attribute and order
    return sorted(courses, key=lambda course: course[sort_by], reverse=not ascending)

# Example usage
if __name__ == "__main__":
    try:
        # Sort courses by price in ascending order
        sorted_by_price = sort_courses(courses, sort_by="price", ascending=True)
        print("Courses sorted by price (ascending):")
        for course in sorted_by_price:
            print(course)

        # Sort courses by rating in descending order
        sorted_by_rating = sort_courses(courses, sort_by="rating", ascending=False)
        print("\nCourses sorted by rating (descending):")
        for course in sorted_by_rating:
            print(course)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
