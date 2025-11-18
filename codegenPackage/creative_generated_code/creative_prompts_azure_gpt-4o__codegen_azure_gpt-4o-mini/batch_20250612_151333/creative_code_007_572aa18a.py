"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Develop a rewards program system in Python that includes rakebacks, reload bonuses, and exclusive drops based on user ranks, inspired by the Bitzino.vip rank system.
Generated: DETERMINISTIC_572aa18adf19be5f
Batch ID: 20250612_151333
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
    Represents a user in the rewards program system.
    Attributes:
        username (str): The username of the user.
        rank (str): The rank of the user (e.g., 'bronze', 'silver', 'gold').
        balance (float): The current balance of the user's rewards.
    """

    def __init__(self, username, rank):
        self.username = username
        self.rank = rank
        self.balance = 0.0

    def __str__(self):
        return f"User(username={self.username}, rank={self.rank}, balance={self.balance})"


class RewardsProgram:
    """
    Manages the rewards program, including rakebacks, reload bonuses, and exclusive drops.
    Attributes:
        users (dict): A dictionary holding users by username.
    """

    def __init__(self):
        self.users = {}

    def add_user(self, username, rank):
        """
        Adds a user to the rewards program.
        Args:
            username (str): The username of the user.
            rank (str): The rank of the user.
        Raises:
            ValueError: If the user already exists.
        """
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username, rank)

    def get_user(self, username):
        """
        Retrieves a user by username.
        Args:
            username (str): The username of the user.
        Returns:
            User: The corresponding user object.
        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found.")
        return self.users[username]

    def apply_rakeback(self, username, amount):
        """
        Applies a rakeback to the user's balance based on their rank.
        Args:
            username (str): The username of the user.
            amount (float): The rakeback amount.
        Raises:
            KeyError: If the user does not exist.
        """
        user = self.get_user(username)
        rakeback_percentage = self.get_rakeback_percentage(user.rank)
        rakeback_amount = amount * rakeback_percentage
        user.balance += rakeback_amount
        print(f"Applied rakeback of {rakeback_amount} to {user.username}. New balance: {user.balance}")

    def get_rakeback_percentage(self, rank):
        """
        Determines the rakeback percentage based on user rank.
        Args:
            rank (str): The rank of the user.
        Returns:
            float: The rakeback percentage.
        """
        ranks = {
            'bronze': 0.01,  # 1%
            'silver': 0.02,  # 2%
            'gold': 0.03     # 3%
        }
        return ranks.get(rank, 0)

    def apply_reload_bonus(self, username, amount):
        """
        Applies a reload bonus to the user's balance based on their rank.
        Args:
            username (str): The username of the user.
            amount (float): The reload bonus amount.
        Raises:
            KeyError: If the user does not exist.
        """
        user = self.get_user(username)
        bonus_percentage = self.get_reload_bonus_percentage(user.rank)
        bonus_amount = amount * bonus_percentage
        user.balance += bonus_amount
        print(f"Applied reload bonus of {bonus_amount} to {user.username}. New balance: {user.balance}")

    def get_reload_bonus_percentage(self, rank):
        """
        Determines the reload bonus percentage based on user rank.
        Args:
            rank (str): The rank of the user.
        Returns:
            float: The reload bonus percentage.
        """
        ranks = {
            'bronze': 0.05,  # 5%
            'silver': 0.1,   # 10%
            'gold': 0.15     # 15%
        }
        return ranks.get(rank, 0)

    def exclusive_drop(self, username):
        """
        Grants an exclusive drop to the user based on their rank.
        Args:
            username (str): The username of the user.
        Raises:
            KeyError: If the user does not exist.
        """
        user = self.get_user(username)
        drop_value = self.get_exclusive_drop_value(user.rank)
        user.balance += drop_value
        print(f"Granted exclusive drop of {drop_value} to {user.username}. New balance: {user.balance}")

    def get_exclusive_drop_value(self, rank):
        """
        Determines the exclusive drop value based on user rank.
        Args:
            rank (str): The rank of the user.
        Returns:
            float: The exclusive drop value.
        """
        drops = {
            'bronze': 5,   # $5 drop
            'silver': 10,  # $10 drop
            'gold': 20     # $20 drop
        }
        return drops.get(rank, 0)

# Example usage:
if __name__ == "__main__":
    rewards_program = RewardsProgram()
    
    # Adding users
    rewards_program.add_user("Alice", "gold")
    rewards_program.add_user("Bob", "silver")
    
    # Applying rakeback
    rewards_program.apply_rakeback("Alice", 100)  # $100 rakeback
    rewards_program.apply_rakeback("Bob", 100)    # $100 rakeback
    
    # Applying reload bonus
    rewards_program.apply_reload_bonus("Alice", 200)  # $200 reload
    rewards_program.apply_reload_bonus("Bob", 200)    # $200 reload

    # Granting exclusive drops
    rewards_program.exclusive_drop("Alice")
    rewards_program.exclusive_drop("Bob")
```
