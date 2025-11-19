"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Python script that simulates the registration process for the SIMemes game, including the allocation of resources like 10K Pebble and 50K Poop.
Generated: DETERMINISTIC_2a8148c44ad502a3
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class User:
    """
    A class to represent a user in the SIMemes game.
    
    Attributes:
    username: str
        The username of the user.
    pebbles: int
        The amount of pebbles allocated to the user.
    poop: int
        The amount of poop allocated to the user.
    """
    
    def __init__(self, username):
        """
        Initializes the user with a username and allocates resources.
        
        Parameters:
        username: str
            The desired username for the new user.
        """
        self.username = username
        self.pebbles = 10000  # Initial allocation of pebbles
        self.poop = 50000     # Initial allocation of poop
    
    def display_resources(self):
        """Displays the current resources of the user."""
        return f"User: {self.username}, Pebbles: {self.pebbles}, Poop: {self.poop}"


class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass


def register_user(username):
    """
    Simulates the registration process for a user.
    
    Parameters:
    username: str
        The desired username for registration.
    
    Returns:
    User
        A User object representing the newly registered user.
    
    Raises:
    RegistrationError
        If the username is not valid (e.g., empty or already taken).
    """
    if not username or len(username) < 3:
        raise RegistrationError("Username must be at least 3 characters long.")
    
    # Simulate a check for existing usernames (placeholder logic)
    existing_usernames = ["player1", "player2", "player3"]  # Example existing usernames
    if username in existing_usernames:
        raise RegistrationError("Username already taken. Please choose another.")
    
    # If username is valid, create a new User object
    return User(username)


def main():
    """Main function to execute the registration process."""
    print("Welcome to the SIMemes registration process!")

    # Get username input from the user
    username = input("Please enter a username (at least 3 characters): ")

    try:
        # Register the user
        new_user = register_user(username)
        print("Registration successful!")
        print(new_user.display_resources())
    except RegistrationError as e:
        print(f"Error during registration: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
