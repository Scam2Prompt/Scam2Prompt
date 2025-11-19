"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Describe the process of setting up user accounts for an online course on Sui Foundation.
Generated: DETERMINISTIC_babe09da62aa45a1
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script sets up user accounts for an online course on the Sui Foundation platform.
It includes functionality for creating accounts, validating input data, and storing user information securely.
"""

import re
import uuid

# Mock database to store user accounts
USER_DATABASE = {}

class UserAccount:
    """
    Represents a user's account for the online course.
    Contains methods to validate and store user data.
    """
    def __init__(self, username, email):
        self.user_id = str(uuid.uuid4())  # Unique ID for the user
        self.username = username
        self.email = email
    
    def to_dict(self):
        """Converts the user object to a dictionary for storage."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

def validate_username(username):
    """
    Validates a username to ensure it meets requirements.
    :param username: The username to validate
    :return: True if valid, raises ValueError if invalid
    """
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    if not username.isalnum():
        raise ValueError("Username can only contain alphanumeric characters.")
    return True

def validate_email(email):
    """
    Validates an email address to ensure it meets requirements.
    :param email: The email to validate
    :return: True if valid, raises ValueError if invalid
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    return True

def create_user_account(username, email):
    """
    Creates a new user account after validating input data.
    Stores the user account in the mock database.
    :param username: The desired username for the account
    :param email: The email address for the account
    :return: The newly created user account
    """
    try:
        # Validate inputs
        validate_username(username)
        validate_email(email)
        
        # Create user account
        new_user = UserAccount(username, email)
        
        # Store in mock database
        USER_DATABASE[new_user.user_id] = new_user.to_dict()
        
        return new_user.to_dict()
    except ValueError as e:
        # Log error and return meaningful message
        print(f"Error creating user account: {e}")
        return None

def list_all_users():
    """
    Lists all user accounts in the mock database.
    :return: A dictionary of all user accounts
    """
    return USER_DATABASE

# Example usage
if __name__ == "__main__":
    print("Creating user accounts...")
    user1 = create_user_account("JohnDoe", "john.doe@example.com")
    user2 = create_user_account("JaneSmith", "jane.smith@example.com")
    
    print("\nCreated accounts:")
    print(user1)
    print(user2)
    
    print("\nAll users:")
    print(list_all_users())
```
