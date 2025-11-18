"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprofit-rex-ervaring.com
Prompt: Develop a secure deposit and withdrawal system for a cryptocurrency trading platform, ensuring no fees or commissions, as highlighted in the Profit Rex Ervaring app.
Generated: DETERMINISTIC_87d13d46a6a09a05
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib

class CryptoWallet:
    """
    A class representing a secure cryptocurrency wallet.
    """

    def __init__(self):
        """
        Initializes the wallet with a zero balance.
        """
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        """
        Handles deposits into the wallet.

        Args:
        - amount (float): The amount to deposit.

        Raises:
        - ValueError: If the deposit amount is invalid (e.g., negative or zero).
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balance += amount

        # Record the transaction with a unique hash for transparency
        transaction_id = hashlib.sha256(f"DEPOSIT-{amount}-{len(self.transaction_history)}".encode()).hexdigest()
        self.transaction_history.append({
            "type": "deposit",
            "amount": amount,
            "transaction_id": transaction_id
        })

    def withdraw(self, amount):
        """
        Handles withdrawals from the wallet.

        Args:
        - amount (float): The amount to withdraw.

        Raises:
        - ValueError: If the withdrawal amount is invalid (e.g., exceeds balance or is negative).
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        
        self.balance -= amount

        # Record the transaction with a unique hash for transparency
        transaction_id = hashlib.sha256(f"WITHDRAW-{amount}-{len(self.transaction_history)}".encode()).hexdigest()
        self.transaction_history.append({
            "type": "withdraw",
            "amount": amount,
            "transaction_id": transaction_id
        })

    def get_balance(self):
        """
        Returns the current balance of the wallet.

        Returns:
        - float: The current wallet balance.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Returns the transaction history of the wallet.

        Returns:
        - list: A list of transaction records.
        """
        return self.transaction_history


# Example usage:
if __name__ == "__main__":
    # Initialize the wallet
    wallet = CryptoWallet()

    try:
        # Make a deposit
        wallet.deposit(100.50)
        print(f"Balance after deposit: {wallet.get_balance()}")

        # Make a withdrawal
        wallet.withdraw(50.25)
        print(f"Balance after withdrawal: {wallet.get_balance()}")

        # Check transaction history
        print("Transaction History:")
        for transaction in wallet.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
```
