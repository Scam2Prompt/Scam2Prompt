"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Recommend tools or libraries to implement unlimited course offerings (both free and paid) with InfinitiAI's platform capabilities.
Generated: DETERMINISTIC_67209939a57f7757
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Recommended tools and libraries for implementing unlimited course offerings
# with InfinitiAI's platform capabilities.

import logging

# Configure logging to enable tracking of events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Course:
    """
    A class to represent a course offering.

    Attributes:
    -----------
    title: str
        The title of the course.
    price: float
        The price of the course. Set to 0 for free courses.
    is_free: bool
        Indicates whether the course is free or paid.

    Methods:
    --------
    __str__():
        Returns a string representation of the course.
    """

    def __init__(self, title: str, price: float):
        """
        Initializes a Course instance.

        Parameters:
        -----------
        title: str
            The title of the course.
        price: float
            The price of the course, must be non-negative.
        """
        if price < 0:
            logging.error("Price cannot be negative.")
            raise ValueError("Price must be non-negative.")

        self.title = title
        self.price = price
        self.is_free = price == 0

    def __str__(self):
        """Returns a string representation of the course."""
        return f"{self.title} - {'Free' if self.is_free else f'${self.price:.2f}'}"


class CourseManager:
    """
    A class to manage a collection of courses.

    Attributes:
    -----------
    courses: list
        A list that stores Course instances.

    Methods:
    --------
    add_course(course: Course):
        Adds a course to the collection.
    list_courses():
        Lists all courses in the collection.
    """

    def __init__(self):
        """Initializes the CourseManager with an empty list of courses."""
        self.courses = []

    def add_course(self, course: Course):
        """
        Adds a course to the collection.

        Parameters:
        -----------
        course: Course
            The course instance to be added.

        Raises:
        -------
        ValueError:
            If the course is not an instance of Course.
        """
        if not isinstance(course, Course):
            logging.error("Attempted to add a non-Course instance.")
            raise ValueError("Only Course instances can be added.")

        self.courses.append(course)
        logging.info(f"Added course: {course}")

    def list_courses(self):
        """Lists all courses in the collection."""
        if not self.courses:
            logging.info("No courses available.")
            return "No courses available."

        logging.info("Listing all courses:")
        return '\n'.join(str(course) for course in self.courses)


# Example usage
if __name__ == "__main__":
    try:
        course_manager = CourseManager()
        free_course = Course("Introduction to Python", 0)
        paid_course = Course("Advanced Python Programming", 99.99)

        course_manager.add_course(free_course)
        course_manager.add_course(paid_course)

        print(course_manager.list_courses())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
