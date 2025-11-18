"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: Write code to validate a username and password input field for a login form, inspired by the functionality on dxnoke.com.
Generated: DETERMINISTIC_d3f2748b74a0b345
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class LoginFormValidator:
    """
    A class to validate login form fields including username and password.
    """

    def __init__(self):
        # Define regex patterns for validation
        self.username_pattern = r'^[a-zA-Z0-9_]{3,20}$'  # Alphanumeric and underscores, 3-20 characters
        self.password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$'  # At least 8 characters, 1 letter, 1 number

    def validate_username(self, username: str) -> bool:
        """
        Validate the username against the defined pattern.
        
        Args:
            username (str): The username to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not username:
            raise ValueError("Username field cannot be empty.")
        if re.match(self.username_pattern, username):
            return True
        return False

    def validate_password(self, password: str) -> bool:
        """
        Validate the password against the defined pattern.
        
        Args:
            password (str): The password to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        if not password:
            raise ValueError("Password field cannot be empty.")
        if re.match(self.password_pattern, password):
            return True
        return False

def main():
    """
    Main function to demonstrate username and password validation.
    """
    validator = LoginFormValidator()

    # Sample user input for demonstration
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        if validator.validate_username(username):
            print("Username is valid.")
        else:
            print("Username is invalid.")

        if validator.validate_password(password):
            print("Password is valid.")
        else:
            print("Password is invalid.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
