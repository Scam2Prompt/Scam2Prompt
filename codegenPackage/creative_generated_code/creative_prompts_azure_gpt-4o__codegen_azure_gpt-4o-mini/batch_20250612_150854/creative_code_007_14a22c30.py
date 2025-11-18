"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Write code to validate and process user input for an investment education platform, ensuring compliance with Immediate Peak's data privacy notice.
Generated: DETERMINISTIC_14a22c3098c6f631
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

class UserInputError(Exception):
    """Custom exception for user input validation errors."""
    pass

def validate_email(email):
    """Validates the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise UserInputError("Invalid email format.")

def validate_name(name):
    """Validates the user's name to ensure it contains only alphabetic characters."""
    if not name.isalpha():
        raise UserInputError("Name must contain only alphabetic characters.")

def validate_age(age):
    """Validates the user's age to ensure it is a positive integer."""
    if not age.isdigit() or int(age) <= 0:
        raise UserInputError("Age must be a positive integer.")

def process_user_input(name, email, age):
    """
    Processes user input for an investment education platform.
    
    Parameters:
        name (str): The user's name.
        email (str): The user's email address.
        age (str): The user's age.
    
    Returns:
        dict: A dictionary containing validated user information.
    
    Raises:
        UserInputError: If any of the input fields fail validation.
    """
    try:
        # Validate each input field
        validate_name(name)
        validate_email(email)
        validate_age(age)
        
        # Return a dictionary of validated user information
        return {
            'name': name,
            'email': email,
            'age': int(age)  # Convert age to an integer for further processing
        }
    except UserInputError as e:
        # Handle validation errors by logging or re-raising
        print(f"Input validation error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    user_age = input("Enter your age: ")

    try:
        user_info = process_user_input(user_name, user_email, user_age)
        print("User information processed successfully:", user_info)
    except UserInputError:
        print("Failed to process user information due to invalid input.")
```
