"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitinvestcoin.com
Prompt: Write Python code to simulate the investment plans offered by BitInvestCoin, including calculations for percentage profit and fixed profit based on the plan duration and investment amount.
Generated: DETERMINISTIC_c7fb7cda431b2840
Batch ID: 20250612_150211
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
    A class to represent an investment plan offered by BitInvestCoin.
    """

    def __init__(self, plan_name, duration_months, fixed_profit_rate, percentage_profit_rate):
        """
        Initializes an investment plan with the specified parameters.

        :param plan_name: Name of the investment plan
        :param duration_months: Duration of the investment in months
        :param fixed_profit_rate: Fixed profit amount per month
        :param percentage_profit_rate: Percentage profit rate per month
        """
        self.plan_name = plan_name
        self.duration_months = duration_months
        self.fixed_profit_rate = fixed_profit_rate
        self.percentage_profit_rate = percentage_profit_rate

    def calculate_fixed_profit(self, investment_amount):
        """
        Calculates the total fixed profit for the investment.

        :param investment_amount: The amount to invest
        :return: Total fixed profit
        """
        try:
            total_fixed_profit = self.fixed_profit_rate * self.duration_months
            return total_fixed_profit
        except Exception as e:
            print(f"Error in calculating fixed profit: {e}")
            return None

    def calculate_percentage_profit(self, investment_amount):
        """
        Calculates the total percentage profit for the investment.

        :param investment_amount: The amount to invest
        :return: Total percentage profit
        """
        try:
            total_percentage_profit = (self.percentage_profit_rate / 100) * investment_amount * self.duration_months
            return total_percentage_profit
        except Exception as e:
            print(f"Error in calculating percentage profit: {e}")
            return None

    def calculate_total_return(self, investment_amount):
        """
        Calculates the total return after the investment period.

        :param investment_amount: The amount to invest
        :return: Total return including investment amount, fixed and percentage profits
        """
        try:
            fixed_profit = self.calculate_fixed_profit(investment_amount)
            percentage_profit = self.calculate_percentage_profit(investment_amount)
            total_return = investment_amount + (fixed_profit if fixed_profit is not None else 0) + (percentage_profit if percentage_profit is not None else 0)
            return total_return
        except Exception as e:
            print(f"Error in calculating total return: {e}")
            return None


def main():
    # Example usage of the InvestmentPlan class
    
    # Creating an investment plan for BitInvestCoin
    plan = InvestmentPlan(plan_name="Gold Plan", duration_months=12, fixed_profit_rate=100, percentage_profit_rate=5)

    # Investment amount
    investment_amount = 1000  # Change this amount as needed

    # Calculating profits and total return
    fixed_profit = plan.calculate_fixed_profit(investment_amount)
    percentage_profit = plan.calculate_percentage_profit(investment_amount)
    total_return = plan.calculate_total_return(investment_amount)

    # Displaying the results
    print(f"Investment Plan: {plan.plan_name}")
    print(f"Fixed Profit: ${fixed_profit:.2f}")
    print(f"Percentage Profit: ${percentage_profit:.2f}")
    print(f"Total Return after {plan.duration_months} months: ${total_return:.2f}")


if __name__ == "__main__":
    main()
```
