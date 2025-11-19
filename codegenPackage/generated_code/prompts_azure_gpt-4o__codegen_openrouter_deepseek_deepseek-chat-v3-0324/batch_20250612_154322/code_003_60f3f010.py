"""
Generated Code Metadata:
========================
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Create a script to calculate staking rewards for $EMT tokens based on the presale bonus stages and the staking calculator parameters (e.g., 90 days, 120 days, etc.).
Generated: DETERMINISTIC_60f3f010605b203e
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class StakingRewardCalculator:
    """
    A class to calculate staking rewards for $EMT tokens based on presale bonus stages and staking periods.
    """

    def __init__(self, presale_bonus_stages: Dict[str, float], staking_periods: Dict[str, int]):
        """
        Initialize the calculator with presale bonus stages and staking periods.

        Args:
            presale_bonus_stages (Dict[str, float]): Dictionary mapping stage names to bonus percentages.
            staking_periods (Dict[str, int]): Dictionary mapping staking period names to days.
        """
        self.presale_bonus_stages = presale_bonus_stages
        self.staking_periods = staking_periods

    def calculate_rewards(
        self,
        amount: float,
        stage: str,
        period: str,
        annual_interest_rate: float
    ) -> Tuple[float, float, float]:
        """
        Calculate the staking rewards for a given amount, stage, and period.

        Args:
            amount (float): The amount of $EMT tokens to stake.
            stage (str): The presale bonus stage.
            period (str): The staking period.
            annual_interest_rate (float): The annual interest rate (as a decimal, e.g., 0.1 for 10%).

        Returns:
            Tuple[float, float, float]: A tuple containing (bonus_amount, interest_amount, total_rewards).

        Raises:
            ValueError: If the stage or period is invalid.
        """
        if stage not in self.presale_bonus_stages:
            raise ValueError(f"Invalid stage: {stage}. Valid stages are: {list(self.presale_bonus_stages.keys())}")
        
        if period not in self.staking_periods:
            raise ValueError(f"Invalid period: {period}. Valid periods are: {list(self.staking_periods.keys())}")

        bonus_percentage = self.presale_bonus_stages[stage]
        days = self.staking_periods[period]

        # Calculate bonus amount
        bonus_amount = amount * bonus_percentage / 100

        # Calculate interest amount
        daily_interest_rate = annual_interest_rate / 365
        interest_amount = amount * daily_interest_rate * days

        # Total rewards (bonus + interest)
        total_rewards = bonus_amount + interest_amount

        return bonus_amount, interest_amount, total_rewards

    def get_stages(self) -> List[str]:
        """Return the list of valid presale bonus stages."""
        return list(self.presale_bonus_stages.keys())

    def get_periods(self) -> List[str]:
        """Return the list of valid staking periods."""
        return list(self.staking_periods.keys())


# Example usage
if __name__ == "__main__":
    # Define presale bonus stages (stage name: bonus percentage)
    presale_bonus_stages = {
        "Stage 1": 30.0,
        "Stage 2": 20.0,
        "Stage 3": 10.0,
        "Stage 4": 5.0,
    }

    # Define staking periods (period name: days)
    staking_periods = {
        "90 days": 90,
        "120 days": 120,
        "180 days": 180,
        "365 days": 365,
    }

    # Annual interest rate (10%)
    annual_interest_rate = 0.10

    # Initialize calculator
    calculator = StakingRewardCalculator(presale_bonus_stages, staking_periods)

    # Example calculation
    try:
        amount = 1000.0  # 1000 EMT tokens
        stage = "Stage 1"
        period = "90 days"

        bonus, interest, total = calculator.calculate_rewards(amount, stage, period, annual_interest_rate)

        print(f"Staking {amount} EMT tokens in {stage} for {period}:")
        print(f"Bonus: {bonus:.2f} EMT")
        print(f"Interest: {interest:.2f} EMT")
        print(f"Total rewards: {total:.2f} EMT")

    except ValueError as e:
        print(f"Error: {e}")
```
