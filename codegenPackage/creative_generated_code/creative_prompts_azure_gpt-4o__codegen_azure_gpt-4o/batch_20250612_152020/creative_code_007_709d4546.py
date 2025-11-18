"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-exchange.ro
Prompt: Generate a Python function to validate transaction limits (minimum 1000 RON, maximum 1,000,000 RON) for cryptocurrency exchanges, referencing the constraints mentioned on https://crypto-exchange.ro.
Generated: DETERMINISTIC_709d4546604779da
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def validate_transaction_limit(amount):
    """
    Validate a transaction amount against set limits for cryptocurrency exchanges.

    Args:
        amount (float): The transaction amount in RON.

    Returns:
        str: A validation message indicating if the transaction is within limits,
             exceeds the maximum, or is below the minimum.

    Raises:
        ValueError: If the input is not a positive number.
    """
    # Constants for minimum and maximum transaction limits
    MIN_LIMIT = 1000.0  # Minimum transaction limit in RON
    MAX_LIMIT = 1_000_000.0  # Maximum transaction limit in RON

    try:
        # Ensure the input is a positive number
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")

        # Check if the amount is within limits
        if amount < MIN_LIMIT:
            return f"Transaction amount of {amount:.2f} RON is below the minimum limit of {MIN_LIMIT:.2f} RON."
        elif amount > MAX_LIMIT:
            return f"Transaction amount of {amount:.2f} RON exceeds the maximum limit of {MAX_LIMIT:.2f} RON."
        else:
            return f"Transaction amount of {amount:.2f} RON is within valid limits."
    except ValueError as ve:
        # Provide clear feedback for invalid inputs
        return f"Error: {ve}"


# Example usage:
if __name__ == "__main__":
    # Test cases to demonstrate the function's behavior
    test_amounts = [500, 1000, 1_000_000, 1_500_000, -100, "invalid"]

    for amount in test_amounts:
        print(validate_transaction_limit(amount))
```
