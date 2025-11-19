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
import bcrypt

class UserAuthentication:
    def __init__(self, user_db):
        """
        Initializes the UserAuthentication class with a user database.
        
        :param user_db: A dictionary simulating a user database with usernames as keys 
                        and hashed passwords as values.
        """
        self.user_db = user_db

    def validate_username(self, username):
        """
        Validates the username according to specified criteria.

        :param username: The username to validate.
        :return: True if valid, False otherwise.
        """
        # Username must be 3-20 characters long and alphanumeric
        if 3 <= len(username) <= 20 and re.match("^[a-zA-Z0-9_]+$", username):
            return True
        return False

    def validate_password(self, password):
        """
        Validates the password complexity.

        :param password: The password to validate.
        :return: True if valid, False otherwise.
        """
        # Password must be at least 8 characters, contain at least one number and one uppercase letter
        if (len(password) >= 8 and
                re.search(r"[A-Z]", password) and
                re.search(r"[0-9]", password)):
            return True
        return False

    def authenticate_user(self, username, password):
        """
        Authenticates a user by validating credentials against the user database.

        :param username: The username of the user.
        :param password: The password of the user.
        :return: True if authentication is successful, False otherwise.
        """
        try:
            # Validate username
            if not self.validate_username(username):
                print("Invalid username.")
                return False
            
            # Validate password
            if not self.validate_password(password):
                print("Invalid password.")
                return False
            
            # Check if the user exists in the database
            if username in self.user_db:
                # Compare the hashed password with the provided password
                if bcrypt.checkpw(password.encode('utf-8'), self.user_db[username]):
                    return True
                else:
                    print("Incorrect password.")
                    return False
            else:
                print("User does not exist.")
                return False

        except Exception as e:
            print(f"An error occurred during authentication: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Simulated user database with hashed passwords
    user_database = {
        "user1": bcrypt.hashpw("Password123".encode('utf-8'), bcrypt.gensalt()),
        "user2": bcrypt.hashpw("MySecurePass456".encode('utf-8'), bcrypt.gensalt())
    }

    auth = UserAuthentication(user_database)
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if auth.authenticate_user(username_input, password_input):
        print("Authentication successful!")
    else:
        print("Authentication failed.")
```
