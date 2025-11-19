"""
Generated Code Metadata:
========================
Original URL: https://flagship.luc.edu
Prompt: Write Python code to simulate a login system that verifies a user's UVID and password, similar to the authentication system described on the Loyola University Chicago Libraries portal.
Generated: DETERMINISTIC_95af5bf02cc5d2c1
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# login_system.py

class User:
    """Represents a user with a UVID and password."""

    def __init__(self, uvid, password):
        """
        Initializes a User object.

        Args:
            uvid (str): The user's UVID.
            password (str): The user's password.
        """
        self.uvid = uvid
        self.password = password


class LoginSystem:
    """Simulates a login system that verifies a user's UVID and password."""

    def __init__(self):
        """
        Initializes a LoginSystem object with an empty user database.
        """
        self.users = {}

    def add_user(self, uvid, password):
        """
        Adds a new user to the system.

        Args:
            uvid (str): The user's UVID.
            password (str): The user's password.

        Raises:
            ValueError: If the UVID is already taken.
        """
        if uvid in self.users:
            raise ValueError("UVID already taken")
        self.users[uvid] = User(uvid, password)

    def login(self, uvid, password):
        """
        Attempts to log in a user with the given UVID and password.

        Args:
            uvid (str): The user's UVID.
            password (str): The user's password.

        Returns:
            bool: True if the login is successful, False otherwise.
        """
        if uvid not in self.users:
            return False
        user = self.users[uvid]
        return user.password == password

    def authenticate(self, uvid, password):
        """
        Authenticates a user's credentials.

        Args:
            uvid (str): The user's UVID.
            password (str): The user's password.

        Returns:
            str: A success message if authenticated, an error message otherwise.
        """
        try:
            if self.login(uvid, password):
                return f"Login successful for UVID: {uvid}"
            else:
                return "Invalid UVID or password"
        except Exception as e:
            return f"An error occurred: {str(e)}"


def main():
    # Create a login system
    login_system = LoginSystem()

    # Add some test users
    login_system.add_user("john_doe", "password123")
    login_system.add_user("jane_doe", "ilovepython")

    # Test login attempts
    print(login_system.authenticate("john_doe", "password123"))  # Login successful
    print(login_system.authenticate("john_doe", "wrong_password"))  # Invalid password
    print(login_system.authenticate("unknown_uvid", "password"))  # Unknown UVID

if __name__ == "__main__":
    main()
```
