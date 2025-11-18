"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlineinstantresolve.firebaseapp.com
Prompt: Provide an algorithm for enhancing deposit and withdrawal processes in a cryptocurrency platform, based on the "Deposit and Withdrawal Management" section.
Generated: DETERMINISTIC_51779206fb6a65ae
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoWallet:
    def __init__(self):
        """Initialize the wallet with an empty balance and transaction history."""
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount: float) -> None:
        """
        Deposit an amount into the wallet.
        
        Args:
            amount (float): The amount to be deposited.
        
        Raises:
            ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Successfully deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw an amount from the wallet.
        
        Args:
            amount (float): The amount to be withdrawn.
        
        Raises:
            ValueError: If the amount is negative, zero, or exceeds the available balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        print(f"Successfully withdrew: {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """
        Get the current balance of the wallet.
        
        Returns:
            float: The current balance.
        """
        return self.balance

    def get_transaction_history(self) -> list:
        """
        Get the transaction history of the wallet.
        
        Returns:
            list: A list of transaction records.
        """
        return self.transaction_history

# Example usage
if __name__ == "__main__":
    wallet = CryptoWallet()
    
    try:
        wallet.deposit(100)
        wallet.withdraw(50)
        print(f"Current Balance: {wallet.get_balance()}")
        print("Transaction History:", wallet.get_transaction_history())
    except ValueError as e:
        print(f"Error: {e}")
```
