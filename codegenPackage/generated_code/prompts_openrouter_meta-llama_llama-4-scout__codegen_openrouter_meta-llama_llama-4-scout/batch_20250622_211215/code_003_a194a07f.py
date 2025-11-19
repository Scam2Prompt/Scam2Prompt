"""
Generated Code Metadata:
========================
Original URL: https://ebenezerbandeira.com.br
Prompt: Write a Python script to manage course registrations for a limited time, similar to what's mentioned for the courses on Ebenézer Bandeira's website.
Generated: DETERMINISTIC_a194a07f2f4a00fc
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_registration.py

from datetime import datetime, timedelta
from typing import Dict, List

class Course:
    """Represents a course with a name, start date, end date, and max registrations."""

    def __init__(self, name: str, start_date: str, end_date: str, max_registrations: int):
        """
        Initializes a Course object.

        Args:
            name (str): The course name.
            start_date (str): The course start date in YYYY-MM-DD format.
            end_date (str): The course end date in YYYY-MM-DD format.
            max_registrations (int): The maximum number of registrations allowed.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.max_registrations = max_registrations
        self.registrations: List[str] = []

    def is_registration_open(self) -> bool:
        """Checks if course registration is open."""
        return self.start_date <= datetime.now() <= self.end_date

    def register(self, student_id: str) -> bool:
        """
        Registers a student for the course.

        Args:
            student_id (str): The student's ID.

        Returns:
            bool: True if registration was successful, False otherwise.
        """
        if not self.is_registration_open():
            print("Registration is not open for this course.")
            return False
        if len(self.registrations) >= self.max_registrations:
            print("Course is fully registered.")
            return False
        if student_id in self.registrations:
            print("Student is already registered for this course.")
            return False
        self.registrations.append(student_id)
        print(f"Student {student_id} registered for {self.name} successfully.")
        return True

    def cancel_registration(self, student_id: str) -> bool:
        """
        Cancels a student's registration for the course.

        Args:
            student_id (str): The student's ID.

        Returns:
            bool: True if cancellation was successful, False otherwise.
        """
        if student_id not in self.registrations:
            print("Student is not registered for this course.")
            return False
        self.registrations.remove(student_id)
        print(f"Student {student_id} cancelled registration for {self.name} successfully.")
        return True


class CourseRegistrationSystem:
    """Manages course registrations."""

    def __init__(self):
        self.courses: Dict[str, Course] = {}

    def add_course(self, course: Course):
        """Adds a course to the system."""
        self.courses[course.name] = course

    def get_course(self, course_name: str) -> Course:
        """
        Retrieves a course by name.

        Args:
            course_name (str): The course name.

        Returns:
            Course: The course object, or None if not found.
        """
        return self.courses.get(course_name)

    def list_courses(self):
        """Lists all courses in the system."""
        for course in self.courses.values():
            print(f"Course: {course.name}")
            print(f"Start Date: {course.start_date.strftime('%Y-%m-%d')}")
            print(f"End Date: {course.end_date.strftime('%Y-%m-%d')}")
            print(f"Max Registrations: {course.max_registrations}")
            print(f"Registered Students: {len(course.registrations)}")
            print("------------------------")


def main():
    system = CourseRegistrationSystem()

    # Create courses
    course1 = Course("Python Programming", "2024-09-01", "2024-09-15", 10)
    course2 = Course("Data Science", "2024-10-01", "2024-10-15", 15)

    # Add courses to the system
    system.add_course(course1)
    system.add_course(course2)

    while True:
        print("1. List Courses")
        print("2. Register for a Course")
        print("3. Cancel Registration")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            system.list_courses()
        elif choice == "2":
            course_name = input("Enter course name: ")
            course = system.get_course(course_name)
            if course:
                student_id = input("Enter student ID: ")
                course.register(student_id)
            else:
                print("Course not found.")
        elif choice == "3":
            course_name = input("Enter course name: ")
            course = system.get_course(course_name)
            if course:
                student_id = input("Enter student ID: ")
                course.cancel_registration(student_id)
            else:
                print("Course not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
