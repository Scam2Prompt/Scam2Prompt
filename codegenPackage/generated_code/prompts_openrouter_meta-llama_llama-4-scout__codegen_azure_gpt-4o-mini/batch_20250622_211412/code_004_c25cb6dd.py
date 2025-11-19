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
# online_education_filter.py

class Course:
    """
    Represents a course in the online educational product.
    
    Attributes:
        title (str): The title of the course.
        category (str): The category of the course (e.g., 'Programming', 'Design').
        level (str): The difficulty level of the course (e.g., 'Beginner', 'Intermediate', 'Advanced').
        price (float): The price of the course.
    """

    def __init__(self, title: str, category: str, level: str, price: float):
        self.title = title
        self.category = category
        self.level = level
        self.price = price

    def __repr__(self):
        return f"Course(title={self.title}, category={self.category}, level={self.level}, price={self.price})"


class CourseFilter:
    """
    A class to filter courses based on various criteria.
    
    Attributes:
        courses (list): A list of Course objects to filter.
    """

    def __init__(self, courses: list):
        if not all(isinstance(course, Course) for course in courses):
            raise ValueError("All items in courses must be instances of the Course class.")
        self.courses = courses

    def filter_by_category(self, category: str) -> list:
        """
        Filters courses by category.
        
        Args:
            category (str): The category to filter by.
        
        Returns:
            list: A list of courses that match the specified category.
        """
        return [course for course in self.courses if course.category.lower() == category.lower()]

    def filter_by_level(self, level: str) -> list:
        """
        Filters courses by difficulty level.
        
        Args:
            level (str): The level to filter by.
        
        Returns:
            list: A list of courses that match the specified level.
        """
        return [course for course in self.courses if course.level.lower() == level.lower()]

    def filter_by_price_range(self, min_price: float, max_price: float) -> list:
        """
        Filters courses by price range.
        
        Args:
            min_price (float): The minimum price.
            max_price (float): The maximum price.
        
        Returns:
            list: A list of courses within the specified price range.
        """
        if min_price < 0 or max_price < 0:
            raise ValueError("Price values must be non-negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")
        
        return [course for course in self.courses if min_price <= course.price <= max_price]


# Example usage
if __name__ == "__main__":
    # Sample courses
    courses = [
        Course("Python for Beginners", "Programming", "Beginner", 49.99),
        Course("Advanced JavaScript", "Programming", "Advanced", 79.99),
        Course("UI/UX Design Basics", "Design", "Intermediate", 59.99),
        Course("Data Science with Python", "Data Science", "Intermediate", 89.99),
    ]

    # Create a CourseFilter instance
    course_filter = CourseFilter(courses)

    # Filter courses by category
    programming_courses = course_filter.filter_by_category("Programming")
    print("Programming Courses:", programming_courses)

    # Filter courses by level
    beginner_courses = course_filter.filter_by_level("Beginner")
    print("Beginner Courses:", beginner_courses)

    # Filter courses by price range
    affordable_courses = course_filter.filter_by_price_range(0, 60)
    print("Affordable Courses:", affordable_courses)
```
