"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paal-ai.pages.dev
Prompt: Generate code to calculate compounding rewards for staking $PAAL tokens using the APR and reward share percentages provided by the Paal AI staking platform.
Generated: DETERMINISTIC_0cfba0cc23b5e7d0
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class StakingRewardsCalculator:
    """
    A class to calculate compounding rewards for staking $PAAL tokens.
    """

    def __init__(self, apr: float, reward_share_percentage: float):
        """
        Initialize the StakingRewardsCalculator.

        :param apr: Annual Percentage Rate (APR) as a percentage (e.g., 15 for 15%)
        :param reward_share_percentage: Percentage of APR allocated to the staker (e.g., 80 for 80%)
        """
        if not (0 <= apr <= 100):
            raise ValueError("APR must be between 0 and 100.")
        if not (0 <= reward_share_percentage <= 100):
            raise ValueError("Reward share percentage must be between 0 and 100.")

        self.apr = apr / 100  # Convert APR to decimal
        self.reward_share_percentage = reward_share_percentage / 100  # Convert percentage to decimal

    def calculate_rewards(self, initial_stake: float, days: int, compounds_per_year: int = 365):
        """
        Calculate compounding rewards for staking.

        :param initial_stake: The initial amount of $PAAL tokens staked
        :param days: Number of days the tokens are staked
        :param compounds_per_year: Number of compounding intervals per year (default is 365 for daily compounding)
        :return: The total rewards earned and the final stake balance
        """
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of staking days must be greater than zero.")
        if compounds_per_year <= 0:
            raise ValueError("Compounds per year must be greater than zero.")

        # Convert days to years for calculation
        years = days / 365

        # Effective APR after applying the reward share percentage
        effective_apr = self.apr * self.reward_share_percentage

        # Compound interest formula: A = P * (1 + r/n)^(n*t)
        # A = final amount, P = initial principal, r = annual rate, n = compounding frequency, t = time in years
        final_balance = initial_stake * math.pow(
            (1 + effective_apr / compounds_per_year), compounds_per_year * years
        )

        # Total rewards earned is the difference between final balance and initial stake
        total_rewards = final_balance - initial_stake

        return total_rewards, final_balance


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with APR and reward share percentage
        apr = 15  # Example: 15% APR
        reward_share = 80  # Example: 80% reward share
        staking_calculator = StakingRewardsCalculator(apr, reward_share)

        # Inputs for calculation
        initial_stake = 1000  # Example: 1000 $PAAL tokens
        staking_days = 90  # Example: 90 days

        # Calculate rewards
        rewards, final_balance = staking_calculator.calculate_rewards(initial_stake, staking_days)

        # Output results
        print(f"Initial Stake: {initial_stake} $PAAL")
        print(f"Staking Duration: {staking_days} days")
        print(f"Total Rewards Earned: {rewards:.2f} $PAAL")
        print(f"Final Stake Balance: {final_balance:.2f} $PAAL")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
