"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-blubtheblob.com
Prompt: Generate code to validate user inputs for the "Blub The Blob" presale registration form based on the guidelines provided on the website.
Generated: DETERMINISTIC_2b4b0f569e1d21ef
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserInputValidator:
    """Validator for user inputs in the 'Blub The Blob' presale registration form."""

    def __init__(self):
        self.errors = []

    def validate_email(self, email: str) -> bool:
        """Validate the format of the email address."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            self.errors.append("Invalid email format.")
            return False
        return True

    def validate_username(self, username: str) -> bool:
        """Validate the username to ensure it meets the criteria."""
        if len(username) < 3 or len(username) > 15:
            self.errors.append("Username must be between 3 and 15 characters long.")
            return False
        if not username.isalnum():
            self.errors.append("Username can only contain alphanumeric characters.")
            return False
        return True

    def validate_password(self, password: str) -> bool:
        """Validate the password strength."""
        if len(password) < 8:
            self.errors.append("Password must be at least 8 characters long.")
            return False
        if not any(char.isdigit() for char in password):
            self.errors.append("Password must contain at least one digit.")
            return False
        if not any(char.isupper() for char in password):
            self.errors.append("Password must contain at least one uppercase letter.")
            return False
        return True

    def validate_inputs(self, username: str, email: str, password: str) -> bool:
        """Validate all inputs and return True if all validations pass, else False."""
        self.errors.clear()  # Clear previous errors

        if not self.validate_username(username):
            return False
        if not self.validate_email(email):
            return False
        if not self.validate_password(password):
            return False
        
        return True

    def get_errors(self) -> list:
        """Return the list of errors encountered during validation."""
        return self.errors

# Example usage
if __name__ == "__main__":
    validator = UserInputValidator()

    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if validator.validate_inputs(username, email, password):
        print("All inputs are valid. Proceeding with registration.")
    else:
        print("Errors found:")
        for error in validator.get_errors():
            print(f"- {error}")
```
