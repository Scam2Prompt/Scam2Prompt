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
import re

# Define a custom exception for invalid input
class RegistrationError(Exception):
    pass

class User:
    """Class representing a user"""
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.bonus = 0

    def allocate_bonus(self, bonus_amount):
        """Allocates a bonus to the user"""
        if bonus_amount < 0:
            raise ValueError("Bonus amount cannot be negative.")
        self.bonus += bonus_amount

    def __str__(self):
        """Returns a string representation of the user"""
        return f"User: {self.username}, Email: {self.email}, Bonus: ${self.bonus:.2f}"

def is_valid_email(email):
    """
    Validates email format using regex.
    Returns True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def register_user(username, email):
    """
    Registers a user with the provided username and email.
    Raises RegistrationError for invalid inputs.
    """
    if not username or not email:
        raise RegistrationError("Username and email are required.")
    
    if not is_valid_email(email):
        raise RegistrationError("Invalid email format.")
    
    return User(username, email)

def main():
    """
    Main function to handle user registration and bonus allocation.
    """
    print("Welcome to BaxBet's quick registration and bonus system!")
    
    try:
        # Prompt user for registration details
        username = input("Enter your username: ").strip()
        email = input("Enter your email: ").strip()

        # Register the user
        user = register_user(username, email)
        print("Registration successful!")
        print(user)

        # Allocate a bonus to the user
        bonus_amount = float(input("Enter the bonus amount to allocate: "))
        user.allocate_bonus(bonus_amount)
        print("Bonus allocated successfully!")
        print(user)

    except RegistrationError as e:
        print(f"Registration failed: {e}")
    except ValueError as e:
        print(f"Error during bonus allocation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
