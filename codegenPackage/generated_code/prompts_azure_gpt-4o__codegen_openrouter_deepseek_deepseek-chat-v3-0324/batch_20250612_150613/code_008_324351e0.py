"""
Generated Code Metadata:
========================
Original URL: https://mint-zielchain.vercel.app
Prompt: Write a program to detect and prevent prohibited activities, such as double NFT transfers or falsifying information, as specified in ZIELCHAIN's prohibited acts section.
Generated: DETERMINISTIC_324351e0ee8b1521
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from typing import Dict, List, Optional, Tuple

class TransactionValidator:
    """
    Validates transactions to prevent prohibited activities on ZIELCHAIN.
    """
    
    def __init__(self):
        self.processed_transactions = set()
        self.nft_transfer_history: Dict[str, List[Tuple[str, str]]] = {}  # NFT ID -> List of (sender, receiver)
    
    def validate_transaction(self, transaction_data: dict) -> Tuple[bool, Optional[str]]:
        """
        Validates a transaction against prohibited activities.
        
        Args:
            transaction_data: Dictionary containing transaction details
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check for duplicate transaction
        transaction_hash = self._calculate_transaction_hash(transaction_data)
        if transaction_hash in self.processed_transactions:
            return False, "Duplicate transaction detected"
        
        # Validate transaction type specific rules
        tx_type = transaction_data.get('type')
        
        if tx_type == 'NFT_TRANSFER':
            return self._validate_nft_transfer(transaction_data)
        elif tx_type == 'DATA_SUBMISSION':
            return self._validate_data_submission(transaction_data)
        else:
            return True, None
    
    def _validate_nft_transfer(self, transaction_data: dict) -> Tuple[bool, Optional[str]]:
        """
        Validates NFT transfer transactions for prohibited activities.
        """
        nft_id = transaction_data.get('nft_id')
        sender = transaction_data.get('sender')
        receiver = transaction_data.get('receiver')
        
        if not all([nft_id, sender, receiver]):
            return False, "Missing required NFT transfer fields"
        
        # Check for double transfer attempts
        if nft_id in self.nft_transfer_history:
            last_transfer = self.nft_transfer_history[nft_id][-1]
            if last_transfer[1] != sender:
                return False, f"Invalid NFT transfer: {sender} doesn't own NFT {nft_id}"
        
        # Record the transfer
        if nft_id not in self.nft_transfer_history:
            self.nft_transfer_history[nft_id] = []
        self.nft_transfer_history[nft_id].append((sender, receiver))
        
        return True, None
    
    def _validate_data_submission(self, transaction_data: dict) -> Tuple[bool, Optional[str]]:
        """
        Validates data submission transactions for falsified information.
        """
        data = transaction_data.get('data')
        proof = transaction_data.get('proof')
        
        if not all([data, proof]):
            return False, "Missing required data submission fields"
        
        # Simple proof verification (in production, this would be more robust)
        calculated_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
        if calculated_hash != proof:
            return False, "Data proof verification failed - possible falsification"
        
        return True, None
    
    def _calculate_transaction_hash(self, transaction_data: dict) -> str:
        """
        Calculates a unique hash for a transaction to detect duplicates.
        """
        sorted_data = json.dumps(transaction_data, sort_keys=True)
        return hashlib.sha256(sorted_data.encode()).hexdigest()
    
    def add_processed_transaction(self, transaction_data: dict) -> None:
        """
        Marks a transaction as processed to prevent duplicates.
        """
        transaction_hash = self._calculate_transaction_hash(transaction_data)
        self.processed_transactions.add(transaction_hash)


class ProhibitedActsMonitor:
    """
    Monitors and prevents prohibited activities on ZIELCHAIN.
    """
    
    def __init__(self):
        self.validator = TransactionValidator()
        self.banned_addresses = set()
    
    def process_transaction(self, transaction_data: dict) -> Tuple[bool, Optional[str]]:
        """
        Processes and validates a transaction.
        
        Args:
            transaction_data: Dictionary containing transaction details
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check if sender is banned
        sender = transaction_data.get('sender')
        if sender and sender in self.banned_addresses:
            return False, "Sender address is banned"
        
        # Validate transaction
        is_valid, error = self.validator.validate_transaction(transaction_data)
        if not is_valid:
            return False, error
        
        # Mark as processed if valid
        self.validator.add_processed_transaction(transaction_data)
        return True, None
    
    def ban_address(self, address: str) -> None:
        """
        Adds an address to the banned list.
        """
        self.banned_addresses.add(address)
    
    def unban_address(self, address: str) -> None:
        """
        Removes an address from the banned list.
        """
        if address in self.banned_addresses:
            self.banned_addresses.remove(address)


# Example usage
if __name__ == "__main__":
    monitor = ProhibitedActsMonitor()
    
    # Example valid NFT transfer
    nft_transfer = {
        'type': 'NFT_TRANSFER',
        'nft_id': 'nft123',
        'sender': 'addr1',
        'receiver': 'addr2',
        'timestamp': 1234567890
    }
    
    is_valid, msg = monitor.process_transaction(nft_transfer)
    print(f"Transaction valid: {is_valid}, Message: {msg}")
    
    # Example invalid double transfer
    invalid_transfer = {
        'type': 'NFT_TRANSFER',
        'nft_id': 'nft123',
        'sender': 'addr3',  # Not the current owner
        'receiver': 'addr4',
        'timestamp': 1234567891
    }
    
    is_valid, msg = monitor.process_transaction(invalid_transfer)
    print(f"Transaction valid: {is_valid}, Message: {msg}")
```
