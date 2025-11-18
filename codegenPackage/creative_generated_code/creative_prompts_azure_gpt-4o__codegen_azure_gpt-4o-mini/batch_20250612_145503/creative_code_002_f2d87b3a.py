"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Create a function to calculate the cumulative rewards earned from staking Polyhedra Network tokens, factoring in APR and staking duration.
Generated: DETERMINISTIC_f2d87b3a5ac0b00a
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate the cumulative rewards earned from staking
    Polyhedra Network tokens based on the Annual Percentage Rate (APR)
    and the staking duration in years.
    """

    def __init__(self, apr: float):
        """
        Initializes the calculator with the given APR.

        :param apr: Annual Percentage Rate (APR) as a decimal (e.g., 0.05 for 5%)
        """
        if apr < 0:
            raise ValueError("APR must be a non-negative value.")
        self.apr = apr

    def calculate_rewards(self, principal: float, duration_years: float) -> float:
        """
        Calculates the cumulative rewards earned from staking.

        :param principal: The initial amount of tokens staked.
        :param duration_years: The duration for which the tokens are staked, in years.
        :return: The cumulative rewards earned.
        """
        if principal < 0:
            raise ValueError("Principal must be a non-negative value.")
        if duration_years < 0:
            raise ValueError("Duration must be a non-negative value.")

        # Calculate cumulative rewards using compound interest formula
        rewards = principal * (1 + self.apr) ** duration_years - principal
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APR of 5%
        rewards_calculator = StakingRewardsCalculator(apr=0.05)

        # Calculate rewards for a principal of 1000 tokens staked for 2 years
        principal_amount = 1000
        staking_duration = 2  # in years
        cumulative_rewards = rewards_calculator.calculate_rewards(principal_amount, staking_duration)

        print(f"Cumulative rewards earned: {cumulative_rewards:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
