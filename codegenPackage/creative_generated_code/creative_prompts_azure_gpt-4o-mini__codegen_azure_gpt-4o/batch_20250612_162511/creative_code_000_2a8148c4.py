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
import uuid

class RegistrationError(Exception):
    """Custom exception to handle registration errors."""
    pass

class SIMemesGame:
    def __init__(self):
        # Database to store registered users
        self.users = {}
        # Default resources allocated on registration
        self.default_resources = {
            "Pebble": 10000,
            "Poop": 50000
        }

    def generate_user_id(self):
        """
        Generates a unique user ID using UUID4.

        Returns:
            str: A unique user ID.
        """
        return str(uuid.uuid4())

    def register_user(self, username):
        """
        Simulates the registration of a user in the SIMemes game,
        allocating default resources to the new user.

        Args:
            username (str): The username of the user to register.

        Returns:
            dict: Registration details including user ID, username, and allocated resources.

        Raises:
            RegistrationError: If the username is already registered or invalid.
        """
        if not username or not isinstance(username, str):
            raise RegistrationError("Invalid username provided.")
        
        if username in self.users:
            raise RegistrationError(f"Username '{username}' is already registered.")
        
        user_id = self.generate_user_id()
        self.users[username] = {
            "user_id": user_id,
            "resources": self.default_resources.copy()
        }
        return {
            "user_id": user_id,
            "username": username,
            "resources": self.default_resources.copy()
        }

    def get_user_info(self, username):
        """
        Retrieves the information of a registered user.

        Args:
            username (str): The username to query.

        Returns:
            dict: User information including user ID and resources.

        Raises:
            RegistrationError: If the username is not found.
        """
        if username not in self.users:
            raise RegistrationError(f"Username '{username}' is not registered.")
        
        return self.users[username]

# Main script
if __name__ == "__main__":
    game = SIMemesGame()
    try:
        # Example registration of two users
        user1 = game.register_user("Player1")
        print("Registration successful:", user1)

        user2 = game.register_user("Player2")
        print("Registration successful:", user2)

        # Fetch information of a registered user
        player_info = game.get_user_info("Player1")
        print("Player1 Info:", player_info)

        # Attempt to register a duplicate username (should raise error)
        duplicate_user = game.register_user("Player1")
    except RegistrationError as e:
        print("Registration error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```
