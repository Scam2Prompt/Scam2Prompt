"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-prime.com
Prompt: Write Python code to simulate the registration process described on Immediate Prime, including validation for first name, last name, and email address as outlined on the site.
Generated: DETERMINISTIC_b94b84a603d90566
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserRegistration:
    def __init__(self):
        self.users = []

    def validate_name(self, name: str) -> bool:
        """Validate the first or last name. Must be alphabetic and between 1 to 50 characters."""
        if isinstance(name, str) and 1 <= len(name) <= 50 and name.isalpha():
            return True
        return False

    def validate_email(self, email: str) -> bool:
        """Validate the email address format using a regular expression."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            return True
        return False

    def register_user(self, first_name: str, last_name: str, email: str) -> str:
        """Register a new user if validation checks pass."""
        try:
            # Validate first name
            if not self.validate_name(first_name):
                raise ValueError("Invalid first name. It must contain only letters and be between 1 to 50 characters.")

            # Validate last name
            if not self.validate_name(last_name):
                raise ValueError("Invalid last name. It must contain only letters and be between 1 to 50 characters.")

            # Validate email
            if not self.validate_email(email):
                raise ValueError("Invalid email address format.")

            # Check if the user already exists
            if any(user['email'] == email for user in self.users):
                raise ValueError("Email is already registered.")

            # Register the user
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            }
            self.users.append(user)

            return "Registration successful."

        except ValueError as e:
            return str(e)

if __name__ == "__main__":
    registration_system = UserRegistration()
    
    # Example registration process
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")

    result = registration_system.register_user(first_name, last_name, email)
    print(result)
```
