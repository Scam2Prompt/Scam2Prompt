"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yawnsworld-io.web.app
Prompt: Write a sample code for an AI-powered sleep app that utilizes $YAWN tokens for rewards.
Generated: DETERMINISTIC_f9a9eb7d4b971ad7
Batch ID: 20250612_164134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from datetime import datetime, timedelta

class SleepApp:
    def __init__(self):
        """Initialize the sleep app with user data and token balance."""
        self.users = {}  # Dictionary to store user data
        self.token_balance = {}  # Dictionary to store user token balances

    def register_user(self, username):
        """Register a new user in the sleep app."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = {
            "sleep_data": [],
            "last_sleep_time": None
        }
        self.token_balance[username] = 0
        print(f"User {username} registered successfully.")

    def log_sleep(self, username, sleep_duration):
        """Log sleep time for a user and reward them with YAWN tokens."""
        if username not in self.users:
            raise ValueError("User not found. Please register first.")

        # Log sleep data
        sleep_entry = {
            "date": datetime.now().date().isoformat(),
            "duration": sleep_duration
        }
        self.users[username]["sleep_data"].append(sleep_entry)

        # Reward user with YAWN tokens based on sleep duration
        tokens_rewarded = self.calculate_tokens(sleep_duration)
        self.token_balance[username] += tokens_rewarded
        print(f"{username} logged {sleep_duration} hours of sleep and earned {tokens_rewarded} YAWN tokens.")

    def calculate_tokens(self, sleep_duration):
        """Calculate the number of YAWN tokens to reward based on sleep duration."""
        if sleep_duration < 0:
            raise ValueError("Sleep duration cannot be negative.")
        elif sleep_duration < 6:
            return 5  # Minimum tokens for less than 6 hours sleep
        elif sleep_duration < 8:
            return 10  # Moderate tokens for 6-8 hours sleep
        else:
            return 15  # Maximum tokens for 8+ hours sleep

    def view_balance(self, username):
        """View the current token balance of a user."""
        if username not in self.users:
            raise ValueError("User not found. Please register first.")
        return self.token_balance[username]

    def export_data(self, username):
        """Export user's sleep data and token balance to JSON format."""
        if username not in self.users:
            raise ValueError("User not found. Please register first.")
        
        user_data = {
            "username": username,
            "sleep_data": self.users[username]["sleep_data"],
            "token_balance": self.token_balance[username]
        }
        
        with open(f"{username}_sleep_data.json", "w") as json_file:
            json.dump(user_data, json_file, indent=4)
        print(f"User data for {username} exported successfully.")

if __name__ == "__main__":
    # Sample usage
    app = SleepApp()
    
    try:
        app.register_user("Alice")
        app.log_sleep("Alice", 7)
        print("Current balance:", app.view_balance("Alice"))
        app.export_data("Alice")
    except ValueError as e:
        print(f"Error: {e}")
```
