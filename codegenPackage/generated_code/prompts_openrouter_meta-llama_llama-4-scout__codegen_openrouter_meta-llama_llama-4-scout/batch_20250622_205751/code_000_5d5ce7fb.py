"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write a Python code to manage online courses and e-learning platforms for a non-profit organization like SKI Foundation.
Generated: DETERMINISTIC_5d5ce7fb4821808b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_management_system.py

from typing import List, Dict
from datetime import datetime

class Course:
    """Represents an online course."""

    def __init__(self, id: int, title: str, description: str, start_date: str, end_date: str):
        """
        Initializes a Course object.

        Args:
            id (int): Unique course ID.
            title (str): Course title.
            description (str): Course description.
            start_date (str): Course start date in YYYY-MM-DD format.
            end_date (str): Course end date in YYYY-MM-DD format.
        """
        self.id = id
        self.title = title
        self.description = description
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def __str__(self):
        return f"Course {self.id}: {self.title}"


class CourseManagementSystem:
    """Manages online courses and e-learning platforms."""

    def __init__(self):
        """Initializes the course management system."""
        self.courses: Dict[int, Course] = {}

    def add_course(self, course: Course):
        """
        Adds a course to the system.

        Args:
            course (Course): Course to add.

        Raises:
            ValueError: If a course with the same ID already exists.
        """
        if course.id in self.courses:
            raise ValueError("Course with the same ID already exists.")
        self.courses[course.id] = course

    def remove_course(self, course_id: int):
        """
        Removes a course from the system.

        Args:
            course_id (int): ID of the course to remove.

        Raises:
            KeyError: If the course does not exist.
        """
        if course_id not in self.courses:
            raise KeyError("Course does not exist.")
        del self.courses[course_id]

    def get_course(self, course_id: int) -> Course:
        """
        Retrieves a course by ID.

        Args:
            course_id (int): ID of the course to retrieve.

        Returns:
            Course: The course with the specified ID.

        Raises:
            KeyError: If the course does not exist.
        """
        if course_id not in self.courses:
            raise KeyError("Course does not exist.")
        return self.courses[course_id]

    def list_courses(self) -> List[Course]:
        """Returns a list of all courses."""
        return list(self.courses.values())


class User:
    """Represents a user."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a User object.

        Args:
            id (int): Unique user ID.
            name (str): User name.
            email (str): User email.
        """
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"User {self.id}: {self.name}"


class Enrollment:
    """Represents a course enrollment."""

    def __init__(self, user: User, course: Course):
        """
        Initializes an Enrollment object.

        Args:
            user (User): Enrolled user.
            course (Course): Enrolled course.
        """
        self.user = user
        self.course = course

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"


class EnrollmentManagementSystem:
    """Manages course enrollments."""

    def __init__(self):
        """Initializes the enrollment management system."""
        self.enrollments: List[Enrollment] = []

    def enroll_user(self, user: User, course: Course):
        """
        Enrolls a user in a course.

        Args:
            user (User): User to enroll.
            course (Course): Course to enroll in.

        Raises:
            ValueError: If the user is already enrolled in the course.
        """
        for enrollment in self.enrollments:
            if enrollment.user.id == user.id and enrollment.course.id == course.id:
                raise ValueError("User is already enrolled in the course.")
        self.enrollments.append(Enrollment(user, course))

    def unenroll_user(self, user: User, course: Course):
        """
        Unenrolls a user from a course.

        Args:
            user (User): User to unenroll.
            course (Course): Course to unenroll from.

        Raises:
            ValueError: If the user is not enrolled in the course.
        """
        for enrollment in self.enrollments:
            if enrollment.user.id == user.id and enrollment.course.id == course.id:
                self.enrollments.remove(enrollment)
                return
        raise ValueError("User is not enrolled in the course.")

    def list_enrollments(self) -> List[Enrollment]:
        """Returns a list of all enrollments."""
        return self.enrollments


def main():
    # Create courses
    course1 = Course(1, "Python Programming", "Learn Python basics.", "2024-01-01", "2024-01-31")
    course2 = Course(2, "Data Science", "Learn data science fundamentals.", "2024-02-01", "2024-02-28")

    # Create users
    user1 = User(1, "John Doe", "john@example.com")
    user2 = User(2, "Jane Doe", "jane@example.com")

    # Create course management system
    course_system = CourseManagementSystem()
    course_system.add_course(course1)
    course_system.add_course(course2)

    # Create enrollment management system
    enrollment_system = EnrollmentManagementSystem()
    enrollment_system.enroll_user(user1, course1)
    enrollment_system.enroll_user(user2, course2)
    enrollment_system.enroll_user(user1, course2)

    # Print courses
    print("Courses:")
    for course in course_system.list_courses():
        print(course)

    # Print enrollments
    print("\nEnrollments:")
    for enrollment in enrollment_system.list_enrollments():
        print(enrollment)


if __name__ == "__main__":
    main()
```
