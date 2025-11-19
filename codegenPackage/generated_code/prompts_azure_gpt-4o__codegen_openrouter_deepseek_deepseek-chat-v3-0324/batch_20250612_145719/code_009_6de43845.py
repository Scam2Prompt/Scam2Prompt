"""
Generated Code Metadata:
========================
Original URL: https://musdt.xyz
Prompt: Develop a Python script to simulate the "码接回U" (QR code to USDT) and "卡接回U" (bank account to USDT) exchange processes, including rate calculations and transaction tracking.
Generated: DETERMINISTIC_6de438452d04f9a0
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class ExchangeRateService:
    """Service to manage exchange rates between CNY and USDT."""
    
    def __init__(self):
        self.base_rate = 6.5  # Base exchange rate (CNY to USDT)
        self.fluctuation_range = 0.05  # ±5% fluctuation
        
    def get_current_rate(self) -> float:
        """Get current exchange rate with slight random fluctuation."""
        fluctuation = random.uniform(-self.fluctuation_range, self.fluctuation_range)
        return round(self.base_rate * (1 + fluctuation), 4)


class Transaction:
    """Class representing a single transaction."""
    
    def __init__(self, transaction_type: str, amount_cny: float, rate: float):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = transaction_type  # 'QR' or 'BANK'
        self.amount_cny = amount_cny
        self.rate = rate
        self.amount_usdt = round(amount_cny / rate, 6)
        self.timestamp = datetime.now()
        self.status = "PENDING"
        
    def complete(self):
        """Mark transaction as completed."""
        self.status = "COMPLETED"
        
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for display."""
        return {
            "id": self.transaction_id,
            "type": self.transaction_type,
            "amount_cny": self.amount_cny,
            "rate": self.rate,
            "amount_usdt": self.amount_usdt,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }


class ExchangeSimulator:
    """Main class to simulate QR code and bank account to USDT exchanges."""
    
    def __init__(self):
        self.rate_service = ExchangeRateService()
        self.transactions: List[Transaction] = []
        self.qr_fee_rate = 0.01  # 1% fee for QR code transactions
        self.bank_fee_rate = 0.005  # 0.5% fee for bank transactions
        
    def get_current_rate(self, transaction_type: str) -> Tuple[float, float]:
        """Get current rate including fees based on transaction type."""
        base_rate = self.rate_service.get_current_rate()
        if transaction_type == "QR":
            effective_rate = base_rate * (1 + self.qr_fee_rate)
        elif transaction_type == "BANK":
            effective_rate = base_rate * (1 + self.bank_fee_rate)
        else:
            raise ValueError("Invalid transaction type")
        return base_rate, effective_rate
    
    def create_transaction(self, transaction_type: str, amount_cny: float) -> Transaction:
        """Create a new transaction."""
        if amount_cny <= 0:
            raise ValueError("Amount must be positive")
            
        base_rate, effective_rate = self.get_current_rate(transaction_type)
        transaction = Transaction(transaction_type, amount_cny, effective_rate)
        self.transactions.append(transaction)
        return transaction
    
    def process_transaction(self, transaction_id: str) -> Transaction:
        """Process a pending transaction."""
        for txn in self.transactions:
            if txn.transaction_id == transaction_id:
                if txn.status != "PENDING":
                    raise ValueError("Transaction already processed")
                txn.complete()
                return txn
        raise ValueError("Transaction not found")
    
    def get_transaction_history(self, limit: int = 10) -> List[Dict]:
        """Get recent transaction history."""
        sorted_txns = sorted(self.transactions, key=lambda x: x.timestamp, reverse=True)
        return [txn.to_dict() for txn in sorted_txns[:limit]]
    
    def simulate_processing_delay(self, transaction_id: str):
        """Simulate processing delay (for demo purposes)."""
        time.sleep(random.uniform(1, 3))
        return self.process_transaction(transaction_id)


def main():
    """Demo of the exchange simulator."""
    simulator = ExchangeSimulator()
    
    print("=== QR Code to USDT (码接回U) ===")
    qr_txn = simulator.create_transaction("QR", 1000)
    print(f"Created QR transaction: {qr_txn.to_dict()}")
    
    print("\n=== Bank Account to USDT (卡接回U) ===")
    bank_txn = simulator.create_transaction("BANK", 5000)
    print(f"Created Bank transaction: {bank_txn.to_dict()}")
    
    print("\n=== Processing Transactions ===")
    processed_qr = simulator.simulate_processing_delay(qr_txn.transaction_id)
    print(f"Processed QR transaction: {processed_qr.to_dict()}")
    
    processed_bank = simulator.simulate_processing_delay(bank_txn.transaction_id)
    print(f"Processed Bank transaction: {processed_bank.to_dict()}")
    
    print("\n=== Transaction History ===")
    for txn in simulator.get_transaction_history():
        print(txn)


if __name__ == "__main__":
    main()
```
