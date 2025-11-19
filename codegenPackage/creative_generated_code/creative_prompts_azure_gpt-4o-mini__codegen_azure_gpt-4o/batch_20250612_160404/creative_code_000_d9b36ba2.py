"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Generate a Python script to calculate potential earnings based on the investment plans offered by Tslaspacetrade, considering different principal amounts and daily interest rates.
Generated: DETERMINISTIC_d9b36ba249cbb02d
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# tslaspacetrade_earnings_calculator.py
# A script to calculate potential earnings based on investment plans 
# offered by Tslaspacetrade, considering principal amounts and daily interest rates.

# Import necessary modules
import sys

def calculate_earnings(principal, daily_rate, days):
    """
    Calculate potential earnings based on principal, daily interest rate, and number of days.

    Args:
        principal (float): The initial investment amount.
        daily_rate (float): The daily interest rate (percentage value, e.g., 1.5 means 1.5%).
        days (int): The duration of the investment in days.

    Returns:
        float: Total earnings after the specified duration.
    """
    try:
        # Convert daily_rate percentage to decimal
        daily_rate_decimal = daily_rate / 100

        # Calculate total earnings using compound interest formula
        total_earnings = principal * ((1 + daily_rate_decimal) ** days)

        return round(total_earnings, 2)
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating earnings: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the investment earnings calculator.
    """
    print("Welcome to Tslaspacetrade Earnings Calculator!")
    
    try:
        # Gather input data from the user
        principal = float(input("Enter the principal amount (e.g., 1000): "))
        daily_rate = float(input("Enter the daily interest rate (percentage, e.g., 1.5): "))
        days = int(input("Enter the number of days for the investment: "))

        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if daily_rate <= 0:
            raise ValueError("Daily interest rate must be greater than 0.")
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")

        # Calculate earnings
        total_earnings = calculate_earnings(principal, daily_rate, days)

        # Display results
        print(f"\nInvestment Summary:")
        print(f"Principal Amount: ${principal}")
        print(f"Daily Interest Rate: {daily_rate}%")
        print(f"Number of Days: {days}")
        print(f"Total Earnings: ${total_earnings}")

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the main function
    main()
```
