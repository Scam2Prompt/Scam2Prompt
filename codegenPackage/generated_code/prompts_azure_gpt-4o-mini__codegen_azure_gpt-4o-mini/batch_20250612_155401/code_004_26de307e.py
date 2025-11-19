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
# user_registration.py

import re
from typing import List, Dict, Any

class User:
    """Class to represent a user in the Meet A Great American community."""
    
    def __init__(self, name: str, email: str, achievements: List[str]):
        self.name = name
        self.email = email
        self.achievements = achievements

    def __repr__(self) -> str:
        return f"User(name={self.name}, email={self.email}, achievements={self.achievements})"

class UserRegistrationSystem:
    """Class to handle user registration and management."""
    
    def __init__(self):
        self.users: List[User] = []

    def validate_email(self, email: str) -> bool:
        """Validate the email format using a regular expression."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def register_user(self, name: str, email: str, achievements: List[str]) -> Dict[str, Any]:
        """Register a new user with the provided details."""
        if not name or not email or not achievements:
            raise ValueError("Name, email, and achievements are required fields.")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        
        # Check for duplicate email
        if any(user.email == email for user in self.users):
            raise ValueError("Email already registered.")
        
        # Create and store the new user
        new_user = User(name, email, achievements)
        self.users.append(new_user)
        
        return {"message": "User registered successfully.", "user": new_user}

    def get_all_users(self) -> List[User]:
        """Return a list of all registered users."""
        return self.users

# Example usage
if __name__ == "__main__":
    registration_system = UserRegistrationSystem()
    
    try:
        # Register a new user
        response = registration_system.register_user(
            name="John Doe",
            email="john.doe@example.com",
            achievements=["Published a book", "Speaker at tech conferences"]
        )
        print(response)

        # Retrieve all registered users
        all_users = registration_system.get_all_users()
        print("Registered Users:", all_users)

    except ValueError as e:
        print(f"Error: {e}")
```
