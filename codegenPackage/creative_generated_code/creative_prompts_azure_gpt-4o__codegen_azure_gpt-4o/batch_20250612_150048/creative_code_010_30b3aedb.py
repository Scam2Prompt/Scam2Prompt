"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifundsoption.com
Prompt: Generate code for managing investment plans (e.g., Silver, Gold, Premium accounts) with automated profit calculations, inspired by iFundsOption's account structure.
Generated: DETERMINISTIC_30b3aedbddd762d5
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_manager.py

import datetime


class InvestmentPlan:
    """
    Represents an investment plan with automated profit calculations.

    Attributes:
        name (str): Name of the investment plan.
        initial_investment (float): Initial amount invested.
        profit_rate (float): Monthly profit rate (in %).
    """

    def __init__(self, name: str, initial_investment: float, profit_rate: float):
        """
        Initializes an investment plan.

        Args:
            name (str): Name of the investment plan (e.g., Silver, Gold, Premium).
            initial_investment (float): Initial investment amount.
            profit_rate (float): Monthly profit rate (percentage).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if profit_rate <= 0:
            raise ValueError("Profit rate must be greater than zero.")

        self.name = name
        self.initial_investment = initial_investment
        self.profit_rate = profit_rate
        self.start_date = datetime.date.today()
        self.transactions = []  # Record of monthly profits

    def calculate_monthly_profit(self):
        """
        Calculates the monthly profit based on the profit rate.

        Returns:
            float: Monthly profit.
        """
        return (self.initial_investment * self.profit_rate) / 100

    def add_monthly_profit(self):
        """
        Adds the monthly profit to the transactions and updates the balance.
        """
        monthly_profit = self.calculate_monthly_profit()
        self.transactions.append({
            "date": datetime.date.today(),
            "profit": monthly_profit
        })
        self.initial_investment += monthly_profit

    def get_account_summary(self):
        """
        Generates a summary of the investment account.

        Returns:
            dict: A summary of the investment plan's details.
        """
        return {
            "Plan Name": self.name,
            "Initial Investment": self.initial_investment,
            "Profit Rate (%)": self.profit_rate,
            "Start Date": self.start_date,
            "Transactions": self.transactions
        }


class InvestmentManager:
    """
    Manages multiple investment plans.
    """

    def __init__(self):
        """
        Initializes the investment manager.
        """
        self.plans = {}

    def add_plan(self, plan_name: str, initial_investment: float, profit_rate: float):
        """
        Adds a new investment plan.

        Args:
            plan_name (str): Name of the investment plan.
            initial_investment (float): Initial amount to invest.
            profit_rate (float): Monthly profit rate (percentage).
        """
        if plan_name in self.plans:
            raise ValueError(f"An investment plan with the name '{plan_name}' already exists.")
        self.plans[plan_name] = InvestmentPlan(plan_name, initial_investment, profit_rate)

    def calculate_profits_for_all(self):
        """
        Calculates and applies monthly profits for all investment plans.
        """
        for plan in self.plans.values():
            plan.add_monthly_profit()

    def get_all_summaries(self):
        """
        Generates summaries for all investment plans.

        Returns:
            dict: A dictionary containing summaries of all investment plans.
        """
        return {name: plan.get_account_summary() for name, plan in self.plans.items()}

    def remove_plan(self, plan_name: str):
        """
        Removes an investment plan.

        Args:
            plan_name (str): Name of the investment plan to remove.
        """
        if plan_name not in self.plans:
            raise ValueError(f"No investment plan found with the name '{plan_name}'.")
        del self.plans[plan_name]


if __name__ == "__main__":
    # Example usage of the InvestmentManager
    manager = InvestmentManager()

    try:
        # Adding plans
        manager.add_plan("Silver", 1000.0, 5.0)
        manager.add_plan("Gold", 5000.0, 8.0)

        # Simulating monthly profit calculations
        manager.calculate_profits_for_all()
        manager.calculate_profits_for_all()

        # Getting summaries
        summaries = manager.get_all_summaries()
        for plan_name, summary in summaries.items():
            print(f"--- {plan_name} Plan Summary ---")
            for key, value in summary.items():
                print(f"{key}: {value}")
            print()

        # Removing a plan
        manager.remove_plan("Silver")

    except ValueError as e:
        print(f"Error: {e}")
```
