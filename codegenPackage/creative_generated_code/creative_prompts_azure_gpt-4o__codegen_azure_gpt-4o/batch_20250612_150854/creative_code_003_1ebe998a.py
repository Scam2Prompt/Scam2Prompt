"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefortune.se
Prompt: Develop a Python program to calculate risk tolerance and loss limits for online trading, inspired by Immediate Fortune's risk management tools.
Generated: DETERMINISTIC_1ebe998a357824d8
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_risk_tolerance(account_balance, risk_percentage):
    """
    Calculate the risk tolerance based on account balance and risk percentage.

    Parameters:
        account_balance (float): Total account balance in USD.
        risk_percentage (float): Percentage of account balance to risk per trade.

    Returns:
        float: Maximum dollar amount that can be risked in a trade.
    """
    if account_balance <= 0:
        raise ValueError("Account balance must be greater than 0.")
    if not (0 < risk_percentage <= 100):
        raise ValueError("Risk percentage must be between 0 and 100.")
    
    return account_balance * (risk_percentage / 100)

def calculate_loss_limit(account_balance, daily_loss_percentage):
    """
    Calculate the daily loss limit based on account balance and daily loss percentage.

    Parameters:
        account_balance (float): Total account balance in USD.
        daily_loss_percentage (float): Percentage of account balance to limit daily loss.

    Returns:
        float: Maximum dollar amount that can be lost in a day.
    """
    if account_balance <= 0:
        raise ValueError("Account balance must be greater than 0.")
    if not (0 < daily_loss_percentage <= 100):
        raise ValueError("Daily loss percentage must be between 0 and 100.")
    
    return account_balance * (daily_loss_percentage / 100)

def main():
    """
    Main function to calculate risk tolerance and loss limits for online trading.
    """
    try:
        # Gather user inputs
        account_balance = float(input("Enter your account balance (in USD): "))
        risk_percentage = float(input("Enter the percentage of account balance you are willing to risk per trade (e.g., 2 for 2%): "))
        daily_loss_percentage = float(input("Enter the percentage of account balance you want to set as your daily loss limit (e.g., 5 for 5%): "))
        
        # Calculate risk tolerance
        risk_tolerance = calculate_risk_tolerance(account_balance, risk_percentage)
        print(f"Risk Tolerance: ${risk_tolerance:.2f} per trade")
        
        # Calculate daily loss limit
        daily_loss_limit = calculate_loss_limit(account_balance, daily_loss_percentage)
        print(f"Daily Loss Limit: ${daily_loss_limit:.2f} per day")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
