"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Write Python code to calculate daily profits for the investment plans offered by Finance Impact Pro, including Basic, Silver, Gold, and Ultimate plans, based on their guaranteed profit percentages and durations.
Generated: DETERMINISTIC_f1ba9f71017b351a
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    Represents an investment plan with a name, guaranteed profit percentage, and duration in days.
    """

    def __init__(self, name: str, profit_percentage: float, duration_days: int):
        """
        Initializes an instance of InvestmentPlan.

        :param name: The name of the investment plan.
        :param profit_percentage: The guaranteed profit percentage for the plan.
        :param duration_days: The duration of the investment in days.
        """
        self.name = name
        self.profit_percentage = profit_percentage
        self.duration_days = duration_days

    def calculate_daily_profit(self, investment_amount: float) -> float:
        """
        Calculates the daily profit based on the investment amount.

        :param investment_amount: The amount invested in the plan.
        :return: Daily profit from the investment.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")

        total_profit = (investment_amount * self.profit_percentage / 100) * (self.duration_days / 365)
        daily_profit = total_profit / self.duration_days
        return daily_profit


def main():
    # Define investment plans
    plans = [
        InvestmentPlan("Basic", 5.0, 30),       # 5% profit over 30 days
        InvestmentPlan("Silver", 7.0, 60),      # 7% profit over 60 days
        InvestmentPlan("Gold", 10.0, 90),       # 10% profit over 90 days
        InvestmentPlan("Ultimate", 15.0, 120)   # 15% profit over 120 days
    ]

    # Amount to invest
    investment_amount = 1000.0  # Example investment amount

    # Calculate daily profits for each plan
    try:
        for plan in plans:
            daily_profit = plan.calculate_daily_profit(investment_amount)
            print(f"Daily profit for {plan.name} plan: ${daily_profit:.2f}")
    except ValueError as e:
        print(f"Error calculating daily profit: {e}")


if __name__ == "__main__":
    main()
```
