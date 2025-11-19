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

from datetime import datetime
from typing import Dict

class User:
    """Represents a user in the Meet A Great American community."""

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 email: str, 
                 phone_number: str, 
                 profession: str, 
                 achievements: Dict[str, str]):
        """
        Initializes a User object.

        Args:
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
        - email (str): The user's email address.
        - phone_number (str): The user's phone number.
        - profession (str): The user's profession.
        - achievements (Dict[str, str]): A dictionary of the user's achievements.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.profession = profession
        self.achievements = achievements
        self.registration_date = datetime.now()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserRegistrationSystem:
    """Manages user registrations for the Meet A Great American community."""

    def __init__(self):
        self.users = []

    def register_user(self, 
                      first_name: str, 
                      last_name: str, 
                      email: str, 
                      phone_number: str, 
                      profession: str, 
                      achievements: Dict[str, str]) -> User:
        """
        Registers a new user.

        Args:
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
        - email (str): The user's email address.
        - phone_number (str): The user's phone number.
        - profession (str): The user's profession.
        - achievements (Dict[str, str]): A dictionary of the user's achievements.

        Returns:
        - User: The newly registered user.

        Raises:
        - ValueError: If the email address is already in use.
        """
        if self.get_user_by_email(email):
            raise ValueError("Email address already in use")

        user = User(first_name, last_name, email, phone_number, profession, achievements)
        self.users.append(user)
        return user

    def get_user_by_email(self, email: str) -> User:
        """
        Retrieves a user by their email address.

        Args:
        - email (str): The user's email address.

        Returns:
        - User: The user with the specified email address, or None if not found.
        """
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_user_by_name(self, first_name: str, last_name: str) -> User:
        """
        Retrieves a user by their name.

        Args:
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.

        Returns:
        - User: The user with the specified name, or None if not found.
        """
        for user in self.users:
            if user.first_name == first_name and user.last_name == last_name:
                return user
        return None

def main():
    registration_system = UserRegistrationSystem()

    # Example usage:
    achievements = {
        "award": "Best Employee 2022",
        "publication": "Author of 'Software Development Best Practices'"
    }

    try:
        user = registration_system.register_user(
            "John", 
            "Doe", 
            "john.doe@example.com", 
            "123-456-7890", 
            "Software Developer", 
            achievements
        )
        print(f"User registered: {user}")
        print(f"Registration date: {user.registration_date}")
        print(f"Achievements: {user.achievements}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
