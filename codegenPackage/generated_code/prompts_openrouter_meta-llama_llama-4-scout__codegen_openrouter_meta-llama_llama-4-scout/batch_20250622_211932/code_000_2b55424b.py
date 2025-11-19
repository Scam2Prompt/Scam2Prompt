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
# course_booking_system.py

from datetime import datetime
from typing import Dict, List

class Course:
    """Represents a course offered by CoLa Training Services."""

    def __init__(self, course_id: int, name: str, description: str, capacity: int):
        """
        Initializes a Course object.

        Args:
        course_id (int): Unique identifier for the course.
        name (str): Name of the course.
        description (str): Brief description of the course.
        capacity (int): Maximum number of bookings allowed for the course.
        """
        self.course_id = course_id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.bookings = []

    def add_booking(self, booking):
        """Adds a booking to the course."""
        if len(self.bookings) < self.capacity:
            self.bookings.append(booking)
            return True
        return False

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Capacity: {self.capacity}, Bookings: {len(self.bookings)}"


class Booking:
    """Represents a booking for a course."""

    def __init__(self, booking_id: int, course_id: int, student_name: str, start_date: datetime, end_date: datetime):
        """
        Initializes a Booking object.

        Args:
        booking_id (int): Unique identifier for the booking.
        course_id (int): Identifier of the course being booked.
        student_name (str): Name of the student making the booking.
        start_date (datetime): Start date of the course.
        end_date (datetime): End date of the course.
        """
        self.booking_id = booking_id
        self.course_id = course_id
        self.student_name = student_name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Course ID: {self.course_id}, Student Name: {self.student_name}, Dates: {self.start_date} - {self.end_date}"


class CourseBookingSystem:
    """Manages course bookings for CoLa Training Services."""

    def __init__(self):
        self.courses: Dict[int, Course] = {}
        self.bookings: Dict[int, Booking] = {}
        self.booking_id_counter = 1
        self.course_id_counter = 1

    def add_course(self, name: str, description: str, capacity: int) -> int:
        """
        Adds a new course to the system.

        Args:
        name (str): Name of the course.
        description (str): Brief description of the course.
        capacity (int): Maximum number of bookings allowed for the course.

        Returns:
        int: The ID of the newly added course.
        """
        course_id = self.course_id_counter
        self.courses[course_id] = Course(course_id, name, description, capacity)
        self.course_id_counter += 1
        return course_id

    def make_booking(self, course_id: int, student_name: str, start_date: datetime, end_date: datetime) -> int:
        """
        Creates a new booking for a course.

        Args:
        course_id (int): Identifier of the course being booked.
        student_name (str): Name of the student making the booking.
        start_date (datetime): Start date of the course.
        end_date (datetime): End date of the course.

        Returns:
        int: The ID of the newly created booking, or -1 if the booking fails.
        """
        if course_id not in self.courses:
            raise ValueError("Course not found")

        course = self.courses[course_id]
        booking_id = self.booking_id_counter
        booking = Booking(booking_id, course_id, student_name, start_date, end_date)

        if course.add_booking(booking):
            self.bookings[booking_id] = booking
            self.booking_id_counter += 1
            return booking_id
        return -1

    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancels a booking.

        Args:
        booking_id (int): Identifier of the booking to cancel.

        Returns:
        bool: True if the booking was cancelled successfully, False otherwise.
        """
        if booking_id not in self.bookings:
            return False

        booking = self.bookings[booking_id]
        course = self.courses[booking.course_id]
        course.bookings = [b for b in course.bookings if b.booking_id != booking_id]
        del self.bookings[booking_id]
        return True

    def get_course(self, course_id: int) -> Course:
        """
        Retrieves a course by its ID.

        Args:
        course_id (int): Identifier of the course.

        Returns:
        Course: The course object, or None if not found.
        """
        return self.courses.get(course_id)

    def get_booking(self, booking_id: int) -> Booking:
        """
        Retrieves a booking by its ID.

        Args:
        booking_id (int): Identifier of the booking.

        Returns:
        Booking: The booking object, or None if not found.
        """
        return self.bookings.get(booking_id)


def main():
    # Create a course booking system
    system = CourseBookingSystem()

    # Add courses
    course_id_1 = system.add_course("Online Training Program", "An online training program.", 10)
    course_id_2 = system.add_course("Machinery Operation Course", "A course on operating machinery.", 5)

    # Make bookings
    try:
        booking_id_1 = system.make_booking(course_id_1, "John Doe", datetime(2024, 9, 16), datetime(2024, 9, 17))
        booking_id_2 = system.make_booking(course_id_2, "Jane Doe", datetime(2024, 9, 18), datetime(2024, 9, 19))
        print(f"Booking ID 1: {booking_id_1}")
        print(f"Booking ID 2: {booking_id_2}")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve and print course and booking information
    course = system.get_course(course_id_1)
    if course:
        print(course)

    booking = system.get_booking(booking_id_1)
    if booking:
        print(booking)

    # Cancel a booking
    if system.cancel_booking(booking_id_1):
        print(f"Booking {booking_id_1} cancelled successfully.")
    else:
        print(f"Failed to cancel booking {booking_id_1}.")

if __name__ == "__main__":
    main()
```
