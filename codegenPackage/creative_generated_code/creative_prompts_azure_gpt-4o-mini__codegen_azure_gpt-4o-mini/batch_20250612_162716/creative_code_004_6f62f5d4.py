"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelth-mint.web.app
Prompt: Illustrate how to implement a rewards system for users based on their level status and items owned within the Stelth Mint ecosystem.
Generated: DETERMINISTIC_6f62f5d4f31ce460
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, user_id, level, items_owned):
        """
        Initialize a new User instance.

        :param user_id: Unique identifier for the user
        :param level: Current level of the user
        :param items_owned: List of items owned by the user
        """
        self.user_id = user_id
        self.level = level
        self.items_owned = items_owned
    
    def calculate_rewards(self):
        """
        Calculate rewards based on the user's level and items owned.

        :return: Total reward points
        """
        base_reward = 10
        level_multiplier = self.level * 2
        item_bonus = len(self.items_owned) * 5
        
        total_rewards = base_reward + level_multiplier + item_bonus
        return total_rewards

class RewardSystem:
    def __init__(self):
        """
        Initialize the RewardSystem instance.
        """
        self.users = {}

    def add_user(self, user_id, level, items_owned):
        """
        Add a new user to the rewards system.

        :param user_id: Unique identifier for the user
        :param level: Current level of the user
        :param items_owned: List of items owned by the user
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        
        self.users[user_id] = User(user_id, level, items_owned)

    def calculate_user_rewards(self, user_id):
        """
        Calculate rewards for a given user.

        :param user_id: Unique identifier for the user
        :return: Total reward points or error message
        """
        if user_id not in self.users:
            return f"User with ID {user_id} does not exist."
        
        user = self.users[user_id]
        return user.calculate_rewards()

    def display_all_rewards(self):
        """
        Display rewards for all users in the system.
        """
        for user_id, user in self.users.items():
            rewards = user.calculate_rewards()
            print(f"User ID: {user_id}, Level: {user.level}, Items Owned: {len(user.items_owned)}, Rewards: {rewards}")

# Example usage
if __name__ == "__main__":
    try:
        reward_system = RewardSystem()
        
        # Adding users
        reward_system.add_user("user1", 1, ["item1", "item2"])
        reward_system.add_user("user2", 3, ["item3", "item4", "item5"])
        
        # Calculating rewards for a specific user
        print(reward_system.calculate_user_rewards("user1"))  # Should print the reward points for user1
        
        # Displaying all rewards in the system
        reward_system.display_all_rewards()
        
    except ValueError as e:
        print(f"Error: {e}")
```
