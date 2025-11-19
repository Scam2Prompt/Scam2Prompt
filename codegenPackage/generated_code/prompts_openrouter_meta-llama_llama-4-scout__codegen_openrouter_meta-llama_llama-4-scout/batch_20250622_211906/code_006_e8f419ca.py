"""
Generated Code Metadata:
========================
Original URL: https://affinityprimetrade.com
Prompt: Write a script to calculate the daily interest earnings for an Affinity Prime Trade account, considering the different account types and their corresponding interest rates.
Generated: DETERMINISTIC_e8f419ca86d737c7
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affinity_prime_trade.py

from enum import Enum
from typing import Dict

class AccountType(str, Enum):
    """Enum representing Affinity Prime Trade account types."""
    STANDARD = "standard"
    PREMIUM = "premium"
    ELITE = "elite"

class AffinityPrimeTrade:
    """Class to calculate daily interest earnings for Affinity Prime Trade accounts."""

    def __init__(self):
        # Define interest rates for each account type
        self.interest_rates: Dict[AccountType, float] = {
            AccountType.STANDARD: 0.05,  # 5% interest rate
            AccountType.PREMIUM: 0.075,  # 7.5% interest rate
            AccountType.ELITE: 0.10     # 10% interest rate
        }

    def calculate_daily_interest(self, account_type: AccountType, balance: float) -> float:
        """
        Calculate daily interest earnings for the given account type and balance.

        Args:
            account_type (AccountType): The type of Affinity Prime Trade account.
            balance (float): The current balance in the account.

        Returns:
            float: The daily interest earnings.

        Raises:
            ValueError: If the account type is not supported.
            ValueError: If the balance is negative.
        """
        if account_type not in self.interest_rates:
            raise ValueError(f"Unsupported account type: {account_type}")

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        interest_rate = self.interest_rates[account_type]
        daily_interest = balance * (interest_rate / 365)  # Assume 365-day year
        return daily_interest

def main():
    try:
        affinity_prime_trade = AffinityPrimeTrade()

        # Example usage
        account_type = AccountType.PREMIUM
        balance = 10000.0
        daily_interest = affinity_prime_trade.calculate_daily_interest(account_type, balance)
        print(f"Daily interest earnings for {account_type.value} account with balance ${balance:.2f}: ${daily_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
