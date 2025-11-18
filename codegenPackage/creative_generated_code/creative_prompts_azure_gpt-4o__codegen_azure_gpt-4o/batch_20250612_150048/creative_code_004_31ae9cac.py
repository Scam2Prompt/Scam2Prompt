"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdltl0.top
Prompt: Suggest a method to implement a fee calculation system for USDT transfers, referencing the "Fee" and "You will receive" details from the "Transfer Connect Token USDT0" documentation.
Generated: DETERMINISTIC_31ae9cac9d7d465c
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class FeeCalculationError(Exception):
    """Custom exception for fee calculation errors."""
    pass

class USDTTransferFeeCalculator:
    def __init__(self, fee_percentage: float):
        """
        Initialize the fee calculator with a given fee percentage.
        :param fee_percentage: The percentage fee applied to the transfer.
        """
        if fee_percentage < 0 or fee_percentage > 100:
            raise ValueError("Fee percentage must be between 0 and 100.")
        self.fee_percentage = fee_percentage

    def calculate_fee(self, transfer_amount: decimal.Decimal) -> decimal.Decimal:
        """
        Calculate the fee for a given transfer amount.
        :param transfer_amount: The amount being transferred.
        :return: The fee associated with the transfer.
        """
        if transfer_amount <= 0:
            raise FeeCalculationError("Transfer amount must be greater than zero.")
        fee = (transfer_amount * decimal.Decimal(self.fee_percentage)) / 100
        return fee.quantize(decimal.Decimal("0.01"))  # Round to 2 decimal places

    def calculate_receivable_amount(self, transfer_amount: decimal.Decimal) -> decimal.Decimal:
        """
        Calculate the amount the recipient will receive after the fee deduction.
        :param transfer_amount: The amount being transferred.
        :return: The amount the recipient will receive.
        """
        fee = self.calculate_fee(transfer_amount)
        receivable_amount = transfer_amount - fee
        if receivable_amount < 0:
            raise FeeCalculationError("Receivable amount cannot be negative.")
        return receivable_amount.quantize(decimal.Decimal("0.01"))  # Round to 2 decimal places


# Example Usage
if __name__ == "__main__":
    try:
        # Configure the fee percentage (e.g., 1% fee)
        fee_percentage = 1.0  # 1% fee
        calculator = USDTTransferFeeCalculator(fee_percentage)

        # Example transfer amount
        transfer_amount = decimal.Decimal("100.00")  # $100 USD

        # Calculate the fee and receivable amount
        fee = calculator.calculate_fee(transfer_amount)
        receivable_amount = calculator.calculate_receivable_amount(transfer_amount)

        print(f"Transfer Amount: ${transfer_amount}")
        print(f"Fee ({fee_percentage}%): ${fee}")
        print(f"You will receive: ${receivable_amount}")

    except (FeeCalculationError, ValueError) as e:
        print(f"Error: {e}")
```

This code implements a fee calculation system for USDT transfers, adhering to best practices, with proper error handling and documentation.
