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
import numpy as np

def simulate_investment_growth(principal, annual_rate, years, compounding_periods):
    """
    Simulates the growth of an investment for various compounding periods.
    
    :param principal: Initial investment amount (float).
    :param annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%) (float).
    :param years: Number of years the investment will grow (int).
    :param compounding_periods: List of compounding periods per year (e.g., [1, 2, 4, 12]) (list of int).
    :return: Dictionary of compounding period and final amount (dict).
    """
    results = {}
    
    for periods in compounding_periods:
        try:
            # Calculate the compound interest formula: A = P * (1 + r/n)^(n*t)
            amount = principal * (1 + annual_rate / periods) ** (periods * years)
            results[periods] = round(amount, 2)
        except Exception as e:
            # Handle any unexpected errors during calculations
            print(f"Error occurred for compounding period {periods}: {e}")
            results[periods] = None
    
    return results


def display_results(principal, annual_rate, years, results):
    """
    Displays the investment growth results in a readable format.

    :param principal: Initial investment amount (float).
    :param annual_rate: Annual interest rate as a decimal (float).
    :param years: Number of years the investment will grow (int).
    :param results: Dictionary of compounding period to final amount (dict).
    """
    print("\n--- Investment Growth Simulation Results ---")
    print(f"Principal: ${principal}")
    print(f"Annual Interest Rate: {annual_rate * 100:.2f}%")
    print(f"Investment Duration: {years} years\n")
    
    print(f"{'Compounding Periods':<20} {'Final Amount ($)':<15}")
    print("-" * 35)
    for periods, amount in results.items():
        if amount is not None:
            print(f"{periods:<20} {amount:<15}")
        else:
            print(f"{periods:<20} {'Error':<15}")


if __name__ == "__main__":
    # Example inputs
    principal = 10000  # Initial investment
    annual_rate = 0.05  # Annual interest rate (5%)
    years = 10  # Investment duration in years
    compounding_periods = [1, 2, 4, 12, 365]  # Compounding periods per year

    # Simulate investment growth for different compounding periods
    results = simulate_investment_growth(principal, annual_rate, years, compounding_periods)
    
    # Display results
    display_results(principal, annual_rate, years, results)
```
