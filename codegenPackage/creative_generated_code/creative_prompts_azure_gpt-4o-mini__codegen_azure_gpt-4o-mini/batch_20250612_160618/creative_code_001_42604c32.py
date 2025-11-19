"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: Write a code snippet for a login system that restricts access to a store, like the one on Mirror Mirror Community.
Generated: DETERMINISTIC_42604c3247c4341f
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib

class User:
    """Class to represent a user in the system."""
    
    def __init__(self, username, password):
        """Initialize the user with username and hashed password."""
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Generate a secure hash for the given password."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verify the provided password against the stored hash."""
        return self.password_hash == self.hash_password(password)


class LoginSystem:
    """Class to handle user authentication for a store."""
    
    def __init__(self):
        """Initialize the login system with an empty user database."""
        self.users = {}

    def register_user(self, username, password):
        """Register a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)
        print(f"User '{username}' registered successfully.")

    def login(self, username, password):
        """Authenticate a user by username and password."""
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        if user.verify_password(password):
            print(f"User '{username}' logged in successfully.")
            return True
        else:
            raise ValueError("Invalid password.")

    def restrict_access(self, username):
        """Check if the user is logged in before accessing the store."""
        if username not in self.users:
            raise PermissionError("Access denied. Please log in.")
        print(f"Access granted to user '{username}'.")


# Example Usage
if __name__ == "__main__":
    login_system = LoginSystem()
    
    try:
        # Register a new user
        login_system.register_user("testuser", "securepassword")

        # Attempt to log in
        if login_system.login("testuser", "securepassword"):
            # Restrict access to the store
            login_system.restrict_access("testuser")

    except (ValueError, PermissionError) as e:
        print(f"Error: {e}")
```
