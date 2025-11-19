"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: How can I implement an access control system using biometric and RFID solutions for a business in Kenya, based on the offerings of Donture Systems Ltd?
Generated: DETERMINISTIC_260033ee14e785d2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
import random
from datetime import datetime

# Constants for access levels
ACCESS_LEVELS = {
    'admin': 3,
    'employee': 2,
    'guest': 1
}

# A simple in-memory database to store user data
user_database = {}

class AccessControlSystem:
    def __init__(self):
        """Initialize a new access control system."""
        self.log = []

    def add_user(self, username, role, biometric_data):
        """
        Adds a new user to the system with their corresponding role and biometric data.
        
        :param username: The username of the new user
        :param role: The role assigned to the user
        :param biometric_data: The biometric data of the user
        :raises ValueError: If the role is not valid
        """
        if role not in ACCESS_LEVELS:
            raise ValueError(f"Invalid role: {role}. Valid roles are {list(ACCESS_LEVELS.keys())}.")
        
        user_database[username] = {
            'role': role,
            'biometric_data': self.hash_biometric_data(biometric_data),
            'access_level': ACCESS_LEVELS[role]
        }
        print(f"User {username} added successfully.")

    def hash_biometric_data(self, biometric_data):
        """
        Hashes the biometric data for security purposes.
        
        :param biometric_data: The biometric data to be hashed
        :return: The hashed biometric data
        """
        return hashlib.sha256(biometric_data.encode()).hexdigest()

    def authenticate_user(self, username, biometric_data):
        """
        Authenticates a user based on their username and biometric data.
        
        :param username: The username of the user attempting to authenticate
        :param biometric_data: The biometric data provided for authentication
        :return: True if authenticated, False otherwise
        """
        user = user_database.get(username)
        if user and user['biometric_data'] == self.hash_biometric_data(biometric_data):
            self.log_access_attempt(username, True)
            return True
        else:
            self.log_access_attempt(username, False)
            return False

    def log_access_attempt(self, username, success):
        """
        Logs an access attempt to the system.
        
        :param username: The username of the user attempting to access
        :param success: Whether the authentication was successful
        """
        timestamp = datetime.now().isoformat()
        self.log.append({'username': username, 'success': success, 'timestamp': timestamp})

    def check_access(self, username):
        """
        Checks the access level of a user.
        
        :param username: The username of the user
        :return: Access level of the user
        :raises KeyError: If the user does not exist
        """
        if username in user_database:
            return user_database[username]['access_level']
        else:
            raise KeyError(f"User {username} not found in database.")

def main():
    """Main function to demonstrate the access control system."""
    acs = AccessControlSystem()

    # Adding users
    acs.add_user('alice', 'admin', 'fingerprint_data_1')
    acs.add_user('bob', 'employee', 'fingerprint_data_2')

    # Authenticating users
    username = 'alice'
    is_authenticated = acs.authenticate_user(username, 'fingerprint_data_1')
    print(f"User {username} authenticated: {is_authenticated}")

    # Checking access levels
    try:
        access_level = acs.check_access('bob')
        print(f"Bob's access level: {access_level}")
    except KeyError as e:
        print(e)

if __name__ == "__main__":
    main()
```
