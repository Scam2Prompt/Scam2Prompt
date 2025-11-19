"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Suggest tools or frameworks for building an online learning platform that supports strategic personal planning, vision creation, and life purpose definition, inspired by Virtual5's course offerings.
Generated: DETERMINISTIC_945802a882d08bf0
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_learning_platform.py

"""
This module provides a basic structure for an online learning platform
that supports strategic personal planning, vision creation, and life purpose definition.
Inspired by Virtual5's course offerings, it includes classes for courses, users, and a platform manager.
"""

class Course:
    """
    Represents a course in the online learning platform.
    """

    def __init__(self, title: str, description: str, duration: int):
        """
        Initializes a new course with a title, description, and duration.

        :param title: Title of the course
        :param description: Description of the course
        :param duration: Duration of the course in hours
        """
        self.title = title
        self.description = description
        self.duration = duration

    def __str__(self):
        return f"Course: {self.title}, Duration: {self.duration} hours"


class User:
    """
    Represents a user of the online learning platform.
    """

    def __init__(self, username: str, email: str):
        """
        Initializes a new user with a username and email.

        :param username: Username of the user
        :param email: Email of the user
        """
        self.username = username
        self.email = email
        self.enrolled_courses = []

    def enroll(self, course: Course):
        """
        Enrolls the user in a course.

        :param course: Course to enroll in
        """
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
        else:
            raise ValueError(f"User {self.username} is already enrolled in {course.title}")

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"


class PlatformManager:
    """
    Manages the online learning platform, including courses and users.
    """

    def __init__(self):
        self.courses = []
        self.users = []

    def add_course(self, course: Course):
        """
        Adds a new course to the platform.

        :param course: Course to add
        """
        self.courses.append(course)

    def register_user(self, user: User):
        """
        Registers a new user on the platform.

        :param user: User to register
        """
        self.users.append(user)

    def find_course(self, title: str) -> Course:
        """
        Finds a course by its title.

        :param title: Title of the course to find
        :return: Course object if found, else raises ValueError
        """
        for course in self.courses:
            if course.title == title:
                return course
        raise ValueError(f"Course with title '{title}' not found.")

    def __str__(self):
        return f"Platform has {len(self.courses)} courses and {len(self.users)} users."


# Example usage
if __name__ == "__main__":
    try:
        platform = PlatformManager()

        # Create courses
        course1 = Course("Strategic Personal Planning", "Learn to plan your personal goals strategically.", 10)
        course2 = Course("Vision Creation", "Create a compelling vision for your life.", 8)

        # Add courses to platform
        platform.add_course(course1)
        platform.add_course(course2)

        # Register users
        user1 = User("john_doe", "john@example.com")
        platform.register_user(user1)

        # Enroll user in a course
        user1.enroll(course1)

        # Output platform status
        print(platform)
        print(user1)
        print(user1.enrolled_courses)

    except Exception as e:
        print(f"An error occurred: {e}")
```
