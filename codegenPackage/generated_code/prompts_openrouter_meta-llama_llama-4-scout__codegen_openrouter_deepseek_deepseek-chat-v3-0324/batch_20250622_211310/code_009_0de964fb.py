"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a simple investment calculator using a programming language (e.g., Python, JavaScript) to demonstrate the impact of investment strategies on returns.
Generated: DETERMINISTIC_0de964fbd84ab6bf
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Investment Calculator
# Calculates future investment value based on initial investment, contributions, returns, and time

import math

def calculate_investment(
    initial_investment: float,
    monthly_contribution: float,
    annual_return: float,
    years: int
) -> float:
    """
    Calculate the future value of an investment with compound interest.

    Args:
        initial_investment: Initial amount invested (positive number)
        monthly_contribution: Amount added each month (positive number)
        annual_return: Expected annual return rate (decimal, e.g., 0.07 for 7%)
        years: Investment period in years (positive integer)

    Returns:
        Future value of the investment

    Raises:
        ValueError: If any input is invalid
    """
    # Validate inputs
    if initial_investment < 0:
        raise ValueError("Initial investment must be positive")
    if monthly_contribution < 0:
        raise ValueError("Monthly contribution must be positive")
    if annual_return < 0:
        raise ValueError("Annual return must be positive")
    if years <= 0:
        raise ValueError("Investment period must be at least 1 year")

    monthly_return = annual_return / 12
    months = years * 12

    # Future value calculation with compound interest
    future_value = initial_investment * (1 + monthly_return) ** months
    future_value += monthly_contribution * (((1 + monthly_return) ** months - 1) / monthly_return)

    return round(future_value, 2)

def main():
    """Main function to run the investment calculator."""
    print("Investment Calculator")
    print("---------------------\n")

    try:
        # Get user inputs
        initial = float(input("Enter initial investment amount: $"))
        monthly = float(input("Enter monthly contribution amount: $"))
        rate = float(input("Enter expected annual return rate (e.g., 7 for 7%): ")) / 100
        duration = int(input("Enter investment duration in years: "))

        # Calculate and display results
        result = calculate_investment(initial, monthly, rate, duration)
        print(f"\nFuture investment value: ${result:,.2f}")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
