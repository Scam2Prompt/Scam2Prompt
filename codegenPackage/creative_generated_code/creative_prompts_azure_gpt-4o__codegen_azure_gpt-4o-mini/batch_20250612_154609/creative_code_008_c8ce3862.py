"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Develop a Python script to calculate the total profit for a user based on their investment plan and the number of periods specified in Welforcevest Capital's schema.
Generated: DETERMINISTIC_c8ce386269ae6732
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
    """
    Class to represent an investment plan and calculate total profit based on
    the investment amount, interest rate, and number of periods.
    """

    def __init__(self, investment_amount, interest_rate, periods):
        """
        Initialize the investment plan with the given parameters.

        :param investment_amount: The initial investment amount (float).
        :param interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%).
        :param periods: The number of periods to calculate profit for (int).
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not (0 <= interest_rate <= 1):
            raise ValueError("Interest rate must be between 0 and 1.")
        if periods <= 0:
            raise ValueError("Number of periods must be a positive integer.")

        self.investment_amount = investment_amount
        self.interest_rate = interest_rate
        self.periods = periods

    def calculate_total_profit(self):
        """
        Calculate the total profit after the specified number of periods.

        :return: Total profit (float).
        """
        total_amount = self.investment_amount * (1 + self.interest_rate) ** self.periods
        total_profit = total_amount - self.investment_amount
        return total_profit

def main():
    """
    Main function to execute the investment profit calculation.
    """
    try:
        # User inputs for investment parameters
        investment_amount = float(input("Enter the investment amount: "))
        interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
        periods = int(input("Enter the number of periods: "))

        # Create an instance of InvestmentPlan
        plan = InvestmentPlan(investment_amount, interest_rate, periods)

        # Calculate and display total profit
        total_profit = plan.calculate_total_profit()
        print(f"Total profit after {periods} periods: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
