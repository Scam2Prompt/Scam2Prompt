"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Write code for a transaction monitoring system that checks compliance with legal regulations to prevent money laundering, inspired by MMOGDV.COM's warnings about "Nội Dung Chuyển Khoản."
Generated: DETERMINISTIC_f46acd3cfddefaad
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    """Class representing a financial transaction."""
    
    def __init__(self, transaction_id: str, amount: float, sender: str, receiver: str, description: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.description = description

class TransactionMonitor:
    """Class responsible for monitoring transactions for compliance with regulations."""
    
    def __init__(self, thresholds: Dict[str, float]):
        """
        Initializes the TransactionMonitor with compliance thresholds.
        
        :param thresholds: A dictionary mapping transaction types to their threshold values.
        """
        self.thresholds = thresholds

    def is_compliant(self, transaction: Transaction) -> bool:
        """
        Checks if a transaction is compliant with the defined thresholds.
        
        :param transaction: The transaction to check.
        :return: True if the transaction is compliant, False otherwise.
        """
        try:
            if transaction.amount > self.thresholds.get(transaction.description, float('inf')):
                logging.warning(f"Transaction {transaction.transaction_id} exceeds the compliance threshold.")
                return False
            return True
        except Exception as e:
            logging.error(f"Error while checking compliance for transaction {transaction.transaction_id}: {e}")
            return False

    def monitor_transactions(self, transactions: List[Transaction]) -> List[Dict[str, Any]]:
        """
        Monitors a list of transactions and returns a report of compliance status.
        
        :param transactions: A list of transactions to monitor.
        :return: A list of dictionaries containing transaction IDs and their compliance status.
        """
        report = []
        
        for transaction in transactions:
            compliant = self.is_compliant(transaction)
            report.append({
                'transaction_id': transaction.transaction_id,
                'compliant': compliant
            })
        
        return report

def main():
    """Main function to run the transaction monitoring system."""
    
    # Define compliance thresholds for different transaction descriptions
    compliance_thresholds = {
        'Nội Dung Chuyển Khoản': 10000.0,  # Example threshold for a specific type
        'Normal Transfer': 5000.0            # Example threshold for normal transfers
    }

    # Initialize the transaction monitor
    monitor = TransactionMonitor(thresholds=compliance_thresholds)

    # Sample transaction data
    transactions = [
        Transaction("TX001", 15000.0, "Alice", "Bob", "Nội Dung Chuyển Khoản"),
        Transaction("TX002", 4000.0, "Charlie", "Dave", "Normal Transfer"),
        Transaction("TX003", 8000.0, "Eve", "Frank", "Nội Dung Chuyển Khoản"),
    ]

    # Monitor the transactions
    report = monitor.monitor_transactions(transactions)

    # Print the compliance report
    for entry in report:
        print(f"Transaction ID: {entry['transaction_id']}, Compliant: {entry['compliant']}")

if __name__ == "__main__":
    main()
```
