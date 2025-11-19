"""
Generated Code Metadata:
========================
Original URL: https://rgtrdeer.pages.dev
Prompt: Generate code to calculate points allocation for a trade on RageTrade given the trading amount and milestones achieved.
Generated: DETERMINISTIC_7f7b23d3b75fd3b0
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

class TradePointsCalculator:
    """
    A class to calculate points allocation for a trade on RageTrade.
    """

    def __init__(self, base_points_rate: float, milestone_points: Dict[str, float]):
        """
        Initialize the TradePointsCalculator.

        :param base_points_rate: The base rate of points per trading amount.
        :param milestone_points: A dictionary containing milestone names and their respective bonus points.
        """
        self.base_points_rate = base_points_rate
        self.milestone_points = milestone_points

    def calculate_points(self, trading_amount: float, milestones_achieved: List[str]) -> float:
        """
        Calculate the total points for a trade based on trading amount and milestones achieved.

        :param trading_amount: The amount traded.
        :param milestones_achieved: A list of milestones achieved during the trade.
        :return: The total points allocated for the trade.
        """
        if trading_amount < 0:
            raise ValueError("Trading amount must be non-negative.")

        # Calculate base points
        total_points = trading_amount * self.base_points_rate

        # Add milestone bonus points
        for milestone in milestones_achieved:
            if milestone in self.milestone_points:
                total_points += self.milestone_points[milestone]
            else:
                raise ValueError(f"Unknown milestone: {milestone}")

        return total_points


# Example usage
if __name__ == "__main__":
    try:
        # Define base points rate and milestone points
        base_points_rate = 0.1  # 0.1 points per unit of trading amount
        milestone_points = {
            "high_volume": 50.0,
            "early_adopter": 30.0,
            "referral_bonus": 20.0
        }

        # Create an instance of TradePointsCalculator
        calculator = TradePointsCalculator(base_points_rate, milestone_points)

        # Example trade details
        trading_amount = 1000.0  # Example trading amount
        milestones_achieved = ["high_volume", "referral_bonus"]  # Example milestones achieved

        # Calculate points
        total_points = calculator.calculate_points(trading_amount, milestones_achieved)
        print(f"Total points allocated: {total_points}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
