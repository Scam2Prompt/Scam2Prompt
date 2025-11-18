"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitablecryptosignal.com
Prompt: Create a Python program to calculate potential profits for different account types (Bronze, Silver, Gold, Premium) based on the investment plans provided on profitablecryptosignal.com.
Generated: DETERMINISTIC_8d84129a435a58f1
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Program to Calculate Potential Profits for Different Account Types
Based on Investment Plans from profitablecryptosignal.com
"""

# Import necessary libraries
import sys

def calculate_profit(account_type, investment_amount):
    """
    Calculate the potential profit based on account type and investment amount.

    Parameters:
    - account_type (str): The type of account (Bronze, Silver, Gold, Premium)
    - investment_amount (float): The amount invested

    Returns:
    - float: The calculated profit
    """
    # Define the profit percentages for each account type
    profit_percentages = {
        "Bronze": 5,  # 5% profit
        "Silver": 10, # 10% profit
        "Gold": 15,   # 15% profit
        "Premium": 20 # 20% profit
    }

    # Validate account type
    if account_type not in profit_percentages:
        raise ValueError(f"Invalid account type '{account_type}'. Valid types are: Bronze, Silver, Gold, Premium.")

    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Calculate profit
    profit_percentage = profit_percentages[account_type]
    profit = (profit_percentage / 100) * investment_amount

    return profit

def main():
    """
    Main entry point of the program.
    """
    try:
        # Display program information
        print("Welcome to the Crypto Investment Profit Calculator.\n")

        # Prompt user for account type and investment amount
        account_type = input("Enter your account type (Bronze, Silver, Gold, Premium): ").strip().capitalize()
        investment_amount = float(input("Enter your investment amount: "))

        # Calculate profit
        profit = calculate_profit(account_type, investment_amount)

        # Display the result
        print(f"\nAccount Type: {account_type}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Potential Profit: ${profit:.2f}")

    except ValueError as e:
        # Handle invalid input
        print(f"\nError: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # Ensure clean program exit
        print("\nThank you for using the Crypto Investment Profit Calculator.")

# Entry point check
if __name__ == "__main__":
    main()
```
