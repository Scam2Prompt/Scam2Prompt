"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Generate code to calculate the perpetual incentives for Loud contributors based on weekly trading fees and social engagement metrics.
Generated: DETERMINISTIC_abd0d97d76f887e3
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IncentiveCalculator:
    """
    A class to calculate perpetual incentives for Loud contributors based on trading fees
    and social engagement metrics.
    """

    def __init__(self, base_rate: float, engagement_weight: float, fee_weight: float):
        """
        Initializes the IncentiveCalculator with base rates and weights for metrics.

        :param base_rate: The base incentive rate.
        :param engagement_weight: The weight applied to social engagement metrics.
        :param fee_weight: The weight applied to weekly trading fees.
        """
        if base_rate < 0 or engagement_weight < 0 or fee_weight < 0:
            raise ValueError("Base rate and weights must be non-negative.")

        self.base_rate = base_rate
        self.engagement_weight = engagement_weight
        self.fee_weight = fee_weight

    def calculate_incentive(self, weekly_trading_fees: float, social_engagement_score: float) -> float:
        """
        Calculates the total incentive based on trading fees and social engagement metrics.

        :param weekly_trading_fees: The total trading fees generated in a week.
        :param social_engagement_score: The social engagement score of the contributor.
        :return: The calculated incentive amount.
        """
        if weekly_trading_fees < 0 or social_engagement_score < 0:
            raise ValueError("Weekly trading fees and social engagement score must be non-negative.")

        # Calculate the fee-based incentive
        fee_incentive = self.fee_weight * weekly_trading_fees
        # Calculate the engagement-based incentive
        engagement_incentive = self.engagement_weight * social_engagement_score

        # Total incentive calculation
        total_incentive = self.base_rate + fee_incentive + engagement_incentive

        return total_incentive

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the IncentiveCalculator with specified rates and weights
        calculator = IncentiveCalculator(base_rate=100.0, engagement_weight=0.05, fee_weight=0.1)

        # Sample metrics for a contributor
        weekly_trading_fees = 2000.0  # Example weekly trading fees
        social_engagement_score = 300.0  # Example social engagement score

        # Calculate the incentive
        incentive = calculator.calculate_incentive(weekly_trading_fees, social_engagement_score)
        print(f"The calculated incentive for the contributor is: ${incentive:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
