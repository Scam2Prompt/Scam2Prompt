"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kon-8si.pages.dev
Prompt: Generate code to implement a feature that rewards users for being online, inspired by KonnektVPN's network device system.
Generated: DETERMINISTIC_6ca89f52944c43b4
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class UserRewardSystem:
    """
    A system to reward users for being online.
    Inspired by KonnektVPN's network device system.
    """

    def __init__(self, payout_interval_minutes=30, reward_points=10):
        """
        Initialize the reward system.

        Args:
            payout_interval_minutes (int): Minutes required to earn rewards.
            reward_points (int): Points rewarded for being online during a payout interval.
        """
        self.payout_interval = timedelta(minutes=payout_interval_minutes)
        self.reward_points = reward_points
        self.users = {}  # Stores user data in the format: {user_id: {"last_online": datetime, "points": int}}

    def user_online(self, user_id):
        """
        Call this method whenever the user is detected as online.

        Args:
            user_id (str): Unique identifier for the user.
        """
        current_time = datetime.now()
        
        # If the user is new, initialize their data
        if user_id not in self.users:
            self.users[user_id] = {
                "last_online": current_time,
                "points": 0
            }
        
        user_data = self.users[user_id]
        # Check if the user qualifies for a reward
        time_since_last_reward = current_time - user_data["last_online"]
        if time_since_last_reward >= self.payout_interval:
            # Reward the user
            user_data["points"] += self.reward_points
            user_data["last_online"] = current_time  # Update last online time

    def get_user_points(self, user_id):
        """
        Retrieve the points for a given user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: The user's current reward points, or 0 if the user doesn't exist.
        """
        return self.users.get(user_id, {}).get("points", 0)

    def display_all_users(self):
        """
        Display all users and their points for monitoring purposes.
        """
        for user_id, data in self.users.items():
            print(f"User ID: {user_id}, Points: {data['points']}, Last Online: {data['last_online']}")

if __name__ == "__main__":
    # Example usage of the UserRewardSystem
    reward_system = UserRewardSystem(payout_interval_minutes=30, reward_points=10)

    # Simulate users coming online
    reward_system.user_online("user1")
    reward_system.user_online("user2")

    # Simulate some passage of time
    time.sleep(2)  # Wait for 2 seconds (in a real application, time elapses naturally)

    reward_system.user_online("user1")  # User1 online again
    
    # Display user points
    print("User1 Points:", reward_system.get_user_points("user1"))
    print("User2 Points:", reward_system.get_user_points("user2"))

    # Display all user data for monitoring
    reward_system.display_all_users()
```
