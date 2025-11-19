"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Explain how the transparent reward tracking system works in MELLSTROY and how it can benefit users.
Generated: DETERMINISTIC_79e1a9875d9b1eb9
Batch ID: 20250612_160503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardTracker:
    """
    A class to track rewards transparently in the MELLSTROY system.
    
    Attributes:
        user_rewards (dict): A dictionary to store users and their respective rewards.
    """

    def __init__(self):
        """Initializes the RewardTracker with an empty reward dictionary."""
        self.user_rewards = {}

    def add_user(self, user_id):
        """
        Adds a new user to the reward tracking system.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user already exists in the system.
        """
        if user_id in self.user_rewards:
            raise ValueError(f"User {user_id} already exists.")
        self.user_rewards[user_id] = 0  # Initialize rewards to 0 for the new user

    def add_reward(self, user_id, amount):
        """
        Adds a reward amount to a user's total rewards.
        
        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of reward to add.
        
        Raises:
            ValueError: If the user does not exist or amount is negative.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} not found.")
        if amount < 0:
            raise ValueError("Reward amount must be non-negative.")
        
        self.user_rewards[user_id] += amount  # Update the user's reward

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            float: The total rewards for the user.
        
        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} not found.")
        
        return self.user_rewards[user_id]

    def display_rewards(self):
        """
        Displays the total rewards for all users in the system.
        """
        for user_id, rewards in self.user_rewards.items():
            print(f"User ID: {user_id}, Total Rewards: {rewards}")


# Example usage:
if __name__ == "__main__":
    try:
        tracker = RewardTracker()
        tracker.add_user("user1")
        tracker.add_reward("user1", 100)
        tracker.add_reward("user1", 50)
        print(tracker.get_user_rewards("user1"))  # Should print 150
        tracker.display_rewards()
    except ValueError as e:
        print(f"Error: {e}")
```
