"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-dezire.com
Prompt: Develop a secure deposit and withdrawal system for a cryptocurrency trading platform, ensuring compliance with the minimum deposit requirements and free transactions, as outlined on the Crypto Dezire website.
Generated: DETERMINISTIC_53c99b9724261030
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoAccount:
    """Represents a cryptocurrency account with deposit and withdrawal functionalities."""

    MIN_DEPOSIT = 10.0  # Minimum deposit requirement in the currency unit
    MIN_BALANCE = 0.0   # Minimum balance requirement, can be adjusted if needed

    def __init__(self, account_id: str):
        """
        Initializes a new CryptoAccount instance.

        :param account_id: Unique identifier for the account
        """
        self.account_id = account_id
        self.balance = 0.0  # Initial balance is set to zero

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit
        :raises ValueError: If the deposit amount is less than the minimum requirement
        """
        if amount < self.MIN_DEPOSIT:
            raise ValueError(f"Deposit amount must be at least {self.MIN_DEPOSIT}.")
        
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw
        :raises ValueError: If the withdrawal amount exceeds the current balance
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self) -> float:
        """
        Retrieves the current balance of the account.

        :return: The current balance
        """
        return self.balance

    def __str__(self):
        """Returns a string representation of the account details."""
        return f"Account ID: {self.account_id}, Balance: {self.balance}"

# Example Usage
if __name__ == "__main__":
    try:
        account = CryptoAccount(account_id="12345ABC")
        account.deposit(20.0)  # Successful deposit
        account.withdraw(5.0)   # Successful withdrawal
        print(account)          # Display account information
    except ValueError as e:
        print(f"Error: {e}")
```
