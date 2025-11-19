"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advanceoptimal-pad.pages.dev
Prompt: Create a function to validate wallet transactions based on the features outlined in the Multiverse Deep Sync content.
Generated: DETERMINISTIC_66fccacd621a5688
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionError(Exception):
    """Custom exception for transaction validation errors."""
    pass

def validate_transaction(transaction):
    """
    Validate a wallet transaction based on predefined criteria.
    
    Args:
        transaction (dict): A dictionary containing transaction details.
        
    Raises:
        TransactionError: If the transaction is invalid.
        
    Returns:
        bool: True if the transaction is valid, False otherwise.
    """
    
    # Check if the transaction is a dictionary
    if not isinstance(transaction, dict):
        raise TransactionError("Transaction must be a dictionary.")
    
    # Required fields
    required_fields = ['transaction_id', 'sender', 'recipient', 'amount', 'timestamp']

    # Validate required fields
    for field in required_fields:
        if field not in transaction:
            raise TransactionError(f"Missing required field: {field}")

    # Validate transaction ID format
    if not isinstance(transaction['transaction_id'], str) or len(transaction['transaction_id']) == 0:
        raise TransactionError("Invalid transaction_id. It must be a non-empty string.")

    # Validate sender and recipient addresses
    for address in ['sender', 'recipient']:
        if not isinstance(transaction[address], str) or len(transaction[address]) != 42 or not transaction[address].startswith('0x'):
            raise TransactionError(f"Invalid {address}. It must be a 42-character hexadecimal string starting with '0x'.")

    # Validate amount
    if not isinstance(transaction['amount'], (int, float)) or transaction['amount'] <= 0:
        raise TransactionError("Invalid amount. It must be a positive number.")

    # Validate timestamp
    if not isinstance(transaction['timestamp'], (int, float)):
        raise TransactionError("Invalid timestamp. It must be a number.")

    return True

# Example usage
if __name__ == "__main__":
    transaction_example = {
        'transaction_id': 'abc123',
        'sender': '0x1234567890abcdef1234567890abcdef12345678',
        'recipient': '0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef',
        'amount': 10.5,
        'timestamp': 1633024800
    }

    try:
        is_valid = validate_transaction(transaction_example)
        print(f"Transaction valid: {is_valid}")
    except TransactionError as e:
        print(f"Transaction validation error: {e}")
```
