"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Write Python code to simulate a basic e-learning platform for SKI Foundation's "E-Course Digipreneur Profesional" program, including user registration and course enrollment functionalities.
Generated: DETERMINISTIC_8fb9485953750fdf
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class User:
    """
    Represents a user in the e-learning platform.
    """

    def __init__(self, name, email):
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.email = email
        self.enrolled_courses = []  # List to store enrolled courses

    def enroll_course(self, course):
        """
        Enroll the user in a course.
        """
        if course in self.enrolled_courses:
            raise ValueError(f"User is already enrolled in the course '{course.name}'.")
        self.enrolled_courses.append(course)

    def __str__(self):
        """
        Printable representation of the user.
        """
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class Course:
    """
    Represents a course in the e-learning platform.
    """

    def __init__(self, name, description):
        self.course_id = str(uuid.uuid4())  # Unique identifier for the course
        self.name = name
        self.description = description

    def __str__(self):
        """
        Printable representation of the course.
        """
        return f"Course ID: {self.course_id}, Name: {self.name}, Description: {self.description}"


class ECoursePlatform:
    """
    Represents the e-learning platform for registration and course enrollment.
    """

    def __init__(self):
        self.users = {}  # Dictionary to store users (key: user_id, value: User instance)
        self.courses = {}  # Dictionary to store courses (key: course_id, value: Course instance)

    def register_user(self, name, email):
        """
        Registers a new user to the platform.
        """
        if email in [user.email for user in self.users.values()]:
            raise ValueError(f"A user with the email '{email}' is already registered.")
        new_user = User(name, email)
        self.users[new_user.user_id] = new_user
        return new_user

    def add_course(self, name, description):
        """
        Adds a new course to the platform.
        """
        new_course = Course(name, description)
        self.courses[new_course.course_id] = new_course
        return new_course

    def enroll_user_in_course(self, user_id, course_id):
        """
        Enrolls a user in a course.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("Invalid user ID. User not found.")

        course = self.courses.get(course_id)
        if not course:
            raise ValueError("Invalid course ID. Course not found.")

        user.enroll_course(course)

    def list_users(self):
        """
        Lists all registered users.
        """
        return self.users.values()

    def list_courses(self):
        """
        Lists all available courses.
        """
        return self.courses.values()


# Main script for demonstration purposes (would typically be in a separate file)
if __name__ == "__main__":
    try:
        # Initialize the e-learning platform
        platform = ECoursePlatform()

        # Register users
        user1 = platform.register_user("Alice Johnson", "alice@example.com")
        user2 = platform.register_user("Bob Smith", "bob@example.com")

        # Add courses
        course1 = platform.add_course("Digital Marketing", "Learn the fundamentals of digital marketing.")
        course2 = platform.add_course("Entrepreneurship Basics", "Start your journey as a digital entrepreneur.")

        # Enroll users in courses
        platform.enroll_user_in_course(user1.user_id, course1.course_id)
        platform.enroll_user_in_course(user2.user_id, course2.course_id)

        # Display registered users
        print("Registered Users:")
        for user in platform.list_users():
            print(user)

        # Display available courses
        print("\nAvailable Courses:")
        for course in platform.list_courses():
            print(course)

        # Display enrolled courses for each user
        print("\nUser Enrollments:")
        for user in platform.list_users():
            print(f"{user.name} is enrolled in:")
            for course in user.enrolled_courses:
                print(f"  - {course.name}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
