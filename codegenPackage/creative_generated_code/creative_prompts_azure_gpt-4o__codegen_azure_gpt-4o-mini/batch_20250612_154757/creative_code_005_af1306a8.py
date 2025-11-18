"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geokukt.cn
Prompt: Write code to implement a "Move to Earn" concept, integrating token rewards for physical activities as described in the 欧易官网 content.
Generated: DETERMINISTIC_af1306a8b76b445b
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class User:
    """Class representing a user participating in the Move to Earn program."""
    
    def __init__(self, username):
        """Initialize a new user with a username and a token balance."""
        self.username = username
        self.token_balance = 0
    
    def earn_tokens(self, activity_points):
        """Calculate and add tokens based on activity points."""
        # Token earning logic: 1 token per 10 activity points
        tokens_earned = activity_points // 10
        self.token_balance += tokens_earned
        print(f"{self.username} earned {tokens_earned} tokens! Total balance: {self.token_balance} tokens.")
    
    def redeem_tokens(self, amount):
        """Redeem tokens for rewards, ensuring sufficient balance."""
        if amount > self.token_balance:
            raise ValueError("Insufficient tokens to redeem.")
        self.token_balance -= amount
        print(f"{self.username} redeemed {amount} tokens. Remaining balance: {self.token_balance} tokens.")

class ActivityTracker:
    """Class responsible for tracking user activities and rewarding tokens."""
    
    def __init__(self):
        """Initialize the activity tracker."""
        self.activities = []
    
    def log_activity(self, user, activity, duration):
        """Log an activity and reward the user with tokens based on duration."""
        # Simulating activity points based on duration (1 point per minute)
        activity_points = duration
        self.activities.append((user.username, activity, duration))
        print(f"Logged activity: {user.username} did {activity} for {duration} minutes.")
        user.earn_tokens(activity_points)

def main():
    """Main function to run the Move to Earn program."""
    try:
        # Create users
        alice = User("Alice")
        bob = User("Bob")
        
        # Create an activity tracker
        tracker = ActivityTracker()
        
        # Simulate activities
        tracker.log_activity(alice, "running", 30)  # Alice runs for 30 minutes
        tracker.log_activity(bob, "cycling", 25)    # Bob cycles for 25 minutes
        tracker.log_activity(alice, "walking", 15)  # Alice walks for 15 minutes
        
        # Redeem tokens
        alice.redeem_tokens(3)  # Alice attempts to redeem 3 tokens
        bob.redeem_tokens(1)     # Bob attempts to redeem 1 token
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
