"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-8g6.pages.dev
Prompt: Implement a rewards system for a cryptocurrency portfolio community, similar to the rewards functionality described on the Common Wealth website.
Generated: DETERMINISTIC_7d599fb41e3ba4b3
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the cryptocurrency portfolio community.
    """
    def __init__(self, username, initial_balance=0):
        self.username = username
        self.balance = initial_balance
        self.rewards = 0

    def add_balance(self, amount):
        """
        Adds to the user's balance.
        :param amount: The amount to add to the user's balance.
        """
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def redeem_rewards(self, amount):
        """
        Redeems the user's rewards.
        :param amount: The amount of rewards to redeem.
        :raises ValueError: If the amount exceeds current rewards.
        """
        if amount > self.rewards:
            raise ValueError("Insufficient rewards to redeem.")
        self.rewards -= amount

    def earn_rewards(self, amount):
        """
        Increases the user's rewards by the specified amount.
        :param amount: The amount of rewards to earn.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.rewards += amount

class RewardsSystem:
    """
    Manages rewards for users in the cryptocurrency portfolio community.
    """
    def __init__(self):
        self.users = {}

    def register_user(self, username, initial_balance=0):
        """
        Registers a new user to the rewards system.
        :param username: The username of the new user.
        :param initial_balance: The initial balance of the new user.
        :raises ValueError: If the username is already taken.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, initial_balance)

    def add_balance_to_user(self, username, amount):
        """
        Adds balance to a specified user.
        :param username: The username of the user.
        :param amount: The amount to add to the user's balance.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        self.users[username].add_balance(amount)

    def distribute_rewards(self, username, amount):
        """
        Distributes rewards to a specified user.
        :param username: The username of the user.
        :param amount: The amount of rewards to distribute.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        self.users[username].earn_rewards(amount)

    def redeem_user_rewards(self, username, amount):
        """
        Redeems rewards for a specified user.
        :param username: The username of the user.
        :param amount: The amount of rewards to redeem.
        :raises KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        self.users[username].redeem_rewards(amount)

# Example Usage:
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    try:
        rewards_system.register_user("alice", 100)
        rewards_system.distribute_rewards("alice", 50)
        rewards_system.add_balance_to_user("alice", 20)
        rewards_system.redeem_user_rewards("alice", 30)

        print(f"User: {rewards_system.users['alice'].username}")
        print(f"Balance: {rewards_system.users['alice'].balance}")
        print(f"Rewards: {rewards_system.users['alice'].rewards}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
