"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Suggest a set of technical specifications for an e-learning platform that provides high-quality international training to vocational teachers, students, and employees, with features for micro-credentials and certification."
Generated: DETERMINISTIC_97a037c118c66020
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ELearningPlatform:
    """
    A class to represent an e-learning platform for vocational training.
    
    Attributes:
        name (str): The name of the e-learning platform.
        users (list): A list of users registered on the platform.
        courses (list): A list of courses available on the platform.
    """

    def __init__(self, name):
        """
        Initializes the e-learning platform with a name, an empty user list, and an empty course list.
        
        Args:
            name (str): The name of the e-learning platform.
        """
        self.name = name
        self.users = []
        self.courses = []

    def register_user(self, user):
        """
        Registers a new user to the platform.
        
        Args:
            user (dict): A dictionary containing user details (name, email, role).
        
        Raises:
            ValueError: If the user already exists.
        """
        if any(existing_user['email'] == user['email'] for existing_user in self.users):
            raise ValueError("User already exists.")
        self.users.append(user)

    def add_course(self, course):
        """
        Adds a new course to the platform.
        
        Args:
            course (dict): A dictionary containing course details (title, description, instructor).
        
        Raises:
            ValueError: If the course already exists.
        """
        if any(existing_course['title'] == course['title'] for existing_course in self.courses):
            raise ValueError("Course already exists.")
        self.courses.append(course)

    def issue_certificate(self, user_email, course_title):
        """
        Issues a certificate to a user upon course completion.
        
        Args:
            user_email (str): The email of the user.
            course_title (str): The title of the completed course.
        
        Returns:
            str: A confirmation message if the certificate is issued successfully.
        
        Raises:
            ValueError: If the user or course does not exist.
        """
        user = next((u for u in self.users if u['email'] == user_email), None)
        course = next((c for c in self.courses if c['title'] == course_title), None)

        if user is None:
            raise ValueError("User not found.")
        if course is None:
            raise ValueError("Course not found.")

        return f"Certificate issued to {user['name']} for completing {course['title']}."

    def generate_micro_credential(self, user_email, skill):
        """
        Generates a micro-credential for a user based on a skill.
        
        Args:
            user_email (str): The email of the user.
            skill (str): The skill for which the micro-credential is issued.
        
        Returns:
            str: A confirmation message if the micro-credential is generated successfully.
        
        Raises:
            ValueError: If the user does not exist.
        """
        user = next((u for u in self.users if u['email'] == user_email), None)

        if user is None:
            raise ValueError("User not found.")

        return f"Micro-credential for {skill} issued to {user['name']}."

# Example usage
if __name__ == "__main__":
    platform = ELearningPlatform("Global Vocational Training")

    # Register users
    try:
        platform.register_user({"name": "Alice", "email": "alice@example.com", "role": "teacher"})
        platform.register_user({"name": "Bob", "email": "bob@example.com", "role": "student"})
    except ValueError as e:
        print(e)

    # Add courses
    try:
        platform.add_course({"title": "Advanced Welding", "description": "Learn advanced welding techniques.", "instructor": "John Doe"})
    except ValueError as e:
        print(e)

    # Issue certificate
    try:
        print(platform.issue_certificate("alice@example.com", "Advanced Welding"))
    except ValueError as e:
        print(e)

    # Generate micro-credential
    try:
        print(platform.generate_micro_credential("bob@example.com", "Welding Basics"))
    except ValueError as e:
        print(e)
```
