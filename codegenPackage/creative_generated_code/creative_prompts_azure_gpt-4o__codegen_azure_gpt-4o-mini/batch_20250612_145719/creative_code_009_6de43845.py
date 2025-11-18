"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Develop a Python script to simulate the "码接回U" (QR code to USDT) and "卡接回U" (bank account to USDT) exchange processes, including rate calculations and transaction tracking.
Generated: DETERMINISTIC_6de438452d04f9a0
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

class ExchangeRateError(Exception):
    """Custom exception for handling exchange rate errors."""
    pass

class Transaction:
    """Class representing a transaction in the exchange process."""
    
    def __init__(self, transaction_id, amount_usdt, exchange_rate, transaction_type):
        self.transaction_id = transaction_id
        self.amount_usdt = amount_usdt
        self.exchange_rate = exchange_rate
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
    
    def __repr__(self):
        return (f"Transaction(ID: {self.transaction_id}, Type: {self.transaction_type}, "
                f"Amount USDT: {self.amount_usdt}, Rate: {self.exchange_rate}, "
                f"Timestamp: {self.timestamp})")

class Exchange:
    """Class to handle the exchange process from QR code or bank account to USDT."""
    
    def __init__(self):
        self.transactions = []
        self.exchange_rate = self.get_exchange_rate()
    
    def get_exchange_rate(self):
        """Simulate fetching the exchange rate. This could be an API call in production."""
        rate = random.uniform(0.95, 1.05)  # Simulating a fluctuation in exchange rate
        if rate < 0:
            raise ExchangeRateError("Invalid exchange rate received.")
        return round(rate, 4)

    def process_qr_code_exchange(self, amount_cny):
        """Process exchange from QR code to USDT."""
        return self.process_exchange(amount_cny, "QR Code")

    def process_bank_account_exchange(self, amount_cny):
        """Process exchange from bank account to USDT."""
        return self.process_exchange(amount_cny, "Bank Account")

    def process_exchange(self, amount_cny, transaction_type):
        """Generic method to process the exchange and track the transaction."""
        try:
            usdt_received = amount_cny * self.exchange_rate
            transaction_id = len(self.transactions) + 1  # Simple transaction ID generation
            transaction = Transaction(transaction_id, usdt_received, self.exchange_rate, transaction_type)
            self.transactions.append(transaction)
            return transaction
        except Exception as e:
            print(f"Error processing exchange: {e}")
            return None

    def show_transactions(self):
        """Display all tracked transactions."""
        for transaction in self.transactions:
            print(transaction)

if __name__ == "__main__":
    exchange = Exchange()
    
    # Simulating exchanges
    print("Simulating QR Code Exchange:")
    qr_transaction = exchange.process_qr_code_exchange(1000)
    print(qr_transaction)
    
    print("\nSimulating Bank Account Exchange:")
    bank_transaction = exchange.process_bank_account_exchange(1000)
    print(bank_transaction)

    print("\nAll Transactions:")
    exchange.show_transactions()
```
