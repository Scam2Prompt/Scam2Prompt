"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://markandecastro.com
Prompt: What are best practices for managing account suspension in a user authentication library?
Generated: DETERMINISTIC_1399e0ca29cf090d
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionError(Exception):
    """Custom exception for account suspension errors."""
    pass


class User:
    """A class representing a user in the authentication system."""
    
    def __init__(self, username: str, is_suspended: bool = False):
        """
        Initializes a new user.

        :param username: The username of the user.
        :param is_suspended: A flag indicating if the account is suspended.
        """
        self.username = username
        self.is_suspended = is_suspended

    def suspend(self):
        """Suspend the user's account."""
        self.is_suspended = True
        print(f"User '{self.username}' has been suspended.")

    def unsuspend(self):
        """Unsuspend the user's account."""
        self.is_suspended = False
        print(f"User '{self.username}' has been unsuspended.")

    def authenticate(self, password: str):
        """
        Authenticate the user with a password.

        :param password: The password provided for authentication.
        :raises AccountSuspensionError: If the account is suspended.
        """
        if self.is_suspended:
            raise AccountSuspensionError(f"Account for user '{self.username}' is suspended.")

        # Here would be the logic to check the password (omitted for brevity).
        print(f"User '{self.username}' authenticated successfully.")


class UserManager:
    """A class to manage user accounts."""
    
    def __init__(self):
        """Initializes a new UserManager with an empty user database."""
        self.users = {}

    def add_user(self, username: str):
        """
        Add a new user to the user manager.
        
        :param username: The username of the new user.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists.")
        self.users[username] = User(username)
        print(f"User '{username}' added successfully.")

    def suspend_user(self, username: str):
        """
        Suspend a user's account.

        :param username: The username of the user to suspend.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' not found.")

        self.users[username].suspend()

    def unsuspend_user(self, username: str):
        """
        Unsuspend a user's account.

        :param username: The username of the user to unsuspend.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError(f"User '{username}' not found.")

        self.users[username].unsuspend()


# Example usage
if __name__ == "__main__":
    user_manager = UserManager()
    
    # Adding users
    user_manager.add_user("alice")
    user_manager.add_user("bob")

    # Suspending a user
    user_manager.suspend_user("alice")

    # Attempting to authenticate a suspended user
    try:
        user_manager.users["alice"].authenticate("password123")
    except AccountSuspensionError as e:
        print(e)

    # Unsuspending a user
    user_manager.unsuspend_user("alice")

    # Authenticating the unsuspended user
    try:
        user_manager.users["alice"].authenticate("password123")
    except AccountSuspensionError as e:
        print(e)
```
