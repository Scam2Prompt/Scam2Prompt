"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedex.com
Prompt: Write a program to automate staking rewards calculation for assets staked on Aster, including APY adjustments over time.
Generated: DETERMINISTIC_fc3bbb727a9f9f7b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for assets staked on Aster.
    """

    def __init__(self, initial_staked_amount: float, apy: float):
        """
        Initialize the staking reward calculator.

        :param initial_staked_amount: The initial amount of staked assets.
        :param apy: The annual percentage yield (APY) for staking.
        """
        if initial_staked_amount <= 0:
            raise ValueError("Initial staked amount must be greater than zero.")
        if not (0 <= apy <= 100):
            raise ValueError("APY must be between 0 and 100.")

        self.initial_staked_amount = initial_staked_amount
        self.apy = apy / 100  # Convert APY to a decimal
        self.start_date = datetime.datetime.now()

    def calculate_rewards(self, duration_in_years: float) -> float:
        """
        Calculate the total rewards earned over a specified duration.

        :param duration_in_years: The duration for which rewards are calculated, in years.
        :return: Total rewards earned.
        """
        if duration_in_years <= 0:
            raise ValueError("Duration must be greater than zero.")
        
        # Compound interest formula: A = P(1 + r/n)^(nt)
        # For simplicity, we assume compounding happens annually (n=1)
        total_amount = self.initial_staked_amount * (1 + self.apy) ** duration_in_years
        rewards = total_amount - self.initial_staked_amount
        return rewards

    def adjust_apy(self, new_apy: float):
        """
        Adjust the APY for staking rewards calculations.

        :param new_apy: The new annual percentage yield (APY) for staking.
        """
        if not (0 <= new_apy <= 100):
            raise ValueError("New APY must be between 0 and 100.")
        self.apy = new_apy / 100  # Update APY to decimal

    def get_staking_summary(self, duration_in_years: float):
        """
        Get a summary of the staking rewards over a specified duration.
        
        :param duration_in_years: The duration for which to summarize rewards, in years.
        :return: A summary dictionary containing the details of staking rewards.
        """
        rewards = self.calculate_rewards(duration_in_years)
        total_value = self.initial_staked_amount + rewards
        summary = {
            'initial_staked_amount': self.initial_staked_amount,
            'apy': self.apy * 100,  # Convert back to percentage for display
            'duration_years': duration_in_years,
            'rewards_earned': rewards,
            'total_value': total_value,
            'calculation_date': datetime.datetime.now().isoformat()
        }
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking reward calculator with an initial amount and APY
        calculator = StakingRewardCalculator(initial_staked_amount=1000.0, apy=5.0)
        
        # Calculate rewards over a duration of 2 years
        duration = 2.0
        summary = calculator.get_staking_summary(duration)
        
        # Print the staking summary
        print("Staking Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
