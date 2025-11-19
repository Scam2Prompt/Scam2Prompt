"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Write a function that calculates rewards for staking $DUM tokens based on the FreeDum Fighters tokenomics, including higher rewards for staking with the losing faction.
Generated: DETERMINISTIC_9ec8200396932a7b
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for $DUM tokens based on the FreeDum Fighters tokenomics.
    """

    def __init__(self, base_reward_rate, losing_faction_bonus):
        """
        Initializes the StakingRewardsCalculator with the base reward rate and losing faction bonus.

        :param base_reward_rate: The base reward rate for staking in percentage.
        :param losing_faction_bonus: The additional bonus percentage for staking with the losing faction.
        """
        self.base_reward_rate = base_reward_rate
        self.losing_faction_bonus = losing_faction_bonus

    def calculate_rewards(self, staked_amount, duration_months, is_losing_faction):
        """
        Calculates the total rewards for staking $DUM tokens.

        :param staked_amount: The amount of $DUM tokens staked.
        :param duration_months: The duration of staking in months.
        :param is_losing_faction: Boolean indicating if the staked tokens are from the losing faction.
        :return: The total rewards earned.
        :raises ValueError: If staked_amount or duration_months is negative.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if duration_months < 0:
            raise ValueError("Duration in months must be non-negative.")

        # Calculate the base rewards
        total_reward = staked_amount * (self.base_reward_rate / 100) * duration_months

        # Apply bonus if staking with the losing faction
        if is_losing_faction:
            total_reward += staked_amount * (self.losing_faction_bonus / 100) * duration_months

        return total_reward


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rewards calculator with a base reward rate of 5% and a losing faction bonus of 2%
        calculator = StakingRewardsCalculator(base_reward_rate=5, losing_faction_bonus=2)

        # Calculate rewards for staking 1000 $DUM tokens for 12 months with the losing faction
        rewards = calculator.calculate_rewards(staked_amount=1000, duration_months=12, is_losing_faction=True)
        print(f"Total rewards earned: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
