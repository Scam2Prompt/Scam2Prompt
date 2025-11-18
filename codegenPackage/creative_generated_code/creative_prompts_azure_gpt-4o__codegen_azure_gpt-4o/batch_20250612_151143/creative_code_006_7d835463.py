"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magahat-3gz.pages.dev
Prompt: Write code to validate mint transactions for MAGA•THE•DONALD•TRUMP inscriptions, ensuring that invalid mints are excluded and valid mints fall within the median fee range of 20 sat/vB.
Generated: DETERMINISTIC_7d835463963a200b
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def validate_mint_transactions(transactions):
    """
    Validates mint transactions for MAGA•THE•DONALD•TRUMP inscriptions.
    
    A transaction is considered valid if:
    1. The inscription matches "MAGA•THE•DONALD•TRUMP".
    2. The transaction fee falls within the median fee range of 20 sat/vB.
    
    Args:
        transactions (list of dict): List of transaction details. Each transaction should
                                     have 'inscription', 'fee', and 'size' fields.
    
    Returns:
        list of dict: List of valid transactions.
    """

    # Define the target inscription and median fee per vByte
    TARGET_INSCRIPTION = "MAGA•THE•DONALD•TRUMP"
    MEDIAN_FEE_VB = 20  # sat/vByte

    # Filter transactions with the correct inscription
    inscription_filtered = [
        tx for tx in transactions if tx.get("inscription") == TARGET_INSCRIPTION
    ]

    # Extract fees per vByte for valid inscriptions
    fees_per_vbyte = []
    for tx in inscription_filtered:
        try:
            # Calculate fee per vByte
            fee = tx["fee"]
            size = tx["size"]
            if size <= 0:  # Ensure size is valid
                raise ValueError("Transaction size must be greater than zero.")
            fees_per_vbyte.append(fee / size)
        except (KeyError, ValueError) as e:
            # Skip transactions with invalid data
            print(f"Skipping invalid transaction: {tx} | Error: {e}")

    # Compute the median fee
    if len(fees_per_vbyte) == 0:
        print("No valid transactions found.")
        return []

    median_fee = statistics.median(fees_per_vbyte)

    # Determine valid fee range based on median fee
    valid_fee_lower = median_fee - MEDIAN_FEE_VB
    valid_fee_upper = median_fee + MEDIAN_FEE_VB

    # Filter transactions within the valid fee range
    valid_transactions = [
        tx
        for tx in inscription_filtered
        if valid_fee_lower <= tx["fee"] / tx["size"] <= valid_fee_upper
    ]

    return valid_transactions


# Example usage
if __name__ == "__main__":
    # Sample transactions data
    transactions = [
        {"inscription": "MAGA•THE•DONALD•TRUMP", "fee": 2000, "size": 100},  # Valid
        {"inscription": "MAGA•THE•DONALD•TRUMP", "fee": 500, "size": 50},    # Valid
        {"inscription": "Invalid", "fee": 3000, "size": 150},               # Invalid inscription
        {"inscription": "MAGA•THE•DONALD•TRUMP", "fee": 10000, "size": 100},# Out of fee range
        {"inscription": "MAGA•THE•DONALD•TRUMP", "fee": 100, "size": -1},   # Invalid size
    ]

    # Validate transactions
    valid_transactions = validate_mint_transactions(transactions)

    # Print valid transactions
    print("Valid Transactions:")
    for tx in valid_transactions:
        print(tx)
```
