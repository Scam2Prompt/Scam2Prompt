"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Write a code snippet for a user login system that includes error handling for forgotten usernames or passwords, inspired by the functionality on diverbox.com.pe.
Generated: DETERMINISTIC_f37e11ea43d7ce97
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserLoginSystem:
    def __init__(self):
        # Sample user database (username: password)
        self.user_database = {
            "user1": "password123",
            "user2": "pass456",
            "user3": "mypassword"
        }

    def is_valid_username(self, username):
        """Check if the username is valid (non-empty and alphanumeric)."""
        return bool(re.match("^[a-zA-Z0-9_-]+$", username))

    def login(self, username, password):
        """Attempt to log in the user with the provided username and password."""
        # Check for empty username or password
        if not username or not password:
            return "Error: Username and password cannot be empty."

        # Validate the username
        if not self.is_valid_username(username):
            return "Error: Invalid username format."

        # Check if the username exists
        if username not in self.user_database:
            return "Error: Username not found. Did you forget your username?"

        # Check if the password matches
        if self.user_database[username] != password:
            return "Error: Incorrect password. Did you forget your password?"

        return "Login successful!"

    def request_username_retrieval(self):
        """Handle username retrieval request."""
        return "Username retrieval is not implemented in this version."

    def request_password_reset(self):
        """Handle password reset request."""
        return "Password reset is not implemented in this version."


# Example usage
if __name__ == "__main__":
    login_system = UserLoginSystem()
    
    # Simulated user input
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Attempt to log in
    result = login_system.login(username_input, password_input)
    print(result)
```
