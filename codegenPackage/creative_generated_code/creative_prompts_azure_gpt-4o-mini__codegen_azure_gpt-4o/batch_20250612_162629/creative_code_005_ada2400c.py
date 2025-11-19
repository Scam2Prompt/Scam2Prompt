"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Write a code example that simulates the impact of inflation on investment returns over a 10-year period.
Generated: DETERMINISTIC_ada2400c6dc03cf8
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def simulate_inflation_effect(principal, annual_return_rate, annual_inflation_rate, years):
    """
    Simulates the impact of inflation on investment returns over a specified period of time.

    Args:
        principal (float): Initial investment amount.
        annual_return_rate (float): Annual return rate (as a percentage).
        annual_inflation_rate (float): Annual inflation rate (as a percentage).
        years (int): Number of years to simulate.

    Returns:
        list of dict: A list containing yearly details of the investment value and inflation-adjusted value.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than 0.")
    if annual_return_rate < 0 or annual_inflation_rate < 0:
        raise ValueError("Annual return rate and inflation rate must be non-negative values.")
    if years <= 0:
        raise ValueError("Years must be greater than 0.")

    # Convert rates to decimal for calculations
    return_rate = annual_return_rate / 100
    inflation_rate = annual_inflation_rate / 100

    results = []
    for year in range(1, years + 1):
        # Calculate value at the end of the year
        principal *= (1 + return_rate)
        inflation_adjusted_value = principal / ((1 + inflation_rate) ** year)

        # Append yearly data to results
        results.append({
            "Year": year,
            "Investment Value": round(principal, 2),
            "Inflation-Adjusted Value": round(inflation_adjusted_value, 2)
        })

    return results


def main():
    try:
        # Input parameters
        principal = float(input("Enter initial investment amount (e.g., 10000): "))
        annual_return_rate = float(input("Enter annual return rate (as percentage, e.g., 7): "))
        annual_inflation_rate = float(input("Enter annual inflation rate (as percentage, e.g., 2): "))
        years = int(input("Enter the number of years to simulate (e.g., 10): "))

        # Run simulation
        results = simulate_inflation_effect(principal, annual_return_rate, annual_inflation_rate, years)

        # Display results
        print("\nYearly Investment Results:")
        print(f"{'Year':<10}{'Investment Value':<20}{'Inflation-Adjusted Value':<25}")
        print("-" * 55)
        for result in results:
            print(f"{result['Year']:<10}{result['Investment Value']:<20}{result['Inflation-Adjusted Value']:<25}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
