"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Write code for a login system that includes team selection functionality, similar to the "King Salman Park" portal, where users can choose a team before logging in.
Generated: DETERMINISTIC_042afdabe26073c0
Batch ID: 20250612_151911
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
    def __init__(self, username, password, team):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.team = team
    
    def hash_password(self, password):
        # Hash the password using SHA-256 for secure storage
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        # Verify the provided password against the stored password hash
        return self.password_hash == self.hash_password(password)

class LoginSystem:
    def __init__(self):
        self.users = []  # List to store registered users
        self.teams = ['Team A', 'Team B', 'Team C']  # Available teams

    def register_user(self, username, password, team):
        # Register a new user after validating inputs
        if not username or not password or team not in self.teams:
            raise ValueError("Invalid username, password or team selection.")
        if self.get_user(username):
            raise ValueError("Username already exists.")
        
        new_user = User(username, password, team)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully.")

    def get_user(self, username):
        # Retrieve a user by username
        for user in self.users:
            if user.username == username:
                return user
        return None

    def login(self, username, password):
        # Log in a user after validating credentials
        user = self.get_user(username)
        if user and user.verify_password(password):
            print(f"User '{username}' logged in successfully to {user.team}.")
            return user.team
        else:
            raise ValueError("Invalid username or password.")

def main():
    # Main function to demonstrate registration and login
    login_system = LoginSystem()
    
    # Example User Registration
    try:
        login_system.register_user("alice", "password123", "Team A")
        login_system.register_user("bob", "securePass456", "Team B")
    except ValueError as e:
        print(f"Registration Error: {e}")

    # Example User Login
    try:
        team = login_system.login("alice", "password123")
        print(f"Alice is part of {team}.")
    except ValueError as e:
        print(f"Login Error: {e}")

if __name__ == "__main__":
    main()
```
