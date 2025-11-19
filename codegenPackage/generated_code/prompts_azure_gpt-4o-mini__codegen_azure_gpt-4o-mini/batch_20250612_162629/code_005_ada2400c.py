"""
Generated Code Metadata:
========================
Original URL: https://battle-barkers.com
Prompt: Write a code example that simulates the impact of inflation on investment returns over a 10-year period.
Generated: DETERMINISTIC_ada2400c6dc03cf8
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_investment_growth(initial_investment, annual_return_rate, inflation_rate, years):
    """
    Simulates the growth of an investment over a specified number of years,
    taking into account the annual return rate and inflation rate.

    Parameters:
    initial_investment (float): The initial amount of money invested.
    annual_return_rate (float): The expected annual return rate (as a decimal).
    inflation_rate (float): The expected annual inflation rate (as a decimal).
    years (int): The number of years to simulate.

    Returns:
    tuple: A tuple containing two lists:
        - investment_values: The value of the investment over the years.
        - inflation_adjusted_values: The inflation-adjusted value of the investment over the years.
    """
    # Initialize lists to store values
    investment_values = []
    inflation_adjusted_values = []

    # Calculate the investment value and inflation-adjusted value for each year
    for year in range(years + 1):
        # Calculate the investment value at the end of the year
        investment_value = initial_investment * (1 + annual_return_rate) ** year
        investment_values.append(investment_value)

        # Calculate the inflation-adjusted value
        inflation_adjusted_value = investment_value / (1 + inflation_rate) ** year
        inflation_adjusted_values.append(inflation_adjusted_value)

    return investment_values, inflation_adjusted_values

def plot_investment_growth(years, investment_values, inflation_adjusted_values):
    """
    Plots the investment growth and inflation-adjusted growth over time.

    Parameters:
    years (int): The number of years of the simulation.
    investment_values (list): The values of the investment over the years.
    inflation_adjusted_values (list): The inflation-adjusted values of the investment over the years.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(years + 1), investment_values, label='Investment Value', color='blue')
    plt.plot(range(years + 1), inflation_adjusted_values, label='Inflation Adjusted Value', color='orange')
    plt.title('Investment Growth vs. Inflation Adjusted Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Value ($)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # User-defined parameters
    initial_investment = 10000  # Initial investment amount in dollars
    annual_return_rate = 0.07    # Expected annual return rate (7%)
    inflation_rate = 0.03        # Expected annual inflation rate (3%)
    years = 10                   # Number of years to simulate

    try:
        # Simulate investment growth
        investment_values, inflation_adjusted_values = simulate_investment_growth(
            initial_investment, annual_return_rate, inflation_rate, years
        )

        # Plot the results
        plot_investment_growth(years, investment_values, inflation_adjusted_values)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
