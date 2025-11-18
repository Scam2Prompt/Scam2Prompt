"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Write code to simulate a user registration process for the 8KBet platform, including validation for promotional offers like the 88k bonus.
Generated: DETERMINISTIC_b56157641e7b2335
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class UserRegistration:
    def __init__(self):
        self.users = []
        self.promo_code = "88k"

    def register_user(self, username: str, password: str, promo_code: str = None) -> str:
        """
        Register a new user with the provided username and password.
        Optionally accepts a promotional code.
        
        :param username: The desired username of the user
        :param password: The desired password of the user
        :param promo_code: Optional promotional code for offers
        :return: Success message or error message
        """
        try:
            # Validate username and password
            if not self.validate_username(username):
                return "Invalid username. Must be 3-20 characters and alphanumeric."
            if not self.validate_password(password):
                return "Invalid password. Must be at least 8 characters, include upper and lower case letters, and a number."

            # Check if the user already exists
            if self.user_exists(username):
                return "Username already exists. Please choose another one."

            # Process promotional code if provided
            if promo_code and promo_code != self.promo_code:
                return "Invalid promotional code."

            # Register the user
            self.users.append({"username": username, "password": password})
            return "Registration successful!"

        except Exception as e:
            return f"An error occurred during registration: {str(e)}"

    def validate_username(self, username: str) -> bool:
        """
        Validate the username format.
        
        :param username: The username to validate
        :return: True if valid, False otherwise
        """
        return bool(re.match(r'^[a-zA-Z0-9]{3,20}$', username))

    def validate_password(self, password: str) -> bool:
        """
        Validate the password format.
        
        :param password: The password to validate
        :return: True if valid, False otherwise
        """
        return (len(password) >= 8 and 
                re.search(r"[a-z]", password) and 
                re.search(r"[A-Z]", password) and 
                re.search(r"[0-9]", password))

    def user_exists(self, username: str) -> bool:
        """
        Check if the username already exists in the registered users list.
        
        :param username: The username to check
        :return: True if exists, False otherwise
        """
        return any(user['username'] == username for user in self.users)

# Example usage:
if __name__ == "__main__":
    registration_system = UserRegistration()
    print(registration_system.register_user("User123", "Password1", "88k"))  # Successful registration
    print(registration_system.register_user("User123", "Password1"))  # Username already exists
    print(registration_system.register_user("User", "pass"))  # Invalid password
    print(registration_system.register_user("NewUser", "Password1", "invalid_code"))  # Invalid promo code
```
