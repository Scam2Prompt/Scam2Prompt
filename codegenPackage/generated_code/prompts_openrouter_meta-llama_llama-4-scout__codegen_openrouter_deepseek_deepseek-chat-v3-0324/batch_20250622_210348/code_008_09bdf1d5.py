"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: What are the different types of savings accounts offered by Crédit Agricole, such as the Livret A and the LDDS, and how do they differ in terms of interest rates and withdrawal rules?
Generated: DETERMINISTIC_09bdf1d523efdb0f
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information about Crédit Agricole savings accounts,
including Livret A and LDDS, with their interest rates and withdrawal rules.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class SavingsAccount:
    """Base class representing a savings account."""
    name: str
    description: str
    current_interest_rate: float
    is_tax_free: bool
    withdrawal_rules: str
    max_balance: float = None
    min_deposit: float = None

def get_credit_agricole_savings_accounts() -> List[SavingsAccount]:
    """
    Returns a list of Crédit Agricole savings accounts with their details.
    
    Returns:
        List[SavingsAccount]: List of savings account objects
    """
    return [
        SavingsAccount(
            name="Livret A",
            description="Tax-free savings account with regulated interest rate",
            current_interest_rate=3.0,  # As of February 2023
            is_tax_free=True,
            withdrawal_rules="Free withdrawals at any time",
            max_balance=22950.0,
            min_deposit=10.0
        ),
        SavingsAccount(
            name="LDDS (Livret de Développement Durable et Solidaire)",
            description="Sustainable development savings account",
            current_interest_rate=3.0,  # Same as Livret A
            is_tax_free=True,
            withdrawal_rules="Free withdrawals at any time",
            max_balance=12000.0,
            min_deposit=15.0
        ),
        SavingsAccount(
            name="Livret Jeune",
            description="Savings account for young people aged 12-25",
            current_interest_rate=3.0,  # Minimum legal rate
            is_tax_free=True,
            withdrawal_rules="Free withdrawals with account holder's consent if under 16",
            max_balance=1600.0
        ),
        SavingsAccount(
            name="Compte sur Livret",
            description="Basic savings account",
            current_interest_rate=0.5,  # Example rate, varies by bank
            is_tax_free=False,
            withdrawal_rules="Free withdrawals at any time",
            max_balance=None  # No legal maximum
        )
    ]

def display_accounts_info(accounts: List[SavingsAccount]) -> None:
    """Displays information about savings accounts in a formatted way."""
    print("\nCrédit Agricole Savings Accounts Information:")
    print("-" * 50)
    for account in accounts:
        print(f"\nAccount Name: {account.name}")
        print(f"Description: {account.description}")
        print(f"Current Interest Rate: {account.current_interest_rate}%")
        print(f"Tax Free: {'Yes' if account.is_tax_free else 'No'}")
        print(f"Withdrawal Rules: {account.withdrawal_rules}")
        if account.max_balance:
            print(f"Maximum Balance: €{account.max_balance:,.2f}")
        if account.min_deposit:
            print(f"Minimum Deposit: €{account.min_deposit:,.2f}")
        print("-" * 50)

if __name__ == "__main__":
    try:
        accounts = get_credit_agricole_savings_accounts()
        display_accounts_info(accounts)
    except Exception as e:
        print(f"An error occurred while retrieving account information: {e}")
```
