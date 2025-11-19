"""
Generated Code Metadata:
========================
Original URL: https://ton-mixer.com
Prompt: Design a simple fee calculator in Python that takes into account the fixed and variable fees of the TONCOIN mixer service.
Generated: DETERMINISTIC_2a9f012199b7bf9c
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ToncoinFeeCalculator:
    """
    A simple fee calculator for the TONCOIN mixer service.

    Attributes:
        fixed_fee (float): The fixed fee for the TONCOIN mixer service.
        variable_fee_percentage (float): The variable fee percentage for the TONCOIN mixer service.
    """

    def __init__(self, fixed_fee: float, variable_fee_percentage: float):
        """
        Initializes the ToncoinFeeCalculator with the fixed and variable fees.

        Args:
            fixed_fee (float): The fixed fee for the TONCOIN mixer service.
            variable_fee_percentage (float): The variable fee percentage for the TONCOIN mixer service.

        Raises:
            ValueError: If the fixed fee or variable fee percentage is negative.
        """
        if fixed_fee < 0:
            raise ValueError("Fixed fee cannot be negative")
        if variable_fee_percentage < 0:
            raise ValueError("Variable fee percentage cannot be negative")

        self.fixed_fee = fixed_fee
        self.variable_fee_percentage = variable_fee_percentage

    def calculate_fee(self, amount: float) -> float:
        """
        Calculates the total fee for a given amount.

        Args:
            amount (float): The amount to calculate the fee for.

        Returns:
            float: The total fee.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        variable_fee = (amount * self.variable_fee_percentage) / 100
        total_fee = self.fixed_fee + variable_fee
        return total_fee

    def calculate_output_amount(self, amount: float) -> float:
        """
        Calculates the output amount after deducting the fee.

        Args:
            amount (float): The amount to calculate the output for.

        Returns:
            float: The output amount.

        Raises:
            ValueError: If the amount is negative.
        """
        fee = self.calculate_fee(amount)
        if amount < fee:
            raise ValueError("Insufficient amount to cover the fee")

        output_amount = amount - fee
        return output_amount


def main():
    try:
        # Example usage
        calculator = ToncoinFeeCalculator(fixed_fee=1.0, variable_fee_percentage=0.5)
        amount = 100.0
        fee = calculator.calculate_fee(amount)
        output_amount = calculator.calculate_output_amount(amount)

        print(f"Fee: {fee:.2f}")
        print(f"Output Amount: {output_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
