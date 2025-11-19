"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Write code to implement a rewards system in a mobile game that incentivizes user activity, based on PlayEmber's focus on making games more rewarding.
Generated: DETERMINISTIC_421f1b6aaf71d0d0
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RewardsSystem:
    """
    A class to represent a rewards system for a mobile game.
    
    Attributes
    ----------
    user_rewards : dict
        A dictionary to store user IDs and their corresponding rewards points.
    activity_threshold : int
        The minimum activity level required to earn rewards.
    reward_points : int
        The number of points awarded for each activity.
    """

    def __init__(self, activity_threshold=10, reward_points=100):
        """
        Initializes the RewardsSystem with specified thresholds and points.
        
        Parameters
        ----------
        activity_threshold : int, optional
            The minimum activity level required to earn rewards (default is 10).
        reward_points : int, optional
            The number of points awarded for each activity (default is 100).
        """
        self.user_rewards = {}
        self.activity_threshold = activity_threshold
        self.reward_points = reward_points

    def add_user(self, user_id):
        """
        Adds a new user to the rewards system.
        
        Parameters
        ----------
        user_id : str
            The unique identifier for the user.
        
        Raises
        ------
        ValueError
            If the user ID already exists in the system.
        """
        if user_id in self.user_rewards:
            raise ValueError(f"User ID {user_id} already exists.")
        self.user_rewards[user_id] = 0

    def record_activity(self, user_id, activity_level):
        """
        Records user activity and awards rewards if the activity level meets the threshold.
        
        Parameters
        ----------
        user_id : str
            The unique identifier for the user.
        activity_level : int
            The level of activity performed by the user.
        
        Raises
        ------
        KeyError
            If the user ID does not exist in the system.
        ValueError
            If the activity level is negative.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User ID {user_id} not found.")
        if activity_level < 0:
            raise ValueError("Activity level cannot be negative.")

        # Check if the user meets the activity threshold
        if activity_level >= self.activity_threshold:
            self.user_rewards[user_id] += self.reward_points
            print(f"User {user_id} rewarded {self.reward_points} points for activity level {activity_level}.")
        else:
            print(f"User {user_id} did not meet the activity threshold. No rewards given.")

    def get_rewards(self, user_id):
        """
        Retrieves the total rewards points for a user.
        
        Parameters
        ----------
        user_id : str
            The unique identifier for the user.
        
        Returns
        -------
        int
            The total rewards points for the user.
        
        Raises
        ------
        KeyError
            If the user ID does not exist in the system.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User ID {user_id} not found.")
        return self.user_rewards[user_id]

    def reset_rewards(self, user_id):
        """
        Resets the rewards points for a user to zero.
        
        Parameters
        ----------
        user_id : str
            The unique identifier for the user.
        
        Raises
        ------
        KeyError
            If the user ID does not exist in the system.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User ID {user_id} not found.")
        self.user_rewards[user_id] = 0
        print(f"Rewards for user {user_id} have been reset.")

# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Adding users
    rewards_system.add_user("user123")
    rewards_system.add_user("user456")

    # Recording activities
    rewards_system.record_activity("user123", 15)  # Should reward points
    rewards_system.record_activity("user456", 5)   # Should not reward points

    # Getting rewards
    print(f"User123 Rewards: {rewards_system.get_rewards('user123')}")
    print(f"User456 Rewards: {rewards_system.get_rewards('user456')}")

    # Resetting rewards
    rewards_system.reset_rewards("user123")
    print(f"User123 Rewards after reset: {rewards_system.get_rewards('user123')}")
```
