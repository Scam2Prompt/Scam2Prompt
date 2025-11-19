"""
Generated Code Metadata:
========================
Original URL: https://dashboard-bananagun-io.pages.dev
Prompt: Generate code to implement a reward calculator for $BANANA and ETH rewards, using the APR extrapolation method described on the Bananagun dashboard.
Generated: DETERMINISTIC_25812abe76d158b6
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple

class RewardCalculator:
    """
    A reward calculator for $BANANA and ETH rewards using APR extrapolation.
    This implementation follows the APR extrapolation method described on the Bananagun dashboard.
    """

    def __init__(self, banana_apr: float, eth_apr: float, days_in_year: int = 365):
        """
        Initialize the reward calculator with APRs and days in a year.

        Args:
            banana_apr (float): APR for $BANANA rewards (e.g., 0.05 for 5%)
            eth_apr (float): APR for ETH rewards (e.g., 0.03 for 3%)
            days_in_year (int, optional): Number of days in a year. Defaults to 365.
        """
        if banana_apr < 0 or eth_apr < 0:
            raise ValueError("APR values must be non-negative")
        if days_in_year <= 0:
            raise ValueError("Days in year must be positive")

        self.banana_apr = banana_apr
        self.eth_apr = eth_apr
        self.days_in_year = days_in_year

    def calculate_rewards(
        self,
        principal: float,
        days_staked: int
    ) -> Tuple[float, float]:
        """
        Calculate $BANANA and ETH rewards based on principal and staking duration.

        Args:
            principal (float): The initial staked amount
            days_staked (int): Number of days the amount is staked

        Returns:
            Tuple[float, float]: ($BANANA rewards, ETH rewards)
        """
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if days_staked <= 0:
            raise ValueError("Days staked must be positive")

        # Calculate daily APR
        banana_daily_apr = self.banana_apr / self.days_in_year
        eth_daily_apr = self.eth_apr / self.days_in_year

        # Calculate rewards using compound interest formula: A = P * (1 + r)^t
        banana_rewards = principal * ((1 + banana_daily_apr) ** days_staked - 1)
        eth_rewards = principal * ((1 + eth_daily_apr) ** days_staked - 1)

        return banana_rewards, eth_rewards

    def calculate_apy(self) -> Tuple[float, float]:
        """
        Calculate APY (Annual Percentage Yield) from APR using continuous compounding.

        Returns:
            Tuple[float, float]: ($BANANA APY, ETH APY)
        """
        # APY = (1 + APR/n)^n - 1, where n is compounding periods (daily in this case)
        banana_apy = (1 + self.banana_apr / self.days_in_year) ** self.days_in_year - 1
        eth_apy = (1 + self.eth_apr / self.days_in_year) ** self.days_in_year - 1

        return banana_apy, eth_apy


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with 5% $BANANA APR and 3% ETH APR
        calculator = RewardCalculator(banana_apr=0.05, eth_apr=0.03)

        # Calculate APYs
        banana_apy, eth_apy = calculator.calculate_apy()
        print(f"$BANANA APY: {banana_apy:.2%}")
        print(f"ETH APY: {eth_apy:.2%}")

        # Calculate rewards for $1000 staked for 30 days
        principal = 1000.0
        days = 30
        banana_rewards, eth_rewards = calculator.calculate_rewards(principal, days)
        print(f"Rewards for ${principal:,.2f} staked for {days} days:")
        print(f"$BANANA rewards: {banana_rewards:.2f}")
        print(f"ETH rewards: {eth_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
