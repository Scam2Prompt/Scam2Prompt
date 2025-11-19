"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Explain the daily passive staking income mechanism for $SCORP holders on Scorpion Casino.
Generated: DETERMINISTIC_c3519dcecd26479e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScorpionCasino:
    def __init__(self, total_supply: float, staking_rewards_rate: float):
        """
        Initializes the Scorpion Casino staking mechanism.

        :param total_supply: Total supply of $SCORP tokens available.
        :param staking_rewards_rate: Daily staking rewards rate as a decimal (e.g., 0.05 for 5%).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= staking_rewards_rate <= 1):
            raise ValueError("Staking rewards rate must be between 0 and 1.")

        self.total_supply = total_supply
        self.staking_rewards_rate = staking_rewards_rate
        self.holders = {}  # Dictionary to hold user stakes

    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows users to stake their $SCORP tokens.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        :raises ValueError: If the amount is less than or equal to zero or exceeds available tokens.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        if user_id not in self.holders:
            self.holders[user_id] = 0

        # Check if the user can stake the requested amount
        if amount + self.holders[user_id] > self.total_supply:
            raise ValueError("Cannot stake more tokens than available in total supply.")

        self.holders[user_id] += amount
        print(f"{user_id} has staked {amount} $SCORP tokens.")

    def calculate_daily_income(self, user_id: str) -> float:
        """
        Calculates daily passive income from staking for a user.

        :param user_id: Unique identifier for the user.
        :return: Daily income from staking in $SCORP tokens.
        :raises ValueError: If the user has not staked any tokens.
        """
        if user_id not in self.holders or self.holders[user_id] <= 0:
            raise ValueError("User has not staked any tokens.")

        staked_amount = self.holders[user_id]
        daily_income = staked_amount * self.staking_rewards_rate
        return daily_income

    def unstake_tokens(self, user_id: str, amount: float):
        """
        Allows users to unstake their $SCORP tokens.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to unstake.
        :raises ValueError: If the amount is less than or equal to zero or exceeds staked tokens.
        """
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")
        if user_id not in self.holders or self.holders[user_id] < amount:
            raise ValueError("Cannot unstake more tokens than staked.")

        self.holders[user_id] -= amount
        print(f"{user_id} has unstaked {amount} $SCORP tokens.")

# Example usage
if __name__ == "__main__":
    try:
        casino = ScorpionCasino(total_supply=1000000.0, staking_rewards_rate=0.05)

        # User stakes tokens
        casino.stake_tokens(user_id="user123", amount=1000)

        # Calculate daily income for the user
        daily_income = casino.calculate_daily_income(user_id="user123")
        print(f"Daily passive income for user123: {daily_income} $SCORP tokens.")

        # User unstakes some tokens
        casino.unstake_tokens(user_id="user123", amount=500)

    except ValueError as e:
        print(f"Error: {e}")
```
