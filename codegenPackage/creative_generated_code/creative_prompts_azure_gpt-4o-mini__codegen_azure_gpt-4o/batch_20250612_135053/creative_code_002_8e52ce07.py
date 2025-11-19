"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Create a function that calculates the mixing fee based on a user-defined percentage (1% to 5%) and includes the miner fee for a Bitcoin mixer application.
Generated: DETERMINISTIC_8e52ce07a34c22d3
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mixing_fee(transaction_amount, user_defined_percentage, miner_fee):
    """
    Calculate the total mixing fee for a Bitcoin transaction.

    Args:
        transaction_amount (float): The amount of Bitcoin being transacted.
        user_defined_percentage (float): The user-defined mixing fee percentage (1% to 5%).
        miner_fee (float): The fixed miner fee in Bitcoin.

    Returns:
        float: The total fee (mixing fee + miner fee).
    
    Raises:
        ValueError: If user_defined_percentage is not within the allowed range of 1% to 5%.
        ValueError: If transaction_amount or miner_fee is negative.
    """
    # Validate inputs
    if not (1 <= user_defined_percentage <= 5):
        raise ValueError("User-defined percentage must be between 1% and 5%.")
    if transaction_amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
    if miner_fee < 0:
        raise ValueError("Miner fee cannot be negative.")

    # Calculate mixing fee based on user-defined percentage
    mixing_fee = (user_defined_percentage / 100) * transaction_amount

    # Calculate total fee
    total_fee = mixing_fee + miner_fee

    return total_fee


# Example usage:
if __name__ == "__main__":
    try:
        # Example values
        transaction_amount = 0.5  # 0.5 BTC
        user_defined_percentage = 3  # 3% mixing fee
        miner_fee = 0.0002  # 0.0002 BTC miner fee

        # Calculate the total mixing fee
        total_fee = calculate_mixing_fee(transaction_amount, user_defined_percentage, miner_fee)
        print(f"The total mixing fee is: {total_fee} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
