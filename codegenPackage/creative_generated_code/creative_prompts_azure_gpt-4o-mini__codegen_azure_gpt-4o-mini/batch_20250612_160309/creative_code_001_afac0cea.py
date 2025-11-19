"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaultstake.xyz
Prompt: Write a code snippet that demonstrates how to calculate daily rewards for a staking platform like VaultStake.
Generated: DETERMINISTIC_afac0cea9c4eb1a2
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPlatform:
    """
    A class to represent a staking platform that calculates daily rewards for stakers.
    """

    def __init__(self, annual_interest_rate: float):
        """
        Initializes the StakingPlatform with a specified annual interest rate.

        :param annual_interest_rate: The annual interest rate (as a decimal, e.g. 0.05 for 5%).
        """
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        
        self.annual_interest_rate = annual_interest_rate

    def calculate_daily_reward(self, staked_amount: float) -> float:
        """
        Calculates the daily reward for a given staked amount.

        :param staked_amount: The amount of tokens staked by the user.
        :return: The amount of daily rewards.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        
        # Daily interest rate calculation
        daily_interest_rate = self.annual_interest_rate / 365
        daily_reward = staked_amount * daily_interest_rate

        return daily_reward


def main():
    """
    Main function to demonstrate the daily reward calculation for a staking platform.
    """
    try:
        # Example usage of the StakingPlatform class
        platform = StakingPlatform(annual_interest_rate=0.05)  # 5% annual interest rate

        # Staking amount
        staked_amount = 1000.0  # Example staked amount

        # Calculate daily rewards
        daily_reward = platform.calculate_daily_reward(staked_amount)
        print(f"Daily reward for staking {staked_amount} tokens is: {daily_reward:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")  # Handle exceptions by printing error message


if __name__ == "__main__":
    main()
```
