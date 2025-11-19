"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: Develop a script to calculate transaction fees in Bitcoin, ensuring the prevention of errors like the 8.18 BTC fee mentioned on Bitcoinzat.com.
Generated: DETERMINISTIC_6379f07735bc0cd4
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal

# Set the precision for decimal calculations
decimal.getcontext().prec = 8

class TransactionFeeCalculator:
    def __init__(self, transaction_amount: float, fee_percentage: float):
        """
        Initializes the TransactionFeeCalculator with the transaction amount and fee percentage.

        :param transaction_amount: The amount of Bitcoin being transacted.
        :param fee_percentage: The percentage fee to be applied to the transaction.
        """
        self.transaction_amount = decimal.Decimal(transaction_amount)
        self.fee_percentage = decimal.Decimal(fee_percentage) / decimal.Decimal(100)

    def calculate_fee(self) -> decimal.Decimal:
        """
        Calculates the transaction fee based on the transaction amount and fee percentage.

        :return: The calculated transaction fee in Bitcoin.
        """
        if self.transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        if self.fee_percentage < 0:
            raise ValueError("Fee percentage must be non-negative.")

        fee = self.transaction_amount * self.fee_percentage
        return fee.quantize(decimal.Decimal('0.00000001'))  # Round to 8 decimal places

    def total_amount_with_fee(self) -> decimal.Decimal:
        """
        Calculates the total amount including the transaction fee.

        :return: The total amount in Bitcoin including the fee.
        """
        fee = self.calculate_fee()
        total_amount = self.transaction_amount + fee
        return total_amount.quantize(decimal.Decimal('0.00000001'))  # Round to 8 decimal places

def main():
    try:
        # Example transaction amount and fee percentage
        transaction_amount = 1.0  # 1 BTC
        fee_percentage = 0.5      # 0.5%

        # Create a TransactionFeeCalculator instance
        calculator = TransactionFeeCalculator(transaction_amount, fee_percentage)

        # Calculate the fee and total amount
        fee = calculator.calculate_fee()
        total_amount = calculator.total_amount_with_fee()

        # Output the results
        print(f"Transaction Amount: {transaction_amount} BTC")
        print(f"Transaction Fee: {fee} BTC")
        print(f"Total Amount (including fee): {total_amount} BTC")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
