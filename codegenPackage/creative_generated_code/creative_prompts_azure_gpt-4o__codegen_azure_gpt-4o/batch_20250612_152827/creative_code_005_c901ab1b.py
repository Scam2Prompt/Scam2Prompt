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
import math

class REITPortfolio:
    """
    A class to represent a REIT portfolio and calculate secure income projections.
    """

    def __init__(self, short_term_growth_rate, long_term_growth_rate, initial_income):
        """
        Initialize the REITPortfolio instance with growth rates and initial income.

        :param short_term_growth_rate: Expected short-term growth rate (annualized) as a percentage (e.g., 5 for 5%).
        :param long_term_growth_rate: Expected long-term growth rate (annualized) as a percentage (e.g., 3 for 3%).
        :param initial_income: Initial annual income from the REIT portfolio.
        """
        self.short_term_growth_rate = short_term_growth_rate / 100  # Convert percentage to decimal
        self.long_term_growth_rate = long_term_growth_rate / 100  # Convert percentage to decimal
        self.initial_income = initial_income

    def calculate_income_projection(self, years, is_short_term=True):
        """
        Calculate secure income projections for a given number of years.

        :param years: Number of years for the projection.
        :param is_short_term: If True, use short-term growth rate; otherwise, use long-term growth rate.
        :return: Projected income at the end of the given period.
        """
        try:
            # Select growth rate based on the projection type
            growth_rate = self.short_term_growth_rate if is_short_term else self.long_term_growth_rate
            
            # Use compound growth calculation to project income
            projected_income = self.initial_income * math.pow(1 + growth_rate, years)

            return round(projected_income, 2)  # Return rounded income projection
        except TypeError:
            raise ValueError("All input values must be numeric.")  # Raise an error for invalid inputs


# Example usage
if __name__ == "__main__":
    try:
        # Initialize portfolio based on Rosebud Holdings investment policy
        rosebud_reit = REITPortfolio(
            short_term_growth_rate=6,  # Example: 6% annualized short-term growth rate
            long_term_growth_rate=4,  # Example: 4% annualized long-term growth rate
            initial_income=50000      # Example: Initial annual income of $50,000
        )

        # Calculate 5-year short-term projection
        short_term_projection = rosebud_reit.calculate_income_projection(years=5, is_short_term=True)
        print(f"Secure 5-year short-term income projection: ${short_term_projection}")

        # Calculate 10-year long-term projection
        long_term_projection = rosebud_reit.calculate_income_projection(years=10, is_short_term=False)
        print(f"Secure 10-year long-term income projection: ${long_term_projection}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
