"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalepullix.pages.dev
Prompt: What are the best practices for handling user privacy and terms of service in a sign-up process, as seen on Pullix?
Generated: DETERMINISTIC_1f97f49225a963fc
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class User:
    def __init__(self, username, email, password, accepted_terms):
        self.username = username
        self.email = email
        self.password = password
        self.accepted_terms = accepted_terms

class SignUpProcess:
    def __init__(self):
        self.users = []

    def validate_email(self, email):
        """Validate the email format using a regular expression."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            return True
        else:
            raise ValueError("Invalid email format.")

    def validate_password(self, password):
        """Validate password to ensure it meets complexity requirements."""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValueError("Password must contain at least one digit.")
        return True

    def accept_terms(self, accepted_terms):
        """Check if the user has accepted the terms of service."""
        if not accepted_terms:
            raise ValueError("You must accept the terms of service to sign up.")
        return True

    def sign_up(self, username, email, password, accepted_terms):
        """Sign up a new user after validating inputs."""
        try:
            self.validate_email(email)
            self.validate_password(password)
            self.accept_terms(accepted_terms)

            # Create a new user and add to the users list.
            new_user = User(username, email, password, accepted_terms)
            self.users.append(new_user)
            return f"User {username} signed up successfully."

        except ValueError as e:
            return str(e)

# Example usage:
if __name__ == "__main__":
    signup_process = SignUpProcess()
    response = signup_process.sign_up(
        username="john_doe",
        email="john.doe@example.com",
        password="Password123",
        accepted_terms=True
    )
    print(response)  # Output: User john_doe signed up successfully.
```
