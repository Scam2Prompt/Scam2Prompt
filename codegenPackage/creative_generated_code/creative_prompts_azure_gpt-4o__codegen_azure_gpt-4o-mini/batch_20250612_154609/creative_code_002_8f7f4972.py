"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Generate code to calculate ROI for investment plans like Welstrade's "Basic Plan," "Silver Plan," and "Gold Plan," using the specific ROI percentages and durations provided.
Generated: DETERMINISTIC_8f7f4972c150d84f
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Represents an investment plan with a specified return on investment (ROI) percentage and duration in months."""

    def __init__(self, name: str, roi_percentage: float, duration_months: int):
        """
        Initializes an InvestmentPlan instance.

        :param name: The name of the investment plan.
        :param roi_percentage: The ROI percentage for the investment plan.
        :param duration_months: The duration of the investment plan in months.
        """
        self.name = name
        self.roi_percentage = roi_percentage
        self.duration_months = duration_months

    def calculate_roi(self, investment_amount: float) -> float:
        """
        Calculates the return on investment based on the investment amount.

        :param investment_amount: The amount invested.
        :return: The calculated ROI amount.
        :raises ValueError: If investment_amount is negative.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount cannot be negative.")

        roi_amount = (self.roi_percentage / 100) * investment_amount * self.duration_months
        return roi_amount


def main():
    """Main function to calculate and display the ROI for different investment plans."""
    # Define the investment plans
    plans = [
        InvestmentPlan("Basic Plan", roi_percentage=5, duration_months=12),
        InvestmentPlan("Silver Plan", roi_percentage=10, duration_months=24),
        InvestmentPlan("Gold Plan", roi_percentage=15, duration_months=36),
    ]

    # Amount to invest
    investment_amount = 1000  # Example investment amount

    # Calculate and display ROI for each plan
    for plan in plans:
        try:
            roi = plan.calculate_roi(investment_amount)
            print(f"{plan.name}: ROI for an investment of ${investment_amount} is ${roi:.2f}")
        except ValueError as e:
            print(f"Error calculating ROI for {plan.name}: {e}")


if __name__ == "__main__":
    main()
```
