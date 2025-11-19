"""
Generated Code Metadata:
========================
Original URL: https://moneygrowthway.com
Prompt: "Design a simple cryptocurrency payment system using Python, allowing users to make deposits and withdrawals with a minimum withdrawal amount of $10."
Generated: DETERMINISTIC_111864300b2eb602
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds during withdrawal."""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid deposit or withdrawal amounts."""
    pass

class CryptocurrencyWallet:
    def __init__(self):
        """Initialize the wallet with a balance of 0 and a unique wallet ID."""
        self.balance = 0.0
        self.wallet_id = self.generate_wallet_id()

    @staticmethod
    def generate_wallet_id(length=10):
        """Generate a unique wallet ID consisting of letters and digits."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def deposit(self, amount):
        """Deposit a specified amount into the wallet.

        Args:
            amount (float): The amount to deposit.

        Raises:
            InvalidAmountError: If the deposit amount is less than or equal to zero.
        """
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw a specified amount from the wallet.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            InsufficientFundsError: If the withdrawal amount exceeds the current balance.
            InvalidAmountError: If the withdrawal amount is less than the minimum required.
        """
        if amount < 10:
            raise InvalidAmountError("Minimum withdrawal amount is $10.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """Return the current balance of the wallet."""
        return self.balance

    def __str__(self):
        """Return a string representation of the wallet."""
        return f"Wallet ID: {self.wallet_id}, Balance: ${self.balance:.2f}"

# Example usage
if __name__ == "__main__":
    wallet = CryptocurrencyWallet()
    print(wallet)

    try:
        wallet.deposit(50)
        wallet.withdraw(20)
        wallet.withdraw(10)
        print(wallet)
    except (InsufficientFundsError, InvalidAmountError) as e:
        print(f"Error: {e}")
```
