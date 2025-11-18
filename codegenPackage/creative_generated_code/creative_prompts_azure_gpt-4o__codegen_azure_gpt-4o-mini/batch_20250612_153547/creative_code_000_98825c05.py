"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bbmanews.com
Prompt: Write code to simulate a user login process using a username and password for a credit application portal.
Generated: DETERMINISTIC_98825c05a7fb1b05
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib

class User:
    """Class to represent a user in the application."""
    
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        """Verifies the provided password against the stored password hash."""
        return self.password_hash == self.hash_password(password)


class UserDatabase:
    """Class to simulate a user database."""
    
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, password: str):
        """Adds a user to the database."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)

    def get_user(self, username: str) -> User:
        """Retrieves a user from the database."""
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username]


class LoginSystem:
    """Class to handle the login process for the application."""

    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db

    def login(self, username: str, password: str) -> str:
        """Processes the login attempt for a user."""
        try:
            user = self.user_db.get_user(username)
            if user.check_password(password):
                return "Login successful!"
            else:
                return "Invalid password."
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    # Create a new user database
    user_db = UserDatabase()
    
    # Add a user
    try:
        user_db.add_user("test_user", "secure_password123")
    except ValueError as e:
        print(f"Error adding user: {e}")

    # Initialize the login system
    login_system = LoginSystem(user_db)

    # Attempt to login
    username_input = "test_user"
    password_input = "secure_password123"
    login_message = login_system.login(username_input, password_input)
    print(login_message)  # Expected: Login successful!

    # Attempt to login with an incorrect password
    login_message = login_system.login(username_input, "wrong_password")
    print(login_message)  # Expected: Invalid password.

    # Attempt to login with a non-existent user
    login_message = login_system.login("non_existent_user", "any_password")
    print(login_message)  # Expected: User not found.
```
