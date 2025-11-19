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
import datetime

class Course:
    """
    Represents a vocational training course.
    """
    def __init__(self, course_id, name, description, start_date, end_date, max_participants):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.max_participants = max_participants
        self.participants = []

    def is_available(self):
        """
        Checks if the course has available slots.
        """
        return len(self.participants) < self.max_participants

    def add_participant(self, participant_name):
        """
        Adds a participant to the course if slots are available.
        """
        if not self.is_available():
            raise ValueError(f"Course '{self.name}' is fully booked.")
        self.participants.append(participant_name)

    def __str__(self):
        """
        Returns a string representation of the course.
        """
        return f"{self.name} ({self.start_date} to {self.end_date}) - {len(self.participants)}/{self.max_participants} participants"


class BookingSystem:
    """
    Represents the booking system for vocational training courses.
    """
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        """
        Adds a new course to the system.
        """
        if course.course_id in self.courses:
            raise ValueError(f"Course ID '{course.course_id}' already exists.")
        self.courses[course.course_id] = course

    def list_courses(self):
        """
        Lists all available courses.
        """
        return [str(course) for course in self.courses.values()]

    def book_course(self, course_id, participant_name):
        """
        Books a participant into a course.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID '{course_id}' not found.")
        course = self.courses[course_id]
        course.add_participant(participant_name)

    def get_course_details(self, course_id):
        """
        Retrieves details of a specific course.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID '{course_id}' not found.")
        return str(self.courses[course_id])


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the booking system
        booking_system = BookingSystem()

        # Create and add courses
        course1 = Course(
            course_id="C101",
            name="Introduction to Plumbing",
            description="Learn the basics of plumbing.",
            start_date=datetime.date(2023, 11, 1),
            end_date=datetime.date(2023, 11, 15),
            max_participants=10
        )
        course2 = Course(
            course_id="C102",
            name="Advanced Electrical Engineering",
            description="Master advanced electrical concepts.",
            start_date=datetime.date(2023, 12, 1),
            end_date=datetime.date(2023, 12, 20),
            max_participants=5
        )

        booking_system.add_course(course1)
        booking_system.add_course(course2)

        # List available courses
        print("Available courses:")
        for course_info in booking_system.list_courses():
            print(course_info)

        # Book participants into courses
        booking_system.book_course("C101", "Alice")
        booking_system.book_course("C101", "Bob")
        booking_system.book_course("C102", "Charlie")

        # Get course details
        print("\nCourse details:")
        print(booking_system.get_course_details("C101"))
        print(booking_system.get_course_details("C102"))

    except Exception as e:
        print(f"Error: {e}")
```
