"""
Generated Code Metadata:
========================
Original URL: https://duolingo.wiki
Prompt: Create a tool that validates the Duolingo username or email input as per the guidelines provided on the Duolingo Super membership webpage.
Generated: DETERMINISTIC_13b171dab9f7c6c1
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class DuolingoValidator:
    """
    A class to validate Duolingo usernames and email addresses based on specified guidelines.
    """

    def __init__(self):
        # Define regex patterns for username and email validation
        self.username_pattern = r'^[a-zA-Z0-9_]{1,30}$'  # 1-30 characters, alphanumeric and underscores
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Standard email format

    def validate_username(self, username):
        """
        Validate the provided username against Duolingo's guidelines.

        :param username: str - The username to validate
        :return: bool - True if valid, False otherwise
        """
        if not isinstance(username, str):
            raise ValueError("Username must be a string.")
        
        is_valid = re.match(self.username_pattern, username) is not None
        return is_valid

    def validate_email(self, email):
        """
        Validate the provided email address against Duolingo's guidelines.

        :param email: str - The email address to validate
        :return: bool - True if valid, False otherwise
        """
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        
        is_valid = re.match(self.email_pattern, email) is not None
        return is_valid

def main():
    """
    Main function to demonstrate the usage of the DuolingoValidator class.
    """
    validator = DuolingoValidator()

    # Example inputs for validation
    usernames = ["valid_username", "invalid username", "too_long_username_123456789012345678901234567890"]
    emails = ["valid.email@example.com", "invalid-email@", "another.invalid.email@.com"]

    # Validate usernames
    print("Username Validation Results:")
    for username in usernames:
        try:
            result = validator.validate_username(username)
            print(f"'{username}': {'Valid' if result else 'Invalid'}")
        except ValueError as e:
            print(f"Error validating '{username}': {e}")

    # Validate emails
    print("\nEmail Validation Results:")
    for email in emails:
        try:
            result = validator.validate_email(email)
            print(f"'{email}': {'Valid' if result else 'Invalid'}")
        except ValueError as e:
            print(f"Error validating '{email}': {e}")

if __name__ == "__main__":
    main()
```
