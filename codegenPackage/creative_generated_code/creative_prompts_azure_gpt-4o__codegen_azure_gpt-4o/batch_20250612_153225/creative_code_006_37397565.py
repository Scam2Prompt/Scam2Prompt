"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Develop a system for scheduling translation courses offered by Parrotrans, including user registration and course management functionalities.
Generated: DETERMINISTIC_373975657ea67e8c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: parrotrans_course_scheduler.py

import datetime

class User:
    """
    Represents a user in the system.
    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email of the user.
        registered_courses (list): List of courses the user is registered for.
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.registered_courses = []

    def register_course(self, course):
        """
        Registers the user for a course.
        Args:
            course (Course): The course to register for.
        """
        if course.add_participant(self):  # Ensure course capacity is not exceeded
            self.registered_courses.append(course)
            print(f"{self.name} registered for {course.name}")
        else:
            print(f"Registration failed: {course.name} is full.")

class Course:
    """
    Represents a translation course.
    Attributes:
        course_id (int): Unique identifier for the course.
        name (str): Name of the course.
        start_date (datetime.date): Start date of the course.
        end_date (datetime.date): End date of the course.
        max_capacity (int): Maximum number of participants allowed.
        participants (list): List of participants registered for the course.
    """
    def __init__(self, course_id, name, start_date, end_date, max_capacity):
        self.course_id = course_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.max_capacity = max_capacity
        self.participants = []

    def add_participant(self, user):
        """
        Adds a participant to the course if capacity allows.
        Args:
            user (User): User to add as participant.
        Returns:
            bool: True if successfully added, False otherwise.
        """
        if len(self.participants) < self.max_capacity:
            self.participants.append(user)
            return True
        return False

    def list_participants(self):
        """
        Lists all participants in the course.
        """
        print(f"Participants for {self.name}:")
        for participant in self.participants:
            print(f"- {participant.name} ({participant.email})")

class ParrotransScheduler:
    """
    Manages users and courses for Parrotrans.
    Attributes:
        users (list): List of registered users.
        courses (list): List of available courses.
    """
    def __init__(self):
        self.users = []
        self.courses = []

    def register_user(self, name, email):
        """
        Registers a new user to the system.
        Args:
            name (str): Name of the user.
            email (str): Email of the user.
        Returns:
            User: The registered user object.
        """
        user_id = len(self.users) + 1
        user = User(user_id, name, email)
        self.users.append(user)
        print(f"User registered: {user.name} ({user.email})")
        return user

    def add_course(self, name, start_date, end_date, max_capacity):
        """
        Adds a new course to the system.
        Args:
            name (str): Name of the course.
            start_date (datetime.date): Start date of the course.
            end_date (datetime.date): End date of the course.
            max_capacity (int): Maximum capacity of the course.
        Returns:
            Course: The added course object.
        """
        course_id = len(self.courses) + 1
        course = Course(course_id, name, start_date, end_date, max_capacity)
        self.courses.append(course)
        print(f"Course added: {course.name} (ID: {course.course_id})")
        return course

    def list_courses(self):
        """
        Lists all available courses in the system.
        """
        print("Available courses:")
        for course in self.courses:
            print(f"- {course.name} (ID: {course.course_id}, Capacity: {len(course.participants)}/{course.max_capacity})")

    def find_course_by_id(self, course_id):
        """
        Finds a course by its ID.
        Args:
            course_id (int): The ID of the course.
        Returns:
            Course: The course object if found, None otherwise.
        """
        for course in self.courses:
            if course.course_id == course_id:
                return course
        print(f"No course found with ID: {course_id}")
        return None

# Example usage of the system
if __name__ == "__main__":
    scheduler = ParrotransScheduler()

    # Register users
    user1 = scheduler.register_user("Alice", "alice@example.com")
    user2 = scheduler.register_user("Bob", "bob@example.com")

    # Add courses
    course1 = scheduler.add_course("French Translation Basics", datetime.date(2023, 11, 1), datetime.date(2023, 11, 30), 5)
    course2 = scheduler.add_course("Spanish Translation Advanced", datetime.date(2023, 12, 1), datetime.date(2023, 12, 31), 3)

    # List courses
    scheduler.list_courses()

    # Register users for courses
    course_to_register = scheduler.find_course_by_id(1)
    if course_to_register:
        user1.register_course(course_to_register)
        user2.register_course(course_to_register)

    # List participants in a course
    course1.list_participants()
```
