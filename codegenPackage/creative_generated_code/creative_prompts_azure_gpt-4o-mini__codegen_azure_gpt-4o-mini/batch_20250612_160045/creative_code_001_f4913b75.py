"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write a Python script to implement a user registration system for a betting website, incorporating features like quick sign-up and bonus rewards.
Generated: DETERMINISTIC_f4913b750eff70bc
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from datetime import datetime

class UserRegistrationSystem:
    def __init__(self, database_file='users.json'):
        """Initialize the registration system with a database file."""
        self.database_file = database_file
        self.load_users()

    def load_users(self):
        """Load users from the database file."""
        try:
            with open(self.database_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = []
        except json.JSONDecodeError:
            print("Error: Database file is corrupted. Starting fresh.")
            self.users = []

    def save_users(self):
        """Save users to the database file."""
        with open(self.database_file, 'w') as file:
            json.dump(self.users, file)

    def validate_email(self, email):
        """Check if the provided email is valid using regex."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def register_user(self, username, email):
        """Register a new user if inputs are valid and unique."""
        if not username or not email:
            raise ValueError("Username and email cannot be empty.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        if any(user['email'] == email for user in self.users):
            raise ValueError("Email is already registered.")

        # Create a new user with a bonus reward
        user = {
            'username': username,
            'email': email,
            'registration_date': datetime.now().isoformat(),
            'bonus_reward': 10  # Initial bonus reward
        }
        self.users.append(user)
        self.save_users()
        return user

    def quick_sign_up(self, email):
        """Quick sign-up using email only."""
        if not email:
            raise ValueError("Email cannot be empty for quick sign-up.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        if any(user['email'] == email for user in self.users):
            raise ValueError("Email is already registered.")
        
        # Generate a default username
        username = f"user_{len(self.users) + 1}"

        # Create a new user with a bonus reward
        user = {
            'username': username,
            'email': email,
            'registration_date': datetime.now().isoformat(),
            'bonus_reward': 5  # Quick sign-up bonus
        }
        self.users.append(user)
        self.save_users()
        return user

# Example usage
if __name__ == "__main__":
    reg_system = UserRegistrationSystem()

    try:
        new_user = reg_system.register_user("john_doe", "john@example.com")
        print(f"User registered: {new_user}")

        quick_user = reg_system.quick_sign_up("quick_user@example.com")
        print(f"Quick signed up user: {quick_user}")

    except ValueError as e:
        print(f"Registration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
