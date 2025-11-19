"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Create a code snippet that simulates the effects of different compounding periods on investment growth, referencing Arbiquant's educational content.
Generated: DETERMINISTIC_209d583a23633542
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

def calculate_compound_interest(principal, rate, time, periods_per_year):
    """
    Calculate the compound interest over a specified period.

    Parameters:
    principal (float): The initial amount of money invested.
    rate (float): The annual interest rate (in decimal).
    time (float): The time in years the money is invested for.
    periods_per_year (int): The number of times interest is compounded per year.

    Returns:
    float: The amount of money accumulated after n years, including interest.
    """
    try:
        # Calculate compound interest using the formula A = P (1 + r/n)^(nt)
        amount = principal * (1 + rate / periods_per_year) ** (periods_per_year * time)
        return amount
    except ZeroDivisionError:
        print("Error: The number of periods per year cannot be zero.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def simulate_investment_growth(principal, rate, time, periods):
    """
    Simulate investment growth for different compounding periods.

    Parameters:
    principal (float): The initial investment amount.
    rate (float): Annual interest rate in decimal.
    time (float): Investment duration in years.
    periods (list): List of compounding periods to simulate.

    Returns:
    dict: A dictionary mapping each period to the final investment amount.
    """
    results = {}
    for p in periods:
        amount = calculate_compound_interest(principal, rate, time, p)
        if amount is not None:
            results[p] = amount
    return results

def plot_investment_growth(results):
    """
    Plot the investment growth based on different compounding periods.

    Parameters:
    results (dict): A dictionary of compounding periods and corresponding amounts.
    """
    periods = list(results.keys())
    amounts = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.plot(periods, amounts, marker='o')

    plt.title('Investment Growth vs Compounding Periods')
    plt.xlabel('Compounding Periods per Year')
    plt.ylabel('Amount ($)')
    plt.xticks(periods)
    plt.grid(True)
    plt.axis([min(periods) - 1, max(periods) + 1, 0, max(amounts) * 1.1])
    plt.show()

def main():
    # User-defined investment parameters
    principal = 1000  # Initial investment amount
    rate = 0.05       # Annual interest rate (5%)
    time = 10         # Investment duration in years
    compounding_periods = [1, 2, 4, 12, 365]  # Annual, semi-annual, quarterly, monthly, daily

    # Simulate and plot investment growth
    results = simulate_investment_growth(principal, rate, time, compounding_periods)
    plot_investment_growth(results)

if __name__ == "__main__":
    main()
```
