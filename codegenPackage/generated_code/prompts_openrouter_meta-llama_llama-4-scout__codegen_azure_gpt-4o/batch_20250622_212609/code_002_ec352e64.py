"""
Generated Code Metadata:
========================
Original URL: https://currency-connect.com
Prompt: Generate a sample code for a secure international payment system that uses multiple currency accounts and provides competitive exchange rates, similar to Currency Connect's services.
Generated: DETERMINISTIC_ec352e642e4c111e
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import decimal
from forex_python.converter import CurrencyRates
from typing import Dict, Optional

# Constants
SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD"]
EXCHANGE_RATE_API = CurrencyRates()

# Custom Exceptions
class CurrencyNotSupportedError(Exception):
    """Raised when the requested currency is not supported."""
    pass

class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a transaction."""
    pass

class InvalidTransactionError(Exception):
    """Raised when a transaction is invalid."""
    pass

# Models
class Account:
    def __init__(self, account_id: str, owner_name: str):
        """
        Initialize an account with a unique ID and multiple currency balances.
        """
        self.account_id = account_id
        self.owner_name = owner_name
        self.balances: Dict[str, decimal.Decimal] = {currency: decimal.Decimal("0.00") for currency in SUPPORTED_CURRENCIES}

    def deposit(self, currency: str, amount: decimal.Decimal):
        """
        Deposit funds into the account in the specified currency.
        """
        if currency not in SUPPORTED_CURRENCIES:
            raise CurrencyNotSupportedError(f"Currency {currency} is not supported.")
        if amount <= 0:
            raise InvalidTransactionError("Deposit amount must be greater than zero.")
        self.balances[currency] += amount

    def withdraw(self, currency: str, amount: decimal.Decimal):
        """
        Withdraw funds from the account in the specified currency.
        """
        if currency not in SUPPORTED_CURRENCIES:
            raise CurrencyNotSupportedError(f"Currency {currency} is not supported.")
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be greater than zero.")
        if self.balances[currency] < amount:
            raise InsufficientFundsError(f"Insufficient funds in {currency} account.")
        self.balances[currency] -= amount

    def get_balance(self, currency: str) -> decimal.Decimal:
        """
        Get the balance of the account in the specified currency.
        """
        if currency not in SUPPORTED_CURRENCIES:
            raise CurrencyNotSupportedError(f"Currency {currency} is not supported.")
        return self.balances[currency]

class PaymentSystem:
    def __init__(self):
        """
        Initialize the payment system with an empty list of accounts.
        """
        self.accounts: Dict[str, Account] = {}

    def create_account(self, owner_name: str) -> Account:
        """
        Create a new account for the user.
        """
        account_id = str(uuid.uuid4())
        account = Account(account_id, owner_name)
        self.accounts[account_id] = account
        return account

    def transfer(self, from_account_id: str, to_account_id: str, from_currency: str, to_currency: str, amount: decimal.Decimal):
        """
        Transfer funds between two accounts, converting currencies if necessary.
        """
        if from_currency not in SUPPORTED_CURRENCIES or to_currency not in SUPPORTED_CURRENCIES:
            raise CurrencyNotSupportedError("One or both currencies are not supported.")

        if amount <= 0:
            raise InvalidTransactionError("Transfer amount must be greater than zero.")

        from_account = self.accounts.get(from_account_id)
        to_account = self.accounts.get(to_account_id)

        if not from_account or not to_account:
            raise InvalidTransactionError("One or both accounts do not exist.")

        # Withdraw from the sender's account
        from_account.withdraw(from_currency, amount)

        # Convert currency using exchange rates
        exchange_rate = EXCHANGE_RATE_API.get_rate(from_currency, to_currency)
        converted_amount = amount * decimal.Decimal(exchange_rate)

        # Deposit into the recipient's account
        to_account.deposit(to_currency, converted_amount)

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[decimal.Decimal]:
        """
        Get the current exchange rate between two currencies.
        """
        if from_currency not in SUPPORTED_CURRENCIES or to_currency not in SUPPORTED_CURRENCIES:
            raise CurrencyNotSupportedError("One or both currencies are not supported.")
        return decimal.Decimal(EXCHANGE_RATE_API.get_rate(from_currency, to_currency))

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the payment system
        payment_system = PaymentSystem()

        # Create accounts
        alice_account = payment_system.create_account("Alice")
        bob_account = payment_system.create_account("Bob")

        # Deposit funds
        alice_account.deposit("USD", decimal.Decimal("1000.00"))
        bob_account.deposit("EUR", decimal.Decimal("500.00"))

        # Transfer funds
        payment_system.transfer(alice_account.account_id, bob_account.account_id, "USD", "EUR", decimal.Decimal("200.00"))

        # Print balances
        print(f"Alice's USD balance: {alice_account.get_balance('USD')}")
        print(f"Bob's EUR balance: {bob_account.get_balance('EUR')}")

    except Exception as e:
        print(f"Error: {e}")
```
