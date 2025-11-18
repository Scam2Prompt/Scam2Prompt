"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-prime.com
Prompt: Create a secure form validation script for user registration, ensuring compliance with Immediate Prime's data privacy notice requirements.
Generated: DETERMINISTIC_0322a694026cc633
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
from werkzeug.security import generate_password_hash

def validate_registration_form(data):
    """
    Validates the user registration form data.

    Args:
        data (dict): A dictionary containing user registration fields.

    Returns:
        tuple: A tuple containing a boolean indicating success and an error message (if applicable).
    """
    # Check if all required fields are present
    required_fields = ["username", "email", "password"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    # Validate username (alphanumeric, 3-20 characters)
    username = data["username"]
    if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        return False, "Invalid username. Must be alphanumeric and between 3-20 characters."

    # Validate email format
    email = data["email"]
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex, email):
        return False, "Invalid email address."

    # Validate password (min 8 characters, at least 1 lowercase letter, 1 uppercase letter, 1 number, 1 special character)
    password = data["password"]
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(password_regex, password):
        return False, "Password must be at least 8 characters long and include one lowercase letter, one uppercase letter, one number, and one special character."

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password)

    # Return success
    return True, {"username": username, "email": email, "password_hash": hashed_password}


# Example usage:
if __name__ == "__main__":
    # Sample registration data
    user_data = {
        "username": "john_doe",
        "email": "john.doe@example.com",
        "password": "SecureP@ssword1"
    }

    # Validate the form
    is_valid, result = validate_registration_form(user_data)
    if is_valid:
        print("Registration successful!")
        print(result)  # Contains validated data and hashed password
    else:
        print(f"Registration failed: {result}")
```
