"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acextradex.ltd
Prompt: Develop a script that simulates the investment process on Acex Tradex, allowing users to select an investment plan and calculate their returns over time.
Generated: DETERMINISTIC_56ccd4c42ea81c4b
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    def __init__(self, name, interest_rate, duration_years):
        """
        Initializes an investment plan with name, interest rate, and duration.

        :param name: str : Name of the investment plan
        :param interest_rate: float : Annual interest rate (as a percentage)
        :param duration_years: int : Duration of the investment in years
        """
        self.name = name
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_return(self, principal):
        """
        Calculates the total return on investment after a specified duration.

        :param principal: float : Initial investment amount
        :return: float : Total return after duration
        """
        return principal * (1 + self.interest_rate) ** self.duration_years


class InvestmentSimulator:
    def __init__(self):
        """
        Initializes the investment simulator with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("Basic Plan", 5.0, 5),
            InvestmentPlan("Advanced Plan", 7.5, 10),
            InvestmentPlan("Premium Plan", 10.0, 15),
        ]

    def display_plans(self):
        """
        Displays available investment plans to the user.
        """
        print("Available Investment Plans:")
        for idx, plan in enumerate(self.plans):
            print(f"{idx + 1}. {plan.name} - {plan.interest_rate * 100}% interest for {plan.duration_years} years")

    def get_user_selection(self):
        """
        Gets the user's selection of investment plan and amount.

        :return: InvestmentPlan, float : Selected investment plan and principal amount
        """
        try:
            selection = int(input("Select an investment plan (number): ")) - 1
            if selection < 0 or selection >= len(self.plans):
                raise ValueError("Invalid selection.")
            principal = float(input("Enter the amount to invest: "))
            if principal <= 0:
                raise ValueError("Investment amount must be greater than zero.")
            return self.plans[selection], principal
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    def simulate_investment(self):
        """
        Runs the investment simulation process.
        """
        self.display_plans()
        plan, principal = self.get_user_selection()
        total_return = plan.calculate_return(principal)
        print(f"Investment in '{plan.name}' will yield a total of ${total_return:.2f} after {plan.duration_years} years.")


if __name__ == "__main__":
    simulator = InvestmentSimulator()
    simulator.simulate_investment()
```
