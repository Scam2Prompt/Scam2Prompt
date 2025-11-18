"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Develop a program to compare the profitability of Finance Force Ltd's "Basic Plan," "Flexible Plan," and "Advanced Plan" based on initial deposit amounts and daily returns. Use Python for the calculations and provide a summary of the best option.
Generated: DETERMINISTIC_4096efbb23defd03
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan with an initial deposit and daily return rate."""
    
    def __init__(self, name: str, initial_deposit: float, daily_return_rate: float):
        """
        Initialize the investment plan.

        :param name: Name of the investment plan
        :param initial_deposit: Initial amount to invest
        :param daily_return_rate: Daily return rate as a percentage (e.g., 5 for 5%)
        """
        self.name = name
        self.initial_deposit = initial_deposit
        self.daily_return_rate = daily_return_rate / 100  # Convert percentage to decimal

    def calculate_profit(self, days: int) -> float:
        """
        Calculate the profit after a certain number of days.

        :param days: Number of days for the investment
        :return: Total amount after the specified number of days
        """
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        
        total_amount = self.initial_deposit * (1 + self.daily_return_rate) ** days
        return total_amount

def compare_investment_plans(plans: list, days: int) -> str:
    """
    Compare the profitability of different investment plans.

    :param plans: List of InvestmentPlan objects
    :param days: Number of days to calculate profit for
    :return: Summary of the most profitable plan
    """
    if not plans:
        raise ValueError("No investment plans provided for comparison.")
    
    best_plan = None
    highest_profit = 0

    for plan in plans:
        profit = plan.calculate_profit(days)
        print(f"{plan.name} Profit after {days} days: ${profit:.2f}")
        
        if profit > highest_profit:
            highest_profit = profit
            best_plan = plan.name

    return f"The best investment plan is '{best_plan}' with a profit of ${highest_profit:.2f}."

def main():
    """Main function to execute the investment comparison."""
    try:
        # Define the investment plans
        basic_plan = InvestmentPlan("Basic Plan", initial_deposit=1000, daily_return_rate=5)
        flexible_plan = InvestmentPlan("Flexible Plan", initial_deposit=1500, daily_return_rate=4)
        advanced_plan = InvestmentPlan("Advanced Plan", initial_deposit=2000, daily_return_rate=3)

        # List of investment plans
        plans = [basic_plan, flexible_plan, advanced_plan]

        # Number of days to simulate
        days = 30
        
        # Compare the plans and get the result
        summary = compare_investment_plans(plans, days)
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
