"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stake.pages.dev
Prompt: Create a function that simulates the yield earned from Flashstake over different time periods for various tokens.
Generated: DETERMINISTIC_68660c3330515da7
Batch ID: 20250612_161201
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

class FlashstakeSimulator:
    """
    A class to simulate the yield earnings from Flashstake over specified time periods for various tokens.
    """

    def __init__(self, token_rates):
        """
        Initializes the simulator with a dictionary of token rates.

        :param token_rates: A dictionary where keys are token names and values are the annual yield rates as percentages.
        """
        self.token_rates = token_rates

    def calculate_yield(self, token, principal, time_period_years):
        """
        Calculates the yield earned for a given token over a specified time period.

        :param token: The token name as a string.
        :param principal: The initial investment amount (float).
        :param time_period_years: The time period in years (float).
        :return: The total yield earned (float) and the total amount after the yield.
        """
        if token not in self.token_rates:
            raise ValueError(f"Token '{token}' is not available in the token rates.")
        
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        
        if time_period_years < 0:
            raise ValueError("Time period cannot be negative.")

        # Annual yield rate as a decimal
        annual_rate = self.token_rates[token] / 100
        
        # Calculate total yield using compound interest formula: A = P(1 + r/n)^(nt)
        # For Flashstake, assuming compounding annually (n=1)
        total_amount = principal * (1 + annual_rate) ** time_period_years
        total_yield = total_amount - principal
        
        return total_yield, total_amount

    def simulate_yields(self, principal, time_periods):
        """
        Simulates the yield for all tokens over specified time periods.

        :param principal: The initial investment amount (float).
        :param time_periods: A list of time periods in years (list of floats).
        :return: A DataFrame containing the yields for each token over each time period.
        """
        results = []

        for token in self.token_rates.keys():
            for period in time_periods:
                try:
                    total_yield, total_amount = self.calculate_yield(token, principal, period)
                    results.append({
                        'Token': token,
                        'Time Period (Years)': period,
                        'Total Yield': total_yield,
                        'Total Amount': total_amount
                    })
                except ValueError as e:
                    print(f"Error processing token '{token}' for period {period}: {e}")

        return pd.DataFrame(results)


# Example usage:
if __name__ == "__main__":
    # Token rates in percentage
    token_rates = {
        'ETH': 5,
        'BTC': 4,
        'USDT': 2,
        'DAI': 3
    }

    # Initialize the simulator
    simulator = FlashstakeSimulator(token_rates)

    # Define principal amount and time periods
    principal_amount = 1000.0  # Example principal
    time_periods_years = [1, 2, 5]  # Time periods in years

    # Simulate yields
    yield_results = simulator.simulate_yields(principal_amount, time_periods_years)

    # Display the results
    print(yield_results)
```
