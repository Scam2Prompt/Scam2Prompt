"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meme-indexs.pages.dev
Prompt: Write code to implement a staking rewards calculator for `$MEMEX` tokens based on the tokenomics described in the site.
Generated: DETERMINISTIC_ab44676e269aa837
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Optional
from datetime import datetime, timedelta


class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for $MEMEX tokens.
    """

    def __init__(self, annual_percentage_yield: float, token_decimals: int = 18):
        """
        Initialize the staking rewards calculator.

        :param annual_percentage_yield: The staking APY as a percentage (e.g., 12.5 for 12.5% APY).
        :param token_decimals: Number of decimals the $MEMEX token uses (default is 18).
        """
        if annual_percentage_yield <= 0:
            raise ValueError("Annual Percentage Yield (APY) must be a positive value.")
        self.apy = annual_percentage_yield / 100  # Convert percentage to fraction
        self.token_decimals = token_decimals

    def calculate_rewards(
        self,
        staked_tokens: float,
        staking_start_date: datetime,
        staking_end_date: Optional[datetime] = None,
    ) -> float:
        """
        Calculate staking rewards for the given time period.

        :param staked_tokens: The amount of staked $MEMEX tokens.
        :param staking_start_date: The start date of staking as a datetime object.
        :param staking_end_date: The end date of staking as a datetime object (default is now).
        :return: The calculated staking rewards in $MEMEX.
        """
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than zero.")
        if not isinstance(staking_start_date, datetime):
            raise ValueError("staking_start_date must be a datetime object.")
        if staking_end_date and not isinstance(staking_end_date, datetime):
            raise ValueError("staking_end_date must be a datetime object.")

        # Default the staking end date to the current date and time if not provided
        staking_end_date = staking_end_date or datetime.now()

        if staking_end_date <= staking_start_date:
            raise ValueError("staking_end_date must be after staking_start_date.")

        # Calculate the staking duration in days
        duration = (staking_end_date - staking_start_date).total_seconds() / (60 * 60 * 24)
        
        # Calculate daily rewards rate based on APY
        daily_rate = self.apy / 365

        # Calculate the total rewards
        rewards = staked_tokens * daily_rate * duration

        # Return rewards rounded to match the token's decimal precision
        return round(rewards, self.token_decimals)


# Example usage of the class
if __name__ == "__main__":
    try:
        # Initialize the calculator with 12.5% APY
        calculator = StakingRewardsCalculator(annual_percentage_yield=12.5)

        # Define staking parameters
        staked_amount = 1000.0  # 1000 $MEMEX tokens
        staking_start = datetime(2023, 1, 1, 0, 0, 0)
        staking_end = datetime(2023, 6, 1, 0, 0, 0)

        # Calculate rewards
        rewards = calculator.calculate_rewards(
            staked_tokens=staked_amount,
            staking_start_date=staking_start,
            staking_end_date=staking_end
        )
        print(f"Staking Rewards: {rewards} $MEMEX")
    except Exception as e:
        print(f"Error: {e}")
```
