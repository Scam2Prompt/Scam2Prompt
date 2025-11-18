"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Write a script to calculate inflation-adjusted returns for real estate investments, incorporating the inflation hedge concept from Investolazlo.
Generated: DETERMINISTIC_38c7ec88cffdfbe2
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class RealEstateInvestment:
    def __init__(self, initial_investment, annual_return_rate, inflation_rate):
        """
        Initializes the RealEstateInvestment object with given parameters.

        :param initial_investment: float - the initial amount of money invested
        :param annual_return_rate: float - expected annual return rate (as a decimal)
        :param inflation_rate: float - expected annual inflation rate (as a decimal)
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= annual_return_rate <= 1):
            raise ValueError("Annual return rate must be between 0 and 1.")
        if not (0 <= inflation_rate <= 1):
            raise ValueError("Inflation rate must be between 0 and 1.")

        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.inflation_rate = inflation_rate

    def calculate_inflation_adjusted_return(self, years):
        """
        Calculates the inflation-adjusted return over a specified number of years.

        :param years: int - number of years to calculate the return over
        :return: float - the inflation-adjusted return amount
        """
        if years < 0:
            raise ValueError("Number of years must be zero or greater.")

        # Calculate the nominal return after the specified years
        nominal_return = self.initial_investment * (1 + self.annual_return_rate) ** years

        # Calculate the cumulative inflation over the specified years
        cumulative_inflation = (1 + self.inflation_rate) ** years

        # Calculate the inflation-adjusted return
        inflation_adjusted_return = nominal_return / cumulative_inflation

        return inflation_adjusted_return

def main():
    # Example usage of the RealEstateInvestment class
    try:
        # Initialize investment parameters
        initial_investment = 100000  # Initial investment amount
        annual_return_rate = 0.07    # Expected annual return rate of 7%
        inflation_rate = 0.03         # Expected annual inflation rate of 3%
        investment_duration = 10       # Duration for investment in years

        # Create an instance of the RealEstateInvestment
        investment = RealEstateInvestment(initial_investment, annual_return_rate, inflation_rate)

        # Calculate the inflation-adjusted return
        adjusted_return = investment.calculate_inflation_adjusted_return(investment_duration)

        print(f"Inflation-adjusted return after {investment_duration} years: ${adjusted_return:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
