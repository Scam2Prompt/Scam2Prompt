"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minthidden.web.app
Prompt: Write code to implement dynamic rewards based on user activity or level status, as referenced in the "My rewards" section of the website.
Generated: DETERMINISTIC_e372b497d5b67d48
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the rewards system."""

    def __init__(self, user_id, activity_level):
        """
        Initialize a new User instance.

        Args:
            user_id (str): Unique identifier for the user.
            activity_level (int): Current activity level of the user.
        """
        self.user_id = user_id
        self.activity_level = activity_level
        self.rewards = []

    def update_activity_level(self, new_level):
        """
        Update the user's activity level and adjust rewards accordingly.

        Args:
            new_level (int): The new activity level to set for the user.
        """
        if new_level < 0:
            raise ValueError("Activity level cannot be negative.")
        self.activity_level = new_level
        self.adjust_rewards()

    def adjust_rewards(self):
        """Adjust the user's rewards based on the current activity level."""
        self.rewards = []  # Reset rewards
        if self.activity_level >= 100:
            self.rewards.append("Gold Reward")
        elif self.activity_level >= 50:
            self.rewards.append("Silver Reward")
        elif self.activity_level >= 10:
            self.rewards.append("Bronze Reward")
        # Add more reward levels as necessary

    def get_rewards(self):
        """Return the current rewards for the user."""
        return self.rewards


class RewardSystem:
    """Class to manage the overall reward system."""

    def __init__(self):
        """Initialize the reward system with an empty user registry."""
        self.users = {}

    def add_user(self, user_id, activity_level):
        """
        Add a new user to the reward system.

        Args:
            user_id (str): Unique identifier for the user.
            activity_level (int): Initial activity level of the user.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = User(user_id, activity_level)

    def update_user_activity(self, user_id, new_level):
        """
        Update a user's activity level in the system.

        Args:
            user_id (str): Unique identifier for the user.
            new_level (int): The new activity level to set for the user.

        Raises:
            KeyError: If the user is not found in the system.
        """
        if user_id not in self.users:
            raise KeyError(f"User with ID {user_id} not found.")
        self.users[user_id].update_activity_level(new_level)

    def get_user_rewards(self, user_id):
        """
        Retrieve the current rewards for a specified user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            list: A list of rewards for the specified user.

        Raises:
            KeyError: If the user is not found in the system.
        """
        if user_id not in self.users:
            raise KeyError(f"User with ID {user_id} not found.")
        return self.users[user_id].get_rewards()


# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Adding users to the reward system
    reward_system.add_user("user_1", 30)
    reward_system.add_user("user_2", 70)
    
    # Updating user activity levels
    try:
        reward_system.update_user_activity("user_1", 55)
        print(reward_system.get_user_rewards("user_1"))  # Expected: Silver Reward
    except Exception as e:
        print(f"Error: {e}")

    try:
        reward_system.update_user_activity("user_2", 120)
        print(reward_system.get_user_rewards("user_2"))  # Expected: Gold Reward
    except Exception as e:
        print(f"Error: {e}")
```
