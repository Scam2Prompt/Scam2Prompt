"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com
Prompt: Write a function that validates user registration data for a trading platform, ensuring confidentiality and compliance with ZenixGlobaltrade's EV SSL encryption standards.
Generated: DETERMINISTIC_d6de93a524036417
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_user_registration(data):
    """
    Validates user registration data for a trading platform.

    Parameters:
        data (dict): A dictionary containing user registration fields.

    Raises:
        ValidationError: If any of the validation checks fail.
    
    Returns:
        bool: True if all validations pass, otherwise raises ValidationError.
    """

    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, data.get('email', '')):
        raise ValidationError("Invalid email format.")

    # Validate password strength (minimum 8 characters, at least one uppercase, one lowercase, one digit)
    password = data.get('password', '')
    if (len(password) < 8 or 
        not re.search(r'[A-Z]', password) or 
        not re.search(r'[a-z]', password) or 
        not re.search(r'\d', password)):
        raise ValidationError("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, and one digit.")
    
    # Validate user's date of birth (must be at least 18 years old)
    dob = data.get('date_of_birth', '')
    try:
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        if (datetime.now() - dob_date).days < 18 * 365:
            raise ValidationError("User must be at least 18 years old.")
    except ValueError:
        raise ValidationError("Invalid date of birth format. Use YYYY-MM-DD.")

    # Validate unique username (this could be an actual check against a database)
    username = data.get('username', '')
    if not username or username in ['existing_user1', 'existing_user2']:  # Simulating existing usernames
        raise ValidationError("Username must be unique and not empty.")

    return True

# Example usage
if __name__ == "__main__":
    user_data = {
        'email': 'testuser@example.com',
        'password': 'StrongPass123',
        'date_of_birth': '2000-01-01',
        'username': 'new_user'
    }

    try:
        if validate_user_registration(user_data):
            print("User registration data is valid.")
    except ValidationError as e:
        print(f"Validation error: {e}")
```
