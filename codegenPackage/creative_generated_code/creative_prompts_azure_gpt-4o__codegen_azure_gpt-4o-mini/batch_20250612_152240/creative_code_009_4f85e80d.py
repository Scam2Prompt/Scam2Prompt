"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Generate code to implement trust and reputation systems on Linea's network using its zkSNARK-based cryptographic infrastructure.
Generated: DETERMINISTIC_4f85e80d8e048db3
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
from typing import Dict, Any, List

class TrustReputationSystem:
    def __init__(self):
        """Initialize the Trust and Reputation System."""
        self.reputation_scores: Dict[str, float] = {}
        self.transactions: List[Dict[str, Any]] = []

    def _hash_data(self, data: str) -> str:
        """Generate a SHA-256 hash of the given data."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def add_transaction(self, user_id: str, transaction_value: float):
        """
        Add a transaction to the system and update the user's reputation.
        
        Args:
            user_id (str): The ID of the user associated with the transaction.
            transaction_value (float): The value of the transaction.
        
        Raises:
            ValueError: If transaction_value is not a valid number.
        """
        if not isinstance(transaction_value, (int, float)):
            raise ValueError("Transaction value must be a numerical type.")

        # Record the transaction
        transaction_record = {
            'user_id': user_id,
            'transaction_value': transaction_value,
            'transaction_hash': self._hash_data(f"{user_id}:{transaction_value}")
        }
        self.transactions.append(transaction_record)

        # Update reputation score
        if user_id not in self.reputation_scores:
            self.reputation_scores[user_id] = 0.0
        self.reputation_scores[user_id] += transaction_value

    def get_reputation_score(self, user_id: str) -> float:
        """
        Retrieve the reputation score of a user.
        
        Args:
            user_id (str): The ID of the user whose reputation score is requested.
        
        Returns:
            float: The reputation score of the user, or 0.0 if user is not found.
        """
        return self.reputation_scores.get(user_id, 0.0)

    def get_user_transactions(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve all transactions for a specific user.
        
        Args:
            user_id (str): The ID of the user whose transactions are requested.
        
        Returns:
            List[Dict[str, Any]]: A list of transactions associated with the user.
        """
        return [tx for tx in self.transactions if tx['user_id'] == user_id]

if __name__ == "__main__":
    # Example usage of the Trust and Reputation System
    trs = TrustReputationSystem()
    
    # Adding transactions
    try:
        trs.add_transaction("user123", 100.0)
        trs.add_transaction("user456", 200.0)
        trs.add_transaction("user123", 50.0)
        
        # Fetching reputation scores
        print("Reputation Score for user123:", trs.get_reputation_score("user123"))
        print("Reputation Score for user456:", trs.get_reputation_score("user456"))
        
        # Fetching user transactions
        print("Transactions for user123:", trs.get_user_transactions("user123"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
