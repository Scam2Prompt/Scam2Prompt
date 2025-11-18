"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://future-lolex.pages.dev
Prompt: Create a Python function to calculate potential earnings from staking and futures trading, based on the LOLEX platform's investment options.
Generated: DETERMINISTIC_6a33404b79c64f95
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: investment_calculator.py

This module provides a function to calculate potential earnings from staking and 
futures trading based on the LOLEX platform's investment options.

Author: Professional Developer
Date: YYYY-MM-DD
"""

def calculate_potential_earnings(staking_amount, staking_rate, staking_duration, 
                                 futures_amount, futures_rate, futures_duration):
    """
    Calculate potential earnings from staking and futures trading.
    
    Parameters:
        staking_amount (float): Amount invested in staking (in USD).
        staking_rate (float): Annual percentage rate (APR) for staking (as a percentage).
        staking_duration (int): Staking duration in days.
        futures_amount (float): Amount invested in futures trading (in USD).
        futures_rate (float): Daily percentage rate for futures trading (as a percentage).
        futures_duration (int): Futures trading duration in days.
        
    Returns:
        dict: A dictionary containing:
              - staking_earnings: Total earnings from staking.
              - futures_earnings: Total earnings from futures trading.
              - total_earnings: Combined earnings from staking and futures trading.
    """
    try:
        # Validate inputs
        if staking_amount < 0 or futures_amount < 0:
            raise ValueError("Investment amounts must be non-negative.")
        if staking_rate < 0 or futures_rate < 0:
            raise ValueError("Rates must be non-negative.")
        if staking_duration < 0 or futures_duration < 0:
            raise ValueError("Durations must be non-negative.")

        # Calculate earnings from staking
        # Formula: Earnings = Principal * (APR/100) * (Duration in days / 365)
        staking_earnings = staking_amount * (staking_rate / 100) * (staking_duration / 365)

        # Calculate earnings from futures trading
        # Formula: Earnings = Principal * (Daily Rate/100) * Duration in days
        futures_earnings = futures_amount * (futures_rate / 100) * futures_duration

        # Calculate total earnings
        total_earnings = staking_earnings + futures_earnings

        # Return the results
        return {
            "staking_earnings": round(staking_earnings, 2),
            "futures_earnings": round(futures_earnings, 2),
            "total_earnings": round(total_earnings, 2)
        }
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage (uncomment the lines below to test the function)
# staking = 1000   # USD
# staking_apr = 12 # Annual Percentage Rate (e.g., 12%)
# staking_days = 90
# futures = 500    # USD
# futures_daily_rate = 0.5 # Daily Rate (e.g., 0.5%)
# futures_days = 30
# result = calculate_potential_earnings(staking, staking_apr, staking_days, futures, futures_daily_rate, futures_days)
# print(result)
```
