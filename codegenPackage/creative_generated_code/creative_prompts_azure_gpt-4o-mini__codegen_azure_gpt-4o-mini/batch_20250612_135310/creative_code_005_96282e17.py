"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-opttradexcoin.com
Prompt: Create a function that calculates potential returns on investment for cryptocurrency based on the guaranteed ROIs mentioned by Co-opt Trade Xcoin.
Generated: DETERMINISTIC_96282e176c15ff2b
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_crypto_investment_return(principal: float, roi_percentage: float, years: int) -> float:
    """
    Calculate the potential returns on investment for cryptocurrency.

    Parameters:
    principal (float): The initial amount of money invested.
    roi_percentage (float): The guaranteed return on investment percentage expressed as a decimal.
    years (int): The number of years the investment will be held.

    Returns:
    float: The total value of the investment after the specified number of years.

    Raises:
    ValueError: If principal is less than or equal to 0, or if roi_percentage is less than 0, 
                or if years is less than 0.
    """

    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal investment must be greater than zero.")
    if roi_percentage < 0:
        raise ValueError("ROI percentage must not be negative.")
    if years < 0:
        raise ValueError("Number of years must not be negative.")

    # Calculate the total return using the formula for compound interest
    total_value = principal * (1 + roi_percentage) ** years

    return total_value

# Example usage
if __name__ == "__main__":
    try:
        principal_investment = 1000.0  # Example principal amount
        guaranteed_roi = 0.05           # Example guaranteed ROI of 5%
        investment_duration = 5          # Example investment period of 5 years

        future_value = calculate_crypto_investment_return(principal_investment, guaranteed_roi, investment_duration)
        print(f"The potential return on investment after {investment_duration} years is: ${future_value:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
```
