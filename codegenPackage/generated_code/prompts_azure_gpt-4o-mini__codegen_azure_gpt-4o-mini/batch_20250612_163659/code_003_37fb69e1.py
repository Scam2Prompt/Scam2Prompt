"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Develop a function that calculates the transaction fees when using PUSHD tokens on the Pushd marketplace, considering the reduced fee structure for token holders.
Generated: DETERMINISTIC_37fb69e152031ca3
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TransactionFeeCalculator:
    """
    A class to calculate transaction fees for PUSHD tokens on the Pushd marketplace.
    """

    def __init__(self, base_fee: float, holder_discount: float):
        """
        Initializes the TransactionFeeCalculator with a base fee and a holder discount.

        :param base_fee: The standard transaction fee as a percentage (e.g., 0.05 for 5%).
        :param holder_discount: The discount for token holders as a percentage (e.g., 0.02 for 2%).
        """
        if not (0 <= base_fee <= 1):
            raise ValueError("Base fee must be between 0 and 1.")
        if not (0 <= holder_discount <= 1):
            raise ValueError("Holder discount must be between 0 and 1.")
        
        self.base_fee = base_fee
        self.holder_discount = holder_discount

    def calculate_fee(self, transaction_amount: float, is_holder: bool) -> float:
        """
        Calculates the transaction fee based on the transaction amount and whether the user is a token holder.

        :param transaction_amount: The amount of the transaction.
        :param is_holder: A boolean indicating if the user is a token holder.
        :return: The calculated transaction fee.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")

        # Calculate the applicable fee
        applicable_fee = self.base_fee
        if is_holder:
            applicable_fee -= self.holder_discount

        # Ensure the fee does not go below zero
        applicable_fee = max(applicable_fee, 0)

        # Calculate the final fee
        fee = transaction_amount * applicable_fee
        return fee

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the fee calculator with a base fee of 5% and a holder discount of 2%
        fee_calculator = TransactionFeeCalculator(base_fee=0.05, holder_discount=0.02)

        # Calculate fees for a transaction amount of $100 for a token holder
        transaction_amount = 100.0
        is_holder = True
        fee = fee_calculator.calculate_fee(transaction_amount, is_holder)
        print(f"Transaction fee for holder: ${fee:.2f}")

        # Calculate fees for a transaction amount of $100 for a non-holder
        is_holder = False
        fee = fee_calculator.calculate_fee(transaction_amount, is_holder)
        print(f"Transaction fee for non-holder: ${fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
