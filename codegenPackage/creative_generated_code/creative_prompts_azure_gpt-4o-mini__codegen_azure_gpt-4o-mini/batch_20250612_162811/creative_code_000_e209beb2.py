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
def calculate_real_estate_return(initial_value, appreciation_rate, duration_years):
    """
    Calculate the potential returns on a real estate investment.

    Parameters:
    initial_value (float): The initial value of the property.
    appreciation_rate (float): The annual appreciation rate of the property (as a decimal).
    duration_years (int): The number of years the investment is held.

    Returns:
    float: The projected value of the property at the end of the investment period.
    float: The total return on investment (ROI) calculated as a percentage.

    Raises:
    ValueError: If initial_value is negative, appreciation_rate is not between 0 and 1, or duration_years is negative.
    """

    # Input validation
    if initial_value < 0:
        raise ValueError("Initial property value must be non-negative.")
    if not (0 <= appreciation_rate <= 1):
        raise ValueError("Appreciation rate must be between 0 and 1 (inclusive).")
    if duration_years < 0:
        raise ValueError("Investment duration must be non-negative.")

    # Calculate the projected value after the given duration
    future_value = initial_value * (1 + appreciation_rate) ** duration_years

    # Calculate total return on investment (ROI)
    total_roi = ((future_value - initial_value) / initial_value) * 100

    return future_value, total_roi

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 300000  # Initial property value in dollars
        rate_of_appreciation = 0.05   # 5% annual appreciation
        investment_duration = 10       # 10 years

        projected_value, roi = calculate_real_estate_return(initial_investment, rate_of_appreciation, investment_duration)
        print(f"Projected Value after {investment_duration} years: ${projected_value:.2f}")
        print(f"Total Return on Investment: {roi:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
