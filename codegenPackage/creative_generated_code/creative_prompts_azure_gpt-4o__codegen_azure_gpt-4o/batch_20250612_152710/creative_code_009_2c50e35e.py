"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realio-bridge.web.app
Prompt: Create a script to calculate transaction and asset tokenization fees on the Realio Network using $RIO tokens.
Generated: DETERMINISTIC_2c50e35eeaf90d24
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_fees(transaction_amount, asset_value, transaction_fee_rate, tokenization_fee_rate):
    """
    Calculate transaction and asset tokenization fees on the Realio Network.

    Parameters:
        transaction_amount (float): The amount of the transaction in USD.
        asset_value (float): The value of the asset being tokenized in USD.
        transaction_fee_rate (float): The transaction fee rate (percentage) as a decimal. Example: 0.01 for 1%.
        tokenization_fee_rate (float): The tokenization fee rate (percentage) as a decimal. Example: 0.02 for 2%.

    Returns:
        dict: A dictionary containing transaction fee, tokenization fee, and total fees, all in $RIO tokens.
    """
    try:
        # Ensure inputs are valid numbers
        if not (transaction_amount > 0 and asset_value > 0 and transaction_fee_rate >= 0 and tokenization_fee_rate >= 0):
            raise ValueError("Invalid input values. All values must be positive numbers.")

        # Calculate individual fees
        transaction_fee = transaction_amount * transaction_fee_rate
        tokenization_fee = asset_value * tokenization_fee_rate

        # Calculate total fees
        total_fee = transaction_fee + tokenization_fee

        # Return fees as dictionary
        return {
            "transaction_fee_RIO": transaction_fee,
            "tokenization_fee_RIO": tokenization_fee,
            "total_fee_RIO": total_fee
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example user inputs
    try:
        transaction_amount = float(input("Enter the transaction amount in USD: "))
        asset_value = float(input("Enter the asset value in USD: "))
        transaction_fee_rate = float(input("Enter the transaction fee rate (as a decimal, e.g., 0.01 for 1%): "))
        tokenization_fee_rate = float(input("Enter the tokenization fee rate (as a decimal, e.g., 0.02 for 2%): "))

        # Calculate fees
        fees = calculate_fees(transaction_amount, asset_value, transaction_fee_rate, tokenization_fee_rate)

        # Print results
        print("\nFee Calculation Results:")
        print(f"Transaction Fee in $RIO: {fees['transaction_fee_RIO']:.2f}")
        print(f"Tokenization Fee in $RIO: {fees['tokenization_fee_RIO']:.2f}")
        print(f"Total Fee in $RIO: {fees['total_fee_RIO']:.2f}")

    except ValueError:
        print("Please enter valid numeric inputs.")
        sys.exit(1)
```
