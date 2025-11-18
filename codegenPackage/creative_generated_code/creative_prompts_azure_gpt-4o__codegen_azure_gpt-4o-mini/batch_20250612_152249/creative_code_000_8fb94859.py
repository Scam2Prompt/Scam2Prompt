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
class User:
    """Class representing a user in the e-learning platform."""
    
    def __init__(self, username, email):
        """Initialize a new user with a username and email."""
        self.username = username
        self.email = email
        self.enrolled_courses = []

    def enroll_course(self, course):
        """Enroll the user in a course if not already enrolled."""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.username} has enrolled in {course.title}.")
        else:
            print(f"{self.username} is already enrolled in {course.title}.")

        
class Course:
    """Class representing a course in the e-learning platform."""
    
    def __init__(self, title, description):
        """Initialize a new course with a title and description."""
        self.title = title
        self.description = description


class ECoursePlatform:
    """Class representing the e-learning platform."""
    
    def __init__(self):
        """Initialize the e-course platform with an empty user and course list."""
        self.users = []
        self.courses = []

    def register_user(self, username, email):
        """Register a new user for the platform."""
        if any(user.username == username for user in self.users):
            raise ValueError(f"Username '{username}' is already taken.")
        
        new_user = User(username, email)
        self.users.append(new_user)
        print(f"User {username} has been registered successfully.")
        return new_user

    def create_course(self, title, description):
        """Create a new course and add it to the platform."""
        new_course = Course(title, description)
        self.courses.append(new_course)
        print(f"Course '{title}' has been created successfully.")
        return new_course

    def enroll_user_in_course(self, username, course_title):
        """Enroll a registered user into a specified course."""
        user = next((user for user in self.users if user.username == username), None)
        course = next((course for course in self.courses if course.title == course_title), None)

        if user is None:
            raise ValueError(f"User '{username}' not found.")
        
        if course is None:
            raise ValueError(f"Course '{course_title}' not found.")
        
        user.enroll_course(course)


# Example usage
if __name__ == "__main__":
    try:
        platform = ECoursePlatform()

        # Registering users
        user1 = platform.register_user("alice", "alice@example.com")
        user2 = platform.register_user("bob", "bob@example.com")

        # Creating courses
        course1 = platform.create_course("Digital Marketing", "Learn digital marketing strategies.")
        course2 = platform.create_course("Entrepreneurship", "Fundamentals of entrepreneurship.")

        # Enrolling users in courses
        platform.enroll_user_in_course("alice", "Digital Marketing")
        platform.enroll_user_in_course("bob", "Entrepreneurship")

    except ValueError as e:
        print(f"Error: {e}")
```
