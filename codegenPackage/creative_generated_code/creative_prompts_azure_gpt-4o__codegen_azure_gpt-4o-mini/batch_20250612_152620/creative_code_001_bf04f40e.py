"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Create a script that calculates staking rewards for the HumanizedAi platform based on the lock duration and factor percentage, as described in the site's staking overview.
Generated: DETERMINISTIC_bf04f40e693e2a21
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate staking rewards for the HumanizedAi platform.

    Attributes:
        lock_duration (int): The duration in days for which the tokens are staked.
        factor_percentage (float): The percentage factor applied to calculate rewards.
    """

    def __init__(self, lock_duration: int, factor_percentage: float):
        """
        Initializes the StakingCalculator with lock duration and factor percentage.

        Args:
            lock_duration (int): Duration in days for staking.
            factor_percentage (float): Percentage factor for calculating rewards.
        """
        self.lock_duration = lock_duration
        self.factor_percentage = factor_percentage

    def calculate_rewards(self, staked_amount: float) -> float:
        """
        Calculates the staking rewards based on the staked amount.

        Args:
            staked_amount (float): The amount of tokens staked.

        Returns:
            float: The calculated staking rewards.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if self.lock_duration <= 0:
            raise ValueError("Lock duration must be greater than zero.")
        if not (0 <= self.factor_percentage <= 100):
            raise ValueError("Factor percentage must be between 0 and 100.")

        # Calculate rewards based on the formula: (staked_amount * factor_percentage / 100) * lock_duration
        rewards = (staked_amount * self.factor_percentage / 100) * self.lock_duration
        return rewards


def main():
    """
    Main function to run the staking reward calculation.
    """
    try:
        # Example parameters for staking calculation
        lock_duration = 30  # Duration in days
        factor_percentage = 5.0  # Factor percentage
        staked_amount = 1000.0  # Amount of tokens staked

        # Create an instance of StakingCalculator
        staking_calculator = StakingCalculator(lock_duration, factor_percentage)

        # Calculate rewards
        rewards = staking_calculator.calculate_rewards(staked_amount)

        print(f"Staking rewards for {staked_amount} tokens for {lock_duration} days at "
              f"{factor_percentage}%: {rewards:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
