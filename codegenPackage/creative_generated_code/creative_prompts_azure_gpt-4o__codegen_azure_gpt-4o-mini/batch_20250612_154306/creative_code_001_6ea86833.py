"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Recommend a Python library or API to model variable interest rates for savings plans, such as the "Epargne Revenus" formula with a variable average rate of 9.24% (2023), and provide an example of its implementation.
Generated: DETERMINISTIC_6ea86833e90a32d5
Batch ID: 20250612_154306
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
import matplotlib.pyplot as plt

class VariableInterestRateModel:
    """
    A class to model variable interest rates for savings plans such as 'Epargne Revenus'.
    """

    def __init__(self, initial_amount: float, rate: float, years: int):
        """
        Initialize the model with initial savings amount, interest rate, and duration in years.

        :param initial_amount: The starting balance of the savings account.
        :param rate: The annual interest rate (as a decimal).
        :param years: The number of years to calculate savings.
        """
        self.initial_amount = initial_amount
        self.rate = rate
        self.years = years
        self.balance_over_time = []

    def calculate_balance(self):
        """
        Calculate the balance over the specified number of years, applying the variable interest rate annually.
        """
        try:
            balance = self.initial_amount
            for year in range(1, self.years + 1):
                interest = balance * self.rate
                balance += interest
                self.balance_over_time.append(balance)
        except Exception as e:
            print(f"Error during calculation: {e}")

    def plot_balance(self):
        """
        Plot the balance over time.
        """
        try:
            years = np.arange(1, self.years + 1)
            plt.figure(figsize=(10, 5))
            plt.plot(years, self.balance_over_time, marker='o')
            plt.title('Savings Balance Over Time with Variable Interest Rate')
            plt.xlabel('Years')
            plt.ylabel('Balance')
            plt.grid()
            plt.xticks(years)
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")

# Example usage
if __name__ == "__main__":
    # Define variables
    initial_savings = 10000  # Initial savings amount in currency
    interest_rate = 0.0924    # Variable average rate in decimal form
    investment_duration = 10   # Duration in years
    
    # Create an instance of the model
    savings_model = VariableInterestRateModel(initial_savings, interest_rate, investment_duration)

    # Calculate the balance over time
    savings_model.calculate_balance()

    # Plot the balance over time
    savings_model.plot_balance()
```
