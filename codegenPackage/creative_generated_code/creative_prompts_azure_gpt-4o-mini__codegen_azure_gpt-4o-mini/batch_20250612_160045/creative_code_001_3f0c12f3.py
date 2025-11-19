"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.co
Prompt: Write a script that automates user registration and bonus allocation for a gaming website similar to BaxBet.
Generated: DETERMINISTIC_3f0c12f38658ef0f
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import json
from datetime import datetime

class UserRegistration:
    def __init__(self):
        self.users_db = "users.json"  # Path to the user database
        self.bonus_amount = 50  # Default signup bonus

    def generate_user_id(self):
        """Generate a unique user ID."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def save_user_data(self, user_data):
        """Save user data to the database."""
        try:
            # Load existing users
            with open(self.users_db, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []  # Initialize with an empty list if file does not exist
        except json.JSONDecodeError as e:
            print("Error reading the user database:", e)
            return False

        users.append(user_data)  # Add the new user
        with open(self.users_db, 'w') as file:
            json.dump(users, file, indent=4)  # Save updated users

        return True

    def register_user(self, username, email):
        """Register a new user and allocate a bonus."""
        if self.is_email_taken(email):
            print("Email is already taken. Please choose another.")
            return False
        
        user_id = self.generate_user_id()
        registration_time = datetime.now().isoformat()

        user_data = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "registration_time": registration_time,
            "bonus_amount": self.bonus_amount,
        }

        if self.save_user_data(user_data):
            print(f"User registered successfully: {user_data}")
            return True
        else:
            print("Failed to register user.")
            return False

    def is_email_taken(self, email):
        """Check if the email is already registered."""
        try:
            with open(self.users_db, 'r') as file:
                users = json.load(file)
                for user in users:
                    if user['email'] == email:
                        return True
            return False
        except FileNotFoundError:
            return False  # No users registered yet
        except json.JSONDecodeError as e:
            print("Error reading the user database:", e)
            return True  # Assume email is taken if the database is corrupt

def main():
    registration_system = UserRegistration()

    # Example data - In production, replace this with actual user input
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    registration_system.register_user(username, email)

if __name__ == "__main__":
    main()
```
