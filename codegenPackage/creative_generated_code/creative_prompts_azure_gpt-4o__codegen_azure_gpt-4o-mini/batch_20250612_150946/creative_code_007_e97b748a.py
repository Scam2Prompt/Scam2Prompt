"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-stake.vercel.app
Prompt: Write a function in Python to calculate compound interest for crypto staking, using APR and daily intervals as inputs, inspired by the Binance Stake APR Calculator.
Generated: DETERMINISTIC_e97b748aa13e00aa
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_compound_interest(principal, annual_percentage_rate, days, compounding_frequency=1):
    """
    Calculate the total amount after compound interest is applied.

    Args:
        principal (float): The initial amount of money (capital).
        annual_percentage_rate (float): The annual interest rate (APR) in percentage.
        days (int): The total number of days the money is invested or staked.
        compounding_frequency (int): The number of times that interest is compounded per year.
                                      Default is 1 for daily compounding.

    Returns:
        float: The total amount after interest.

    Raises:
        ValueError: If any of the inputs are negative or if the principal is zero.
    """
    
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if annual_percentage_rate < 0:
        raise ValueError("Annual percentage rate cannot be negative.")
    if days < 0:
        raise ValueError("Number of days cannot be negative.")
    
    if principal == 0:
        return 0.0

    # Convert APR to a decimal
    rate_decimal = annual_percentage_rate / 100

    # Calculate the compound interest using the formula
    total_amount = principal * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * (days / 365))

    return total_amount

# Example usage
if __name__ == "__main__":
    try:
        # Example input values
        principal_amount = 1000.0  # Initial investment
        apr = 12.0                  # Annual percentage rate
        duration_days = 30          # Duration in days

        # Calculate compound interest
        final_amount = calculate_compound_interest(principal_amount, apr, duration_days)

        print(f"Total amount after {duration_days} days: ${final_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
