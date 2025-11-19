"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miner-pepebnb2.vercel.app
Prompt: Develop a script to track user deposits and withdrawals in a decentralized finance (DeFi) application, ensuring compliance with sustainability tax regulations.
Generated: DETERMINISTIC_5cc4af7e1659afdf
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TransactionError(Exception):
    """Custom exception for transaction-related errors."""
    pass

class DeFiTransaction:
    """A class to represent a deposit or withdrawal transaction in a DeFi application."""
    
    def __init__(self):
        # Initialize transaction history and tax rate
        self.transaction_history = []  # List to store all transactions
        self.sustainability_tax_rate = 0.02  # 2% sustainability tax

    def deposit(self, user_id, amount):
        """Process a deposit transaction."""
        if amount <= 0:
            raise TransactionError("Deposit amount must be greater than zero.")
        
        # Record the deposit
        transaction = {
            'user_id': user_id,
            'type': 'deposit',
            'amount': amount,
            'tax': 0,  # No tax for deposits
            'date': datetime.datetime.now()
        }
        self.transaction_history.append(transaction)
        print(f"Deposit of {amount} recorded for user {user_id}.")
        return transaction

    def withdraw(self, user_id, amount):
        """Process a withdrawal transaction."""
        if amount <= 0:
            raise TransactionError("Withdrawal amount must be greater than zero.")
        
        # Calculate sustainability tax
        tax = round(amount * self.sustainability_tax_rate, 2)
        net_amount = amount - tax
        
        if net_amount <= 0:
            raise TransactionError("Withdrawal amount after tax must be greater than zero.")
        
        # Record the withdrawal
        transaction = {
            'user_id': user_id,
            'type': 'withdrawal',
            'amount': amount,
            'tax': tax,
            'net_amount': net_amount,
            'date': datetime.datetime.now()
        }
        self.transaction_history.append(transaction)
        print(f"Withdrawal of {amount} recorded for user {user_id}. Tax applied: {tax}. Net amount: {net_amount}.")
        return transaction

    def get_transaction_history(self, user_id=None):
        """Retrieve transaction history. If user_id is provided, filter by user."""
        if user_id:
            return [trans for trans in self.transaction_history if trans['user_id'] == user_id]
        return self.transaction_history

    def calculate_total_tax_collected(self):
        """Calculate the total sustainability tax collected."""
        total_tax = sum(trans['tax'] for trans in self.transaction_history if trans['type'] == 'withdrawal')
        return total_tax


# Example usage
if __name__ == "__main__":
    # Initialize the DeFiTransaction system
    defi_system = DeFiTransaction()

    try:
        # Process transactions
        defi_system.deposit(user_id="user123", amount=500)
        defi_system.withdraw(user_id="user123", amount=200)
        defi_system.deposit(user_id="user456", amount=1000)
        defi_system.withdraw(user_id="user456", amount=300)

        # Retrieve transaction history
        user123_history = defi_system.get_transaction_history("user123")
        print("\nTransaction history for user123:")
        for transaction in user123_history:
            print(transaction)

        # Calculate total tax collected
        total_tax = defi_system.calculate_total_tax_collected()
        print(f"\nTotal sustainability tax collected: {total_tax}")

    except TransactionError as e:
        print(f"Transaction error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
