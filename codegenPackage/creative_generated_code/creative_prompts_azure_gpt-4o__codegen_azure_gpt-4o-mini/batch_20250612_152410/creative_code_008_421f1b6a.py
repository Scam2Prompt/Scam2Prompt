"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getxter.pages.dev
Prompt: Write code to implement a rewards system in a mobile game that incentivizes user activity, based on PlayEmber's focus on making games more rewarding.
Generated: DETERMINISTIC_421f1b6aaf71d0d0
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class RewardsSystem:
    """
    A class to manage a rewards system in a mobile game,
    incentivizing user activity based on various actions.
    """

    def __init__(self):
        """
        Initializes the RewardsSystem with default values.
        """
        self.user_rewards = {}
        self.reward_points = 0

    def register_user(self, user_id):
        """
        Registers a new user into the rewards system.

        :param user_id: Unique identifier for the user
        :raises ValueError: If the user is already registered
        """
        if user_id in self.user_rewards:
            raise ValueError("User already registered.")
        self.user_rewards[user_id] = 0

    def add_activity(self, user_id, activity_type):
        """
        Adds activity points to the user's rewards based on activity type.

        :param user_id: Unique identifier for the user
        :param activity_type: Type of activity performed by the user
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.user_rewards:
            raise ValueError("User not registered.")

        # Define reward points for each activity type
        activity_rewards = {
            'daily_login': 10,
            'level_up': 50,
            'challenge_completed': 30,
            'in_game_purchase': 100
        }

        if activity_type in activity_rewards:
            self.user_rewards[user_id] += activity_rewards[activity_type]
            print(f"Added {activity_rewards[activity_type]} points to user {user_id}.")
        else:
            raise ValueError("Invalid activity type.")

    def get_user_points(self, user_id):
        """
        Retrieves the total reward points for a registered user.

        :param user_id: Unique identifier for the user
        :return: Total reward points for the user
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.user_rewards:
            raise ValueError("User not registered.")
        return self.user_rewards[user_id]

    def redeem_points(self, user_id, points):
        """
        Redeems a specified number of points for the user.

        :param user_id: Unique identifier for the user
        :param points: Number of points to redeem
        :raises ValueError: If the user is not registered or if points exceed available balance
        """
        if user_id not in self.user_rewards:
            raise ValueError("User not registered.")
        if points > self.user_rewards[user_id]:
            raise ValueError("Insufficient reward points.")

        self.user_rewards[user_id] -= points
        print(f"User {user_id} redeemed {points} points. Remaining points: {self.user_rewards[user_id]}.")

# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Register users
    try:
        rewards_system.register_user("user1")
        rewards_system.register_user("user2")
    except ValueError as e:
        print(e)

    # Add activities
    try:
        rewards_system.add_activity("user1", "daily_login")
        rewards_system.add_activity("user1", "level_up")
        rewards_system.add_activity("user2", "challenge_completed")
    except ValueError as e:
        print(e)

    # Get user points
    try:
        print(f"User1 points: {rewards_system.get_user_points('user1')}")
        print(f"User2 points: {rewards_system.get_user_points('user2')}")
    except ValueError as e:
        print(e)

    # Redeem points
    try:
        rewards_system.redeem_points("user1", 20)
    except ValueError as e:
        print(e)
```
