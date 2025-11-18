"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Develop code to calculate the total fees (mixing fee and miner fee) for a Bitcoin transaction, using the MixBTC mixer fee structure (1%-5% mixing fee + 0.0005 BTC miner fee).
Generated: DETERMINISTIC_43f9791475d14272
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Bitcoin Transaction Fee Calculator (MixBTC Fee Structure)

def calculate_bitcoin_transaction_fee(transaction_amount: float, mixing_fee_percentage: float) -> float:
    """
    Calculate the total fees for a Bitcoin transaction using MixBTC mixer fee structure.

    Parameters:
        transaction_amount (float): The amount (in BTC) being transacted.
        mixing_fee_percentage (float): Mixing fee percentage (1% to 5%).

    Returns:
        float: Total fees for the transaction (mixing fee + miner fee).
    """
    # Validate inputs
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than 0.")
    if not (1 <= mixing_fee_percentage <= 5):
        raise ValueError("Mixing fee percentage must be between 1% and 5%.")

    # Constants
    MINER_FEE = 0.0005  # Fixed miner fee in BTC

    # Calculate mixing fee
    mixing_fee = (mixing_fee_percentage / 100) * transaction_amount

    # Calculate total fee
    total_fee = mixing_fee + MINER_FEE

    return total_fee


def main():
    """
    Main function to demonstrate the Bitcoin transaction fee calculator.
    """
    try:
        # Example input
        transaction_amount = float(input("Enter the transaction amount in BTC: "))
        mixing_fee_percentage = float(input("Enter the mixing fee percentage (1-5): "))

        # Calculate total fees
        total_fees = calculate_bitcoin_transaction_fee(transaction_amount, mixing_fee_percentage)

        # Output the result
        print(f"Total fees for the transaction: {total_fees:.8f} BTC")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
