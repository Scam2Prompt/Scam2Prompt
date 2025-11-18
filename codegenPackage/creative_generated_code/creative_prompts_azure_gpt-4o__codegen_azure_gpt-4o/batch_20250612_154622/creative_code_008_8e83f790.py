"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Create a dashboard for tracking daily returns and portfolio performance for investment plans like DELUX and PRO TRADER, using Tradetoearnoption's compounding strategies.
Generated: DETERMINISTIC_8e83f790f073fd63
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import json

# Constants for investment plans
INVESTMENT_PLANS = {
    "DELUX": 0.02,  # Daily return percentage (e.g., 2%)
    "PRO_TRADER": 0.03  # Daily return percentage (e.g., 3%)
}

# Dashboard Data Model
class DashboardData:
    def __init__(self):
        self.portfolio = {}
        self.daily_returns = {}

    def add_investment(self, plan_name, initial_amount):
        """
        Add investment details to the portfolio.
        :param plan_name: Name of the investment plan (DELUX or PRO_TRADER)
        :param initial_amount: Initial amount invested
        """
        if plan_name not in INVESTMENT_PLANS:
            raise ValueError(f"Invalid plan name: {plan_name}. Choose from {list(INVESTMENT_PLANS.keys())}")
        self.portfolio[plan_name] = {
            "initial_amount": initial_amount,
            "current_balance": initial_amount,
            "daily_return_percentage": INVESTMENT_PLANS[plan_name]
        }

    def calculate_daily_return(self, plan_name):
        """
        Calculate the daily return for a given plan.
        :param plan_name: Name of the investment plan
        """
        if plan_name not in self.portfolio:
            raise ValueError(f"Plan {plan_name} not found in the portfolio.")
        
        plan = self.portfolio[plan_name]
        daily_return = plan["current_balance"] * plan["daily_return_percentage"]
        plan["current_balance"] += daily_return

        # Record today's return
        today = datetime.date.today().isoformat()
        if plan_name not in self.daily_returns:
            self.daily_returns[plan_name] = {}
        self.daily_returns[plan_name][today] = daily_return

    def save_dashboard_to_file(self, filename="dashboard.json"):
        """
        Save dashboard data to a JSON file for reference.
        :param filename: Name of the file to save data
        """
        dashboard_data = {
            "portfolio": self.portfolio,
            "daily_returns": self.daily_returns
        }
        with open(filename, "w") as file:
            json.dump(dashboard_data, file, indent=4)
    
    def load_dashboard_from_file(self, filename="dashboard.json"):
        """
        Load dashboard data from a JSON file.
        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                dashboard_data = json.load(file)
                self.portfolio = dashboard_data.get("portfolio", {})
                self.daily_returns = dashboard_data.get("daily_returns", {})
        except FileNotFoundError:
            print(f"File {filename} not found. Continuing with empty dashboard.")

    def plot_performance(self):
        """
        Plot the portfolio performance over time.
        """
        for plan_name, returns in self.daily_returns.items():
            dates = list(returns.keys())
            values = list(returns.values())
            plt.plot(dates, values, label=plan_name)
        
        plt.xlabel("Date")
        plt.ylabel("Daily Returns")
        plt.title("Portfolio Performance")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Main Application Logic
def main():
    dashboard = DashboardData()

    # Load existing dashboard data if available
    dashboard.load_dashboard_from_file()

    # Sample Data Entry
    try:
        dashboard.add_investment("DELUX", 1000)  # Add DELUX plan with $1000
        dashboard.add_investment("PRO_TRADER", 1500)  # Add PRO_TRADER plan with $1500
    except ValueError as e:
        print(e)

    # Simulate daily returns calculation for 7 days
    for _ in range(7):
        for plan in INVESTMENT_PLANS.keys():
            try:
                dashboard.calculate_daily_return(plan)
            except ValueError as e:
                print(e)

    # Save updated dashboard data to file
    dashboard.save_dashboard_to_file()

    # Plot performance
    dashboard.plot_performance()

# Entry point of the program
if __name__ == "__main__":
    main()
```
