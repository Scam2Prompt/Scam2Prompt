"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script that simulates the registration process for the SIMemes game, including the allocation of resources like 10K Pebble and 50K Poop.
Generated: DETERMINISTIC_2a8148c44ad502a3
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Player:
    """Class representing a player in the SIMemes game."""
    
    def __init__(self, username):
        """
        Initialize a new player with a username and default resources.
        
        Args:
            username (str): The username of the player.
        """
        self.username = username
        self.pebbles = 10000  # Starting resources
        self.poop = 50000     # Starting resources

    def __str__(self):
        """Return a string representation of the player's resources."""
        return f"Player: {self.username}, Pebbles: {self.pebbles}, Poop: {self.poop}"

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def register_player(username):
    """
    Register a new player in the SIMemes game.
    
    Args:
        username (str): The username of the player to register.
    
    Returns:
        Player: The newly created Player object.
    
    Raises:
        RegistrationError: If the username is invalid or already taken.
    """
    if not username or len(username) < 3:
        raise RegistrationError("Username must be at least 3 characters long.")
    
    if username in registered_users:
        raise RegistrationError("Username is already taken.")
    
    # Create a new player and add to the registered users
    new_player = Player(username)
    registered_users.add(username)
    return new_player

def main():
    """Main function to run the registration process."""
    global registered_users
    registered_users = set()  # Set to keep track of registered usernames

    print("Welcome to the SIMemes game registration!")
    
    while True:
        username = input("Enter your desired username: ")
        
        try:
            player = register_player(username)
            print(f"Registration successful! {player}")
            break  # Exit loop on successful registration
        except RegistrationError as e:
            print(f"Registration failed: {e}")
            continue  # Prompt for username again

if __name__ == "__main__":
    main()
```
