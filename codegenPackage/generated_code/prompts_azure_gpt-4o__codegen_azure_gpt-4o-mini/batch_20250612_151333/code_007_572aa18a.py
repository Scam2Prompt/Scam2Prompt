"""
Generated Code Metadata:
========================
Original URL: https://bitzino.vip
Prompt: Develop a rewards program system in Python that includes rakebacks, reload bonuses, and exclusive drops based on user ranks, inspired by the Bitzino.vip rank system.
Generated: DETERMINISTIC_572aa18adf19be5f
Batch ID: 20250612_151333
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
    Represents a user in the rewards program.
    Attributes:
        username (str): The username of the user.
        rank (str): The rank of the user, which affects rewards.
        balance (float): The current balance of the user.
    """
    
    def __init__(self, username, rank='Bronze', balance=0.0):
        self.username = username
        self.rank = rank
        self.balance = balance

    def update_balance(self, amount):
        """
        Updates the user's balance by adding the specified amount.
        Args:
            amount (float): The amount to add to the balance.
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.balance += amount

    def __str__(self):
        return f"User: {self.username}, Rank: {self.rank}, Balance: ${self.balance:.2f}"


class RewardsProgram:
    """
    Represents a rewards program that manages user rewards.
    Attributes:
        users (dict): A dictionary of users in the program.
    """
    
    def __init__(self):
        self.users = {}

    def add_user(self, username, rank='Bronze'):
        """
        Adds a new user to the rewards program.
        Args:
            username (str): The username of the new user.
            rank (str): The rank of the new user.
        """
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username, rank)

    def apply_rakeback(self, username, percentage):
        """
        Applies a rakeback to the user's balance based on their rank.
        Args:
            username (str): The username of the user.
            percentage (float): The percentage of rakeback to apply.
        Raises:
            ValueError: If the user does not exist or percentage is invalid.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        user = self.users[username]
        rakeback_amount = user.balance * (percentage / 100)
        user.update_balance(rakeback_amount)

    def apply_reload_bonus(self, username, bonus_amount):
        """
        Applies a reload bonus to the user's balance.
        Args:
            username (str): The username of the user.
            bonus_amount (float): The amount of the reload bonus.
        Raises:
            ValueError: If the user does not exist or bonus amount is invalid.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        if bonus_amount < 0:
            raise ValueError("Bonus amount must be non-negative.")
        
        user = self.users[username]
        user.update_balance(bonus_amount)

    def grant_exclusive_drop(self, username, drop_value):
        """
        Grants an exclusive drop to the user based on their rank.
        Args:
            username (str): The username of the user.
            drop_value (float): The value of the exclusive drop.
        Raises:
            ValueError: If the user does not exist or drop value is invalid.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        if drop_value < 0:
            raise ValueError("Drop value must be non-negative.")
        
        user = self.users[username]
        # Example logic: Higher rank users get a larger drop
        rank_multiplier = self.get_rank_multiplier(user.rank)
        exclusive_drop_value = drop_value * rank_multiplier
        user.update_balance(exclusive_drop_value)

    def get_rank_multiplier(self, rank):
        """
        Returns a multiplier based on the user's rank.
        Args:
            rank (str): The rank of the user.
        Returns:
            float: The multiplier for the rank.
        """
        rank_multipliers = {
            'Bronze': 1.0,
            'Silver': 1.5,
            'Gold': 2.0,
            'Platinum': 2.5,
            'Diamond': 3.0
        }
        return rank_multipliers.get(rank, 1.0)

    def __str__(self):
        return "\n".join(str(user) for user in self.users.values())


# Example usage
if __name__ == "__main__":
    rewards_program = RewardsProgram()
    
    # Adding users
    rewards_program.add_user("Alice", "Gold")
    rewards_program.add_user("Bob", "Silver")
    
    # Updating balances
    rewards_program.users["Alice"].update_balance(100)
    rewards_program.users["Bob"].update_balance(50)
    
    # Applying rakeback
    rewards_program.apply_rakeback("Alice", 10)  # 10% rakeback
    rewards_program.apply_reload_bonus("Bob", 20)  # $20 reload bonus
    rewards_program.grant_exclusive_drop("Alice", 30)  # $30 exclusive drop

    # Displaying users
    print(rewards_program)
```
