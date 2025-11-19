"""
Generated Code Metadata:
========================
Original URL: https://revoke.markets
Prompt: How can I develop a system to monitor and automatically revoke suspicious market transactions?
Generated: DETERMINISTIC_a6fb5c83bd782c8f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REVOKED = "revoked"
    FLAGGED = "flagged"

class Transaction:
    def __init__(self, transaction_id: str, user_id: str, amount: float, timestamp: datetime):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp
        self.status = TransactionStatus.PENDING

    def __repr__(self):
        return f"Transaction(id={self.transaction_id}, user={self.user_id}, amount={self.amount}, status={self.status.value})"

class FraudDetectionRule:
    def __init__(self, name: str, description: str, condition_func):
        self.name = name
        self.description = description
        self.condition_func = condition_func

    def evaluate(self, transaction: Transaction, user_history: List[Transaction]) -> bool:
        try:
            return self.condition_func(transaction, user_history)
        except Exception as e:
            logger.error(f"Error evaluating rule {self.name}: {e}")
            return False

class TransactionMonitor:
    def __init__(self):
        self.transactions: Dict[str, Transaction] = {}
        self.user_transactions: Dict[str, List[Transaction]] = {}
        self.fraud_rules: List[FraudDetectionRule] = []
        self._initialize_rules()

    def _initialize_rules(self):
        # Rule 1: Large amount transaction
        def large_amount_rule(transaction, _):
            return transaction.amount > 10000
        
        # Rule 2: Multiple transactions in short time
        def rapid_transactions_rule(transaction, history):
            recent_transactions = [
                t for t in history 
                if t.timestamp > transaction.timestamp - timedelta(minutes=30)
            ]
            return len(recent_transactions) > 5
        
        # Rule 3: Unusual time for user
        def unusual_time_rule(transaction, history):
            if not history:
                return False
            avg_hour = sum(t.timestamp.hour for t in history) / len(history)
            return abs(transaction.timestamp.hour - avg_hour) > 3
        
        self.fraud_rules.extend([
            FraudDetectionRule(
                "Large Amount", 
                "Transaction amount exceeds $10,000",
                large_amount_rule
            ),
            FraudDetectionRule(
                "Rapid Transactions",
                "More than 5 transactions in 30 minutes",
                rapid_transactions_rule
            ),
            FraudDetectionRule(
                "Unusual Time",
                "Transaction occurs at unusual hour for user",
                unusual_time_rule
            )
        ])

    def add_transaction(self, transaction: Transaction):
        self.transactions[transaction.transaction_id] = transaction
        
        if transaction.user_id not in self.user_transactions:
            self.user_transactions[transaction.user_id] = []
        self.user_transactions[transaction.user_id].append(transaction)

    def check_for_fraud(self, transaction_id: str) -> Optional[Transaction]:
        if transaction_id not in self.transactions:
            logger.warning(f"Transaction {transaction_id} not found")
            return None

        transaction = self.transactions[transaction_id]
        user_history = self.user_transactions.get(transaction.user_id, [])

        for rule in self.fraud_rules:
            if rule.evaluate(transaction, user_history):
                transaction.status = TransactionStatus.FLAGGED
                logger.warning(f"Transaction {transaction_id} flagged by rule: {rule.name}")
                return transaction

        transaction.status = TransactionStatus.COMPLETED
        return transaction

    def revoke_transaction(self, transaction_id: str) -> bool:
        if transaction_id not in self.transactions:
            logger.warning(f"Transaction {transaction_id} not found for revocation")
            return False

        transaction = self.transactions[transaction_id]
        if transaction.status == TransactionStatus.COMPLETED:
            logger.warning(f"Cannot revoke completed transaction {transaction_id}")
            return False

        transaction.status = TransactionStatus.REVOKED
        logger.info(f"Transaction {transaction_id} revoked successfully")
        return True

    def monitor_transactions(self, interval: int = 60):
        """Continuously monitor transactions for fraud detection."""
        logger.info("Starting transaction monitoring system")
        try:
            while True:
                current_time = datetime.now()
                for transaction in list(self.transactions.values()):
                    if (current_time - transaction.timestamp) > timedelta(minutes=5):
                        if transaction.status == TransactionStatus.PENDING:
                            self.check_for_fraud(transaction.transaction_id)
                
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Stopping transaction monitoring system")
        except Exception as e:
            logger.error(f"Error in monitoring loop: {e}")

# Example usage
if __name__ == "__main__":
    monitor = TransactionMonitor()
    
    # Simulate adding transactions
    test_transactions = [
        Transaction("tx1", "user1", 500.0, datetime.now()),
        Transaction("tx2", "user1", 15000.0, datetime.now()),
        Transaction("tx3", "user2", 200.0, datetime.now()),
        Transaction("tx4", "user1", 100.0, datetime.now() - timedelta(minutes=10)),
        Transaction("tx5", "user1", 100.0, datetime.now() - timedelta(minutes=20)),
        Transaction("tx6", "user1", 100.0, datetime.now() - timedelta(minutes=25)),
        Transaction("tx7", "user1", 100.0, datetime.now() - timedelta(minutes=28)),
        Transaction("tx8", "user1", 100.0, datetime.now() - timedelta(minutes=29)),
        Transaction("tx9", "user1", 100.0, datetime.now() - timedelta(minutes=31)),
    ]
    
    for tx in test_transactions:
        monitor.add_transaction(tx)
    
    # Check transactions
    for tx_id in ["tx1", "tx2", "tx3", "tx8"]:
        result = monitor.check_for_fraud(tx_id)
        if result and result.status == TransactionStatus.FLAGGED:
            monitor.revoke_transaction(tx_id)
    
    # Start monitoring
    monitor.monitor_transactions()
```
