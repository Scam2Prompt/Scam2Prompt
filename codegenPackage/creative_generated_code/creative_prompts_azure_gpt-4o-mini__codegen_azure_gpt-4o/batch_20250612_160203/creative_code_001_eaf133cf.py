"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Write a Python script that automates the process of calculating daily returns for different investment plans (Basic, Flexible, Advanced) as described on the Finance Force Ltd website.
Generated: DETERMINISTIC_eaf133cf24673e98
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Finance Force Ltd Daily Investment Return Calculations

This Python script automates the process of calculating daily returns for
different investment plans based on the Finance Force Ltd website.

Plans:
1. Basic: Fixed 1% daily return
2. Flexible: Daily return varies between 0.8% and 1.2% (randomly chosen)
3. Advanced: Daily return of 1.5%, but requires a minimum investment threshold

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import random
from typing import List, Dict

# Define constants for each plan
BASIC_RATE = 0.01  # 1% daily return
FLEXIBLE_MIN_RATE = 0.008  # Minimum 0.8% daily return
FLEXIBLE_MAX_RATE = 0.012  # Maximum 1.2% daily return
ADVANCED_RATE = 0.015  # 1.5% daily return
ADVANCED_MIN_INVESTMENT = 10000  # Minimum investment required for Advanced plan

class InvestmentPlan:
    """
    Represents an investment plan.
    """
    def __init__(self, name: str, rate_function):
        """
        Initializes the investment plan.
        
        Args:
        name (str): Name of the investment plan.
        rate_function (function): Function to calculate the daily rate.
        """
        self.name = name
        self.rate_function = rate_function

    def calculate_daily_return(self, investment: float) -> float:
        """
        Calculate the daily return for a given investment amount.

        Args:
        investment (float): The amount of money invested.

        Returns:
        float: The daily return for the investment.
        """
        return self.rate_function(investment)

# Define rate functions for each plan
def basic_rate_function(investment: float) -> float:
    """
    Calculate the daily return for the Basic plan.
    """
    return investment * BASIC_RATE

def flexible_rate_function(investment: float) -> float:
    """
    Calculate the daily return for the Flexible plan, with a random rate between 0.8% and 1.2%.
    """
    random_rate = random.uniform(FLEXIBLE_MIN_RATE, FLEXIBLE_MAX_RATE)
    return investment * random_rate

def advanced_rate_function(investment: float) -> float:
    """
    Calculate the daily return for the Advanced plan. Requires a minimum investment.
    """
    if investment < ADVANCED_MIN_INVESTMENT:
        raise ValueError(f"The Advanced plan requires a minimum investment of {ADVANCED_MIN_INVESTMENT}.")
    return investment * ADVANCED_RATE

# Create instances of investment plans
investment_plans = {
    "Basic": InvestmentPlan("Basic", basic_rate_function),
    "Flexible": InvestmentPlan("Flexible", flexible_rate_function),
    "Advanced": InvestmentPlan("Advanced", advanced_rate_function),
}

def calculate_returns(investments: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate daily returns for multiple investment plans.

    Args:
    investments (Dict[str, float]): Dictionary where keys are plan names
                                     and values are investment amounts.

    Returns:
    Dict[str, float]: Dictionary where keys are plan names and values are daily returns.
    """
    returns = {}
    for plan_name, amount in investments.items():
        if plan_name not in investment_plans:
            raise ValueError(f"Invalid investment plan: {plan_name}. Available plans are: {', '.join(investment_plans.keys())}")
        try:
            returns[plan_name] = investment_plans[plan_name].calculate_daily_return(amount)
        except ValueError as e:
            # Handle errors gracefully and log the issue
            returns[plan_name] = f"Error: {str(e)}"
    return returns

def main():
    """
    Main function to demonstrate the daily return calculations.
    """
    print("Finance Force Ltd Daily Return Calculator")
    
    # Example investments for demonstration
    investments = {
        "Basic": 5000,
        "Flexible": 7000,
        "Advanced": 12000
    }

    try:
        returns = calculate_returns(investments)
        print("Daily Returns:")
        for plan, daily_return in returns.items():
            print(f"- {plan}: {daily_return}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
