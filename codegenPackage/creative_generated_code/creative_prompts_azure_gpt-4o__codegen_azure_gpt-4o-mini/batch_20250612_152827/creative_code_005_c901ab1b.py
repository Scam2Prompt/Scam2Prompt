"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Write a function to calculate secure short-term and long-term income projections for a REIT portfolio, referencing the investment policy of Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_c901ab1bcde52b5c
Batch ID: 20250612_152827
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

class REITIncomeProjection:
    """
    A class to project short-term and long-term income for a REIT portfolio based on investment policy.
    """

    def __init__(self, initial_investment, short_term_rate, long_term_rate, years):
        """
        Initializes the REITIncomeProjection instance.

        Args:
            initial_investment (float): The initial investment amount.
            short_term_rate (float): Expected short-term income rate as a decimal (e.g., 0.05 for 5%).
            long_term_rate (float): Expected long-term income rate as a decimal (e.g., 0.08 for 8%).
            years (int): Number of years for the projection.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= short_term_rate <= 1):
            raise ValueError("Short-term rate must be between 0 and 1.")
        if not (0 <= long_term_rate <= 1):
            raise ValueError("Long-term rate must be between 0 and 1.")
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")

        self.initial_investment = initial_investment
        self.short_term_rate = short_term_rate
        self.long_term_rate = long_term_rate
        self.years = years

    def calculate_short_term_projection(self):
        """
        Calculate the short-term income projection for the REIT portfolio.

        Returns:
            pd.DataFrame: A DataFrame containing the short-term income projection.
        """
        # Calculate short-term income projections over the specified years
        short_term_projection = {
            "Year": np.arange(1, self.years + 1),
            "Projected Income": [self.initial_investment * (1 + self.short_term_rate) ** year for year in range(1, self.years + 1)]
        }
        return pd.DataFrame(short_term_projection)

    def calculate_long_term_projection(self):
        """
        Calculate the long-term income projection for the REIT portfolio.

        Returns:
            pd.DataFrame: A DataFrame containing the long-term income projection.
        """
        # Calculate long-term income projections over the specified years
        long_term_projection = {
            "Year": np.arange(1, self.years + 1),
            "Projected Income": [self.initial_investment * (1 + self.long_term_rate) ** year for year in range(1, self.years + 1)]
        }
        return pd.DataFrame(long_term_projection)

    def run_projections(self):
        """
        Run both short-term and long-term projections and return the results.

        Returns:
            dict: A dictionary containing both short-term and long-term projections as DataFrames.
        """
        short_term = self.calculate_short_term_projection()
        long_term = self.calculate_long_term_projection()

        return {
            "Short Term Projection": short_term,
            "Long Term Projection": long_term
        }

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 100000  # Initial investment amount
        short_term_rate = 0.05  # 5% short-term income
        long_term_rate = 0.08  # 8% long-term income
        years = 10  # Project for 10 years

        # Create REITIncomeProjection instance
        reit_projection = REITIncomeProjection(initial_investment, short_term_rate, long_term_rate, years)

        # Get projections
        projections = reit_projection.run_projections()

        # Display results
        print("Short Term Projection:")
        print(projections["Short Term Projection"])
        print("\nLong Term Projection:")
        print(projections["Long Term Projection"])

    except ValueError as e:
        print(f"Error: {e}")
```
