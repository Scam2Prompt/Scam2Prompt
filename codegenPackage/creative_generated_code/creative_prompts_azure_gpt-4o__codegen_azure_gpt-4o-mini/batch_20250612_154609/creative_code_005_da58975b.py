"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplusinvestment.com
Prompt: Develop a Python script that simulates the investment process described on Bitplus Investment, including account creation, plan selection, and automated profit calculation.
Generated: DETERMINISTIC_da58975b317c4af0
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class InvestmentAccount:
    """
    Class representing an investment account for a user.
    """
    def __init__(self, username, initial_deposit):
        """
        Initialize the investment account with a username and initial deposit.

        :param username: str - the user's chosen username
        :param initial_deposit: float - the initial amount of money to deposit
        """
        self.username = username
        self.balance = initial_deposit
        self.investment_plan = None
        self.investment_duration = 0

    def select_plan(self, plan_name, duration):
        """
        Select an investment plan for the account.

        :param plan_name: str - the name of the investment plan
        :param duration: int - the duration of the investment in days
        """
        self.investment_plan = plan_name
        self.investment_duration = duration

    def calculate_profit(self):
        """
        Calculate the profit based on the selected investment plan.

        :return: float - the calculated profit
        """
        if not self.investment_plan:
            raise ValueError("No investment plan selected")
        
        # Simulating different profit rates based on the plan
        profit_rates = {
            'Basic': 0.05,  # 5% profit
            'Standard': 0.1,  # 10% profit
            'Premium': 0.15   # 15% profit
        }
        
        if self.investment_plan not in profit_rates:
            raise ValueError("Invalid investment plan selected")

        profit = self.balance * profit_rates[self.investment_plan] * self.investment_duration
        return profit

    def finalize_investment(self):
        """
        Finalize the investment by calculating profit and resetting the account.
        """
        if self.investment_duration <= 0:
            raise ValueError("Investment duration must be greater than 0")

        profit = self.calculate_profit()
        self.balance += profit
        print(f"Investment completed! Total balance after {self.investment_duration} days: ${self.balance:.2f}")
        
        # Resetting investment plan and duration
        self.investment_plan = None
        self.investment_duration = 0


def create_account():
    """
    Create a new investment account by collecting user input.
    
    :return: InvestmentAccount - the newly created investment account
    """
    username = input("Enter your username: ")
    
    while True:
        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
            if initial_deposit <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            break
        except ValueError as e:
            print(e)

    return InvestmentAccount(username, initial_deposit)


def main():
    """
    Main function to run the investment simulation.
    """
    print("Welcome to the Bitplus Investment Simulator!")
    
    # Create a new account
    account = create_account()
    
    # Select an investment plan
    plans = ['Basic', 'Standard', 'Premium']
    print(f"Available plans: {', '.join(plans)}")
    plan = input("Select an investment plan: ")
    
    while plan not in plans:
        print("Invalid plan. Please choose again.")
        plan = input("Select an investment plan: ")

    while True:
        try:
            duration = int(input("Enter investment duration in days: "))
            if duration <= 0:
                raise ValueError("Duration must be greater than zero.")
            break
        except ValueError as e:
            print(e)

    account.select_plan(plan, duration)
    
    # Simulate investment duration
    print(f"Investing for {duration} days in the {plan} plan...")
    time.sleep(2)  # Simulate waiting period

    # Finalize investment and display results
    account.finalize_investment()


if __name__ == "__main__":
    main()
```
