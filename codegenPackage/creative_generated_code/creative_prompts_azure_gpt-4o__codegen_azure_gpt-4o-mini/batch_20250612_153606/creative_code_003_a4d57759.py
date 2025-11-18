"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-xi-wine.vercel.app
Prompt: Write a script to validate whitelist entries for a platform similar to "Secret Base Society."
Generated: DETERMINISTIC_a4d57759f425ed0a
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from typing import List, Dict, Any

class WhitelistValidator:
    """
    Class to validate whitelist entries for a platform similar to "Secret Base Society."
    """

    # Regular expression for valid email addresses
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, whitelist: List[Dict[str, Any]]):
        """
        Initialize the WhitelistValidator with a list of whitelist entries.

        :param whitelist: List of dictionaries containing whitelist entries.
        """
        self.whitelist = whitelist

    def validate_entries(self) -> List[str]:
        """
        Validate the whitelist entries.

        :return: List of error messages for invalid entries.
        """
        error_messages = []
        for entry in self.whitelist:
            email = entry.get('email')
            username = entry.get('username')

            if not self.is_valid_email(email):
                error_messages.append(f"Invalid email: {email}")

            if not self.is_valid_username(username):
                error_messages.append(f"Invalid username: {username}")

        return error_messages

    def is_valid_email(self, email: str) -> bool:
        """
        Check if the email address is valid.

        :param email: Email address to validate.
        :return: True if valid, False otherwise.
        """
        return re.match(self.EMAIL_REGEX, email) is not None

    def is_valid_username(self, username: str) -> bool:
        """
        Check if the username is valid.

        :param username: Username to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(username, str) and 3 <= len(username) <= 20

def load_whitelist(file_path: str) -> List[Dict[str, Any]]:
    """
    Load the whitelist from a JSON file.

    :param file_path: Path to the JSON file containing whitelist entries.
    :return: List of whitelist entries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading whitelist: {e}")

def main():
    """
    Main function to execute the whitelist validation process.
    """
    try:
        # Load whitelist from a JSON file
        whitelist = load_whitelist('whitelist.json')

        # Create a WhitelistValidator instance
        validator = WhitelistValidator(whitelist)

        # Validate the entries
        errors = validator.validate_entries()

        # Output the results
        if errors:
            print("Validation Errors:")
            for error in errors:
                print(error)
        else:
            print("All whitelist entries are valid.")

    except RuntimeError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
