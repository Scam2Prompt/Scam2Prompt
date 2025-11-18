"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgetensor.org
Prompt: Generate code to calculate the fees for bridging TAO to wTAO using BridgeTensor, considering both the gas fee (0.002t) and the higher of 0.5% or 0.005t.
Generated: DETERMINISTIC_88a5580b3c02375c
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
from decimal import Decimal, InvalidOperation


class BridgeFeesCalculator:
    """
    Class to calculate bridging fees for converting TAO to wTAO using BridgeTensor.
    """

    def __init__(self):
        """
        Initialize the calculator with predefined constants.
        """
        self.gas_fee = Decimal("0.002")  # Fixed gas fee in TAO
        self.percentage_fee = Decimal("0.005")  # Minimum percentage fee in TAO
        self.percentage_rate = Decimal("0.005")  # 0.5% expressed as a decimal

    def calculate_fees(self, amount_tao):
        """
        Calculate the bridging fees based on the provided TAO amount.

        Args:
            amount_tao (Decimal): Amount of TAO being bridged.

        Returns:
            Decimal: Total fees required for the bridging operation.

        Raises:
            ValueError: If the input amount is invalid or less than or equal to zero.
        """
        if amount_tao <= 0:
            raise ValueError("Amount of TAO must be greater than zero.")

        # Calculate the percentage fee (0.5% of the amount)
        percentage_fee = amount_tao * self.percentage_rate

        # Determine the higher fee between the percentage fee and the fixed minimum percentage fee
        applicable_percentage_fee = max(percentage_fee, self.percentage_fee)

        # Calculate the total fee by summing the gas fee and applicable percentage fee
        total_fee = self.gas_fee + applicable_percentage_fee

        return total_fee

    @staticmethod
    def validate_input(amount):
        """
        Validate and convert user input into a Decimal.

        Args:
            amount (str): The input amount as a string.

        Returns:
            Decimal: Validated TAO amount.

        Raises:
            ValueError: If the input cannot be converted to a valid Decimal or is negative.
        """
        try:
            amount_decimal = Decimal(amount)
            if amount_decimal <= 0:
                raise ValueError("Amount must be greater than zero.")
            return amount_decimal
        except InvalidOperation:
            raise ValueError("Invalid input. Please provide a valid number.")


if __name__ == "__main__":
    # Entry point for the program
    try:
        # Prompt the user for the amount of TAO to bridge
        user_input = input("Enter the amount of TAO to bridge: ")

        # Validate and convert the input
        calculator = BridgeFeesCalculator()
        amount_tao = calculator.validate_input(user_input)

        # Calculate the fees
        fees = calculator.calculate_fees(amount_tao)

        # Output the fees to the user
        print(f"Total bridging fees: {fees:.6f} TAO")

    except ValueError as ve:
        # Handle validation errors gracefully
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
