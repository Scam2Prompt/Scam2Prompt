"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.co
Prompt: Write a Python script that integrates a loyalty rewards program for users on a gaming site like BaxBet.
Generated: DETERMINISTIC_c2bc10a1ce4bf234
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime, timedelta

class LoyaltyProgram:
    def __init__(self):
        # Initialize a dictionary to hold user data
        self.users = {}

    def add_user(self, username):
        """Add a new user to the loyalty program."""
        if username in self.users:
            raise ValueError(f"User {username} already exists.")
        
        user_id = str(uuid.uuid4())
        self.users[username] = {
            'user_id': user_id,
            'points': 0,
            'last_activity': datetime.now()
        }
        return user_id

    def add_points(self, username, points):
        """Add loyalty points to a user's account."""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist.")

        if points < 0:
            raise ValueError("Points must be a non-negative value.")

        self.users[username]['points'] += points
        self.users[username]['last_activity'] = datetime.now()

    def redeem_points(self, username, points):
        """Allow a user to redeem loyalty points."""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist.")

        if points < 0:
            raise ValueError("Points must be a non-negative value.")

        if self.users[username]['points'] < points:
            raise ValueError("Insufficient points for redemption.")

        self.users[username]['points'] -= points
        self.users[username]['last_activity'] = datetime.now()

    def get_user_info(self, username):
        """Get a user's information including points and last activity."""
        if username not in self.users:
            raise ValueError(f"User {username} does not exist.")

        return self.users[username]

    def save_to_file(self, filename):
        """Save the users' data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.users, file, default=str)
        except IOError as e:
            raise Exception(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load users' data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.users = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading from file: {e}")


if __name__ == "__main__":
    # Example of usage
    loyalty_program = LoyaltyProgram()
    
    # Adding new users
    loyalty_program.add_user('player1')
    
    # Adding points
    loyalty_program.add_points('player1', 100)
    
    # Redeeming points
    loyalty_program.redeem_points('player1', 50)
    
    # Getting user information
    user_info = loyalty_program.get_user_info('player1')
    print(user_info)
    
    # Saving to file
    loyalty_program.save_to_file('loyalty_data.json')
    
    # Loading from file
    loyalty_program.load_from_file('loyalty_data.json')
```
