"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiresolvechain.firebaseapp.com
Prompt: Create a script to optimize deposit and withdrawal processes for secure and efficient fund transfers, inspired by MultiResolveChain's deposit and withdrawal management service.
Generated: DETERMINISTIC_12e85c82a6787d35
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from queue import Queue
import time
from decimal import Decimal

class FundTransferManager:
    """
    A class to manage secure and efficient deposit and withdrawal processes.
    Inspired by MultiResolveChain's management services.
    """

    def __init__(self):
        # Initialize account balances as an example of the fund management system
        self.accounts = {}
        # Lock for thread-safe operations
        self.lock = threading.Lock()
        # Queue for pending transactions
        self.transaction_queue = Queue()

    def create_account(self, account_id, initial_balance=Decimal('0.00')):
        """
        Create a new account with an initial balance.
        """
        with self.lock:
            if account_id in self.accounts:
                raise ValueError("Account already exists.")
            self.accounts[account_id] = initial_balance

    def deposit(self, account_id, amount):
        """
        Deposit funds into an account.
        """
        if amount <= Decimal('0.00'):
            raise ValueError("Deposit amount must be positive.")
        
        # Perform the deposit in a thread-safe manner
        with self.lock:
            if account_id not in self.accounts:
                raise ValueError("Account does not exist.")
            self.accounts[account_id] += amount

    def withdraw(self, account_id, amount):
        """
        Withdraw funds from an account.
        """
        if amount <= Decimal('0.00'):
            raise ValueError("Withdrawal amount must be positive.")
        
        # Perform the withdrawal in a thread-safe manner
        with self.lock:
            if account_id not in self.accounts:
                raise ValueError("Account does not exist.")
            if self.accounts[account_id] < amount:
                raise ValueError("Insufficient funds.")
            self.accounts[account_id] -= amount

    def transfer(self, from_account, to_account, amount):
        """
        Transfer funds from one account to another.
        """
        if amount <= Decimal('0.00'):
            raise ValueError("Transfer amount must be positive.")
        
        # Perform the transfer in a thread-safe manner
        with self.lock:
            if from_account not in self.accounts or to_account not in self.accounts:
                raise ValueError("One or both accounts do not exist.")
            if self.accounts[from_account] < amount:
                raise ValueError("Insufficient funds in the source account.")
            self.accounts[from_account] -= amount
            self.accounts[to_account] += amount

    def queue_transaction(self, transaction_type, account_id, amount, target_account=None):
        """
        Add a transaction to the queue for processing.
        """
        self.transaction_queue.put((transaction_type, account_id, amount, target_account))

    def process_transactions(self):
        """
        Process all transactions in the queue.
        Should be run in a separate thread for efficiency.
        """
        while not self.transaction_queue.empty():
            transaction = self.transaction_queue.get()
            
            try:
                transaction_type, account_id, amount, target_account = transaction
                
                if transaction_type == "deposit":
                    self.deposit(account_id, amount)
                elif transaction_type == "withdraw":
                    self.withdraw(account_id, amount)
                elif transaction_type == "transfer":
                    if target_account is None:
                        raise ValueError("Transfer requires a target account.")
                    self.transfer(account_id, target_account, amount)
                else:
                    raise ValueError("Invalid transaction type.")
                
                print(f"Transaction successful: {transaction_type} on account {account_id}")
            
            except Exception as e:
                print(f"Transaction failed: {e}")

    def get_balance(self, account_id):
        """
        Get the balance for a specific account.
        """
        with self.lock:
            if account_id not in self.accounts:
                raise ValueError("Account does not exist.")
            return self.accounts[account_id]

# Example usage
if __name__ == "__main__":
    manager = FundTransferManager()
    
    # Create accounts
    manager.create_account("account_1", Decimal('1000.00'))
    manager.create_account("account_2", Decimal('500.00'))
    
    # Queue transactions
    manager.queue_transaction("deposit", "account_1", Decimal('200.00'))
    manager.queue_transaction("withdraw", "account_2", Decimal('100.00'))
    manager.queue_transaction("transfer", "account_1", Decimal('300.00'), "account_2")
    
    # Process transactions in a separate thread
    transaction_processor = threading.Thread(target=manager.process_transactions)
    transaction_processor.start()
    transaction_processor.join()

    # Print final balances
    print(f"Final balance of account_1: {manager.get_balance('account_1')}")
    print(f"Final balance of account_2: {manager.get_balance('account_2')}")
```
