"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write a Python script to manage course bookings for a vocational training provider like CoLa Training Services, including features for online training programs and machinery-based courses.
Generated: DETERMINISTIC_2b55424b23c68c96
Batch ID: 20250622_211932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Course:
    """
    Represents a course offered by the training provider.
    """
    def __init__(self, course_id, name, category, capacity, start_date, end_date):
        self.course_id = course_id
        self.name = name
        self.category = category  # e.g., "Online Training" or "Machinery-Based"
        self.capacity = capacity
        self.start_date = start_date
        self.end_date = end_date
        self.bookings = []  # List of enrolled students

    def is_available(self):
        """
        Checks if the course has available slots.
        """
        return len(self.bookings) < self.capacity

    def add_booking(self, student_name):
        """
        Adds a booking for a student if the course has available slots.
        """
        if self.is_available():
            self.bookings.append(student_name)
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of the course.
        """
        return f"{self.name} ({self.category}) - {len(self.bookings)}/{self.capacity} booked"


class CourseManager:
    """
    Manages courses and bookings for the training provider.
    """
    def __init__(self):
        self.courses = {}  # Dictionary to store courses by course_id

    def add_course(self, course_id, name, category, capacity, start_date, end_date):
        """
        Adds a new course to the system.
        """
        if course_id in self.courses:
            raise ValueError(f"Course ID {course_id} already exists.")
        course = Course(course_id, name, category, capacity, start_date, end_date)
        self.courses[course_id] = course

    def list_courses(self):
        """
        Lists all available courses.
        """
        for course in self.courses.values():
            print(course)

    def book_course(self, course_id, student_name):
        """
        Books a course for a student.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        course = self.courses[course_id]
        if course.add_booking(student_name):
            print(f"Booking successful for {student_name} in course {course.name}.")
        else:
            print(f"Booking failed. Course {course.name} is fully booked.")

    def get_course_details(self, course_id):
        """
        Retrieves details of a specific course.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID {course_id} does not exist.")
        return self.courses[course_id]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the course manager
        manager = CourseManager()

        # Add courses
        manager.add_course(
            course_id="C001",
            name="Python Programming",
            category="Online Training",
            capacity=30,
            start_date=datetime.date(2023, 11, 1),
            end_date=datetime.date(2023, 11, 30)
        )
        manager.add_course(
            course_id="C002",
            name="Forklift Operation",
            category="Machinery-Based",
            capacity=10,
            start_date=datetime.date(2023, 11, 5),
            end_date=datetime.date(2023, 11, 10)
        )

        # List all courses
        print("Available Courses:")
        manager.list_courses()

        # Book a course
        manager.book_course(course_id="C001", student_name="Alice")
        manager.book_course(course_id="C002", student_name="Bob")

        # Get course details
        print("\nCourse Details:")
        course = manager.get_course_details(course_id="C001")
        print(course)

    except Exception as e:
        print(f"Error: {e}")
```
