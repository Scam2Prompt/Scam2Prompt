"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-polis.com
Prompt: Create a function to calculate transaction fees for Bitcoin exchanges, using parameters similar to those described on Crypto-Polis.
Generated: DETERMINISTIC_66a86a725d7a8e52
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionFeeCalculator:
    """
    A class to calculate transaction fees for Bitcoin exchanges based on a given set of parameters.
    """

    def __init__(self, base_fee: float, percentage_fee: float):
        """
        Initializes the TransactionFeeCalculator with a base fee and a percentage fee.

        :param base_fee: A flat fee charged for the transaction (in BTC).
        :param percentage_fee: A percentage fee charged on the total transaction amount (as a decimal).
        """
        if base_fee < 0:
            raise ValueError("Base fee cannot be negative.")
        if not (0 <= percentage_fee <= 1):
            raise ValueError("Percentage fee must be between 0 and 1.")

        self.base_fee = base_fee
        self.percentage_fee = percentage_fee

    def calculate_fee(self, transaction_amount: float) -> float:
        """
        Calculates the total transaction fee based on the transaction amount.

        :param transaction_amount: The total amount of the transaction (in BTC).
        :return: The total transaction fee (in BTC).
        :raises ValueError: If the transaction amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")

        # Calculate the percentage fee based on the transaction amount
        percentage_fee_amount = transaction_amount * self.percentage_fee
        
        # Total fee is the sum of the base fee and the calculated percentage fee
        total_fee = self.base_fee + percentage_fee_amount
        
        return total_fee

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the fee calculator with a base fee of 0.0005 BTC and a 0.2% fee
        fee_calculator = TransactionFeeCalculator(base_fee=0.0005, percentage_fee=0.002)

        # Calculate the transaction fee for a transaction amount of 0.05 BTC
        transaction_amount = 0.05
        fee = fee_calculator.calculate_fee(transaction_amount)

        print(f"The transaction fee for {transaction_amount} BTC is: {fee:.8f} BTC")
    except ValueError as e:
        print(f"Error: {e}")
```
