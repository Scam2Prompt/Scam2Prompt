"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://affinityprimetrade.com
Prompt: Generate code to calculate daily interest returns for different account types (e.g., Starter, Silver, Gold) based on the investment tiers provided by Affinity Prime Trade.
Generated: DETERMINISTIC_fa844c3c11efcbd7
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class Account:
    """
    Represents a user account with a specific tier and investment amount.
    """
    def __init__(self, account_type, investment_amount):
        self.account_type = account_type
        self.investment_amount = investment_amount
        self.daily_interest_rate = self._get_daily_interest_rate()

    def _get_daily_interest_rate(self):
        """
        Retrieve the daily interest rate based on account tier.
        """
        rates = {
            "Starter": 0.005,  # 0.5% daily interest
            "Silver": 0.01,    # 1% daily interest
            "Gold": 0.015      # 1.5% daily interest
        }
        return rates.get(self.account_type, 0)  # Default to 0 if account type is invalid

    def calculate_daily_interest(self):
        """
        Calculate the daily interest return for this account.
        """
        return round(self.investment_amount * self.daily_interest_rate, 2)

def calculate_interest_for_accounts(accounts):
    """
    Calculate daily interest for a list of accounts.

    Parameters:
        accounts (list): List of Account objects.

    Returns:
        dict: A dictionary mapping account names to their daily interest returns.
    """
    interest_results = {}
    for account in accounts:
        try:
            interest_results[account.account_type] = account.calculate_daily_interest()
        except Exception as e:
            # Log error (in production, use an actual logging system)
            print(f"Error calculating interest for {account.account_type}: {e}")
    return interest_results

# Main entry point
if __name__ == "__main__":
    try:
        # Define a list of accounts with their respective tiers and investment amounts
        accounts = [
            Account("Starter", 1000),  # Starter account with $1000 investment
            Account("Silver", 5000),  # Silver account with $5000 investment
            Account("Gold", 10000)    # Gold account with $10000 investment
        ]

        # Calculate daily interest for all accounts
        daily_interest = calculate_interest_for_accounts(accounts)

        # Display the results
        print("Daily Interest Returns:")
        for account_type, interest in daily_interest.items():
            print(f"{account_type}: ${interest}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
