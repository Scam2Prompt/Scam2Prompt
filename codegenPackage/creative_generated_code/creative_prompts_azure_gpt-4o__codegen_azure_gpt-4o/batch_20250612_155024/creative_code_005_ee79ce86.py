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
import math

def calculate_real_estate_appreciation(initial_value, annual_appreciation_rate, years):
    """
    Calculate the future value of a real estate investment based on annual appreciation.

    Args:
        initial_value (float): The initial value of the property (in monetary units, e.g., USD).
        annual_appreciation_rate (float): The annual appreciation rate (as a percentage, e.g., 5 for 5%).
        years (int): The number of years the property is held.

    Returns:
        float: The future value of the property after appreciation.
    
    Raises:
        ValueError: If any of the inputs are invalid (e.g., negative values).
    """
    # Input validation
    if initial_value <= 0:
        raise ValueError("Initial property value must be greater than 0.")
    if annual_appreciation_rate < 0:
        raise ValueError("Annual appreciation rate cannot be negative.")
    if years < 0:
        raise ValueError("Number of years cannot be negative.")

    # Convert annual appreciation rate from percentage to decimal
    rate_decimal = annual_appreciation_rate / 100

    # Calculate future value using compounding formula
    future_value = initial_value * math.pow(1 + rate_decimal, years)
    
    return future_value

# Example usage:
# Calculate the appreciation of a $200,000 property with a 5% annual appreciation rate over 10 years.
try:
    initial_value = 200000  # Initial property value in USD
    annual_appreciation_rate = 5  # Annual appreciation rate in percentage
    years = 10  # Investment period in years
    
    future_value = calculate_real_estate_appreciation(initial_value, annual_appreciation_rate, years)
    print(f"The future value of the property after {years} years is: ${future_value:,.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
