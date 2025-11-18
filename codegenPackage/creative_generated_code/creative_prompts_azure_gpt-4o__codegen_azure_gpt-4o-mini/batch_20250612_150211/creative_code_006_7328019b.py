"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Write code to validate user input for a login form, ensuring proper handling of email and username fields, as described on Pavonal's website.
Generated: DETERMINISTIC_7328019bb9ec0874
Batch ID: 20250612_150211
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
    """
    A class to validate user input for a login form.
    """

    def __init__(self):
        # Regular expression patterns for validation
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.username_pattern = r'^[a-zA-Z0-9_]{3,15}$'  # Alphanumeric and underscores, 3-15 chars

    def validate_email(self, email: str) -> bool:
        """
        Validate the email format.

        :param email: Email string to validate.
        :return: True if valid, False otherwise.
        """
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        is_valid = re.match(self.email_pattern, email) is not None
        return is_valid

    def validate_username(self, username: str) -> bool:
        """
        Validate the username format.

        :param username: Username string to validate.
        :return: True if valid, False otherwise.
        """
        if not isinstance(username, str):
            raise ValueError("Username must be a string.")
        is_valid = re.match(self.username_pattern, username) is not None
        return is_valid

def main():
    # Create an instance of the UserInputValidator
    validator = UserInputValidator()

    # Sample user input
    email = input("Enter your email: ")
    username = input("Enter your username: ")

    try:
        # Validate email
        if validator.validate_email(email):
            print("Email is valid.")
        else:
            print("Invalid email format.")

        # Validate username
        if validator.validate_username(username):
            print("Username is valid.")
        else:
            print("Invalid username format.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
