"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenet.works.app
Prompt: Write code to simulate a login process using a Space ID, Login ID, and password for a workspace platform like "サスケWorks."
Generated: DETERMINISTIC_e4ef37ba96b11521
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt

class User:
    def __init__(self, space_id, login_id, password):
        self.space_id = space_id
        self.login_id = login_id
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        """Hashes the password using bcrypt."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Verifies the provided password against the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

class AuthService:
    def __init__(self):
        self.users = {}

    def register_user(self, space_id, login_id, password):
        """Registers a new user in the system."""
        if login_id in self.users:
            raise ValueError("User with this Login ID already exists.")
        
        user = User(space_id, login_id, password)
        self.users[login_id] = user
        return "User registered successfully."

    def login_user(self, login_id, password):
        """Authenticates a user by verifying Login ID and password."""
        user = self.users.get(login_id)
        
        if user is None:
            raise ValueError("User not found.")
        
        if user.check_password(password):
            return "Login successful."
        else:
            raise ValueError("Invalid password.")

def main():
    auth_service = AuthService()
    
    # Example usage
    try:
        # Register a user
        print(auth_service.register_user("space123", "user1", "securepassword"))

        # Login with correct credentials
        print(auth_service.login_user("user1", "securepassword"))

        # Attempt to login with incorrect credentials
        print(auth_service.login_user("user1", "wrongpassword"))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
