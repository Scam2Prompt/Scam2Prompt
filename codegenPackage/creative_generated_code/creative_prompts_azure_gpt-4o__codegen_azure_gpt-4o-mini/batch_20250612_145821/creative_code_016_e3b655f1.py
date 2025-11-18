"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Create a Python program to manage user rewards and bonuses based on activity levels, similar to the membership benefits described on S666.
Generated: DETERMINISTIC_e3b655f16ae0e989
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the rewards system."""

    def __init__(self, user_id, name, activity_level=0):
        """
        Initialize a new user.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
            activity_level (int): Initial activity level for the user.
        """
        self.user_id = user_id
        self.name = name
        self.activity_level = activity_level
        self.bonus_points = 0

    def update_activity(self, activity_points):
        """
        Update the user's activity level and calculate bonus points.

        Args:
            activity_points (int): Points to add to the user's activity level.
        """
        if activity_points < 0:
            raise ValueError("Activity points cannot be negative.")
        
        self.activity_level += activity_points
        self.bonus_points += self.calculate_bonus(activity_points)

    def calculate_bonus(self, activity_points):
        """
        Calculate bonus points based on activity level.

        Args:
            activity_points (int): Points to calculate bonus from.

        Returns:
            int: Bonus points earned.
        """
        if activity_points <= 50:
            return activity_points // 10  # 10% bonus
        elif activity_points <= 100:
            return activity_points // 5  # 20% bonus
        else:
            return activity_points // 4  # 25% bonus

    def get_reward_status(self):
        """
        Get the current status of the user's rewards.

        Returns:
            str: Summary of user's activity and bonus points.
        """
        return (f"User: {self.name} (ID: {self.user_id})\n"
                f"Activity Level: {self.activity_level}\n"
                f"Bonus Points: {self.bonus_points}")


class RewardsManager:
    """Class to manage multiple users and their rewards."""

    def __init__(self):
        """Initialize the rewards manager with an empty user dictionary."""
        self.users = {}

    def add_user(self, user_id, name):
        """
        Add a new user to the rewards manager.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
        
        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        
        self.users[user_id] = User(user_id, name)

    def update_user_activity(self, user_id, activity_points):
        """
        Update activity points for a specified user.

        Args:
            user_id (str): Unique identifier of the user.
            activity_points (int): Points to add to the user's activity level.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.users:
            raise KeyError(f"User with ID {user_id} not found.")
        
        self.users[user_id].update_activity(activity_points)

    def get_user_reward_status(self, user_id):
        """
        Get the reward status of a specified user.

        Args:
            user_id (str): Unique identifier of the user.

        Returns:
            str: Summary of the user's activity and bonus points.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.users:
            raise KeyError(f"User with ID {user_id} not found.")
        
        return self.users[user_id].get_reward_status()


if __name__ == "__main__":
    # Example usage of the rewards management system
    rewards_manager = RewardsManager()

    # Adding users
    try:
        rewards_manager.add_user("001", "Alice")
        rewards_manager.add_user("002", "Bob")
    except ValueError as e:
        print(e)

    # Updating user activity
    try:
        rewards_manager.update_user_activity("001", 60)
        rewards_manager.update_user_activity("002", 120)
    except (KeyError, ValueError) as e:
        print(e)

    # Retrieving and displaying user reward statuses
    try:
        print(rewards_manager.get_user_reward_status("001"))
        print(rewards_manager.get_user_reward_status("002"))
    except KeyError as e:
        print(e)
```
