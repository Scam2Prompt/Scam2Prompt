"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write a code snippet to calculate the potential market size of the air platforms segment in India over the next decade, considering the government's policy on offsets and the integration of overseas suppliers with the local manufacturing sector.
Generated: DETERMINISTIC_7caad54156a01460
Batch ID: 20250622_205623
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

class MarketSizeCalculator:
    """
    A class to calculate the potential market size of the air platforms segment in India.
    """

    def __init__(self, initial_market_size: float, growth_rate: float, years: int):
        """
        Initializes the MarketSizeCalculator with initial market size, growth rate, and number of years.

        :param initial_market_size: The initial market size in millions.
        :param growth_rate: The annual growth rate as a percentage.
        :param years: The number of years to project into the future.
        """
        self.initial_market_size = initial_market_size
        self.growth_rate = growth_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_market_size(self) -> float:
        """
        Calculates the projected market size after a specified number of years.

        :return: The projected market size in millions.
        """
        try:
            # Calculate future market size using compound growth formula
            future_market_size = self.initial_market_size * (1 + self.growth_rate) ** self.years
            return future_market_size
        except Exception as e:
            print(f"Error calculating market size: {e}")
            return None

    def generate_projection_dataframe(self) -> pd.DataFrame:
        """
        Generates a DataFrame containing the projected market size for each year.

        :return: A DataFrame with years and corresponding market sizes.
        """
        try:
            years_list = np.arange(1, self.years + 1)
            market_sizes = [self.initial_market_size * (1 + self.growth_rate) ** year for year in years_list]
            projection_df = pd.DataFrame({
                'Year': years_list,
                'Projected Market Size (in millions)': market_sizes
            })
            return projection_df
        except Exception as e:
            print(f"Error generating projection DataFrame: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initial market size in millions, growth rate in percentage, and projection for 10 years
    initial_market_size = 5000  # Example initial market size
    growth_rate = 10  # Example growth rate of 10%
    years = 10  # Projecting for the next decade

    market_calculator = MarketSizeCalculator(initial_market_size, growth_rate, years)
    
    # Calculate the total market size after the specified years
    projected_size = market_calculator.calculate_market_size()
    print(f"Projected Market Size after {years} years: {projected_size:.2f} million")

    # Generate and display the projection DataFrame
    projection_df = market_calculator.generate_projection_dataframe()
    if projection_df is not None:
        print(projection_df)
```
