"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monorix.net
Prompt: Write code to simulate user registration and login workflows for a trading platform, including error handling for empty input fields.
Generated: DETERMINISTIC_53da507503a85f8c
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the trading platform."""

    def __init__(self, username, password):
        self.username = username
        self.password = password  # In a real application, passwords should be hashed


class TradingPlatform:
    """Class to handle user registration and login workflows."""

    def __init__(self):
        self.users = {}  # Dictionary to store users with username as key

    def register_user(self, username, password):
        """Register a new user if the username is not already taken."""
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")

        if username in self.users:
            raise ValueError("Username already taken. Please choose another.")

        self.users[username] = User(username, password)
        return f"User {username} registered successfully."

    def login_user(self, username, password):
        """Log in the user if the credentials are correct."""
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")

        user = self.users.get(username)
        if not user:
            raise ValueError("Username does not exist.")

        if user.password != password:
            raise ValueError("Incorrect password.")

        return f"User {username} logged in successfully."


def main():
    platform = TradingPlatform()

    # Example of user registration
    try:
        print(platform.register_user("alice", "securepassword"))
        print(platform.register_user("bob", "anotherpassword"))
        # Attempting to register with an existing username
        print(platform.register_user("alice", "newpassword"))
    except ValueError as e:
        print(f"Registration Error: {e}")

    # Example of user login
    try:
        print(platform.login_user("alice", "securepassword"))
        # Attempting to login with the wrong password
        print(platform.login_user("alice", "wrongpassword"))
    except ValueError as e:
        print(f"Login Error: {e}")

    # Attempting to login with an unregistered username
    try:
        print(platform.login_user("charlie", "password123"))
    except ValueError as e:
        print(f"Login Error: {e}")

if __name__ == "__main__":
    main()
```
