"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointrusts-mining.com
Prompt: Write a Python function to calculate total earnings for a user investing $100 for 5 days at a 3% daily interest rate, as described in Cointrust-mining's investment plan.
Generated: DETERMINISTIC_797bdb63e49c14a3
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(principal: float, daily_interest_rate: float, days: int) -> float:
    """
    Calculate total earnings from an investment with daily compound interest.

    Args:
        principal (float): The initial investment amount.
        daily_interest_rate (float): The daily interest rate as a percentage (e.g., 3 for 3%).
        days (int): The number of days the investment is held.

    Returns:
        float: The total earnings after the investment period.
    """
    try:
        # Validate input values
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if daily_interest_rate <= 0:
            raise ValueError("Daily interest rate must be greater than zero.")
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Convert daily interest rate from percentage to decimal
        daily_rate_decimal = daily_interest_rate / 100

        # Calculate total earnings using the compound interest formula
        total_amount = principal * (1 + daily_rate_decimal) ** days

        return round(total_amount, 2)  # Round to 2 decimal places for currency formatting

    except Exception as e:
        # Catch any unforeseen errors and log them
        print(f"Error: {e}")
        return 0.0  # Return 0.0 in case of an error

# Example usage:
if __name__ == "__main__":
    # Investment details
    principal_amount = 100.0
    daily_interest_percentage = 3.0
    investment_days = 5

    # Calculate earnings
    earnings = calculate_total_earnings(principal_amount, daily_interest_percentage, investment_days)
    print(f"Total earnings after {investment_days} days: ${earnings}")
```
