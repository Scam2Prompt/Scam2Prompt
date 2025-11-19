"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-coins.pro
Prompt: Write a code snippet that calculates potential earnings based on the investment plans offered by smart-coins.pro, considering different deposit amounts and hourly profit rates.
Generated: DETERMINISTIC_8b75f5218fb270de
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_earnings(deposit_amount, hourly_profit_rate, hours):
    """
    Calculate potential earnings based on deposit amount, hourly profit rate, and duration.

    :param deposit_amount: Initial deposit amount (float).
    :param hourly_profit_rate: Hourly profit rate as a percentage (float, e.g., 1.5 for 1.5%).
    :param hours: Total number of hours the investment is held (int).
    :return: Total earnings (float).
    """
    try:
        # Validate input parameters
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        if hourly_profit_rate <= 0:
            raise ValueError("Hourly profit rate must be greater than zero.")
        if hours <= 0:
            raise ValueError("Number of hours must be greater than zero.")

        # Calculate earnings
        total_earnings = deposit_amount
        for hour in range(hours):
            total_earnings += (total_earnings * (hourly_profit_rate / 100))
        
        return total_earnings

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)

# Example usage
if __name__ == "__main__":
    try:
        # Input values (these could be replaced with user inputs or file reading)
        deposit_amount = 1000.0  # Example deposit amount
        hourly_profit_rate = 1.5  # Example hourly profit rate in percentage
        hours = 24  # Example investment duration in hours

        # Calculate and display potential earnings
        earnings = calculate_potential_earnings(deposit_amount, hourly_profit_rate, hours)
        if earnings:
            print(f"Total earnings after {hours} hours: ${earnings:.2f}")

    except Exception as e:
        print(f"An error occurred in the main execution: {e}", file=sys.stderr)
```
