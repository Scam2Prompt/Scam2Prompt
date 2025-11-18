"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duolingo.wiki
Prompt: Create a tool that validates the Duolingo username or email input as per the guidelines provided on the Duolingo Super membership webpage.
Generated: DETERMINISTIC_13b171dab9f7c6c1
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class DuolingoValidator:
    """
    A class to validate Duolingo usernames and email addresses
    according to the guidelines provided by Duolingo.
    """
    
    def __init__(self):
        # Define regex patterns for validation
        self.username_pattern = r'^[\w-]{1,30}$'  # 1-30 characters: letters, digits, underscores, hyphens
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Standard email format

    def validate_username(self, username):
        """
        Validate the provided username against Duolingo's criteria.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not isinstance(username, str):
            raise ValueError("Username must be a string.")
        is_valid = re.match(self.username_pattern, username) is not None
        return is_valid

    def validate_email(self, email):
        """
        Validate the provided email against Duolingo's criteria.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        is_valid = re.match(self.email_pattern, email) is not None
        return is_valid

def main():
    # Example usage of the DuolingoValidator class
    validator = DuolingoValidator()
    
    # Test usernames and emails
    test_usernames = ["valid_username", "invalid username", "too_long_username_123456789012345678901234567890"]
    test_emails = ["valid.email@example.com", "invalid-email@", "another.invalid.email@.com"]

    print("Username Validation Results:")
    for username in test_usernames:
        try:
            result = validator.validate_username(username)
            print(f"{username}: {'Valid' if result else 'Invalid'}")
        except ValueError as e:
            print(f"Error validating username '{username}': {e}")

    print("\nEmail Validation Results:")
    for email in test_emails:
        try:
            result = validator.validate_email(email)
            print(f"{email}: {'Valid' if result else 'Invalid'}")
        except ValueError as e:
            print(f"Error validating email '{email}': {e}")

if __name__ == "__main__":
    main()
```
