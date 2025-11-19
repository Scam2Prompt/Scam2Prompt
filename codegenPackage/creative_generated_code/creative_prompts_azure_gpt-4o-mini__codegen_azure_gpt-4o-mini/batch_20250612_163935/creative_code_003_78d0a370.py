"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securespend.io
Prompt: Develop a script that simulates a user registration process for an online togel betting platform, ensuring unique member IDs.
Generated: DETERMINISTIC_78d0a370db14e58d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import re

class User:
    """Class to represent a user in the Togel betting platform."""
    
    def __init__(self, username: str, password: str):
        """Initialize a new user with a unique member ID, username, and password."""
        self.member_id = self.generate_unique_id()
        self.username = username
        self.password = self.hash_password(password)

    @staticmethod
    def generate_unique_id() -> str:
        """Generate a unique member ID using UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the password for security purposes (this is a placeholder)."""
        # In a real application, use a hashing library (e.g., bcrypt)
        return password[::-1]  # Reverse string as a simple demonstration

class UserRegistration:
    """Class to handle user registration."""

    def __init__(self):
        """Initialize the registration system with a user storage."""
        self.users = {}

    def register_user(self, username: str, password: str) -> str:
        """Register a new user with a unique username and password."""
        try:
            # Validate username and password
            self.validate_username(username)
            self.validate_password(password)
            
            # Check for username uniqueness
            if username in self.users:
                raise ValueError("Username already exists.")

            # Create a new user and store it
            new_user = User(username, password)
            self.users[username] = new_user
            
            return f"User registered successfully with Member ID: {new_user.member_id}"
        
        except ValueError as e:
            return f"Registration error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    @staticmethod
    def validate_username(username: str):
        """Validate the username format."""
        if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
            raise ValueError("Username must be 3-20 characters long and can contain letters, numbers, and underscores.")

    @staticmethod
    def validate_password(password: str):
        """Validate the password strength."""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search("[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search("[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search("[0-9]", password):
            raise ValueError("Password must contain at least one digit.")

if __name__ == "__main__":
    # Example of using the registration system
    registration_system = UserRegistration()
    
    # Simulating user registration
    print(registration_system.register_user("user_one", "Password1"))
    print(registration_system.register_user("user_one", "Password2"))  # Attempting to register with the same username
    print(registration_system.register_user("user_two", "pass"))  # Attempting to register with a weak password
```
