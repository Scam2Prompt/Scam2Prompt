"""
Generated Code Metadata:
========================
Original URL: https://presale-poodlinu.pages.dev
Prompt: Develop a simple staking rewards calculator for Poodl Inu, taking into account the 176% annual rewards and the total amount of $POODL staked.
Generated: DETERMINISTIC_e50ae7c62177733c
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Poodl Inu Staking Rewards Calculator

Calculates the staking rewards for Poodl Inu based on the total amount staked and the annual rewards rate.

Author: [Your Name]
Date: [Today's Date]
"""

class PoodlInuStakingRewardsCalculator:
    def __init__(self, annual_rewards_rate=1.76, compounding_frequency=365):
        """
        Initializes the calculator with the annual rewards rate and compounding frequency.

        Args:
            annual_rewards_rate (float, optional): The annual rewards rate. Defaults to 1.76 (176%).
            compounding_frequency (int, optional): The compounding frequency in days. Defaults to 365 (daily compounding).
        """
        self.annual_rewards_rate = annual_rewards_rate
        self.compounding_frequency = compounding_frequency

    def calculate_rewards(self, total_staked, staking_period_in_days):
        """
        Calculates the staking rewards for the given total staked amount and staking period.

        Args:
            total_staked (float): The total amount of $POODL staked.
            staking_period_in_days (int): The staking period in days.

        Returns:
            float: The staking rewards.

        Raises:
            ValueError: If the total staked amount or staking period is negative.
        """
        if total_staked < 0:
            raise ValueError("Total staked amount cannot be negative")
        if staking_period_in_days < 0:
            raise ValueError("Staking period cannot be negative")

        # Calculate the daily rewards rate
        daily_rewards_rate = (self.annual_rewards_rate - 1) / self.compounding_frequency + 1

        # Calculate the staking rewards using compound interest formula
        rewards = total_staked * ((daily_rewards_rate ** staking_period_in_days) - 1)

        return rewards

    def calculate_apr(self, total_staked, staking_period_in_days):
        """
        Calculates the APR (Annual Percentage Rate) for the given total staked amount and staking period.

        Args:
            total_staked (float): The total amount of $POODL staked.
            staking_period_in_days (int): The staking period in days.

        Returns:
            float: The APR.

        Raises:
            ValueError: If the total staked amount or staking period is negative.
        """
        rewards = self.calculate_rewards(total_staked, staking_period_in_days)
        apr = (rewards / total_staked) * (365 / staking_period_in_days) * 100

        return apr


def main():
    calculator = PoodlInuStakingRewardsCalculator()

    try:
        total_staked = float(input("Enter the total amount of $POODL staked: "))
        staking_period_in_days = int(input("Enter the staking period in days: "))

        rewards = calculator.calculate_rewards(total_staked, staking_period_in_days)
        apr = calculator.calculate_apr(total_staked, staking_period_in_days)

        print(f"Staking Rewards: ${rewards:.2f}")
        print(f"APR: {apr:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
