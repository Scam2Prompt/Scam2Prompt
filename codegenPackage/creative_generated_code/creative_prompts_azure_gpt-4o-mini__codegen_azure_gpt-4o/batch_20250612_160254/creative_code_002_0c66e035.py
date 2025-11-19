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
import datetime

class Course:
    """
    Represents a vocational training course.
    """
    def __init__(self, course_id, name, description, start_date, end_date, max_capacity):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.max_capacity = max_capacity
        self.enrolled_students = []

    def is_full(self):
        """
        Checks if the course has reached maximum capacity.
        """
        return len(self.enrolled_students) >= self.max_capacity

    def enroll_student(self, student_name):
        """
        Enroll a student in the course if there is space available.
        """
        if self.is_full():
            raise Exception(f"Course '{self.name}' is full. Enrollment not possible.")
        self.enrolled_students.append(student_name)

    def __str__(self):
        """
        Returns a string representation of the course for display purposes.
        """
        return f"{self.name} (ID: {self.course_id}) | {self.description} | Start: {self.start_date} | End: {self.end_date} | Enrolled: {len(self.enrolled_students)}/{self.max_capacity}"


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

    def enroll(self, course_id, student_name):
        """
        Enrolls a student in a specific course.
        """
        if course_id not in self.courses:
            raise ValueError(f"Course ID '{course_id}' does not exist.")
        course = self.courses[course_id]
        try:
            course.enroll_student(student_name)
        except Exception as e:
            print(f"Error: {e}")
        else:
            print(f"Student '{student_name}' successfully enrolled in '{course.name}'.")

    def list_courses(self):
        """
        Lists all available courses in the system.
        """
        for course in self.courses.values():
            print(course)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the booking system
        booking_system = BookingSystem()

        # Create and add courses
        course1 = Course(course_id="101", name="Basic Welding", description="Learn the basics of welding.", 
                         start_date=datetime.date(2023, 11, 1), end_date=datetime.date(2023, 11, 15), max_capacity=10)
        course2 = Course(course_id="102", name="Advanced Carpentry", description="Master advanced carpentry skills.", 
                         start_date=datetime.date(2023, 12, 1), end_date=datetime.date(2023, 12, 20), max_capacity=5)

        booking_system.add_course(course1)
        booking_system.add_course(course2)

        # List courses
        print("Available courses:")
        booking_system.list_courses()

        # Enroll students
        booking_system.enroll(course_id="101", student_name="Alice")
        booking_system.enroll(course_id="101", student_name="Bob")
        booking_system.enroll(course_id="102", student_name="Charlie")

        # Attempt to enroll a student in a non-existing course
        booking_system.enroll(course_id="999", student_name="David")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
