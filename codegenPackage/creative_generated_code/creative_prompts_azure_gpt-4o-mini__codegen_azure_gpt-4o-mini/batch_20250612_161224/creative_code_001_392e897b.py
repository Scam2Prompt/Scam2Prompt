"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debugfi.pages.dev
Prompt: Write a function that implements the staking and unstaking processes for tokens, referencing the staking features mentioned in the DebugFi documentation.
Generated: DETERMINISTIC_392e897b973aa00c
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenStaking:
    def __init__(self):
        # Dictionary to hold the stake amounts for each user
        self.stakes = {}
        # Total amount of staked tokens
        self.total_staked = 0

    def stake_tokens(self, user, amount):
        """
        Stakes a specified amount of tokens for a user.

        Parameters:
        user (str): The identifier for the user
        amount (float): The amount of tokens to stake

        Raises:
        ValueError: If the amount is less than or equal to zero
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Add the amount to the user's stake
        if user in self.stakes:
            self.stakes[user] += amount
        else:
            self.stakes[user] = amount
        
        # Update the total staked amount
        self.total_staked += amount
        print(f"{user} has staked {amount} tokens. Total staked: {self.total_staked}")

    def unstake_tokens(self, user, amount):
        """
        Unstakes a specified amount of tokens for a user.

        Parameters:
        user (str): The identifier for the user
        amount (float): The amount of tokens to unstake

        Raises:
        ValueError: If the amount is less than or equal to zero or exceeds the user's stake
        KeyError: If the user has no staked tokens
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        if user not in self.stakes:
            raise KeyError("No staked tokens found for this user.")

        if amount > self.stakes[user]:
            raise ValueError("Unstake amount exceeds the amount staked.")

        # Deduct the amount from the user's stake
        self.stakes[user] -= amount
        self.total_staked -= amount

        # If the user's stake reaches zero, remove them from the stakes dictionary
        if self.stakes[user] == 0:
            del self.stakes[user]

        print(f"{user} has unstaked {amount} tokens. Total staked: {self.total_staked}")

    def get_user_stake(self, user):
        """
        Returns the amount of staked tokens for a specific user.

        Parameters:
        user (str): The identifier for the user

        Returns:
        float: The amount of tokens staked by the user

        Raises:
        KeyError: If the user has no staked tokens
        """
        if user not in self.stakes:
            raise KeyError("No staked tokens found for this user.")
        
        return self.stakes[user]

    def get_total_staked(self):
        """
        Returns the total amount of staked tokens.

        Returns:
        float: Total amount of staked tokens
        """
        return self.total_staked
```
