"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeforcetd.com
Prompt: Write Python code to calculate daily returns for the "Flexible Plan" offered by Finance Force Ltd, which provides a 6% daily return for 5 days. Include functionality to calculate total earnings, including the referral bonus.
Generated: DETERMINISTIC_0fd556c518825d04
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flexible Plan Daily Returns Calculation
# This script calculates daily returns, total earnings, and includes referral bonuses
# for the "Flexible Plan" offered by Finance Force Ltd.

def calculate_daily_returns(principal, daily_rate, days):
    """
    Calculate daily returns for a given principal amount, daily interest rate, and the number of days.
    
    Args:
        principal (float): The initial amount invested.
        daily_rate (float): The daily return rate as a percentage (e.g., for 6%, provide 6.0).
        days (int): The number of days to calculate returns for.
        
    Returns:
        list: A list of daily return amounts.
    """
    try:
        daily_returns = []
        for day in range(1, days + 1):
            daily_return = principal * (daily_rate / 100)
            daily_returns.append(daily_return)
        return daily_returns
    except Exception as e:
        raise ValueError(f"Error calculating daily returns: {e}")


def calculate_total_earnings(daily_returns, referral_bonus=0.0):
    """
    Calculate total earnings including referral bonuses.
    
    Args:
        daily_returns (list): A list of daily return amounts.
        referral_bonus (float): The referral bonus amount (default is 0.0).
        
    Returns:
        float: The total earnings including referral bonuses.
    """
    try:
        total_earnings = sum(daily_returns) + referral_bonus
        return total_earnings
    except Exception as e:
        raise ValueError(f"Error calculating total earnings: {e}")


def main():
    """
    Main function to execute the calculation of daily returns and earnings for the Flexible Plan.
    """
    # Input values
    principal_amount = 1000.0  # The amount invested
    daily_return_rate = 6.0    # Daily return rate of 6%
    investment_days = 5        # Number of days the investment runs
    referral_bonus = 50.0      # Referral bonus amount

    try:
        # Calculate daily returns
        daily_returns = calculate_daily_returns(principal_amount, daily_return_rate, investment_days)
        
        # Calculate total earnings including referral bonus
        total_earnings = calculate_total_earnings(daily_returns, referral_bonus)
        
        # Display results
        print("Investment Summary for Flexible Plan:")
        print(f"Principal Amount: ${principal_amount:.2f}")
        print(f"Daily Return Rate: {daily_return_rate:.2f}%")
        print(f"Investment Period: {investment_days} days")
        print(f"Referral Bonus: ${referral_bonus:.2f}\n")
        
        print("Daily Returns:")
        for day, daily_return in enumerate(daily_returns, start=1):
            print(f"Day {day}: ${daily_return:.2f}")
        
        print(f"\nTotal Earnings (including referral bonus): ${total_earnings:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
