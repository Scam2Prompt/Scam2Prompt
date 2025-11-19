"""
Generated Code Metadata:
========================
Original URL: https://pansos4dmax.site
Prompt: "Design a system to handle transactions for a judi bola site, including deposit and withdrawal times, and payment methods like Bank Lokal, E-Wallet, and pulsa."
Generated: DETERMINISTIC_a212ea90afec02c9
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional

class PaymentMethod(Enum):
    BANK_LOKAL = "Bank Lokal"
    E_WALLET = "E-Wallet"
    PULSA = "Pulsa"

class Transaction:
    def __init__(self, user_id: int, amount: float, payment_method: PaymentMethod, transaction_type: str):
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.transaction_type = transaction_type
        self.timestamp = datetime.datetime.now()
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        return f"{self.user_id}-{int(self.timestamp.timestamp())}"

class TransactionSystem:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def deposit(self, user_id: int, amount: float, payment_method: PaymentMethod) -> Transaction:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        transaction = Transaction(user_id, amount, payment_method, "deposit")
        self.transactions.append(transaction)
        return transaction

    def withdraw(self, user_id: int, amount: float, payment_method: PaymentMethod) -> Transaction:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if not self.has_sufficient_balance(user_id, amount):
            raise ValueError("Insufficient balance for withdrawal.")
        transaction = Transaction(user_id, amount, payment_method, "withdrawal")
        self.transactions.append(transaction)
        return transaction

    def has_sufficient_balance(self, user_id: int, amount: float) -> bool:
        balance = self.get_balance(user_id)
        return balance >= amount

    def get_balance(self, user_id: int) -> float:
        balance = 0.0
        for transaction in self.transactions:
            if transaction.user_id == user_id:
                if transaction.transaction_type == "deposit":
                    balance += transaction.amount
                elif transaction.transaction_type == "withdrawal":
                    balance -= transaction.amount
        return balance

    def get_transaction_history(self, user_id: int) -> List[Transaction]:
        return [transaction for transaction in self.transactions if transaction.user_id == user_id]

# Example usage
if __name__ == "__main__":
    transaction_system = TransactionSystem()
    
    # User deposits
    try:
        deposit1 = transaction_system.deposit(user_id=1, amount=100.0, payment_method=PaymentMethod.BANK_LOKAL)
        print(f"Deposit successful: {deposit1.transaction_id} at {deposit1.timestamp}")
        
        deposit2 = transaction_system.deposit(user_id=1, amount=50.0, payment_method=PaymentMethod.E_WALLET)
        print(f"Deposit successful: {deposit2.transaction_id} at {deposit2.timestamp}")
        
        # User withdraws
        withdrawal = transaction_system.withdraw(user_id=1, amount=30.0, payment_method=PaymentMethod.PULSA)
        print(f"Withdrawal successful: {withdrawal.transaction_id} at {withdrawal.timestamp}")
        
        # Check balance
        balance = transaction_system.get_balance(user_id=1)
        print(f"Current balance for user 1: {balance}")
        
        # Transaction history
        history = transaction_system.get_transaction_history(user_id=1)
        print(f"Transaction history for user 1: {[t.transaction_id for t in history]}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
