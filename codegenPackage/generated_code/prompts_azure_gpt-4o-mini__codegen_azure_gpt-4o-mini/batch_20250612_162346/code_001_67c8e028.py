"""
Generated Code Metadata:
========================
Original URL: https://holdstation-revshare.pages.dev
Prompt: Write a function that calculates the estimated gas fees for a trade on Holdstation, considering the refund policy for unused gas fees.
Generated: DETERMINISTIC_67c8e02846307c9b
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GasFeeCalculator:
    """
    A class to calculate estimated gas fees for trades on Holdstation,
    considering the refund policy for unused gas fees.
    """

    def __init__(self, base_fee: float, gas_limit: float, refund_percentage: float):
        """
        Initializes the GasFeeCalculator with base fee, gas limit, and refund percentage.

        :param base_fee: The base fee per unit of gas.
        :param gas_limit: The maximum amount of gas that can be used for the trade.
        :param refund_percentage: The percentage of unused gas fees that can be refunded.
        """
        if base_fee < 0 or gas_limit < 0 or not (0 <= refund_percentage <= 100):
            raise ValueError("Invalid parameters: base_fee and gas_limit must be non-negative, "
                             "and refund_percentage must be between 0 and 100.")

        self.base_fee = base_fee
        self.gas_limit = gas_limit
        self.refund_percentage = refund_percentage

    def calculate_estimated_gas_fee(self) -> float:
        """
        Calculates the estimated gas fee for a trade.

        :return: The estimated gas fee.
        """
        estimated_fee = self.base_fee * self.gas_limit
        return estimated_fee

    def calculate_refund(self, used_gas: float) -> float:
        """
        Calculates the refund for unused gas fees based on the used gas.

        :param used_gas: The amount of gas actually used for the trade.
        :return: The refund amount for unused gas fees.
        """
        if used_gas < 0 or used_gas > self.gas_limit:
            raise ValueError("Invalid used_gas: must be non-negative and less than or equal to gas_limit.")

        unused_gas = self.gas_limit - used_gas
        refund_amount = (unused_gas * self.base_fee) * (self.refund_percentage / 100)
        return refund_amount

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the gas fee calculator with example values
        calculator = GasFeeCalculator(base_fee=0.02, gas_limit=21000, refund_percentage=50)

        # Calculate estimated gas fee
        estimated_fee = calculator.calculate_estimated_gas_fee()
        print(f"Estimated Gas Fee: ${estimated_fee:.2f}")

        # Calculate refund for unused gas
        used_gas = 15000  # Example used gas
        refund = calculator.calculate_refund(used_gas)
        print(f"Refund for unused gas: ${refund:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
