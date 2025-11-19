"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Write Python code to simulate a basic e-learning platform for SKI Foundation's "E-Course Digipreneur Profesional" program, including user registration and course enrollment functionalities.
Generated: DETERMINISTIC_8fb9485953750fdf
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_learning_platform.py

class User:
    """Represents a user in the e-learning platform."""

    def __init__(self, user_id, name, email, password):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            name (str): User's name.
            email (str): User's email address.
            password (str): User's password.
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_courses = []

    def enroll_course(self, course):
        """
        Enrolls the user in a course.

        Args:
            course (Course): Course to enroll in.

        Raises:
            ValueError: If the user is already enrolled in the course.
        """
        if course in self.enrolled_courses:
            raise ValueError("User is already enrolled in this course.")
        self.enrolled_courses.append(course)


class Course:
    """Represents a course in the e-learning platform."""

    def __init__(self, course_id, name, description):
        """
        Initializes a Course object.

        Args:
            course_id (int): Unique identifier for the course.
            name (str): Course name.
            description (str): Course description.
        """
        self.course_id = course_id
        self.name = name
        self.description = description


class ELearningPlatform:
    """Simulates a basic e-learning platform."""

    def __init__(self):
        """
        Initializes the e-learning platform.

        Attributes:
            users (dict): Dictionary of registered users.
            courses (dict): Dictionary of available courses.
        """
        self.users = {}
        self.courses = {}
        self.user_id_counter = 1
        self.course_id_counter = 1

    def register_user(self, name, email, password):
        """
        Registers a new user.

        Args:
            name (str): User's name.
            email (str): User's email address.
            password (str): User's password.

        Returns:
            User: The newly registered user.

        Raises:
            ValueError: If the email address is already in use.
        """
        if email in [user.email for user in self.users.values()]:
            raise ValueError("Email address is already in use.")
        user = User(self.user_id_counter, name, email, password)
        self.users[self.user_id_counter] = user
        self.user_id_counter += 1
        return user

    def create_course(self, name, description):
        """
        Creates a new course.

        Args:
            name (str): Course name.
            description (str): Course description.

        Returns:
            Course: The newly created course.
        """
        course = Course(self.course_id_counter, name, description)
        self.courses[self.course_id_counter] = course
        self.course_id_counter += 1
        return course

    def enroll_user_in_course(self, user_id, course_id):
        """
        Enrolls a user in a course.

        Args:
            user_id (int): ID of the user to enroll.
            course_id (int): ID of the course to enroll in.

        Raises:
            ValueError: If the user or course does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if course_id not in self.courses:
            raise ValueError("Course does not exist.")
        user = self.users[user_id]
        course = self.courses[course_id]
        user.enroll_course(course)


def main():
    platform = ELearningPlatform()

    # Create courses
    course1 = platform.create_course("Digital Marketing", "Learn the basics of digital marketing.")
    course2 = platform.create_course("E-commerce", "Learn how to start an e-commerce business.")

    # Register users
    user1 = platform.register_user("John Doe", "john@example.com", "password123")
    user2 = platform.register_user("Jane Doe", "jane@example.com", "password456")

    # Enroll users in courses
    platform.enroll_user_in_course(user1.user_id, course1.course_id)
    platform.enroll_user_in_course(user2.user_id, course2.course_id)
    platform.enroll_user_in_course(user1.user_id, course2.course_id)

    # Print enrolled courses for each user
    for user in platform.users.values():
        print(f"User: {user.name}")
        print("Enrolled Courses:")
        for course in user.enrolled_courses:
            print(f"- {course.name}")
        print()


if __name__ == "__main__":
    main()
```
