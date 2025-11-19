"""
Generated Code Metadata:
========================
Original URL: https://daos-world-wl.pages.dev
Prompt: Provide a step-by-step guide to implement a rewards system for users participating in AI hedge funds, inspired by the daos.world platform.
Generated: DETERMINISTIC_c2fd685d31cfcb7e
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_system.py

class User:
    """Class representing a user in the rewards system."""
    
    def __init__(self, user_id, name):
        """
        Initialize a new user.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        """
        self.user_id = user_id
        self.name = name
        self.rewards_points = 0

    def add_rewards(self, points):
        """
        Add rewards points to the user.

        :param points: Number of points to add
        :raises ValueError: If points are negative
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.rewards_points += points

    def redeem_rewards(self, points):
        """
        Redeem rewards points from the user.

        :param points: Number of points to redeem
        :raises ValueError: If points are negative or exceed available points
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        if points > self.rewards_points:
            raise ValueError("Insufficient rewards points.")
        self.rewards_points -= points

class RewardsSystem:
    """Class to manage the rewards system for users."""
    
    def __init__(self):
        """Initialize the rewards system with an empty user list."""
        self.users = {}

    def add_user(self, user_id, name):
        """
        Add a new user to the rewards system.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :raises ValueError: If user already exists
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id, name)

    def add_rewards(self, user_id, points):
        """
        Add rewards points to a user.

        :param user_id: Unique identifier for the user
        :param points: Number of points to add
        :raises ValueError: If user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].add_rewards(points)

    def redeem_rewards(self, user_id, points):
        """
        Redeem rewards points for a user.

        :param user_id: Unique identifier for the user
        :param points: Number of points to redeem
        :raises ValueError: If user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].redeem_rewards(points)

    def get_user_rewards(self, user_id):
        """
        Get the current rewards points for a user.

        :param user_id: Unique identifier for the user
        :return: Current rewards points
        :raises ValueError: If user does not exist
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].rewards_points

# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()
    
    # Adding users
    try:
        rewards_system.add_user(1, "Alice")
        rewards_system.add_user(2, "Bob")
        
        # Adding rewards
        rewards_system.add_rewards(1, 100)
        rewards_system.add_rewards(2, 150)
        
        # Redeeming rewards
        rewards_system.redeem_rewards(1, 50)
        
        # Checking rewards
        print(f"Alice's rewards: {rewards_system.get_user_rewards(1)}")  # Output: 50
        print(f"Bob's rewards: {rewards_system.get_user_rewards(2)}")    # Output: 150
        
    except ValueError as e:
        print(f"Error: {e}")
```
