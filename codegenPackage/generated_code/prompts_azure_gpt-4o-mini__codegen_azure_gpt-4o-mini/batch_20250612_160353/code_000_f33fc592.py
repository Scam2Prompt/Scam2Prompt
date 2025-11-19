"""
Generated Code Metadata:
========================
Original URL: https://top-trading.fund
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Top Trading, specifically for the Platinum, Gold, Silver, and Diamond plans.
Generated: DETERMINISTIC_f33fc5928a4115c4
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.
    """

    def __init__(self, name, initial_investment, return_rate, duration):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount invested
        :param return_rate: Expected return rate (as a decimal)
        :param duration: Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.return_rate = return_rate
        self.duration = duration

    def calculate_profit(self):
        """
        Calculates the potential profit from the investment plan.

        :return: The potential profit
        """
        try:
            # Calculate the total amount after the investment duration
            total_amount = self.initial_investment * (1 + self.return_rate) ** self.duration
            # Calculate profit by subtracting the initial investment
            profit = total_amount - self.initial_investment
            return profit
        except Exception as e:
            print(f"Error calculating profit for {self.name}: {e}")
            return None


def main():
    """
    Main function to execute the investment profit calculations.
    """
    # Define investment plans with their respective parameters
    plans = [
        InvestmentPlan("Platinum", 10000, 0.15, 5),  # 15% return over 5 years
        InvestmentPlan("Gold", 5000, 0.10, 3),      # 10% return over 3 years
        InvestmentPlan("Silver", 2000, 0.05, 2),     # 5% return over 2 years
        InvestmentPlan("Diamond", 15000, 0.20, 4)    # 20% return over 4 years
    ]

    # Calculate and display profits for each plan
    for plan in plans:
        profit = plan.calculate_profit()
        if profit is not None:
            print(f"Potential profit for {plan.name} plan: ${profit:.2f}")


if __name__ == "__main__":
    main()
```
