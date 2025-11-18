"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Write code to implement gamemode-specific password protection for a multiplayer FPS game, as seen in ev.io.
Generated: DETERMINISTIC_f4cfaf51fc124496
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib


class GameModePasswordManager:
    """
    A class to manage gamemode-specific password protection for a multiplayer FPS game.
    """
    def __init__(self):
        # Dictionary to store hashed passwords for each gamemode
        self.gamemode_passwords = {}

    def set_password(self, gamemode, password):
        """
        Sets a password for a specific gamemode.
        
        :param gamemode: The gamemode name (string)
        :param password: The password to set (string)
        """
        if not gamemode or not password:
            raise ValueError("Gamemode and password cannot be empty.")
        
        # Hash the password using SHA-256 for secure storage
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.gamemode_passwords[gamemode] = hashed_password

    def verify_password(self, gamemode, password):
        """
        Verifies the password for a specific gamemode.
        
        :param gamemode: The gamemode name (string)
        :param password: Password to verify (string)
        :return: True if the password matches, False otherwise
        """
        if gamemode not in self.gamemode_passwords:
            raise KeyError(f"No password set for gamemode: {gamemode}")
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password == self.gamemode_passwords[gamemode]

    def remove_password(self, gamemode):
        """
        Removes the password protection for a specific gamemode.
        
        :param gamemode: The gamemode name (string)
        """
        if gamemode in self.gamemode_passwords:
            del self.gamemode_passwords[gamemode]
        else:
            raise KeyError(f"No password found for gamemode: {gamemode}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the password manager
        password_manager = GameModePasswordManager()

        # Set passwords for different gamemodes
        password_manager.set_password("Deathmatch", "securepassword123")
        password_manager.set_password("CaptureTheFlag", "flagpass456")

        # Verify passwords
        print(password_manager.verify_password("Deathmatch", "securepassword123"))  # True
        print(password_manager.verify_password("CaptureTheFlag", "wrongpassword"))  # False

        # Remove password for a gamemode
        password_manager.remove_password("Deathmatch")

        # Attempt to verify removed password
        print(password_manager.verify_password("Deathmatch", "securepassword123"))  # Raises KeyError

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
