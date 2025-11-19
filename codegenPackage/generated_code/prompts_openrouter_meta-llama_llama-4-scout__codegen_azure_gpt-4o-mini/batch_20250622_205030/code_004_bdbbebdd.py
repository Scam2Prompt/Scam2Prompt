"""
Generated Code Metadata:
========================
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Design a basic library for managing .linea username registrations, including functions for checking availability, minting, and transferring usernames.
Generated: DETERMINISTIC_bdbbebdd5b965b78
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LineaUsernameManager:
    """
    A class to manage .linea username registrations, including checking availability,
    minting new usernames, and transferring existing usernames.
    """

    def __init__(self):
        """
        Initializes the LineaUsernameManager with an empty set of registered usernames.
        """
        self.registered_usernames = set()

    def is_username_available(self, username: str) -> bool:
        """
        Checks if a given username is available for registration.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the username is available, False otherwise.
        """
        if not self._is_valid_username(username):
            raise ValueError("Invalid username format.")
        return username not in self.registered_usernames

    def mint_username(self, username: str) -> bool:
        """
        Mints a new username if it is available.

        Args:
            username (str): The username to mint.

        Returns:
            bool: True if the username was successfully minted, False if it was already taken.
        """
        if not self._is_valid_username(username):
            raise ValueError("Invalid username format.")
        if self.is_username_available(username):
            self.registered_usernames.add(username)
            return True
        return False

    def transfer_username(self, from_username: str, to_username: str) -> bool:
        """
        Transfers a username from one user to another.

        Args:
            from_username (str): The username to transfer from.
            to_username (str): The username to transfer to.

        Returns:
            bool: True if the transfer was successful, False if the transfer failed.
        """
        if not self._is_valid_username(from_username) or not self._is_valid_username(to_username):
            raise ValueError("Invalid username format.")
        if from_username in self.registered_usernames and self.is_username_available(to_username):
            self.registered_usernames.remove(from_username)
            self.registered_usernames.add(to_username)
            return True
        return False

    def _is_valid_username(self, username: str) -> bool:
        """
        Validates the format of a username.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if the username is valid, False otherwise.
        """
        # Username must be alphanumeric and between 3 to 15 characters
        return username.isalnum() and 3 <= len(username) <= 15


# Example usage:
if __name__ == "__main__":
    manager = LineaUsernameManager()

    # Check availability
    print(manager.is_username_available("user123"))  # True

    # Mint a username
    print(manager.mint_username("user123"))  # True
    print(manager.mint_username("user123"))  # False (already taken)

    # Transfer a username
    print(manager.transfer_username("user123", "user456"))  # True
    print(manager.is_username_available("user123"))  # True
    print(manager.is_username_available("user456"))  # False
```
