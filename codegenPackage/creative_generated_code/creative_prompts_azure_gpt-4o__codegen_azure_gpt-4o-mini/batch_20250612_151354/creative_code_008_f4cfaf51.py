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
import random
import string

class GameModePasswordProtection:
    def __init__(self):
        # Dictionary to store passwords for different game modes
        self.passwords = {}

    def generate_password(self, length=12):
        """Generate a random password of specified length."""
        characters = string.ascii_letters + string.digits + string.punctuation
        random_password = ''.join(random.choice(characters) for _ in range(length))
        return random_password

    def set_password(self, game_mode, password):
        """Set a password for a specific game mode."""
        if not self.validate_password(password):
            raise ValueError("Invalid password. Must be at least 8 characters long and contain letters, numbers, and special characters.")
        
        # Hash the password for security
        hashed_password = self.hash_password(password)
        self.passwords[game_mode] = hashed_password

    def validate_password(self, password):
        """Validate the format of the provided password."""
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

    def hash_password(self, password):
        """Hash the password using SHA-256 for security."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, game_mode, password):
        """Check if the provided password matches the stored hashed password for the given game mode."""
        if game_mode not in self.passwords:
            raise KeyError(f"No password has been set for game mode: {game_mode}")
        
        hashed_password = self.hash_password(password)
        return hashed_password == self.passwords[game_mode]

    def remove_password(self, game_mode):
        """Remove the password for a specific game mode."""
        if game_mode in self.passwords:
            del self.passwords[game_mode]
        else:
            raise KeyError(f"No password found for game mode: {game_mode}")

# Example usage
if __name__ == "__main__":
    try:
        password_protection = GameModePasswordProtection()
        
        # Set a password for a specific game mode
        game_mode = "Battle Royale"
        password = password_protection.generate_password()
        password_protection.set_password(game_mode, password)
        print(f"Password for {game_mode} set to: {password}")

        # Check the password
        is_correct = password_protection.check_password(game_mode, password)
        print(f"Password check for {game_mode}: {'Correct' if is_correct else 'Incorrect'}")

        # Remove the password
        password_protection.remove_password(game_mode)
        print(f"Password for {game_mode} removed.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
