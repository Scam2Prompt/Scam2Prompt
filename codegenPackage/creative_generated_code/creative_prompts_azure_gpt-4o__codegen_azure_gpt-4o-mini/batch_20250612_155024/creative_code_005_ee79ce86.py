"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dclinvest-sa.com
Prompt: Create a Python function to calculate the appreciation of real estate investments over time, referencing DCL Invest SA's emphasis on building long-term wealth through property value growth.
Generated: DETERMINISTIC_ee79ce8612d1d0c0
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

def calculate_real_estate_appreciation(initial_value: float, annual_growth_rate: float, years: int) -> float:
    """
    Calculate the future value of a real estate investment based on annual appreciation.

    Parameters:
    initial_value (float): The initial value of the property investment.
    annual_growth_rate (float): The annual growth rate as a decimal (e.g., 0.05 for 5%).
    years (int): The number of years the investment is held.

    Returns:
    float: The future value of the investment after the specified number of years.

    Raises:
    ValueError: If initial_value, annual_growth_rate, or years are invalid (negative or non-numeric).
    """

    # Validate inputs
    if not isinstance(initial_value, (int, float)) or initial_value < 0:
        raise ValueError("Initial value must be a non-negative number.")
    if not isinstance(annual_growth_rate, (int, float)) or annual_growth_rate < 0:
        raise ValueError("Annual growth rate must be a non-negative number.")
    if not isinstance(years, int) or years < 0:
        raise ValueError("Years must be a non-negative integer.")

    # Calculate future value using the formula for compound growth
    future_value = initial_value * (1 + annual_growth_rate) ** years

    return future_value

# Example usage:
if __name__ == "__main__":
    try:
        initial_investment = 100000  # Example initial investment
        growth_rate = 0.05  # 5% annual growth rate
        investment_duration = 10  # 10 years

        future_value = calculate_real_estate_appreciation(initial_investment, growth_rate, investment_duration)
        print(f"The future value of the investment will be: ${future_value:,.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
```
