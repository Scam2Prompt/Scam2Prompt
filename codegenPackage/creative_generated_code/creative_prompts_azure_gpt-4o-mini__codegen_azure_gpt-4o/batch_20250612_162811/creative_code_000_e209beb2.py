"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write a Python function that calculates the potential returns on a real estate investment, considering factors like property value, appreciation rate, and investment duration, as discussed in Alghanim Capital's real estate investment section.
Generated: DETERMINISTIC_e209beb276ba725e
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_real_estate_returns(
    property_value: Union[int, float], 
    appreciation_rate: Union[int, float], 
    investment_duration: int
) -> float:
    """
    Calculates the potential returns on a real estate investment.

    Parameters:
        property_value (Union[int, float]): The initial value of the property (e.g., in USD).
        appreciation_rate (Union[int, float]): The annual appreciation rate as a percentage (e.g., 5 for 5%).
        investment_duration (int): The number of years the property is held.

    Returns:
        float: The estimated future value of the property after the investment duration.
    
    Raises:
        ValueError: If any input value is invalid.
    """
    # Validate the inputs
    if property_value <= 0:
        raise ValueError("Property value must be greater than 0.")
    if appreciation_rate < 0:
        raise ValueError("Appreciation rate cannot be negative.")
    if investment_duration <= 0:
        raise ValueError("Investment duration must be greater than 0.")
    
    # Convert appreciation rate from percentage to decimal
    appreciation_decimal = appreciation_rate / 100
    
    # Calculate the future value using the compound interest formula
    future_value = property_value * ((1 + appreciation_decimal) ** investment_duration)
    
    return future_value

# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        initial_value = 300000  # Property value in USD
        annual_appreciation_rate = 5  # Annual appreciation rate in percentage
        duration_years = 10  # Investment duration in years
        
        # Calculate potential returns
        estimated_value = calculate_real_estate_returns(initial_value, annual_appreciation_rate, duration_years)
        
        print(f"Estimated property value after {duration_years} years: ${estimated_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
