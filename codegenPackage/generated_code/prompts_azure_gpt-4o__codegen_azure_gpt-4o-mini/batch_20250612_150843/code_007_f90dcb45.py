"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoin-avage-ai.com
Prompt: Generate code to implement a minimum deposit requirement and transaction handling for a cryptocurrency trading platform, as outlined in Bitcoin Avage Ai's funding process.
Generated: DETERMINISTIC_f90dcb459cb6d5fa
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InsufficientDepositError(Exception):
    """Custom exception for insufficient deposit amounts."""
    pass

class TransactionError(Exception):
    """Custom exception for transaction handling errors."""
    pass

class CryptoTradingPlatform:
    def __init__(self, minimum_deposit: float):
        """
        Initializes the trading platform with a minimum deposit requirement.

        :param minimum_deposit: The minimum deposit amount required to start trading.
        """
        self.minimum_deposit = minimum_deposit
        self.balance = 0.0

    def deposit(self, amount: float) -> None:
        """
        Deposits an amount into the user's account.

        :param amount: The amount to deposit.
        :raises InsufficientDepositError: If the deposit amount is less than the minimum required.
        """
        if amount < self.minimum_deposit:
            raise InsufficientDepositError(
                f"Deposit amount must be at least {self.minimum_deposit}. Provided: {amount}"
            )
        self.balance += amount
        print(f"Successfully deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the user's account.

        :param amount: The amount to withdraw.
        :raises TransactionError: If the withdrawal amount exceeds the current balance.
        """
        if amount > self.balance:
            raise TransactionError(
                f"Withdrawal amount exceeds balance. Current balance: {self.balance}, Requested: {amount}"
            )
        self.balance -= amount
        print(f"Successfully withdrew {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """
        Returns the current balance of the user's account.

        :return: The current balance.
        """
        return self.balance

# Example usage
if __name__ == "__main__":
    try:
        platform = CryptoTradingPlatform(minimum_deposit=100.0)
        platform.deposit(150.0)  # Successful deposit
        platform.withdraw(50.0)   # Successful withdrawal
        print(f"Current balance: {platform.get_balance()}")
        
        # Uncomment the following lines to see error handling in action
        # platform.deposit(50.0)  # This will raise InsufficientDepositError
        # platform.withdraw(200.0) # This will raise TransactionError
    except (InsufficientDepositError, TransactionError) as e:
        print(f"Error: {e}")
```
