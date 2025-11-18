"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Create a script for user registration and bonus allocation, inspired by BaxBet's quick registration and exciting bonus offerings.
Generated: DETERMINISTIC_2609ec649c121d4f
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re

class UserRegistration:
    def __init__(self):
        self.users = {}  # Dictionary to store user data
        self.bonus_amount = 100  # Default bonus amount

    def register_user(self, username: str, password: str) -> str:
        """
        Register a new user with the provided username and password.

        :param username: The desired username for the new user
        :param password: The password for the new user
        :return: A message indicating the result of the registration
        """
        try:
            # Validate username and password
            self.validate_credentials(username, password)

            # Check if the username already exists
            if username in self.users:
                raise ValueError("Username already exists. Please choose a different username.")

            # Register the user
            self.users[username] = {
                'password': password,
                'bonus_allocated': False
            }
            return f"User '{username}' registered successfully."
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred during registration: {str(e)}"

    def validate_credentials(self, username: str, password: str):
        """
        Validate username and password according to specific rules.

        :param username: The username to validate
        :param password: The password to validate
        :raises ValueError: If validation rules are not met
        """
        if not re.match(r'^[a-zA-Z0-9]{3,15}$', username):
            raise ValueError("Username must be 3-15 characters long and contain only letters and numbers.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")

    def allocate_bonus(self, username: str) -> str:
        """
        Allocate a bonus to the specified user if they haven't received one yet.

        :param username: The username of the user receiving the bonus
        :return: A message indicating the result of the bonus allocation
        """
        try:
            # Check if the user exists
            if username not in self.users:
                raise ValueError("User not found. Please register first.")

            # Check if bonus has already been allocated
            if self.users[username]['bonus_allocated']:
                return f"Bonus has already been allocated to user '{username}'."

            # Allocate bonus
            self.users[username]['bonus_allocated'] = True
            self.users[username]['bonus'] = self.bonus_amount
            return f"Bonus of {self.bonus_amount} allocated to user '{username}'."

        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An error occurred during bonus allocation: {str(e)}"


# Example usage of the UserRegistration class
if __name__ == "__main__":
    registration_system = UserRegistration()

    # Register users
    print(registration_system.register_user("Alice123", "securePass"))
    print(registration_system.register_user("Bob456", "12345"))  # This should raise a validation error

    # Allocate bonuses
    print(registration_system.allocate_bonus("Alice123"))
    print(registration_system.allocate_bonus("Bob456"))  # Should indicate user not found
    print(registration_system.allocate_bonus("Alice123"))  # Should indicate bonus already allocated
```
