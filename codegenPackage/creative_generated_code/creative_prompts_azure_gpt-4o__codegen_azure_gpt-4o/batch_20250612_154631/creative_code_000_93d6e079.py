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
# Profit Calculator for Investment Plans offered by BlueStockMarkets

class InvestmentPlan:
    """
    Represents an investment plan with daily return rate and duration.
    """
    def __init__(self, plan_name, daily_return_rate, duration_days):
        """
        Initialize the investment plan.
        
        :param plan_name: Name of the investment plan
        :param daily_return_rate: Daily return rate as a percentage (e.g., 2 for 2%)
        :param duration_days: Duration of the plan in days
        """
        self.plan_name = plan_name
        self.daily_return_rate = daily_return_rate / 100  # Convert percentage to decimal
        self.duration_days = duration_days

    def calculate_daily_profit(self, investment_amount):
        """
        Calculate daily profit based on the investment amount.
        
        :param investment_amount: Amount invested
        :return: Daily profit
        """
        return investment_amount * self.daily_return_rate

    def calculate_total_profit(self, investment_amount):
        """
        Calculate total profit for the duration of the plan based on the investment amount.
        
        :param investment_amount: Amount invested
        :return: Total profit over the plan's duration
        """
        daily_profit = self.calculate_daily_profit(investment_amount)
        return daily_profit * self.duration_days


def main():
    """
    Main function to run the profit calculator.
    """
    print("Welcome to BlueStockMarkets Profit Calculator!")

    try:
        # Get investment details from the user
        investment_amount = float(input("Enter the investment amount: $"))
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Define the available plans
        plans = [
            InvestmentPlan("Starter Plan", daily_return_rate=1.5, duration_days=30),
            InvestmentPlan("Pro Plan", daily_return_rate=2, duration_days=60),
            InvestmentPlan("Elite Plan", daily_return_rate=2.5, duration_days=90),
        ]

        # Display the available plans
        print("\nAvailable Investment Plans:")
        for i, plan in enumerate(plans):
            print(f"{i + 1}. {plan.plan_name} - {plan.daily_return_rate * 100}% daily return for {plan.duration_days} days")

        # Get the user's plan choice
        plan_choice = int(input("\nSelect a plan (1-3): "))
        if plan_choice < 1 or plan_choice > len(plans):
            raise ValueError("Invalid plan selection.")

        # Select the chosen plan
        selected_plan = plans[plan_choice - 1]

        # Calculate profits
        daily_profit = selected_plan.calculate_daily_profit(investment_amount)
        total_profit = selected_plan.calculate_total_profit(investment_amount)

        # Display the results
        print("\nInvestment Summary:")
        print(f"Plan Selected: {selected_plan.plan_name}")
        print(f"Daily Profit: ${daily_profit:.2f}")
        print(f"Total Profit after {selected_plan.duration_days} days: ${total_profit:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    main()
```
