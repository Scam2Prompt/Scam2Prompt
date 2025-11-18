"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Generate a Python script to automate the calculation of daily returns for CoineeHub's investment packages, using input data such as investment amount and duration.
Generated: DETERMINISTIC_577c39c7459d8176
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sys

def calculate_daily_returns(investment_amount, annual_rate, duration_days):
    """
    Calculate the daily returns for an investment package.

    Parameters:
    investment_amount (float): The amount invested.
    annual_rate (float): The annual interest rate as a percentage.
    duration_days (int): The number of days for the investment.

    Returns:
    list: A list of daily return amounts for the duration specified.
    """
    try:
        if investment_amount <= 0 or annual_rate <= 0 or duration_days <= 0:
            raise ValueError("Investment amount, annual rate, and duration must be positive values.")

        # Convert annual rate to daily rate (percentage divided by 365)
        daily_rate = annual_rate / 100 / 365
        
        # Calculate daily returns
        daily_returns = [investment_amount * daily_rate] * duration_days
        return daily_returns
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the daily returns calculation.
    """
    try:
        print("Welcome to CoineeHub's Daily Returns Calculator!")
        
        # Collect user input with error handling
        investment_amount = float(input("Enter investment amount ($): "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        duration_days = int(input("Enter investment duration (days): "))
        
        # Validate inputs
        if investment_amount <= 0 or annual_rate <= 0 or duration_days <= 0:
            raise ValueError("All inputs must be positive values.")
        
        # Calculate daily returns
        daily_returns = calculate_daily_returns(investment_amount, annual_rate, duration_days)
        print(f"\nDaily Returns (for {duration_days} days):")
        
        # Print daily returns with corresponding dates
        start_date = datetime.date.today()
        for i, daily_return in enumerate(daily_returns):
            current_date = start_date + datetime.timedelta(days=i)
            print(f"Date: {current_date} | Daily Return: ${daily_return:.2f}")
        
        print("\nCalculation completed successfully!")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Execute the main function
    main()
```
