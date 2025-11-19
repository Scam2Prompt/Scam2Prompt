"""
Generated Code Metadata:
========================
Original URL: https://minnimi.com.ua
Prompt: Design a system to implement a loyalty program for Slots City, tracking user activity and rewarding them with bonuses, free spins, and other perks.
Generated: DETERMINISTIC_a9d79dee73926c81
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class User:
    """Class representing a user in the loyalty program."""
    
    def __init__(self, username: str):
        self.user_id: str = str(uuid.uuid4())  # Unique identifier for the user
        self.username: str = username
        self.points: int = 0  # Loyalty points
        self.activity_log: List[Dict[str, str]] = []  # Log of user activities
        self.rewards: List[str] = []  # List of rewards earned

    def add_activity(self, activity: str, points: int):
        """Add user activity and corresponding points."""
        self.activity_log.append({
            'activity': activity,
            'points': points,
            'timestamp': datetime.now().isoformat()
        })
        self.points += points

    def redeem_reward(self, reward: str) -> bool:
        """Redeem a reward if enough points are available."""
        if self.points >= 100:  # Assuming 100 points are needed for a reward
            self.points -= 100
            self.rewards.append(reward)
            return True
        return False

class LoyaltyProgram:
    """Class to manage the loyalty program for Slots City."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user_id

    def register_user(self, username: str) -> User:
        """Register a new user in the loyalty program."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[user.user_id] = user
        return user

    def record_activity(self, user_id: str, activity: str, points: int):
        """Record user activity and award points."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        user.add_activity(activity, points)

    def get_user_info(self, user_id: str) -> Optional[Dict[str, any]]:
        """Retrieve user information including points and rewards."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        return {
            'username': user.username,
            'points': user.points,
            'rewards': user.rewards,
            'activity_log': user.activity_log
        }

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Register a new user
    try:
        user = loyalty_program.register_user("john_doe")
        print(f"Registered user: {user.username} with ID: {user.user_id}")
        
        # Record some activities
        loyalty_program.record_activity(user.user_id, "Played Slot Game", 50)
        loyalty_program.record_activity(user.user_id, "Redeemed Free Spin", 30)
        
        # Get user info
        user_info = loyalty_program.get_user_info(user.user_id)
        print(user_info)
        
        # Redeem a reward
        if user.redeem_reward("Free Spin"):
            print("Reward redeemed successfully.")
        else:
            print("Not enough points to redeem reward.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
