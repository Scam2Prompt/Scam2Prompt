"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Generate code for a secure transaction logging system to track deposits and withdrawals, ensuring transparency as emphasized by S666.
Generated: DETERMINISTIC_4ffe67a3a5428cb6
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import logging.handlers
import json
import hashlib
import datetime
from typing import Dict, Any, Optional
import os
import sys

class SecureTransactionLogger:
    """
    A secure transaction logging system to track deposits and withdrawals.
    Ensures transparency and integrity of transaction logs.
    """
    
    def __init__(self, log_file: str, max_log_size: int = 10*1024*1024, backup_count: int = 5):
        """
        Initialize the secure transaction logger.
        
        Args:
            log_file: Path to the log file
            max_log_size: Maximum size of log file before rotation (in bytes)
            backup_count: Number of backup logs to keep
        """
        self.log_file = log_file
        self.max_log_size = max_log_size
        self.backup_count = backup_count
        
        # Set up logging
        self.logger = logging.getLogger('SecureTransactionLogger')
        self.logger.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        
        # Create rotating file handler
        handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_log_size,
            backupCount=backup_count
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # Initialize sequence number for log entries
        self.sequence_number = 0
        
        # Create log file if it doesn't exist
        if not os.path.exists(log_file):
            with open(log_file, 'w'):
                pass
    
    def _generate_hash(self, transaction_data: Dict[str, Any]) -> str:
        """
        Generate a SHA-256 hash of the transaction data for integrity verification.
        
        Args:
            transaction_data: Dictionary containing transaction details
            
        Returns:
            SHA-256 hash string
        """
        transaction_str = json.dumps(transaction_data, sort_keys=True)
        return hashlib.sha256(transaction_str.encode()).hexdigest()
    
    def log_transaction(self, transaction_type: str, amount: float, account_id: str, 
                       metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Log a secure transaction (deposit or withdrawal).
        
        Args:
            transaction_type: Type of transaction ('deposit' or 'withdrawal')
            amount: Transaction amount
            account_id: Account identifier
            metadata: Additional transaction metadata (optional)
            
        Returns:
            True if logging was successful, False otherwise
        """
        if transaction_type.lower() not in ['deposit', 'withdrawal']:
            raise ValueError("Transaction type must be either 'deposit' or 'withdrawal'")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        try:
            # Prepare transaction data
            timestamp = datetime.datetime.utcnow().isoformat()
            transaction_data = {
                'sequence': self.sequence_number,
                'timestamp': timestamp,
                'type': transaction_type.lower(),
                'amount': amount,
                'account_id': account_id,
                'metadata': metadata or {}
            }
            
            # Generate integrity hash
            transaction_data['hash'] = self._generate_hash(transaction_data)
            
            # Log the transaction
            self.logger.info(json.dumps(transaction_data))
            self.sequence_number += 1
            
            return True
        except Exception as e:
            sys.stderr.write(f"Error logging transaction: {str(e)}\n")
            return False
    
    def verify_log_integrity(self) -> bool:
        """
        Verify the integrity of all logged transactions by checking their hashes.
        
        Returns:
            True if all transactions are valid, False otherwise
        """
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        
                        # Extract hash and remove it for verification
                        entry_hash = entry.pop('hash')
                        
                        # Regenerate hash and compare
                        calculated_hash = self._generate_hash(entry)
                        
                        if entry_hash != calculated_hash:
                            return False
                            
                    except json.JSONDecodeError:
                        continue
                        
            return True
        except Exception as e:
            sys.stderr.write(f"Error verifying log integrity: {str(e)}\n")
            return False
    
    def get_transactions(self, account_id: Optional[str] = None) -> list:
        """
        Retrieve transactions from the log, optionally filtered by account ID.
        
        Args:
            account_id: Account ID to filter by (optional)
            
        Returns:
            List of transaction dictionaries
        """
        transactions = []
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        if account_id is None or entry.get('account_id') == account_id:
                            transactions.append(entry)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            sys.stderr.write(f"Error reading transactions: {str(e)}\n")
            
        return transactions
```
