"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: Create a script to simulate the returns for Tradezeenetwork's investment plans (Starter, Advanced, Classic, Expert), including deposit limits, profit percentages, and withdrawal schedules.
Generated: DETERMINISTIC_98512d2d416a6142
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class InvestmentPlan:
    """
    Represents an investment plan with specific parameters.
    """
    
    def __init__(self, name, min_deposit, max_deposit, profit_percentage, withdrawal_frequency_days):
        """
        Initializes an investment plan with its parameters.
        
        Args:
            name (str): The name of the investment plan.
            min_deposit (float): Minimum deposit for the plan.
            max_deposit (float): Maximum deposit for the plan.
            profit_percentage (float): Profit percentage per period.
            withdrawal_frequency_days (int): Number of days between withdrawals.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.profit_percentage = profit_percentage
        self.withdrawal_frequency_days = withdrawal_frequency_days
        
    def calculate_profit(self, deposit, periods):
        """
        Calculates the total profit over a given number of periods.
        
        Args:
            deposit (float): The amount deposited.
            periods (int): Number of periods to calculate profit for.
        
        Returns:
            float: Total profit earned.
        """
        return deposit * (self.profit_percentage / 100) * periods


class InvestmentSimulator:
    """
    Simulates investments based on selected plans.
    """
    
    def __init__(self):
        """
        Initializes the investment simulator with available plans.
        """
        self.plans = {
            'Starter': InvestmentPlan('Starter', 100, 1000, 5, 30),
            'Advanced': InvestmentPlan('Advanced', 1000, 5000, 7, 15),
            'Classic': InvestmentPlan('Classic', 5000, 20000, 10, 7),
            'Expert': InvestmentPlan('Expert', 20000, 100000, 15, 1)
        }
        
    def simulate_investment(self, plan_name, deposit, investment_duration_days):
        """
        Simulates the investment return based on the selected plan and deposit.
        
        Args:
            plan_name (str): The name of the investment plan.
            deposit (float): The amount to invest.
            investment_duration_days (int): Total investment duration in days.
        
        Returns:
            dict: Contains investment details and returns.
        """
        try:
            plan = self.plans[plan_name]
        except KeyError:
            raise ValueError(f"Investment plan '{plan_name}' does not exist.")
        
        if deposit < plan.min_deposit or deposit > plan.max_deposit:
            raise ValueError(f"Deposit must be between {plan.min_deposit} and {plan.max_deposit} for the {plan_name} plan.")
        
        # Calculate the number of withdrawal periods
        periods = investment_duration_days // plan.withdrawal_frequency_days

        # Calculate total profit
        total_profit = plan.calculate_profit(deposit, periods)
        total_return = deposit + total_profit
        
        return {
            'plan': plan_name,
            'deposit': deposit,
            'total_profit': total_profit,
            'total_return': total_return,
            'periods': periods
        }

def main():
    """
    Main function to run the investment simulator.
    """
    simulator = InvestmentSimulator()

    # Example investment simulation
    plan_name = 'Advanced'  # Change as needed
    deposit = 2000          # Change as needed
    investment_duration_days = 90  # Change as needed

    try:
        result = simulator.simulate_investment(plan_name, deposit, investment_duration_days)
        print(f"Investment simulation result for {plan_name}:")
        print(f"Deposit: ${result['deposit']:.2f}")
        print(f"Total Profit: ${result['total_profit']:.2f}")
        print(f"Total Return: ${result['total_return']:.2f}")
        print(f"Periods: {result['periods']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
