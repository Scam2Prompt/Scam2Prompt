"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://focuscompoundingpharm.com
Prompt: Write a code snippet to validate user credentials for a medical-focused web application.
Generated: DETERMINISTIC_8ac936a08d795a8e
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_credentials(username: str, password: str) -> bool:
    """
    Validates user credentials for a medical-focused web application.
    
    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.
    
    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    try:
        # Validate username: Must be alphanumeric and 5-20 characters long
        if not re.match("^[a-zA-Z0-9]{5,20}$", username):
            print("Invalid username: Must be alphanumeric and between 5-20 characters.")
            return False

        # Validate password: Must be 8-20 characters, include at least one digit, one uppercase, one lowercase, and one special character
        password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
        if not re.match(password_pattern, password):
            print("Invalid password: Must be 8-20 characters and include at least one digit, one uppercase, one lowercase, and one special character.")
            return False

        # If both validations pass, return True
        return True

    except Exception as e:
        # Log the error (for production use, replace print with proper logging)
        print(f"An error occurred during validation: {e}")
        return False

# Example usage
if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if validate_credentials(username, password):
        print("Credentials are valid.")
    else:
        print("Invalid credentials.")
```
