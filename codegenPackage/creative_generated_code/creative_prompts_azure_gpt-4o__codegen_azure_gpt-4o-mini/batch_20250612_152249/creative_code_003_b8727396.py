"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjuicefinance.pages.dev
Prompt: Write a script to simulate lending USDB and calculate the expected APY based on the variable rates provided by AppJuice Finance.
Generated: DETERMINISTIC_b8727396ef1583b2
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class LendingSimulator:
    def __init__(self, principal: float, days: int, variable_rate: float):
        """
        Initialize the lending simulator with principal amount, duration in days, and variable interest rate.
        
        :param principal: The amount of USDB to be lent.
        :param days: The number of days for which the amount is lent.
        :param variable_rate: The annual percentage yield (APY) as a decimal (e.g., 0.05 for 5%).
        """
        self.principal = principal
        self.days = days
        self.variable_rate = variable_rate

    def calculate_interest(self) -> float:
        """
        Calculate the total interest earned based on the principal, variable rate, and duration.
        
        :return: Total interest earned.
        """
        try:
            # Ensure that principal, days, and variable_rate are valid
            if self.principal < 0 or self.days < 0 or not (0 <= self.variable_rate <= 1):
                raise ValueError("Invalid input values. Ensure principal and days are non-negative, and variable_rate is between 0 and 1.")

            # Calculate the interest earned using simple interest formula
            interest = self.principal * self.variable_rate * (self.days / 365)
            return interest
            
        except Exception as e:
            print(f"Error calculating interest: {e}")
            return 0.0

    def total_return(self) -> float:
        """
        Calculate the total return after lending, including principal and interest.
        
        :return: Total amount returned after lending period.
        """
        interest = self.calculate_interest()
        total = self.principal + interest
        return total

    def simulate(self, num_simulations: int) -> None:
        """
        Simulate multiple lending scenarios with random variable rates and print the results.
        
        :param num_simulations: The number of lending scenarios to simulate.
        """
        print(f"{'Simulation':<15}{'Variable Rate':<20}{'Total Return':<20}")
        print("=" * 55)

        for i in range(num_simulations):
            # Generate a random variable rate between 1% and 20% (0.01 to 0.20)
            random_rate = round(random.uniform(0.01, 0.20), 4)
            self.variable_rate = random_rate
            total = self.total_return()
            print(f"{i + 1:<15}{self.variable_rate:<20}{total:<20.2f}")

if __name__ == "__main__":
    # Example usage of LendingSimulator
    try:
        principal_amount = 1000.0  # Amount to lend in USDB
        lending_days = 30           # Duration for lending
        initial_rate = 0.05         # Initial APY (5%)

        simulator = LendingSimulator(principal_amount, lending_days, initial_rate)
        simulator.simulate(num_simulations=5)  # Simulate 5 lending scenarios

    except Exception as ex:
        print(f"An error occurred: {ex}")
```
