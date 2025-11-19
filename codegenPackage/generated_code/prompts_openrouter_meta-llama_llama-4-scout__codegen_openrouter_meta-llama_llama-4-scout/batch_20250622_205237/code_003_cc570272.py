"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Design a retirement planning tool that takes into account ESG (Environmental, Social, and Governance) factors, using Grade World Investment Limited's wealth planning services as a reference.
Generated: DETERMINISTIC_cc5702722a842245
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import pandas as pd

class RetirementPlanner:
    """
    A retirement planning tool that takes into account ESG factors.

    Attributes:
    -----------
    current_age : int
        The current age of the user.
    retirement_age : int
        The desired retirement age of the user.
    current_savings : float
        The current savings of the user.
    annual_expenses : float
        The annual expenses of the user in retirement.
    esg_score : float
        The ESG score of the investment portfolio.
    annual_return : float
        The expected annual return on investment.

    Methods:
    --------
    calculate_savings_needed()
        Calculates the total savings needed for retirement.
    calculate_monthly_investment()
        Calculates the monthly investment needed to reach the savings goal.
    assess_esg_risk()
        Assesses the ESG risk of the investment portfolio.
    """

    def __init__(self, current_age, retirement_age, current_savings, annual_expenses, esg_score, annual_return):
        """
        Initializes the RetirementPlanner object.

        Parameters:
        -----------
        current_age : int
            The current age of the user.
        retirement_age : int
            The desired retirement age of the user.
        current_savings : float
            The current savings of the user.
        annual_expenses : float
            The annual expenses of the user in retirement.
        esg_score : float
            The ESG score of the investment portfolio.
        annual_return : float
            The expected annual return on investment.
        """
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.current_savings = current_savings
        self.annual_expenses = annual_expenses
        self.esg_score = esg_score
        self.annual_return = annual_return

    def calculate_savings_needed(self):
        """
        Calculates the total savings needed for retirement.

        Returns:
        --------
        float
            The total savings needed for retirement.
        """
        years_until_retirement = self.retirement_age - self.current_age
        savings_needed = self.annual_expenses * 25  # Assuming 25 years in retirement
        return savings_needed

    def calculate_monthly_investment(self):
        """
        Calculates the monthly investment needed to reach the savings goal.

        Returns:
        --------
        float
            The monthly investment needed to reach the savings goal.
        """
        savings_needed = self.calculate_savings_needed()
        years_until_retirement = self.retirement_age - self.current_age
        months_until_retirement = years_until_retirement * 12
        monthly_return = (1 + self.annual_return) ** (1 / 12) - 1
        monthly_investment = (savings_needed - self.current_savings) * monthly_return / ((1 + monthly_return) ** months_until_retirement - 1)
        return round(monthly_investment, 2)

    def assess_esg_risk(self):
        """
        Assesses the ESG risk of the investment portfolio.

        Returns:
        --------
        str
            The ESG risk level (Low, Medium, High).
        """
        if self.esg_score >= 7:
            return "Low"
        elif self.esg_score >= 4:
            return "Medium"
        else:
            return "High"


def main():
    try:
        # Get user input
        current_age = int(input("Enter your current age: "))
        retirement_age = int(input("Enter your desired retirement age: "))
        current_savings = float(input("Enter your current savings: "))
        annual_expenses = float(input("Enter your annual expenses in retirement: "))
        esg_score = float(input("Enter the ESG score of your investment portfolio: "))
        annual_return = float(input("Enter the expected annual return on investment: "))

        # Create RetirementPlanner object
        planner = RetirementPlanner(current_age, retirement_age, current_savings, annual_expenses, esg_score, annual_return / 100)

        # Calculate and display results
        savings_needed = planner.calculate_savings_needed()
        monthly_investment = planner.calculate_monthly_investment()
        esg_risk = planner.assess_esg_risk()

        print(f"Total savings needed for retirement: ${savings_needed:,.2f}")
        print(f"Monthly investment needed: ${monthly_investment:,.2f}")
        print(f"ESG risk level: {esg_risk}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
```
