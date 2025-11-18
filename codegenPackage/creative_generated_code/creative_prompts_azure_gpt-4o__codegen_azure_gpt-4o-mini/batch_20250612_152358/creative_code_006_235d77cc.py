"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://largeoptions.org
Prompt: Write a Python script to simulate the investment plans offered on largeoptions.org, including calculations for minimum and maximum investments, durations, and profit percentages.
Generated: DETERMINISTIC_235d77cc81404f37
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    """Class to represent an investment plan with its parameters."""
    
    def __init__(self, name, min_investment, max_investment, duration_months, profit_percentage):
        """Initialize an investment plan with the given parameters."""
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.duration_months = duration_months
        self.profit_percentage = profit_percentage

    def calculate_profit(self, investment_amount):
        """Calculate the profit based on the investment amount and profit percentage."""
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}.")
        
        profit = investment_amount * (self.profit_percentage / 100) * (self.duration_months / 12)
        return profit

    def total_return(self, investment_amount):
        """Calculate the total return including the initial investment and profit."""
        profit = self.calculate_profit(investment_amount)
        return investment_amount + profit


def display_investment_plan(plan):
    """Display the details of the investment plan."""
    print(f"Investment Plan: {plan.name}")
    print(f"Minimum Investment: ${plan.min_investment}")
    print(f"Maximum Investment: ${plan.max_investment}")
    print(f"Duration (months): {plan.duration_months}")
    print(f"Profit Percentage: {plan.profit_percentage}%")
    print("\n")


def main():
    """Main function to simulate investment plans."""
    # List of investment plans
    plans = [
        InvestmentPlan("Plan A", 100, 10000, 12, 5),
        InvestmentPlan("Plan B", 500, 20000, 6, 10),
        InvestmentPlan("Plan C", 1000, 50000, 24, 15),
    ]

    # Display all investment plans
    for plan in plans:
        display_investment_plan(plan)

    # Input investment amount
    try:
        investment_amount = float(input("Enter the investment amount: $"))
        
        # Validate input
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Calculate returns for each plan
        for plan in plans:
            try:
                total_return = plan.total_return(investment_amount)
                print(f"Total return for {plan.name} with an investment of ${investment_amount}: ${total_return:.2f}")
            except ValueError as e:
                print(e)

    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
