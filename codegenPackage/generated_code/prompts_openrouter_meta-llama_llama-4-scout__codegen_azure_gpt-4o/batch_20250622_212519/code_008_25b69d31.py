"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Provide a sample investment plan for a long-term investor using a robo-advisor platform or a Python-based investment tool.
Generated: DETERMINISTIC_25b69d31ec01efb9
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from datetime import datetime

# Define the investment plan class
class InvestmentPlan:
    """
    A class to generate a sample investment plan for a long-term investor using a Python-based tool.
    """

    def __init__(self, initial_investment, monthly_contribution, years, risk_tolerance):
        """
        Initialize the investment plan.

        :param initial_investment: Initial amount invested (float).
        :param monthly_contribution: Monthly contribution amount (float).
        :param years: Investment duration in years (int).
        :param risk_tolerance: Risk tolerance level ('low', 'medium', 'high') (str).
        """
        self.initial_investment = initial_investment
        self.monthly_contribution = monthly_contribution
        self.years = years
        self.risk_tolerance = risk_tolerance
        self.annual_return = self._get_annual_return()

    def _get_annual_return(self):
        """
        Determine the annual return rate based on risk tolerance.

        :return: Annual return rate (float).
        """
        risk_return_map = {
            'low': 0.04,  # 4% annual return for low risk
            'medium': 0.06,  # 6% annual return for medium risk
            'high': 0.08  # 8% annual return for high risk
        }
        return risk_return_map.get(self.risk_tolerance, 0.06)  # Default to medium risk if invalid input

    def calculate_growth(self):
        """
        Calculate the investment growth over the specified duration.

        :return: DataFrame containing yearly investment growth details.
        """
        total_months = self.years * 12
        monthly_return = self.annual_return / 12
        balance = self.initial_investment
        growth_data = []

        for month in range(1, total_months + 1):
            balance += self.monthly_contribution  # Add monthly contribution
            balance *= (1 + monthly_return)  # Apply monthly return
            if month % 12 == 0:  # Record data at the end of each year
                growth_data.append({
                    'Year': month // 12,
                    'Balance': round(balance, 2)
                })

        return pd.DataFrame(growth_data)

    def generate_plan(self):
        """
        Generate the investment plan.

        :return: DataFrame containing the investment plan details.
        """
        return self.calculate_growth()


# Main function to demonstrate the investment plan
def main():
    """
    Main function to create and display a sample investment plan.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter initial investment amount (e.g., 10000): "))
        monthly_contribution = float(input("Enter monthly contribution amount (e.g., 500): "))
        years = int(input("Enter investment duration in years (e.g., 20): "))
        risk_tolerance = input("Enter risk tolerance ('low', 'medium', 'high'): ").lower()

        # Validate inputs
        if initial_investment < 0 or monthly_contribution < 0 or years <= 0:
            raise ValueError("Investment amounts and duration must be positive values.")
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("Risk tolerance must be one of: 'low', 'medium', 'high'.")

        # Create investment plan
        plan = InvestmentPlan(initial_investment, monthly_contribution, years, risk_tolerance)
        growth_df = plan.generate_plan()

        # Display the plan
        print("\nSample Investment Plan:")
        print(growth_df)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
