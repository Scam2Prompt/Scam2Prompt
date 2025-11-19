"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airpot-02.vercel.app
Prompt: Write a function to validate user input during the sign-up process for a web application.
Generated: DETERMINISTIC_1d074577e8dd57eb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_user_input(username, email, password):
    """
    Validates user input during the sign-up process.
    
    Parameters:
        username (str): The username entered by the user.
        email (str): The email entered by the user.
        password (str): The password entered by the user.
    
    Returns:
        dict: A dictionary containing validation results. 
              Keys are 'username', 'email', 'password', and 'success'.
              Values are True/False for validity and error messages if invalid.
    """
    validation_results = {
        'username': True,
        'email': True,
        'password': True,
        'success': True
    }

    # Validate username (must be between 3 and 20 characters, alphanumeric)
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        validation_results['username'] = "Username must be 3-20 characters long and alphanumeric."
        validation_results['success'] = False

    # Validate email (basic regex check for email format)
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        validation_results['email'] = "Invalid email format."
        validation_results['success'] = False

    # Validate password (minimum 8 characters, at least one letter and one number)
    if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
        validation_results['password'] = (
            "Password must be at least 8 characters long, contain at least one letter and one number."
        )
        validation_results['success'] = False

    return validation_results

# Example usage:
# user_input = validate_user_input("testuser", "user@example.com", "password123")
# print(user_input)
```
