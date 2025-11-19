"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Apex Digital Limited, including Beginner, Standard, Gold, Ambassador, and VIP plans.
Generated: DETERMINISTIC_8c9628ea73b55b3e
Batch ID: 20250612_160124
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
    A class to represent an investment plan and calculate potential profits.
    """

    def __init__(self, name, investment_amount, duration_months, annual_interest_rate):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan.
        :param investment_amount: The initial amount invested.
        :param duration_months: Duration of the investment in months.
        :param annual_interest_rate: The annual interest rate as a percentage.
        """
        self.name = name
        self.investment_amount = investment_amount
        self.duration_months = duration_months
        self.annual_interest_rate = annual_interest_rate

    def calculate_profit(self):
        """
        Calculates the potential profit for the investment plan.

        :return: Total profit as a float.
        """
        # Convert annual interest rate to a decimal
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        total_months = self.duration_months

        # Calculate compound interest
        total_profit = self.investment_amount * ((1 + monthly_interest_rate) ** total_months - 1)
        return total_profit

def main():
    """
    Main function to execute the investment profit calculation.
    """
    # Define the investment plans offered by Apex Digital Limited
    plans = [
        InvestmentPlan("Beginner", 1000, 12, 5),
        InvestmentPlan("Standard", 5000, 24, 7),
        InvestmentPlan("Gold", 10000, 36, 10),
        InvestmentPlan("Ambassador", 20000, 48, 12),
        InvestmentPlan("VIP", 50000, 60, 15),
    ]

    # Calculate and display the profit for each plan
    for plan in plans:
        try:
            profit = plan.calculate_profit()
            print(f"Plan: {plan.name}, Initial Investment: ${plan.investment_amount}, "
                  f"Profit after {plan.duration_months} months: ${profit:.2f}")
        except Exception as e:
            print(f"Error calculating profit for {plan.name}: {e}")

if __name__ == "__main__":
    main()
```
