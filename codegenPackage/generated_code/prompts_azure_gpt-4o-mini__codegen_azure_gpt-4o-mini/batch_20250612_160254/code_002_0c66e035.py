"""
Generated Code Metadata:
========================
Original URL: https://colatraining.com
Prompt: Write a code snippet that integrates a booking system for vocational training courses, inspired by the course offerings at CoLa Training Services.
Generated: DETERMINISTIC_0c66e0356142e68e
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

from datetime import datetime
from typing import List, Dict, Optional

class Course:
    """Represents a vocational training course."""
    
    def __init__(self, course_id: int, name: str, capacity: int):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = 0

    def enroll(self) -> bool:
        """Enroll a student in the course if capacity allows."""
        if self.enrolled_students < self.capacity:
            self.enrolled_students += 1
            return True
        return False

class BookingSystem:
    """Manages the booking of vocational training courses."""
    
    def __init__(self):
        self.courses: Dict[int, Course] = {}

    def add_course(self, course: Course) -> None:
        """Add a new course to the booking system."""
        self.courses[course.course_id] = course

    def book_course(self, course_id: int) -> Optional[str]:
        """Book a course for a student."""
        course = self.courses.get(course_id)
        if not course:
            return f"Course ID {course_id} not found."
        
        if course.enroll():
            return f"Successfully enrolled in {course.name}."
        else:
            return f"Course {course.name} is fully booked."

    def list_courses(self) -> List[str]:
        """List all available courses."""
        return [f"{course.course_id}: {course.name} (Capacity: {course.capacity}, Enrolled: {course.enrolled_students})"
                for course in self.courses.values()]

def main():
    """Main function to demonstrate the booking system."""
    booking_system = BookingSystem()

    # Adding courses to the booking system
    booking_system.add_course(Course(1, "Python Programming", 10))
    booking_system.add_course(Course(2, "Data Science", 5))
    booking_system.add_course(Course(3, "Web Development", 8))

    # Display available courses
    print("Available Courses:")
    for course in booking_system.list_courses():
        print(course)

    # Attempt to book courses
    print(booking_system.book_course(1))  # Successful booking
    print(booking_system.book_course(2))  # Successful booking
    print(booking_system.book_course(4))  # Course not found
    print(booking_system.book_course(2))  # Attempt to book a full course

if __name__ == "__main__":
    main()
```
