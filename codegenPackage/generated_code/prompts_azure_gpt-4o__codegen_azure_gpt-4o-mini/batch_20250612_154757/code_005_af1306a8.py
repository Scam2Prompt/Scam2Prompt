"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Write code to implement a "Move to Earn" concept, integrating token rewards for physical activities as described in the 欧易官网 content.
Generated: DETERMINISTIC_af1306a8b76b445b
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class User:
    """Class representing a user in the Move to Earn system."""
    
    def __init__(self, username):
        self.username = username
        self.balance = 0.0  # User's token balance
        self.activity_log = []  # Log of activities performed

    def add_tokens(self, amount):
        """Add tokens to the user's balance."""
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.balance += amount
        print(f"{amount} tokens added to {self.username}'s balance. New balance: {self.balance}")

    def log_activity(self, activity):
        """Log an activity performed by the user."""
        self.activity_log.append(activity)
        print(f"Activity logged: {activity}")

class Activity:
    """Class representing a physical activity."""
    
    def __init__(self, name, duration, reward_per_minute):
        self.name = name
        self.duration = duration  # Duration in minutes
        self.reward_per_minute = reward_per_minute  # Token reward per minute

    def calculate_reward(self):
        """Calculate the total reward for the activity."""
        return self.duration * self.reward_per_minute

class MoveToEarn:
    """Main class to manage the Move to Earn system."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users by username

    def register_user(self, username):
        """Register a new user."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)
        print(f"User {username} registered successfully.")

    def perform_activity(self, username, activity):
        """Record an activity performed by a user and reward them."""
        if username not in self.users:
            raise ValueError("User not found.")
        
        user = self.users[username]
        reward = activity.calculate_reward()
        user.add_tokens(reward)
        user.log_activity(f"{activity.name} for {activity.duration} minutes.")
        print(f"{username} performed {activity.name} and earned {reward} tokens.")

def main():
    """Main function to demonstrate the Move to Earn system."""
    try:
        # Initialize the Move to Earn system
        move_to_earn = MoveToEarn()

        # Register users
        move_to_earn.register_user("Alice")
        move_to_earn.register_user("Bob")

        # Define activities
        running = Activity("Running", 30, 2)  # 2 tokens per minute
        cycling = Activity("Cycling", 45, 1.5)  # 1.5 tokens per minute

        # Users perform activities
        move_to_earn.perform_activity("Alice", running)
        move_to_earn.perform_activity("Bob", cycling)

        # Display user balances
        for user in move_to_earn.users.values():
            print(f"{user.username} has a balance of {user.balance} tokens.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
