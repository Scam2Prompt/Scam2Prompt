"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a secure cryptocurrency transaction system for depositing and withdrawing funds in an online casino, inspired by BaxBet's focus on secure crypto payments.
Generated: DETERMINISTIC_a000ad221e9b097c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import hmac
import secrets
from decimal import Decimal

class CryptoTransactionSystem:
    def __init__(self):
        """
        Initializes the transaction system with a ledger and supported cryptocurrencies.
        """
        self.ledger = {}  # User balances: {user_id: {"BTC": Decimal, "ETH": Decimal}}
        self.supported_cryptocurrencies = ["BTC", "ETH"]
        self.transaction_fee_percentage = Decimal("0.02")  # 2% fee for each transaction

    def create_user_account(self, user_id):
        """
        Creates a new user account with zero balance for supported cryptocurrencies.
        """
        if user_id in self.ledger:
            raise ValueError("User account already exists.")
        self.ledger[user_id] = {crypto: Decimal("0.0") for crypto in self.supported_cryptocurrencies}

    def deposit(self, user_id, cryptocurrency, amount):
        """
        Allows a user to deposit funds into their account.
        
        :param user_id: ID of the user depositing the cryptocurrency
        :param cryptocurrency: Type of cryptocurrency being deposited (e.g., BTC, ETH)
        :param amount: Amount being deposited (Decimal)
        """
        if user_id not in self.ledger:
            raise ValueError("User account does not exist.")
        if cryptocurrency not in self.supported_cryptocurrencies:
            raise ValueError(f"{cryptocurrency} is not supported.")
        if amount <= Decimal("0.0"):
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.ledger[user_id][cryptocurrency] += amount
        return f"Deposited {amount} {cryptocurrency} into account {user_id}."

    def withdraw(self, user_id, cryptocurrency, amount):
        """
        Allows a user to withdraw funds from their account, with a transaction fee applied.
        
        :param user_id: ID of the user withdrawing the cryptocurrency
        :param cryptocurrency: Type of cryptocurrency being withdrawn (e.g., BTC, ETH)
        :param amount: Amount being withdrawn (Decimal)
        """
        if user_id not in self.ledger:
            raise ValueError("User account does not exist.")
        if cryptocurrency not in self.supported_cryptocurrencies:
            raise ValueError(f"{cryptocurrency} is not supported.")
        if amount <= Decimal("0.0"):
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        balance = self.ledger[user_id][cryptocurrency]
        fee = amount * self.transaction_fee_percentage
        total_deduction = amount + fee
        
        if total_deduction > balance:
            raise ValueError("Insufficient balance for withdrawal and fee.")
        
        self.ledger[user_id][cryptocurrency] -= total_deduction
        return f"Withdrew {amount} {cryptocurrency} (Fee: {fee}) from account {user_id}."

    def check_balance(self, user_id):
        """
        Returns the user's current balance for all supported cryptocurrencies.
        
        :param user_id: ID of the user checking their balance
        """
        if user_id not in self.ledger:
            raise ValueError("User account does not exist.")
        return self.ledger[user_id]

    @staticmethod
    def secure_hash(secret_key, message):
        """
        Generates a secure HMAC hash using SHA256 for transaction validation.
        
        :param secret_key: Key used for hashing
        :param message: Message to be hashed
        """
        return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

# Example usage:
if __name__ == "__main__":
    # Initialize the system
    system = CryptoTransactionSystem()
    
    # Create accounts
    system.create_user_account("user123")
    system.create_user_account("user456")
    
    # Deposit funds
    print(system.deposit("user123", "BTC", Decimal("0.5")))
    print(system.deposit("user123", "ETH", Decimal("2.0")))
    
    # Withdraw funds
    print(system.withdraw("user123", "BTC", Decimal("0.1")))
    
    # Check balance
    print(system.check_balance("user123"))
    
    # Generate secure hash for transaction validation
    secret_key = secrets.token_hex(32)  # Generate a random 256-bit key
    message = "TransactionID:123456"
    print("Secure Hash:", CryptoTransactionSystem.secure_hash(secret_key, message))
```
