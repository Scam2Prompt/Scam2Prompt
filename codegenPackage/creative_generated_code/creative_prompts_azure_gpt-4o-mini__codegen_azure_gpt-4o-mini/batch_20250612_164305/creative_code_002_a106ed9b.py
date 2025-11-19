"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenfi-teal.vercel.app
Prompt: Explain the process of earning rewards through staking on TokenFi, including how to choose a stake amount and duration.
Generated: DETERMINISTIC_a106ed9bca3d9e07
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenFiStaking:
    """
    A class to represent the staking process on TokenFi.
    
    Attributes:
        total_staked (float): Total amount currently staked.
        rewards_rate (float): The rate at which rewards are earned per staked token per duration.
    """

    def __init__(self, rewards_rate):
        """
        Initializes the TokenFiStaking with a specified rewards rate.

        Args:
            rewards_rate (float): The rate of rewards per token staked.
        """
        self.total_staked = 0.0
        self.rewards_rate = rewards_rate
        self.stakes = []

    def stake_tokens(self, amount, duration):
        """
        Stakes a specified amount of tokens for a given duration.

        Args:
            amount (float): The amount of tokens to stake.
            duration (int): The duration (in days) for which to stake the tokens.

        Raises:
            ValueError: If the amount is less than or equal to zero, or if the duration is not positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        if duration <= 0:
            raise ValueError("Stake duration must be a positive integer.")

        self.total_staked += amount
        self.stakes.append((amount, duration))
        print(f"Staked {amount} tokens for {duration} days.")

    def calculate_rewards(self):
        """
        Calculates the total rewards earned from the staked tokens.

        Returns:
            float: The total rewards earned.
        """
        total_rewards = 0.0
        for amount, duration in self.stakes:
            total_rewards += amount * self.rewards_rate * duration
        return total_rewards

    def unstake_tokens(self):
        """
        Unstakes all tokens and returns the total rewards earned.

        Returns:
            tuple: A tuple containing the unstaked amount and total rewards earned.
        """
        total_rewards = self.calculate_rewards()
        unstaked_amount = self.total_staked
        self.total_staked = 0.0
        self.stakes.clear()  # Clear all stakes after unstaking
        print(f"Unstaked {unstaked_amount} tokens. Total rewards earned: {total_rewards}.")
        return unstaked_amount, total_rewards

# Example usage:
if __name__ == "__main__":
    try:
        staking = TokenFiStaking(rewards_rate=0.05)  # 5% rewards rate
        staking.stake_tokens(1000, 30)  # Stake 1000 tokens for 30 days
        staking.stake_tokens(500, 15)    # Stake 500 tokens for 15 days
        total_rewards = staking.calculate_rewards()
        print(f"Total rewards calculated: {total_rewards}.")
        unstaked_amount, rewards_earned = staking.unstake_tokens()
        print(f"Unstaked amount: {unstaked_amount}, Rewards earned: {rewards_earned}.")
    except ValueError as e:
        print(f"Error: {e}")
```
