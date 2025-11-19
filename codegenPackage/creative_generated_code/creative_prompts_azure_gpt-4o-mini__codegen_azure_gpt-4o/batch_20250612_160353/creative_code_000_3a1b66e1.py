"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coineehub.com
Prompt: Generate a Python script to calculate potential returns from CoineeHub's investment plans, including daily and monthly returns for different packages.
Generated: DETERMINISTIC_3a1b66e1fc6b3b30
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential returns from CoineeHub's investment plans.
This script computes daily and monthly returns for different investment packages.
"""

# Import necessary libraries
import sys

def calculate_returns(principal_amount, daily_rate, days):
    """
    Calculate total return based on principal amount, daily rate, and days invested.

    Parameters:
        principal_amount (float): The initial investment amount.
        daily_rate (float): The daily interest rate in percentage (e.g., 1.5 for 1.5%).
        days (int): The number of days the investment is held.

    Returns:
        daily_return (float): The daily profit generated.
        monthly_return (float): The estimated monthly return.
        total_return (float): The total profit at the end of the investment period.
    """
    try:
        if principal_amount <= 0 or daily_rate <= 0 or days <= 0:
            raise ValueError("Principal amount, daily rate, and days must be positive numbers.")
        
        # Calculate the daily return
        daily_return = principal_amount * (daily_rate / 100)
        
        # Calculate total return for all days
        total_return = daily_return * days
        
        # Estimate monthly return (assuming 30 days in a month)
        monthly_return = daily_return * 30
        
        return daily_return, monthly_return, total_return

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def display_returns(package_name, principal_amount, daily_rate, days):
    """
    Display returns for a given investment package.

    Parameters:
        package_name (str): Name of the investment package.
        principal_amount (float): The initial investment amount.
        daily_rate (float): The daily interest rate in percentage.
        days (int): The number of days the investment is held.
    """
    try:
        # Calculate returns using the helper function
        daily_return, monthly_return, total_return = calculate_returns(principal_amount, daily_rate, days)
        
        # Print formatted results
        print(f"Investment Package: {package_name}")
        print(f"Principal Amount: ${principal_amount:.2f}")
        print(f"Daily Interest Rate: {daily_rate:.2f}%")
        print(f"Investment Duration: {days} days")
        print(f"Daily Return: ${daily_return:.2f}")
        print(f"Estimated Monthly Return: ${monthly_return:.2f}")
        print(f"Total Return Over {days} Days: ${total_return:.2f}")
        print("-" * 40)

    except Exception as e:
        print(f"An error occurred while displaying returns: {e}")
        sys.exit(1)


def main():
    """
    Main entry point of the script. Defines investment packages and calculates returns.
    """
    # Define investment packages
    investment_packages = [
        {"package_name": "Starter Plan", "principal_amount": 1000, "daily_rate": 1.5, "days": 30},
        {"package_name": "Silver Plan", "principal_amount": 5000, "daily_rate": 2.0, "days": 60},
        {"package_name": "Gold Plan", "principal_amount": 10000, "daily_rate": 2.5, "days": 90},
    ]

    # Iterate over each package and display returns
    print("CoineeHub Investment Returns Calculator")
    print("=" * 40)
    for package in investment_packages:
        display_returns(
            package_name=package["package_name"],
            principal_amount=package["principal_amount"],
            daily_rate=package["daily_rate"],
            days=package["days"]
        )


if __name__ == "__main__":
    main()
```
