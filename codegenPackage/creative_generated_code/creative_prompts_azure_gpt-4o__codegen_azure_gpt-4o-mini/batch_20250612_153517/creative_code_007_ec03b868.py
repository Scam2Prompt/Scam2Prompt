"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnodefix.pages.dev
Prompt: Write a program to manage deposit and withdrawal processes securely, optimizing user experience as described in the Web3 Resolver's services.
Generated: DETERMINISTIC_ec03b8687a7649ab
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class Account:
    """Class to represent a bank account for deposit and withdrawal operations."""
    
    def __init__(self, account_id, initial_balance=0):
        """Initialize the account with an ID and an initial balance."""
        self.account_id = account_id
        self.balance = Decimal(initial_balance)
    
    def deposit(self, amount):
        """Deposit an amount to the account, ensuring it is a valid positive number."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balance += Decimal(amount)
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        """Withdraw an amount from the account, ensuring sufficient funds are available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balance -= Decimal(amount)
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def to_json(self):
        """Convert account information to JSON format for easier storage and transmission."""
        return json.dumps({'account_id': self.account_id, 'balance': str(self.balance)})

def main():
    """Main function to run account management operations."""
    try:
        # Create a new account with an initial balance of 100
        account = Account(account_id='12345', initial_balance=100)
        
        # Perform deposit and withdrawal operations
        account.deposit(50)
        account.withdraw(30)
        
        # Print the current balance
        print(f"Current balance: {account.get_balance()}")
        
        # Output account information in JSON format
        print("Account info:", account.to_json())
        
    except ValueError as e:
        print(f"Error: {e}")
    except InvalidOperation as e:
        print("Error processing amount: Invalid number format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
