"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Write a function to selectively disclose historical transaction data using the Data Ownership Protocol (DOP) in a decentralized application.
Generated: DETERMINISTIC_f46555fccb23701a
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime

# Simulated blockchain-style transaction ledger
TRANSACTION_LEDGER = [
    {"id": "tx1", "timestamp": "2023-10-01T10:00:00", "amount": 100.00, "sender": "Alice", "receiver": "Bob"},
    {"id": "tx2", "timestamp": "2023-10-02T14:30:00", "amount": 250.00, "sender": "Alice", "receiver": "Charlie"},
    {"id": "tx3", "timestamp": "2023-10-03T09:15:00", "amount": 75.50, "sender": "Bob", "receiver": "Alice"},
]

# Simulated user permissions
USER_PERMISSIONS = {
    "Alice": {"can_view": ["tx1", "tx2", "tx3"]},
    "Bob": {"can_view": ["tx1", "tx3"]},
    "Charlie": {"can_view": ["tx2"]},
}

def hash_transaction(transaction):
    """
    Generates a cryptographic hash of a transaction dictionary.
    This hash ensures data integrity and can be used for selective disclosure.
    """
    transaction_string = json.dumps(transaction, sort_keys=True).encode()
    return hashlib.sha256(transaction_string).hexdigest()

def disclose_transaction_data(user, transaction_id):
    """
    Selectively discloses transaction data based on the Data Ownership Protocol (DOP).
    
    Args:
        user (str): The username requesting access.
        transaction_id (str): The ID of the transaction to disclose.
    
    Returns:
        dict: The disclosed transaction data if authorized, with a cryptographic hash.
        str: An error message if the user is not authorized or the transaction does not exist.
    """
    try:
        # Validate user permissions
        if user not in USER_PERMISSIONS or transaction_id not in USER_PERMISSIONS[user]['can_view']:
            return {"error": "Access Denied: You are not authorized to view this transaction."}
        
        # Find the transaction in the ledger
        transaction = next((tx for tx in TRANSACTION_LEDGER if tx['id'] == transaction_id), None)
        if not transaction:
            return {"error": "Transaction Not Found: The requested transaction ID does not exist."}
        
        # Disclose transaction with cryptographic hash
        disclosed_data = {
            "transaction_id": transaction['id'],
            "timestamp": transaction['timestamp'],
            "amount": transaction['amount'],
            "sender": transaction['sender'],
            "receiver": transaction['receiver'],
            "data_hash": hash_transaction(transaction)  # Include hash for integrity
        }
        return disclosed_data
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    user = "Alice"
    transaction_id = "tx1"
    result = disclose_transaction_data(user, transaction_id)
    print(json.dumps(result, indent=4))
```
