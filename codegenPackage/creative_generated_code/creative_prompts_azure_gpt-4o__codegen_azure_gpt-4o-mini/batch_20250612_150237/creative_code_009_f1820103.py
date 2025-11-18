"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketmaventrade.com
Prompt: Create a Python program that calculates speculative growth in cryptocurrency demand and its impact on portfolio returns, as highlighted by Market Maven Trade.
Generated: DETERMINISTIC_f1820103d5ae8e31
Batch ID: 20250612_150237
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


class CryptoPortfolio:
    def __init__(self, initial_investment, growth_rate, years):
        """
        Initialize the CryptoPortfolio.

        :param initial_investment: Initial amount invested in cryptocurrency.
        :param growth_rate: Expected annual growth rate of the cryptocurrency (in decimal).
        :param years: Number of years to project growth.
        """
        self.initial_investment = initial_investment
        self.growth_rate = growth_rate
        self.years = years
        self.portfolio_values = []

    def calculate_growth(self):
        """
        Calculate the portfolio value for each year based on the growth rate.

        :return: None
        """
        try:
            for year in range(1, self.years + 1):
                future_value = self.initial_investment * (1 + self.growth_rate) ** year
                self.portfolio_values.append(future_value)
        except Exception as e:
            print(f"Error during growth calculation: {e}")

    def get_portfolio_growth_table(self):
        """
        Generate a DataFrame showing the projected portfolio value over the years.

        :return: DataFrame containing year and corresponding portfolio value.
        """
        try:
            years_list = list(range(1, self.years + 1))
            growth_data = {
                'Year': years_list,
                'Portfolio Value': self.portfolio_values
            }
            return pd.DataFrame(growth_data)
        except Exception as e:
            print(f"Error generating portfolio growth table: {e}")

    def plot_growth(self):
        """
        Plot the projected growth of the portfolio over the specified years.

        :return: None
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(range(1, self.years + 1), self.portfolio_values, marker='o')
            plt.title('Projected Growth of Cryptocurrency Portfolio')
            plt.xlabel('Years')
            plt.ylabel('Portfolio Value ($)')
            plt.grid(True)
            plt.xticks(range(1, self.years + 1))
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")


if __name__ == "__main__":
    # User input parameters for the portfolio
    initial_investment = 10000  # $10,000 initial investment
    growth_rate = 0.15          # 15% annual growth rate
    years = 10                   # Projecting for 10 years

    # Create an instance of CryptoPortfolio
    crypto_portfolio = CryptoPortfolio(initial_investment, growth_rate, years)

    # Calculate growth and generate a portfolio value table
    crypto_portfolio.calculate_growth()
    growth_table = crypto_portfolio.get_portfolio_growth_table()

    # Display the growth table
    print(growth_table)

    # Plot the projected growth
    crypto_portfolio.plot_growth()
```
