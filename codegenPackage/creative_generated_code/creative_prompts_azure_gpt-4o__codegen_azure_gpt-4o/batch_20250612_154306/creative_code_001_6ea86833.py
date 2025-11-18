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
"""
Example implementation to model variable interest rates for savings plans using the 'numpy' library.
The code simulates the growth of savings based on the "Epargne Revenus" formula with a variable average rate.
"""

import numpy as np

class SavingsPlan:
    def __init__(self, initial_amount: float, annual_rate: float, years: int):
        """
        Initialize the savings plan.

        :param initial_amount: Initial deposit amount.
        :param annual_rate: The average annual interest rate (as a percentage).
        :param years: Time period in years for the savings plan.
        """
        if initial_amount < 0:
            raise ValueError("Initial amount must be non-negative.")
        if annual_rate < 0:
            raise ValueError("Annual rate must be non-negative.")
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")
        
        self.initial_amount = initial_amount
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years

    def simulate_growth(self):
        """
        Simulate the growth of savings over the specified years with variable annual rates.

        :return: A list of balances at the end of each year.
        """
        balances = [self.initial_amount]
        for year in range(1, self.years + 1):
            # Simulate a variable rate based on fluctuations (example: ±1% around the average rate)
            rate_fluctuation = np.random.uniform(-0.01, 0.01)  # Fluctuation factor
            effective_rate = self.annual_rate + rate_fluctuation
            
            # Calculate the balance with compound interest
            previous_balance = balances[-1]
            new_balance = previous_balance * (1 + effective_rate)
            balances.append(new_balance)
        
        return balances

    def display_results(self):
        """
        Display the results of the simulation in a user-friendly format.
        """
        balances = self.simulate_growth()
        print("Yearly balances for the savings plan:")
        for year, balance in enumerate(balances):
            print(f"Year {year}: ${balance:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a savings plan with an initial deposit of $10,000, an average rate of 9.24%, and a 10-year duration
        savings_plan = SavingsPlan(initial_amount=10000, annual_rate=9.24, years=10)
        savings_plan.display_results()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
