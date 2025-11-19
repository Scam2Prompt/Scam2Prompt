"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Illustrate how to implement a user registration system for the Meet A Great American community, focusing on capturing user details and their professional achievements.
Generated: DETERMINISTIC_26de307e3e685b60
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_registration_system.py

import re

class UserRegistrationSystem:
    """
    A class to handle user registration for the Meet A Great American community.
    Captures user details and their professional achievements.
    """

    def __init__(self):
        # Initialize an empty list to store registered users
        self.users = []

    def validate_email(self, email):
        """
        Validates the email format using a regular expression.
        :param email: str - The email address to validate.
        :return: bool - True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def register_user(self, name, email, achievements):
        """
        Registers a new user with their details and professional achievements.
        :param name: str - Full name of the user.
        :param email: str - Email address of the user.
        :param achievements: list - List of professional achievements.
        :return: str - Success or error message.
        """
        # Validate input
        if not name or not email or not achievements:
            return "Error: All fields (name, email, achievements) are required."

        if not self.validate_email(email):
            return "Error: Invalid email format."

        # Check if the user is already registered
        for user in self.users:
            if user['email'] == email:
                return "Error: User with this email is already registered."

        # Register the user
        user_data = {
            'name': name,
            'email': email,
            'achievements': achievements
        }
        self.users.append(user_data)
        return f"Success: User '{name}' has been registered."

    def list_users(self):
        """
        Lists all registered users and their details.
        :return: list - List of registered users.
        """
        return self.users


# Example usage
if __name__ == "__main__":
    # Create an instance of the registration system
    registration_system = UserRegistrationSystem()

    # Register a user
    response = registration_system.register_user(
        name="John Doe",
        email="john.doe@example.com",
        achievements=["Published a book", "Won a national award"]
    )
    print(response)  # Output: Success: User 'John Doe' has been registered.

    # Attempt to register the same user again
    response = registration_system.register_user(
        name="John Doe",
        email="john.doe@example.com",
        achievements=["Published a book", "Won a national award"]
    )
    print(response)  # Output: Error: User with this email is already registered.

    # List all registered users
    users = registration_system.list_users()
    print(users)
    # Output: [{'name': 'John Doe', 'email': 'john.doe@example.com', 'achievements': ['Published a book', 'Won a national award']}]
```
