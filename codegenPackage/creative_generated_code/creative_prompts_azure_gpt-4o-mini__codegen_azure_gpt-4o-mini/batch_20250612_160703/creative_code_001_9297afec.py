"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Write a code snippet that calculates potential earnings based on the Super Mining package rates for different investment plans.
Generated: DETERMINISTIC_9297afece6bfbb1c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SuperMiningInvestment:
    """
    A class to calculate potential earnings based on Super Mining package rates
    for different investment plans.
    """

    # Define rates for different investment plans (hypothetical values)
    PLAN_RATES = {
        'basic': 0.05,      # 5% return per month
        'standard': 0.1,    # 10% return per month
        'premium': 0.15     # 15% return per month
    }

    def __init__(self, investment_amount, plan_type):
        """
        Initialize the investment parameters.

        :param investment_amount: The amount of money to invest.
        :param plan_type: The type of investment plan.
        """
        self.investment_amount = investment_amount
        self.plan_type = plan_type.lower()

        # Validate the investment plan type
        if self.plan_type not in self.PLAN_RATES:
            raise ValueError(f"Invalid plan type '{self.plan_type}'. Available plans are: {list(self.PLAN_RATES.keys())}")

    def calculate_monthly_earnings(self):
        """
        Calculate monthly earnings based on the investment amount and plan type.

        :return: The amount of earnings for the month.
        """
        rate = self.PLAN_RATES[self.plan_type]
        earnings = self.investment_amount * rate
        return earnings

    def calculate_annual_earnings(self):
        """
        Calculate annual earnings based on the investment amount and plan type.

        :return: The total earnings for the year.
        """
        monthly_earnings = self.calculate_monthly_earnings()
        annual_earnings = monthly_earnings * 12
        return annual_earnings


if __name__ == "__main__":
    try:
        # Example usage
        investment_amount = float(input("Enter your investment amount: "))
        plan_type = input("Enter your investment plan (basic, standard, premium): ")

        # Create an instance of SuperMiningInvestment
        investment = SuperMiningInvestment(investment_amount, plan_type)

        # Calculate and display earnings
        print(f"Monthly Earnings: ${investment.calculate_monthly_earnings():.2f}")
        print(f"Annual Earnings: ${investment.calculate_annual_earnings():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
