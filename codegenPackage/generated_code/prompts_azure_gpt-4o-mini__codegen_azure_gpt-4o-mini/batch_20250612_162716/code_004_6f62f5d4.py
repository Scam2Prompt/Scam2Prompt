"""
Generated Code Metadata:
========================
Original URL: https://stelth-mint.web.app
Prompt: Illustrate how to implement a rewards system for users based on their level status and items owned within the Stelth Mint ecosystem.
Generated: DETERMINISTIC_6f62f5d4f31ce460
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the Stelth Mint ecosystem.
    Each user has a level status and a list of owned items.
    """

    def __init__(self, username, level=1):
        """
        Initializes a new user with a username and an optional level.
        
        :param username: The username of the user.
        :param level: The level of the user (default is 1).
        """
        self.username = username
        self.level = level
        self.owned_items = []

    def add_item(self, item):
        """
        Adds an item to the user's owned items.
        
        :param item: The item to be added.
        """
        self.owned_items.append(item)

    def get_rewards(self):
        """
        Calculates rewards based on the user's level and owned items.
        
        :return: A dictionary containing the rewards.
        """
        rewards = {
            'points': self.level * 10,
            'bonus_items': self.level // 2,
            'special_access': self.level >= 5
        }

        # Additional rewards based on owned items
        if len(self.owned_items) > 5:
            rewards['extra_points'] = 20
        else:
            rewards['extra_points'] = 0

        return rewards


class RewardsSystem:
    """
    Manages the rewards system for users in the Stelth Mint ecosystem.
    """

    def __init__(self):
        """
        Initializes the rewards system with an empty user list.
        """
        self.users = {}

    def register_user(self, username, level=1):
        """
        Registers a new user in the rewards system.
        
        :param username: The username of the user.
        :param level: The level of the user (default is 1).
        :raises ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, level)

    def add_item_to_user(self, username, item):
        """
        Adds an item to a user's owned items.
        
        :param username: The username of the user.
        :param item: The item to be added.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        self.users[username].add_item(item)

    def get_user_rewards(self, username):
        """
        Retrieves the rewards for a specific user.
        
        :param username: The username of the user.
        :return: A dictionary containing the user's rewards.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        return self.users[username].get_rewards()


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Register users
    try:
        rewards_system.register_user("Alice", level=3)
        rewards_system.register_user("Bob", level=5)

        # Add items to users
        rewards_system.add_item_to_user("Alice", "Item1")
        rewards_system.add_item_to_user("Alice", "Item2")
        rewards_system.add_item_to_user("Alice", "Item3")
        rewards_system.add_item_to_user("Alice", "Item4")
        rewards_system.add_item_to_user("Alice", "Item5")
        rewards_system.add_item_to_user("Alice", "Item6")

        # Get rewards
        alice_rewards = rewards_system.get_user_rewards("Alice")
        bob_rewards = rewards_system.get_user_rewards("Bob")

        print(f"Alice's Rewards: {alice_rewards}")
        print(f"Bob's Rewards: {bob_rewards}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
