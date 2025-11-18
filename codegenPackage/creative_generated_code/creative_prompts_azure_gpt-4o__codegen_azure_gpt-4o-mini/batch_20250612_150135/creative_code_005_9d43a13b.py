"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptominnerfx.com
Prompt: Write code to integrate a profit calculator into a cryptocurrency investment platform, using Cryptominnerfx's investment plan structure as a model.
Generated: DETERMINISTIC_9d43a13b3654f9f4
Batch ID: 20250612_150135
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
    Represents an investment plan in the cryptocurrency platform.
    
    Attributes:
        plan_name (str): The name of the investment plan.
        min_investment (float): The minimum investment required for this plan.
        max_investment (float): The maximum investment allowed for this plan.
        profit_percentage (float): The profit percentage for this plan.
        duration_days (int): The duration of the investment plan in days.
    """
    
    def __init__(self, plan_name, min_investment, max_investment, profit_percentage, duration_days):
        self.plan_name = plan_name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.profit_percentage = profit_percentage
        self.duration_days = duration_days

    def calculate_profit(self, investment_amount):
        """
        Calculates the profit based on the investment amount.
        
        Args:
            investment_amount (float): The amount to invest.
        
        Returns:
            float: The profit generated after the investment duration.
        
        Raises:
            ValueError: If the investment amount is outside of the plan limits.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}.")

        # Calculate profit
        profit = investment_amount * (self.profit_percentage / 100.0)
        return profit


class ProfitCalculator:
    """
    A profit calculator for managing various investment plans.
    
    Attributes:
        plans (list): A list of available investment plans.
    """

    def __init__(self):
        self.plans = []

    def add_plan(self, plan):
        """
        Adds a new investment plan to the calculator.
        
        Args:
            plan (InvestmentPlan): An instance of InvestmentPlan to add.
        """
        if not isinstance(plan, InvestmentPlan):
            raise TypeError("Expected an instance of InvestmentPlan.")

        self.plans.append(plan)

    def calculate_total_profit(self, investment_amount, plan_name):
        """
        Calculates the total profit for a given investment amount and plan name.
        
        Args:
            investment_amount (float): The amount to invest.
            plan_name (str): The name of the investment plan.

        Returns:
            float: The calculated profit.

        Raises:
            ValueError: If the plan name does not exist or if the investment amount is invalid.
        """
        plan = next((p for p in self.plans if p.plan_name == plan_name), None)
        
        if plan is None:
            raise ValueError("Investment plan not found.")

        return plan.calculate_profit(investment_amount)


# Example of usage
if __name__ == "__main__":
    # Create investment plans
    plan1 = InvestmentPlan("Basic Plan", 100, 1000, 10, 30)
    plan2 = InvestmentPlan("Advanced Plan", 1000, 5000, 15, 60)

    # Initialize the profit calculator
    calculator = ProfitCalculator()
    calculator.add_plan(plan1)
    calculator.add_plan(plan2)

    # Calculate profits
    try:
        investment_amount = 500  # Example investment amount
        profit = calculator.calculate_total_profit(investment_amount, "Basic Plan")
        print(f"Profit for {investment_amount} in Basic Plan: {profit}")
        
        profit = calculator.calculate_total_profit(investment_amount, "Advanced Plan")
        print(f"Profit for {investment_amount} in Advanced Plan: {profit}")
    
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
```
