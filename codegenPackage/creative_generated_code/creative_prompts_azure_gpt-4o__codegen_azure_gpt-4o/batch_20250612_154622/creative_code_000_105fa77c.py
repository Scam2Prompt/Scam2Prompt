"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write Python code to calculate investment returns using the profit calculator parameters from Tradetoearnoption, including interest rates and maturity periods for plans like BASIC, SILVER, and GOLD.
Generated: DETERMINISTIC_105fa77c31d88343
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Returns Calculator

This script calculates investment returns for three predefined plans (BASIC, SILVER, GOLD) 
based on interest rates and maturity periods provided by Tradetoearnoption. 
"""

# Importing necessary modules
from typing import Union


class InvestmentPlan:
    """
    Class representing an investment plan.
    """
    def __init__(self, name: str, interest_rate: float, maturity_period: int):
        """
        Initializes the investment plan.

        :param name: Name of the plan (e.g., BASIC, SILVER, GOLD)
        :param interest_rate: Annual interest rate (in percentage)
        :param maturity_period: Maturity period in years
        """
        self.name = name
        self.interest_rate = interest_rate
        self.maturity_period = maturity_period

    def calculate_returns(self, principal: Union[int, float]) -> float:
        """
        Calculates the returns based on the principal and plan parameters.

        :param principal: Initial investment amount
        :return: Total investment returns after maturity period
        """
        try:
            # Formula: A = P * (1 + r / 100)^t
            returns = principal * (1 + self.interest_rate / 100) ** self.maturity_period
            return round(returns, 2)  # Round to 2 decimal places for clarity
        except Exception as e:
            # Catch any unexpected errors and raise a meaningful exception
            raise ValueError(f"Error calculating returns: {e}")


def main():
    """
    Main function to calculate investment returns for different plans.
    """
    try:
        # Predefined investment plans
        plans = {
            "BASIC": InvestmentPlan(name="BASIC", interest_rate=5.0, maturity_period=1),
            "SILVER": InvestmentPlan(name="SILVER", interest_rate=7.5, maturity_period=3),
            "GOLD": InvestmentPlan(name="GOLD", interest_rate=10.0, maturity_period=5),
        }

        # User input for principal amount
        principal = float(input("Enter the principal amount (e.g., 1000.00): "))

        # Validate principal amount
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")

        print("\nInvestment Returns:")
        print("-------------------")

        # Calculate and display returns for each plan
        for plan_name, plan in plans.items():
            returns = plan.calculate_returns(principal)
            print(f"{plan_name} Plan: ${returns} (Principal: ${principal})")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
```
