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
import re

def validate_wallet_transaction(transaction):
    """
    Validates a wallet transaction based on predefined rules.

    Args:
        transaction (dict): A dictionary containing transaction details. Example:
                            {
                                "wallet_id": "abc123",
                                "amount": 100.50,
                                "currency": "USD",
                                "transaction_type": "debit",
                                "timestamp": "2023-10-01T12:30:00Z"
                            }

    Returns:
        bool: True if the transaction is valid, False otherwise.
    """
    
    try:
        # Check if the transaction is a dictionary
        if not isinstance(transaction, dict):
            raise ValueError("Transaction must be a dictionary.")

        # Validate wallet_id: Must be alphanumeric and between 6-30 characters
        wallet_id = transaction.get("wallet_id")
        if not wallet_id or not re.match(r"^[a-zA-Z0-9]{6,30}$", wallet_id):
            raise ValueError("Invalid wallet_id. It must be alphanumeric and 6-30 characters long.")

        # Validate amount: Must be a positive number
        amount = transaction.get("amount")
        if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount. It must be a positive number.")

        # Validate currency: Must be a valid ISO 4217 currency code (3 uppercase letters)
        currency = transaction.get("currency")
        if not currency or not re.match(r"^[A-Z]{3}$", currency):
            raise ValueError("Invalid currency. It must be a valid ISO 4217 code (e.g., USD).")

        # Validate transaction_type: Must be 'debit' or 'credit'
        transaction_type = transaction.get("transaction_type")
        if transaction_type not in {"debit", "credit"}:
            raise ValueError("Invalid transaction type. It must be 'debit' or 'credit'.")

        # Validate timestamp: Must be in ISO 8601 format
        timestamp = transaction.get("timestamp")
        if not timestamp or not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", timestamp):
            raise ValueError("Invalid timestamp. It must be in ISO 8601 format (e.g., 2023-10-01T12:30:00Z).")

        # If all validations pass, return True
        return True

    except ValueError as e:
        # Log the error (In production, use a logging framework instead of print)
        print(f"Transaction validation error: {e}")
        return False
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error during validation: {e}")
        return False

# Example usage:
transaction_example = {
    "wallet_id": "abc123",
    "amount": 150.75,
    "currency": "USD",
    "transaction_type": "debit",
    "timestamp": "2023-10-01T12:30:00Z"
}

# Validate the transaction
print(validate_wallet_transaction(transaction_example))  # Output: True
```
