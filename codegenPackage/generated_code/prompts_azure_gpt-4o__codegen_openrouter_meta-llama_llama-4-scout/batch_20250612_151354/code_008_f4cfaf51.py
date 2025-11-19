"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Write code to implement gamemode-specific password protection for a multiplayer FPS game, as seen in ev.io.
Generated: DETERMINISTIC_f4cfaf51fc124496
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gamemode_password_protection.py

import hashlib
import hmac
import secrets

class GamemodePasswordProtection:
    def __init__(self, gamemodes):
        """
        Initialize the password protection system.

        :param gamemodes: A dictionary of gamemodes with their respective passwords.
        """
        self.gamemodes = gamemodes

    def _hash_password(self, password):
        """
        Hash a password using SHA-256.

        :param password: The password to hash.
        :return: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def _generate_salt(self):
        """
        Generate a random salt.

        :return: A random salt.
        """
        return secrets.token_bytes(16)

    def _hmac_password(self, password, salt):
        """
        Generate an HMAC of a password using a salt.

        :param password: The password to HMAC.
        :param salt: The salt to use.
        :return: The HMAC of the password.
        """
        return hmac.new(salt, password.encode(), hashlib.sha256).hexdigest()

    def create_gamemode(self, name, password):
        """
        Create a new gamemode with a password.

        :param name: The name of the gamemode.
        :param password: The password for the gamemode.
        """
        if name in self.gamemodes:
            raise ValueError("Gamemode already exists")

        salt = self._generate_salt()
        hashed_password = self._hmac_password(password, salt)
        self.gamemodes[name] = (salt, hashed_password)

    def join_gamemode(self, name, password):
        """
        Join a gamemode with a password.

        :param name: The name of the gamemode.
        :param password: The password for the gamemode.
        :return: True if the password is correct, False otherwise.
        """
        if name not in self.gamemodes:
            raise ValueError("Gamemode does not exist")

        salt, hashed_password = self.gamemodes[name]
        provided_hmac = self._hmac_password(password, salt)

        return hmac.compare_digest(hashed_password, provided_hmac)

    def change_password(self, name, old_password, new_password):
        """
        Change the password of a gamemode.

        :param name: The name of the gamemode.
        :param old_password: The current password of the gamemode.
        :param new_password: The new password for the gamemode.
        :return: True if the password was changed, False otherwise.
        """
        if name not in self.gamemodes:
            raise ValueError("Gamemode does not exist")

        salt, hashed_password = self.gamemodes[name]
        provided_hmac = self._hmac_password(old_password, salt)

        if hmac.compare_digest(hashed_password, provided_hmac):
            new_salt = self._generate_salt()
            new_hashed_password = self._hmac_password(new_password, new_salt)
            self.gamemodes[name] = (new_salt, new_hashed_password)
            return True
        return False


def main():
    # Example usage:
    password_protection = GamemodePasswordProtection({})

    password_protection.create_gamemode("deathmatch", "mysecretpassword")

    try:
        print(password_protection.join_gamemode("deathmatch", "wrongpassword"))  # Should print: False
        print(password_protection.join_gamemode("deathmatch", "mysecretpassword"))  # Should print: True
    except ValueError as e:
        print(e)

    password_protection.change_password("deathmatch", "mysecretpassword", "newpassword")

    try:
        print(password_protection.join_gamemode("deathmatch", "mysecretpassword"))  # Should print: False
        print(password_protection.join_gamemode("deathmatch", "newpassword"))  # Should print: True
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
