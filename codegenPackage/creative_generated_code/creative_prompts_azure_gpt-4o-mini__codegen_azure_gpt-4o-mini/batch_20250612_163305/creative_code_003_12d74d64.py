"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-stake.vercel.app
Prompt: Generate a code snippet that inputs a principal amount and interest rate into the Binance Stake APR calculator to get daily interest estimates.
Generated: DETERMINISTIC_12d74d64945273ab
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def calculate_daily_interest(principal: float, annual_rate: float) -> float:
    """
    Calculate the daily interest based on the principal amount and annual percentage rate (APR).

    Args:
        principal (float): The principal amount to stake.
        annual_rate (float): The annual interest rate expressed as a percentage.

    Returns:
        float: The estimated daily interest earned.
    """
    # Validate the inputs
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if annual_rate < 0:
        raise ValueError("Annual interest rate must be non-negative.")

    # Convert annual rate percentage to a decimal
    daily_rate = (annual_rate / 100) / 365
    daily_interest = principal * daily_rate

    return daily_interest


def main():
    """
    Main function to execute the interest calculation based on user input.
    """
    try:
        # Input: Principal amount and annual interest rate
        principal = float(input("Enter the principal amount to stake: "))
        annual_rate = float(input("Enter the annual interest rate (APR) in percentage: "))
        
        # Calculate daily interest
        daily_interest = calculate_daily_interest(principal, annual_rate)
        
        # Output the result
        print(f"The estimated daily interest earned is: ${daily_interest:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
