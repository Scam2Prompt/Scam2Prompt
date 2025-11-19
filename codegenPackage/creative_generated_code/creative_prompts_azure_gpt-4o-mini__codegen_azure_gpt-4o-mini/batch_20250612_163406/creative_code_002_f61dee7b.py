"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jhxdjhgvj.scarexpedition.top
Prompt: Create a function that validates user input for a free data plan registration, ensuring they complete all necessary steps.
Generated: DETERMINISTIC_f61dee7b9577b9be
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_user_input(username: str, email: str, password: str, confirm_password: str) -> None:
    """
    Validates user input for free data plan registration.

    Args:
        username (str): The username provided by the user.
        email (str): The email address provided by the user.
        password (str): The password provided by the user.
        confirm_password (str): The password confirmation provided by the user.

    Raises:
        ValidationError: If any validation step fails.
    """
    
    # Check if username is provided
    if not username:
        raise ValidationError("Username is required.")
    
    # Validate email format using regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format.")
    
    # Check if password is provided
    if not password:
        raise ValidationError("Password is required.")
    
    # Check if password and confirmation match
    if password != confirm_password:
        raise ValidationError("Passwords do not match.")
    
    # Check password strength
    if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
        raise ValidationError("Password must be at least 8 characters long and contain both letters and numbers.")
    
    # All validations passed
    print("User input validated successfully.")

# Example usage
if __name__ == "__main__":
    try:
        validate_user_input("john_doe", "john.doe@example.com", "Password123", "Password123")
    except ValidationError as ve:
        print(f"Validation Error: {ve}")
```
