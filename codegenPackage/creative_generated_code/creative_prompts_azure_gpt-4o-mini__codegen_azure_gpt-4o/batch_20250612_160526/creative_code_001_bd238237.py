"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elcriptomonedas.com
Prompt: Can you provide a code snippet for calculating transaction fees when trading on exchanges like Binance or Kraken as mentioned on ElCriptomonedas?
Generated: DETERMINISTIC_bd238237732d29ca
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_transaction_fee(transaction_amount: float, fee_percentage: float) -> float:
    """
    Calculates the transaction fee based on the transaction amount and fee percentage.

    :param transaction_amount: The amount of the transaction (in base currency, e.g., USD or BTC).
    :param fee_percentage: The fee percentage charged by the exchange (e.g., 0.1% for Binance).
    :return: The calculated transaction fee.
    """
    try:
        # Ensure inputs are valid numbers
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if fee_percentage < 0:
            raise ValueError("Fee percentage cannot be negative.")

        # Use Decimal for precision in financial calculations
        transaction_amount_decimal = decimal.Decimal(str(transaction_amount))
        fee_percentage_decimal = decimal.Decimal(str(fee_percentage)) / decimal.Decimal("100")

        # Calculate the fee
        fee = transaction_amount_decimal * fee_percentage_decimal
        return float(fee)
    except (ValueError, decimal.InvalidOperation) as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    try:
        # Example values for a transaction on Binance
        transaction_amount = 1000.0  # e.g., $1000 USD
        fee_percentage = 0.1  # e.g., 0.1% transaction fee

        # Calculate the transaction fee
        fee = calculate_transaction_fee(transaction_amount, fee_percentage)
        print(f"Transaction Fee: ${fee:.2f}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
