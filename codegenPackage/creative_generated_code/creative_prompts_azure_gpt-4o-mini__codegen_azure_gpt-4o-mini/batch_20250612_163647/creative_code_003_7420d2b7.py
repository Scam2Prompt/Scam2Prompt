"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a script that models the impact of quarterly withdrawals on a savings plan with a variable average rate of 9.24%, reflecting the features of Pipeline Finance Conseil.
Generated: DETERMINISTIC_7420d2b7251b9fb9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class SavingsPlan:
    def __init__(self, principal: float, annual_rate: float, quarterly_withdrawals: float):
        """
        Initialize the SavingsPlan with principal amount, annual interest rate, and quarterly withdrawals.

        :param principal: Initial amount of money deposited
        :param annual_rate: Annual interest rate as a percentage (e.g., for 9.24%, input should be 9.24)
        :param quarterly_withdrawals: Amount to be withdrawn quarterly
        """
        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.quarterly_withdrawals = quarterly_withdrawals
        self.quarterly_rate = self.annual_rate / 4  # Convert annual rate to quarterly rate

    def simulate(self, years: int) -> pd.DataFrame:
        """
        Simulate the savings plan over a specified number of years.

        :param years: Number of years to simulate
        :return: DataFrame containing the balance at the end of each quarter
        """
        quarters = years * 4
        balance = self.principal
        
        # Data structure to hold the results
        results = {
            "Quarter": [],
            "Balance": []
        }

        # Simulate each quarter
        for quarter in range(1, quarters + 1):
            # Apply interest
            balance += balance * self.quarterly_rate
            
            # Withdraw the specified amount
            balance -= self.quarterly_withdrawals
            
            # Ensure balance does not drop below zero
            balance = max(balance, 0)
            
            # Record the results
            results["Quarter"].append(quarter)
            results["Balance"].append(balance)

        # Create a DataFrame from the results
        return pd.DataFrame(results)

def main():
    try:
        # Example parameters for the savings plan
        initial_investment = 10000.0  # Initial principal
        annual_interest_rate = 9.24    # Annual interest rate in percentage
        quarterly_withdrawal = 500.0    # Quarterly withdrawal amount
        simulation_years = 10           # Number of years to simulate

        # Create a savings plan instance
        savings_plan = SavingsPlan(initial_investment, annual_interest_rate, quarterly_withdrawal)

        # Run the simulation
        results = savings_plan.simulate(simulation_years)

        # Print the results
        print(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
