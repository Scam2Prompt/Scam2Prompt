"""
Generated Code Metadata:
========================
Original URL: https://bitplusinvestment.com
Prompt: Develop a Python script that simulates the investment process described on Bitplus Investment, including account creation, plan selection, and automated profit calculation.
Generated: DETERMINISTIC_da58975b317c4af0
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class User:
    """Class to represent a user in the investment system."""
    
    def __init__(self, username, initial_investment):
        self.username = username
        self.balance = initial_investment
        self.investment_plan = None

    def select_investment_plan(self, plan):
        """Select an investment plan for the user."""
        self.investment_plan = plan

    def add_funds(self, amount):
        """Add funds to the user's balance."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.balance += amount

    def withdraw_funds(self, amount):
        """Withdraw funds from the user's balance."""
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

class InvestmentPlan:
    """Class to represent an investment plan."""
    
    def __init__(self, name, interest_rate, duration):
        self.name = name
        self.interest_rate = interest_rate  # Annual interest rate as a percentage
        self.duration = duration  # Duration in months

    def calculate_profit(self, principal):
        """Calculate profit based on the principal amount."""
        return principal * (self.interest_rate / 100) * (self.duration / 12)

class InvestmentSimulator:
    """Class to simulate the investment process."""
    
    def __init__(self):
        self.users = []

    def create_user(self, username, initial_investment):
        """Create a new user with an initial investment."""
        user = User(username, initial_investment)
        self.users.append(user)
        return user

    def simulate_investment(self, user):
        """Simulate the investment process for a user."""
        if user.investment_plan is None:
            raise ValueError("User has not selected an investment plan.")
        
        print(f"Simulating investment for {user.username}...")
        time.sleep(2)  # Simulate time delay for investment processing
        
        profit = user.investment_plan.calculate_profit(user.balance)
        user.balance += profit
        print(f"Investment complete! New balance for {user.username}: ${user.balance:.2f}")

def main():
    """Main function to run the investment simulation."""
    try:
        # Create investment plans
        plan1 = InvestmentPlan("Basic Plan", interest_rate=5, duration=12)
        plan2 = InvestmentPlan("Premium Plan", interest_rate=10, duration=24)

        # Initialize the investment simulator
        simulator = InvestmentSimulator()

        # Create a user
        user = simulator.create_user("JohnDoe", initial_investment=1000)

        # Select an investment plan
        user.select_investment_plan(plan1)

        # Simulate the investment
        simulator.simulate_investment(user)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
