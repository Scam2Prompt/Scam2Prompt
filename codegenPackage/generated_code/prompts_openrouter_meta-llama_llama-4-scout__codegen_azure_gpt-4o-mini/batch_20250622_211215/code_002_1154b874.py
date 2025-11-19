"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: "Design a programmatic rewards system on Farcaster using Moxie, including rewards for referrals and follower actions."
Generated: DETERMINISTIC_1154b874ca8d3fb9
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, List, Optional

class User:
    """Class representing a user in the rewards system."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.followers: List[str] = []  # List of follower user IDs
        self.referrals: List[str] = []   # List of referred user IDs
        self.reward_points: int = 0       # Total reward points

    def add_follower(self, follower_id: str):
        """Add a follower to the user's follower list."""
        if follower_id not in self.followers:
            self.followers.append(follower_id)
            self.reward_points += 10  # Reward for gaining a follower
            print(f"User {self.user_id} gained a follower: {follower_id}. Total points: {self.reward_points}")

    def refer_user(self, referred_user_id: str):
        """Add a referred user to the user's referral list."""
        if referred_user_id not in self.referrals:
            self.referrals.append(referred_user_id)
            self.reward_points += 20  # Reward for a successful referral
            print(f"User {self.user_id} referred a new user: {referred_user_id}. Total points: {self.reward_points}")

class RewardsSystem:
    """Class to manage the rewards system for users."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by user_id

    def add_user(self, user_id: str):
        """Add a new user to the rewards system."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
            print(f"User {user_id} added to the rewards system.")
        else:
            print(f"User {user_id} already exists in the rewards system.")

    def follow_user(self, follower_id: str, followed_id: str):
        """Handle the action of one user following another."""
        if follower_id in self.users and followed_id in self.users:
            self.users[followed_id].add_follower(follower_id)
        else:
            print(f"Error: One of the users does not exist. Follower: {follower_id}, Followed: {followed_id}")

    def refer_user(self, referrer_id: str, referred_user_id: str):
        """Handle the action of one user referring another user."""
        if referrer_id in self.users:
            self.users[referrer_id].refer_user(referred_user_id)
            self.add_user(referred_user_id)  # Automatically add referred user
        else:
            print(f"Error: Referrer user {referrer_id} does not exist.")

    def get_user_rewards(self, user_id: str) -> Optional[int]:
        """Retrieve the total reward points for a user."""
        if user_id in self.users:
            return self.users[user_id].reward_points
        else:
            print(f"Error: User {user_id} does not exist.")
            return None

# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()
    
    # Adding users
    rewards_system.add_user("user1")
    rewards_system.add_user("user2")
    
    # User1 refers User2
    rewards_system.refer_user("user1", "user2")
    
    # User2 follows User1
    rewards_system.follow_user("user2", "user1")
    
    # Get rewards for User1
    print(f"User1's total rewards: {rewards_system.get_user_rewards('user1')}")
    # Get rewards for User2
    print(f"User2's total rewards: {rewards_system.get_user_rewards('user2')}")
```
