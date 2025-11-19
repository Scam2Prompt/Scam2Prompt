"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Write a code snippet to validate user credentials for a Paylocity login, ensuring it meets the password requirements mentioned on the site.
Generated: DETERMINISTIC_880e360f2c26c3af
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class PaylocityLoginValidator:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def validate_credentials(self) -> bool:
        """Validates the username and password according to Paylocity's requirements."""
        return self.validate_username() and self.validate_password()

    def validate_username(self) -> bool:
        """Validates the username for non-empty and length requirements."""
        if not self.username:
            raise ValueError("Username cannot be empty.")
        if len(self.username) < 3 or len(self.username) > 30:
            raise ValueError("Username must be between 3 and 30 characters long.")
        return True

    def validate_password(self) -> bool:
        """Validates the password against specified complexity requirements."""
        if not self.password:
            raise ValueError("Password cannot be empty.")
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", self.password):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", self.password):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", self.password):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            raise ValueError("Password must contain at least one special character.")
        return True

# Example usage
if __name__ == "__main__":
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        validator = PaylocityLoginValidator(username, password)
        if validator.validate_credentials():
            print("Login credentials are valid.")
    except ValueError as e:
        print(f"Validation Error: {e}")
```
