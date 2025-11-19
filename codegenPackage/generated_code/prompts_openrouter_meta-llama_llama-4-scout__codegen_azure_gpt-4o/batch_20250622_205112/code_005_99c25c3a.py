"""
Generated Code Metadata:
========================
Original URL: https://mini-externalpoint.pages.dev
Prompt: "Design a secure transaction validation system for a decentralized application using a platform with an ever-growing list of supported coins."
Generated: DETERMINISTIC_99c25c3a4e5175af
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
from typing import List, Dict, Union

# Constants for security
SECRET_KEY = b"your-secure-secret-key"  # Replace with a strong, secure key
SUPPORTED_COINS = ["BTC", "ETH", "USDT", "ADA", "DOT"]  # Example list of supported coins

class TransactionValidationError(Exception):
    """Custom exception for transaction validation errors."""
    pass

def validate_transaction(transaction: Dict[str, Union[str, float]]) -> bool:
    """
    Validates a transaction for a decentralized application.

    Args:
        transaction (dict): A dictionary containing transaction details.
            Expected keys: 'coin', 'amount', 'sender', 'receiver', 'signature'

    Returns:
        bool: True if the transaction is valid, False otherwise.

    Raises:
        TransactionValidationError: If the transaction is invalid.
    """
    # Ensure all required fields are present
    required_fields = ['coin', 'amount', 'sender', 'receiver', 'signature']
    for field in required_fields:
        if field not in transaction:
            raise TransactionValidationError(f"Missing required field: {field}")

    # Validate coin type
    coin = transaction['coin']
    if coin not in SUPPORTED_COINS:
        raise TransactionValidationError(f"Unsupported coin type: {coin}")

    # Validate amount
    amount = transaction['amount']
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise TransactionValidationError("Invalid transaction amount. Must be a positive number.")

    # Validate sender and receiver addresses
    sender = transaction['sender']
    receiver = transaction['receiver']
    if not sender or not receiver or sender == receiver:
        raise TransactionValidationError("Invalid sender or receiver address.")

    # Validate signature
    signature = transaction['signature']
    if not validate_signature(transaction, signature):
        raise TransactionValidationError("Invalid transaction signature.")

    return True

def validate_signature(transaction: Dict[str, Union[str, float]], signature: str) -> bool:
    """
    Validates the HMAC signature of a transaction.

    Args:
        transaction (dict): The transaction data.
        signature (str): The HMAC signature to validate.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    # Create a copy of the transaction data excluding the signature
    transaction_data = {key: value for key, value in transaction.items() if key != 'signature'}

    # Serialize the transaction data to JSON
    serialized_data = json.dumps(transaction_data, sort_keys=True)

    # Generate the HMAC signature using the secret key
    generated_signature = hmac.new(SECRET_KEY, serialized_data.encode('utf-8'), hashlib.sha256).hexdigest()

    # Compare the generated signature with the provided signature
    return hmac.compare_digest(generated_signature, signature)

def process_transaction(transaction: Dict[str, Union[str, float]]) -> str:
    """
    Processes a transaction after validation.

    Args:
        transaction (dict): The transaction data.

    Returns:
        str: A message indicating the transaction status.
    """
    try:
        # Validate the transaction
        if validate_transaction(transaction):
            return f"Transaction for {transaction['amount']} {transaction['coin']} from {transaction['sender']} to {transaction['receiver']} is valid and processed successfully."
    except TransactionValidationError as e:
        return f"Transaction failed: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example transaction data
    example_transaction = {
        "coin": "BTC",
        "amount": 0.5,
        "sender": "sender_address",
        "receiver": "receiver_address",
        "signature": "example_signature"  # Replace with a valid signature
    }

    # Process the transaction
    result = process_transaction(example_transaction)
    print(result)
```
