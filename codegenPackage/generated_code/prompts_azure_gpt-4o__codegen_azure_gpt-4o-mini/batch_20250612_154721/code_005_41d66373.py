"""
Generated Code Metadata:
========================
Original URL: https://rayatrecruitment.com
Prompt: Create a Python function to generate and display login credentials (application number and password) after successful registration, mimicking the process on the Rayat Shikshan Sanstha website.
Generated: DETERMINISTIC_41d663730b01b9f5
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def generate_application_number(length=8):
    """
    Generate a unique application number consisting of uppercase letters and digits.

    Args:
        length (int): The length of the application number to be generated.

    Returns:
        str: A unique application number.
    """
    characters = string.ascii_uppercase + string.digits
    application_number = ''.join(random.choices(characters, k=length))
    return application_number

def generate_password(length=12):
    """
    Generate a secure password consisting of uppercase letters, lowercase letters, digits, and special characters.

    Args:
        length (int): The length of the password to be generated.

    Returns:
        str: A secure password.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def register_user(username, email):
    """
    Simulate user registration and generate login credentials.

    Args:
        username (str): The username of the user.
        email (str): The email of the user.

    Returns:
        dict: A dictionary containing the application number and password.

    Raises:
        RegistrationError: If registration fails for any reason.
    """
    if not username or not email:
        raise RegistrationError("Username and email are required for registration.")

    # Simulate registration process
    try:
        application_number = generate_application_number()
        password = generate_password()
        # Here you would typically save the user data to a database
        return {
            "application_number": application_number,
            "password": password
        }
    except Exception as e:
        raise RegistrationError(f"Registration failed: {str(e)}")

def display_credentials(credentials):
    """
    Display the generated login credentials.

    Args:
        credentials (dict): A dictionary containing the application number and password.
    """
    print("Registration Successful!")
    print(f"Application Number: {credentials['application_number']}")
    print(f"Password: {credentials['password']}")

# Example usage
if __name__ == "__main__":
    try:
        user_credentials = register_user("john_doe", "john@example.com")
        display_credentials(user_credentials)
    except RegistrationError as e:
        print(f"Error: {e}")
```
