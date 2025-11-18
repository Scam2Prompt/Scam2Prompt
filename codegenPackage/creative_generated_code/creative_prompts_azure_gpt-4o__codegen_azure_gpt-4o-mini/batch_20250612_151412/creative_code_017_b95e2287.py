"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Create a simulation in Python to compare investment returns between Klar's fixed-rate account and other market options.
Generated: DETERMINISTIC_b95e2287419ecc16
Batch ID: 20250612_151412
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

class Investment:
    """
    A class to represent an investment option.

    Attributes
    ----------
    name : str
        Name of the investment option
    rate_of_return : float
        Annual rate of return as a decimal
    """
    
    def __init__(self, name, rate_of_return):
        self.name = name
        self.rate_of_return = rate_of_return

    def calculate_return(self, initial_investment, years):
        """
        Calculate the future value of an investment.

        Parameters
        ----------
        initial_investment : float
            The initial amount of money invested.
        years : int
            The number of years the money is invested for.

        Returns
        -------
        float
            The future value of the investment.
        """
        return initial_investment * (1 + self.rate_of_return) ** years


def simulate_investments(initial_investment, years, investments):
    """
    Simulate the investment returns over a specified number of years.

    Parameters
    ----------
    initial_investment : float
        The initial amount of money to invest.
    years : int
        The number of years to simulate.
    investments : list of Investment
        A list of Investment objects to simulate.

    Returns
    -------
    DataFrame
        A DataFrame containing the year-by-year investment values.
    """
    results = {}

    for investment in investments:
        results[investment.name] = [investment.calculate_return(initial_investment, year) for year in range(years + 1)]

    return pd.DataFrame(results, index=range(years + 1))


def plot_investment_results(df):
    """
    Plot the investment results.

    Parameters
    ----------
    df : DataFrame
        A DataFrame containing the investment results.
    """
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)

    plt.title('Investment Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Investment Value')
    plt.legend()
    plt.grid()
    plt.show()


def main():
    # Investment parameters
    initial_investment = 10000  # Initial investment amount
    years = 10  # Number of years to simulate

    # Define investments
    klar_investment = Investment("Klar Fixed Rate Account", 0.03)  # 3% fixed rate
    market_investments = [
        Investment("Market Option 1 (High Risk)", 0.08),  # 8% return
        Investment("Market Option 2 (Moderate Risk)", 0.05),  # 5% return
        Investment("Market Option 3 (Low Risk)", 0.02)  # 2% return
    ]

    # Combine Klar and market investments
    all_investments = [klar_investment] + market_investments

    # Run simulation
    investment_results = simulate_investments(initial_investment, years, all_investments)

    # Plot results
    plot_investment_results(investment_results)

    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
