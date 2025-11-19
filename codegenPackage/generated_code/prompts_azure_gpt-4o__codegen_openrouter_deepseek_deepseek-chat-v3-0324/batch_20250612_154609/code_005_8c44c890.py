"""
Generated Code Metadata:
========================
Original URL: https://midoin.com
Prompt: Generate a script to enforce user-defined privacy settings when sharing Midoin transaction data with friends or the community.
Generated: DETERMINISTIC_8c44c8909a122e27
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Union

class PrivacyLevel(Enum):
    """Enum representing different privacy levels for transaction sharing."""
    PRIVATE = 0       # Transaction is not shared with anyone
    FRIENDS = 1       # Transaction is shared with friends only
    COMMUNITY = 2     # Transaction is shared with the entire community

class Transaction:
    """Class representing a Midoin transaction."""
    
    def __init__(self, tx_id: str, amount: float, sender: str, receiver: str, metadata: Optional[Dict] = None):
        """Initialize a transaction with required fields and optional metadata.
        
        Args:
            tx_id: Unique transaction identifier
            amount: Transaction amount
            sender: Sender's user ID
            receiver: Receiver's user ID
            metadata: Optional additional transaction data
        """
        self.tx_id = tx_id
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.metadata = metadata or {}
        self.privacy_level = PrivacyLevel.PRIVATE  # Default to most restrictive

    def set_privacy_level(self, level: PrivacyLevel) -> None:
        """Set the privacy level for this transaction.
        
        Args:
            level: PrivacyLevel enum value
        """
        if not isinstance(level, PrivacyLevel):
            raise ValueError("Privacy level must be a PrivacyLevel enum value")
        self.privacy_level = level

    def to_shared_dict(self, requester_id: str) -> Optional[Dict]:
        """Convert transaction to a shareable dictionary based on privacy settings.
        
        Args:
            requester_id: User ID of the person requesting the data
            
        Returns:
            Dictionary with transaction data if allowed, None otherwise
        """
        if self.privacy_level == PrivacyLevel.PRIVATE:
            return None
            
        if self.privacy_level == PrivacyLevel.FRIENDS:
            if requester_id not in [self.sender, self.receiver]:
                return None
                
        # For COMMUNITY level or FRIENDS who are sender/receiver
        shared_data = {
            'tx_id': self.tx_id,
            'amount': self.amount,
            'timestamp': self.metadata.get('timestamp'),
            'description': self.metadata.get('description', '')
        }
        
        # Only show sender/receiver details if requester is involved
        if requester_id in [self.sender, self.receiver]:
            shared_data['sender'] = self.sender
            shared_data['receiver'] = self.receiver
        
        return shared_data

class PrivacyManager:
    """Manages privacy settings and sharing of transactions."""
    
    def __init__(self):
        """Initialize with empty transaction store."""
        self.transactions: Dict[str, Transaction] = {}
    
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to the manager.
        
        Args:
            transaction: Transaction object to add
        """
        if not isinstance(transaction, Transaction):
            raise ValueError("Can only add Transaction objects")
        self.transactions[transaction.tx_id] = transaction
    
    def get_shared_transactions(self, requester_id: str) -> List[Dict]:
        """Get all transactions that can be shared with the requester.
        
        Args:
            requester_id: User ID of the person requesting the data
            
        Returns:
            List of transaction dictionaries that can be shared
        """
        if not requester_id:
            raise ValueError("Requester ID cannot be empty")
            
        shared = []
        for tx in self.transactions.values():
            shared_data = tx.to_shared_dict(requester_id)
            if shared_data:
                shared.append(shared_data)
        return shared
    
    def bulk_set_privacy(self, tx_ids: List[str], level: PrivacyLevel) -> None:
        """Set privacy level for multiple transactions at once.
        
        Args:
            tx_ids: List of transaction IDs to update
            level: PrivacyLevel to set
        """
        if not isinstance(level, PrivacyLevel):
            raise ValueError("Privacy level must be a PrivacyLevel enum value")
            
        for tx_id in tx_ids:
            if tx_id in self.transactions:
                self.transactions[tx_id].set_privacy_level(level)
    
    def export_privacy_settings(self) -> Dict[str, int]:
        """Export current privacy settings for all transactions.
        
        Returns:
            Dictionary mapping transaction IDs to their privacy levels
        """
        return {tx_id: tx.privacy_level.value for tx_id, tx in self.transactions.items()}
    
    def import_privacy_settings(self, settings: Dict[str, int]) -> None:
        """Import privacy settings for transactions.
        
        Args:
            settings: Dictionary mapping transaction IDs to privacy level values
        """
        for tx_id, level_value in settings.items():
            if tx_id in self.transactions:
                try:
                    level = PrivacyLevel(level_value)
                    self.transactions[tx_id].set_privacy_level(level)
                except ValueError:
                    continue  # Skip invalid privacy levels

def validate_user_id(user_id: str) -> bool:
    """Validate that a user ID meets basic requirements.
    
    Args:
        user_id: User ID to validate
        
    Returns:
        True if valid, False otherwise
    """
    return isinstance(user_id, str) and len(user_id) >= 3 and user_id.isalnum()

# Example usage
if __name__ == "__main__":
    # Initialize privacy manager
    manager = PrivacyManager()
    
    # Create some sample transactions
    tx1 = Transaction("tx123", 50.0, "user1", "user2", {"timestamp": "2023-01-01", "description": "Dinner"})
    tx2 = Transaction("tx124", 100.0, "user2", "user3", {"timestamp": "2023-01-02", "description": "Rent"})
    tx3 = Transaction("tx125", 25.0, "user1", "user3", {"timestamp": "2023-01-03", "description": "Gift"})
    
    # Add transactions to manager
    manager.add_transaction(tx1)
    manager.add_transaction(tx2)
    manager.add_transaction(tx3)
    
    # Set privacy levels
    tx1.set_privacy_level(PrivacyLevel.FRIENDS)
    tx2.set_privacy_level(PrivacyLevel.COMMUNITY)
    tx3.set_privacy_level(PrivacyLevel.PRIVATE)
    
    # Test sharing with different users
    print("User1's view:")
    print(json.dumps(manager.get_shared_transactions("user1"), indent=2))
    
    print("\nUser2's view:")
    print(json.dumps(manager.get_shared_transactions("user2"), indent=2))
    
    print("\nUser4's view (stranger):")
    print(json.dumps(manager.get_shared_transactions("user4"), indent=2))
```
