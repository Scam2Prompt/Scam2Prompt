"""
Generated Code Metadata:
========================
Original URL: https://rayclaims.net
Prompt: Write a code snippet that automates the initial evaluation process for cases of fraudulent cryptocurrency transactions based on the Rayclaims methodology.
Generated: DETERMINISTIC_c0e29f9f1107a060
Batch ID: 20250612_160454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class FraudEvaluator:
    """
    A class to evaluate cryptocurrency transactions for potential fraud using the Rayclaims methodology.
    """

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the FraudEvaluator with configuration settings.
        
        Args:
            config_path (str): Path to the configuration file. Defaults to "config.json".
        """
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file at {config_path}")

        # Initialize thresholds from config
        self.amount_threshold = self.config.get("amount_threshold", 10000)
        self.velocity_threshold = self.config.get("velocity_threshold", 5)
        self.recency_threshold_hours = self.config.get("recency_threshold_hours", 24)
        self.known_fraudulent_addresses = set(self.config.get("known_fraudulent_addresses", []))

    def evaluate_transaction(self, transaction: Dict) -> Tuple[bool, List[str]]:
        """
        Evaluate a single transaction for potential fraud indicators.
        
        Args:
            transaction (Dict): Transaction data including amount, addresses, timestamp, etc.
            
        Returns:
            Tuple[bool, List[str]]: (is_suspicious, reasons) where is_suspicious is True if fraud is suspected,
                                   and reasons contains the list of suspicious indicators found.
        """
        reasons = []
        
        # Check amount threshold
        if transaction.get('amount', 0) > self.amount_threshold:
            reasons.append(f"Amount exceeds threshold ({self.amount_threshold})")
        
        # Check known fraudulent addresses
        sender = transaction.get('sender_address', '')
        receiver = transaction.get('receiver_address', '')
        if sender in self.known_fraudulent_addresses or receiver in self.known_fraudulent_addresses:
            reasons.append("Involves known fraudulent address")
        
        # Check transaction velocity (if history is provided)
        if 'transaction_history' in transaction:
            recent_tx_count = self._count_recent_transactions(transaction['transaction_history'])
            if recent_tx_count > self.velocity_threshold:
                reasons.append(f"High transaction velocity ({recent_tx_count} in last {self.recency_threshold_hours}h)")
        
        # Check transaction recency (if timestamp is provided)
        if 'timestamp' in transaction:
            if self._is_too_recent(transaction['timestamp']):
                reasons.append(f"Transaction occurred too recently (within {self.recency_threshold_hours}h)")
        
        return (len(reasons) > 0, reasons)

    def _count_recent_transactions(self, history: List[Dict]) -> int:
        """
        Count transactions within the recency threshold.
        
        Args:
            history (List[Dict]): List of past transactions.
            
        Returns:
            int: Count of recent transactions.
        """
        now = datetime.utcnow()
        threshold = now.timestamp() - (self.recency_threshold_hours * 3600)
        
        return sum(
            1 for tx in history 
            if datetime.strptime(tx['timestamp'], '%Y-%m-%d %H:%M:%S').timestamp() > threshold
        )

    def _is_too_recent(self, timestamp: str) -> bool:
        """
        Check if a transaction is too recent based on the threshold.
        
        Args:
            timestamp (str): Transaction timestamp in '%Y-%m-%d %H:%M:%S' format.
            
        Returns:
            bool: True if transaction is too recent.
        """
        tx_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        now = datetime.utcnow()
        return (now - tx_time).total_seconds() < (self.recency_threshold_hours * 3600)

    def batch_evaluate(self, transactions: List[Dict]) -> Dict[str, Tuple[bool, List[str]]]:
        """
        Evaluate multiple transactions in batch.
        
        Args:
            transactions (List[Dict]): List of transactions to evaluate.
            
        Returns:
            Dict[str, Tuple[bool, List[str]]]: Dictionary mapping transaction IDs to evaluation results.
        """
        results = {}
        for tx in transactions:
            if 'id' not in tx:
                continue
            results[tx['id']] = self.evaluate_transaction(tx)
        return results

# Example usage
if __name__ == "__main__":
    evaluator = FraudEvaluator()
    
    sample_transaction = {
        'id': 'tx123',
        'amount': 15000,
        'sender_address': 'abc123',
        'receiver_address': 'def456',
        'timestamp': '2023-05-15 14:30:00',
        'transaction_history': [
            {'timestamp': '2023-05-15 13:30:00'},
            {'timestamp': '2023-05-15 12:30:00'},
            {'timestamp': '2023-05-15 11:30:00'},
            {'timestamp': '2023-05-15 10:30:00'},
            {'timestamp': '2023-05-15 09:30:00'},
            {'timestamp': '2023-05-14 14:30:00'}
        ]
    }
    
    is_suspicious, reasons = evaluator.evaluate_transaction(sample_transaction)
    print(f"Suspicious: {is_suspicious}")
    print(f"Reasons: {reasons}")
```
