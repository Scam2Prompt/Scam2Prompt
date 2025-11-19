"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write code for a transaction monitoring system that checks compliance with legal regulations to prevent money laundering, inspired by MMOGDV.COM's warnings about "Nội Dung Chuyển Khoản."
Generated: DETERMINISTIC_f46acd3cfddefaad
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('transaction_monitor.log'),
        logging.StreamHandler()
    ]
)

class TransactionMonitor:
    """
    A system to monitor financial transactions for compliance with anti-money laundering (AML) regulations.
    """
    
    def __init__(self, suspicious_keywords: List[str] = None, threshold_amount: float = 10000.0):
        """
        Initialize the transaction monitor with configuration.
        
        Args:
            suspicious_keywords: List of keywords to flag in transaction descriptions
            threshold_amount: Amount above which transactions are flagged for review
        """
        self.suspicious_keywords = suspicious_keywords or [
            'nội dung chuyển khoản', 'transfer content', 'unknown', 'miscellaneous'
        ]
        self.threshold_amount = threshold_amount
        self.sanctioned_entities = self._load_sanctioned_entities()
        
    def _load_sanctioned_entities(self) -> List[str]:
        """Load list of sanctioned entities from a data source (simulated here)."""
        return [
            "XYZ Terror Group",
            "ABC Drug Cartel",
            "Sanctioned Individual"
        ]
    
    def check_transaction(self, transaction: Dict) -> Tuple[bool, List[str]]:
        """
        Check a transaction for compliance issues.
        
        Args:
            transaction: Dictionary containing transaction details with keys:
                - amount: float
                - description: str
                - sender: str
                - receiver: str
                - timestamp: str (ISO format)
                
        Returns:
            Tuple of (is_suspicious: bool, reasons: List[str])
        """
        reasons = []
        
        try:
            # Check amount threshold
            if transaction['amount'] >= self.threshold_amount:
                reasons.append(f"High amount: {transaction['amount']}")
                
            # Check description for suspicious keywords
            description = transaction['description'].lower()
            for keyword in self.suspicious_keywords:
                if re.search(rf'\b{re.escape(keyword.lower())}\b', description):
                    reasons.append(f"Suspicious description: '{keyword}' found")
                    break
                    
            # Check against sanctioned entities
            for entity in self.sanctioned_entities:
                if (entity.lower() in transaction['sender'].lower() or 
                    entity.lower() in transaction['receiver'].lower()):
                    reasons.append(f"Sanctioned entity involved: {entity}")
                    break
                    
            # Check for unusual timing (between midnight and 5 AM)
            transaction_time = datetime.fromisoformat(transaction['timestamp']).time()
            if transaction_time.hour < 5:
                reasons.append(f"Unusual transaction time: {transaction_time}")
                
        except KeyError as e:
            logging.error(f"Invalid transaction data: missing field {e}")
            raise ValueError(f"Transaction missing required field: {e}")
        except Exception as e:
            logging.error(f"Error processing transaction: {e}")
            raise
            
        return (len(reasons) > 0, reasons)
    
    def monitor_transactions(self, transactions: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Process a batch of transactions and return suspicious ones with reasons.
        
        Args:
            transactions: List of transaction dictionaries
            
        Returns:
            Dictionary with:
                - 'suspicious': List of suspicious transactions with reasons
                - 'clean': List of clean transactions
        """
        results = {'suspicious': [], 'clean': []}
        
        for transaction in transactions:
            try:
                is_suspicious, reasons = self.check_transaction(transaction)
                if is_suspicious:
                    results['suspicious'].append({
                        'transaction': transaction,
                        'reasons': reasons
                    })
                    logging.warning(
                        f"Suspicious transaction detected: {transaction['description']}. "
                        f"Reasons: {', '.join(reasons)}"
                    )
                else:
                    results['clean'].append(transaction)
            except Exception as e:
                logging.error(f"Skipping invalid transaction: {e}")
                continue
                
        return results

# Example usage
if __name__ == "__main__":
    monitor = TransactionMonitor()
    
    sample_transactions = [
        {
            "amount": 15000.0,
            "description": "Payment for services - nội dung chuyển khoản",
            "sender": "John Doe",
            "receiver": "Jane Smith",
            "timestamp": "2023-05-15T03:30:00"
        },
        {
            "amount": 500.0,
            "description": "Gift for birthday",
            "sender": "Alice",
            "receiver": "Bob",
            "timestamp": "2023-05-15T14:15:00"
        },
        {
            "amount": 12000.0,
            "description": "Business transaction",
            "sender": "Company A",
            "receiver": "Sanctioned Individual",
            "timestamp": "2023-05-15T10:00:00"
        }
    ]
    
    results = monitor.monitor_transactions(sample_transactions)
    print(f"Suspicious transactions: {len(results['suspicious'])}")
    print(f"Clean transactions: {len(results['clean'])}")
```
