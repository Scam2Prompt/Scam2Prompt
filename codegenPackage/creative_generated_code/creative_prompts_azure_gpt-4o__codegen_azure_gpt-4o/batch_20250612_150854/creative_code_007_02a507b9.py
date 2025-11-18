"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.nl
Prompt: Create a user registration system for a trading platform like Immediate Migna, including validation for names, email addresses, and integration with account manager support.
Generated: DETERMINISTIC_02a507b95efb83d2
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_registration.py
import re

# Mock database for user information
DATABASE = []

# Function to validate name (only alphabetic characters allowed)
def validate_name(name):
    """
    Validate that the name contains only alphabetic characters.
    
    Args:
        name (str): The name to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if not name or not name.isalpha():
        return False
    return True

# Function to validate email address using regex
def validate_email(email):
    """
    Validate the format of the email address.
    
    Args:
        email (str): The email to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not email or not re.match(email_regex, email):
        return False
    return True

# Function to integrate user with account manager support
def integrate_with_account_manager(user_data):
    """
    Mock integration with an account manager system for user registration.
    
    Args:
        user_data (dict): Dictionary containing user data.
    
    Returns:
        bool: True if integration is successful, False otherwise.
    """
    # Simulate integration with account manager support
    # For production, integrate with actual APIs or services
    print(f"Integration with account manager for user: {user_data}")
    return True

# Function to register a new user
def register_user(first_name, last_name, email):
    """
    Register a new user into the system.
    
    Args:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
    
    Returns:
        dict: Dictionary containing user information if registration is successful.
    """
    # Validate first name and last name
    if not validate_name(first_name):
        raise ValueError("Invalid first name. Must contain only alphabetic characters.")
    if not validate_name(last_name):
        raise ValueError("Invalid last name. Must contain only alphabetic characters.")
    
    # Validate email address
    if not validate_email(email):
        raise ValueError("Invalid email format.")
    
    # Check if email is already registered
    for user in DATABASE:
        if user['email'] == email:
            raise ValueError("Email is already registered.")
    
    # Create new user object
    new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }
    
    # Add user to database
    DATABASE.append(new_user)
    
    # Integrate with account manager support
    if not integrate_with_account_manager(new_user):
        raise RuntimeError("Failed to integrate with account manager support.")
    
    print("User registered successfully.")
    return new_user


# Main program (for demonstration purposes)
if __name__ == "__main__":
    try:
        # Collect user input
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        email = input("Enter your email address: ").strip()
        
        # Register the user
        user = register_user(first_name, last_name, email)
        print("Registered User:", user)
    except ValueError as ve:
        print("Error:", ve)
    except RuntimeError as re:
        print("Error:", re)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
