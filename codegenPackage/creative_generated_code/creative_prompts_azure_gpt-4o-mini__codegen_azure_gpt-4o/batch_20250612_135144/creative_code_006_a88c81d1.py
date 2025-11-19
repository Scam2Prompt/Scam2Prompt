"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meversedex.gitbook.io
Prompt: Create a function to calculate potential returns from liquidity provision in the MEVerse DEX ecosystem.
Generated: DETERMINISTIC_a88c81d1a3fac825
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_liquidity_returns(initial_investment, annual_percentage_yield, duration_in_days):
    """
    Calculate potential returns from liquidity provision in the MEVerse DEX ecosystem.

    Args:
        initial_investment (float): The amount of liquidity initially provided (in USD).
        annual_percentage_yield (float): The annual percentage yield (APY) offered by the liquidity pool (in %).
        duration_in_days (int): The duration the liquidity is provided (in days).

    Returns:
        float: The total returns (initial investment + earnings) after the given duration.

    Raises:
        ValueError: If any parameter is negative or invalid.
    """

    # Input validation
    if initial_investment < 0:
        raise ValueError("Initial investment must be a positive value.")
    if annual_percentage_yield < 0:
        raise ValueError("Annual percentage yield must be a positive value.")
    if duration_in_days < 0:
        raise ValueError("Duration in days must be a positive value.")

    # Constants
    DAYS_IN_YEAR = 365

    # Calculate APY as a decimal
    apy_decimal = annual_percentage_yield / 100

    # Calculate returns using compound interest formula
    daily_rate = math.pow(1 + apy_decimal, 1 / DAYS_IN_YEAR) - 1  # Effective daily rate
    total_returns = initial_investment * math.pow(1 + daily_rate, duration_in_days)

    return total_returns


# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000  # USD
        annual_percentage_yield = 12  # APY in %
        duration_in_days = 90       # Duration in days

        potential_returns = calculate_liquidity_returns(initial_investment, annual_percentage_yield, duration_in_days)
        print(f"Potential returns after {duration_in_days} days: ${potential_returns:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
