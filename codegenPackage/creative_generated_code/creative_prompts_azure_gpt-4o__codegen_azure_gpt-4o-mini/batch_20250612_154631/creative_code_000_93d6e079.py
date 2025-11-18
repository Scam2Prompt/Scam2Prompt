"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluestockmarkets.com
Prompt: Write Python code to create a profit calculator for investment plans offered by BlueStockMarkets, including options for daily returns and total profit calculations based on the plan duration and investment amount.
Generated: DETERMINISTIC_93d6e07954443da8
Batch ID: 20250612_154631
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
    A class to represent an investment plan for BlueStockMarkets.

    Attributes:
        plan_name (str): The name of the investment plan.
        daily_return_rate (float): The daily return rate (as a decimal).
        duration_days (int): The duration of the investment in days.
    """

    def __init__(self, plan_name: str, daily_return_rate: float, duration_days: int):
        """
        Initializes the InvestmentPlan with a name, return rate, and duration.

        Args:
            plan_name (str): The name of the investment plan.
            daily_return_rate (float): The daily return rate.
            duration_days (int): The duration of the investment in days.
        """
        if daily_return_rate < 0 or duration_days <= 0:
            raise ValueError("Daily return rate must be non-negative and duration must be positive.")
        self.plan_name = plan_name
        self.daily_return_rate = daily_return_rate
        self.duration_days = duration_days

    def calculate_total_profit(self, investment_amount: float) -> float:
        """
        Calculates the total profit from the investment.

        Args:
            investment_amount (float): The amount of money invested.

        Returns:
            float: The total profit earned from the investment.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        
        total_profit = investment_amount * self.daily_return_rate * self.duration_days
        return total_profit

    def calculate_final_amount(self, investment_amount: float) -> float:
        """
        Calculates the final amount after the investment period.

        Args:
            investment_amount (float): The amount of money invested.

        Returns:
            float: The final amount after the investment period including profit.
        """
        total_profit = self.calculate_total_profit(investment_amount)
        final_amount = investment_amount + total_profit
        return final_amount

def main():
    """
    Main function to execute the profit calculator for investment plans.
    """
    try:
        # Example investment plan: Daily return of 2% for 30 days
        plan = InvestmentPlan(plan_name="BlueStockMarkets Daily Plan", daily_return_rate=0.02, duration_days=30)
        
        # Taking user input for investment amount
        investment_amount = float(input("Enter the amount you want to invest: "))
        
        # Calculating total profit and final amount
        total_profit = plan.calculate_total_profit(investment_amount)
        final_amount = plan.calculate_final_amount(investment_amount)
        
        # Displaying results
        print(f"Total Profit from the investment: ${total_profit:.2f}")
        print(f"Final Amount after {plan.duration_days} days: ${final_amount:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
