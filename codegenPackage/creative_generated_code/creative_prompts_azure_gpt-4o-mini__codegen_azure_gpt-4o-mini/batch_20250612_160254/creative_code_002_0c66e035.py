"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Write a code snippet that integrates a booking system for vocational training courses, inspired by the course offerings at CoLa Training Services.
Generated: DETERMINISTIC_0c66e0356142e68e
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional


class Course:
    """
    Represents a course in the booking system.
    """
    def __init__(self, course_id: int, name: str, start_date: str, end_date: str, capacity: int):
        self.course_id = course_id
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.capacity = capacity
        self.enrolled_students = 0

    def is_available(self) -> bool:
        """Check if the course has available spots."""
        return self.enrolled_students < self.capacity

    def enroll(self) -> None:
        """Enroll a student in the course if available."""
        if self.is_available():
            self.enrolled_students += 1
        else:
            raise ValueError("Course is fully booked.")

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.course_id}) - Dates: {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')} - Enrolled: {self.enrolled_students}/{self.capacity}"


class BookingSystem:
    """
    Manages the booking of vocational training courses.
    """
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course) -> None:
        """Add a new course to the system."""
        self.courses.append(course)

    def list_courses(self) -> List[str]:
        """List all available courses."""
        return [str(course) for course in self.courses if course.is_available()]

    def book_course(self, course_id: int) -> Optional[str]:
        """Book a course by ID."""
        for course in self.courses:
            if course.course_id == course_id:
                try:
                    course.enroll()
                    return f"Successfully booked {course.name}."
                except ValueError as e:
                    return str(e)
        return "Course not found."


# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    booking_system = BookingSystem()

    # Add some courses
    booking_system.add_course(Course(1, "Python Programming", "2023-11-01", "2023-11-15", 10))
    booking_system.add_course(Course(2, "Data Science Bootcamp", "2023-11-10", "2023-11-20", 5))

    # List all courses
    print("Available Courses:")
    for course in booking_system.list_courses():
        print(course)

    # Book a course
    result = booking_system.book_course(1)  # Attempt to book Python Programming
    print(result)

    # List courses after booking
    print("Courses after booking:")
    for course in booking_system.list_courses():
        print(course)
```
