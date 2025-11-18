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
class BridgingCalculator:
    """
    A class to calculate the fees for bridging TAO to wTAO using the BridgeTensor platform.
    """

    GAS_FEE = 0.002  # Fixed gas fee in TAO
    MIN_PERCENTAGE_FEE = 0.005  # Minimum fee in TAO
    PERCENTAGE_FEE_RATE = 0.005  # 0.5% as a decimal

    def __init__(self, amount_tao):
        """
        Initialize the calculator with the amount of TAO to be bridged.

        :param amount_tao: The amount of TAO to bridge.
        """
        if amount_tao <= 0:
            raise ValueError("Amount of TAO must be greater than 0.")
        self.amount_tao = amount_tao

    def calculate_fees(self):
        """
        Calculate the total bridging fees based on the amount of TAO.

        :return: A dictionary containing the gas fee and the calculated percentage fee.
        """
        # Calculate the percentage fee (0.5% of the amount)
        percentage_fee = self.amount_tao * self.PERCENTAGE_FEE_RATE
        
        # Determine the higher fee between the minimum and the percentage fee
        effective_percentage_fee = max(percentage_fee, self.MIN_PERCENTAGE_FEE)

        # Calculate total fees
        total_fees = self.GAS_FEE + effective_percentage_fee

        return {
            "gas_fee": self.GAS_FEE,
            "percentage_fee": effective_percentage_fee,
            "total_fees": total_fees
        }


def main():
    """
    The main function to run the fee calculation.
    """
    try:
        # Example amount of TAO to bridge
        amount_to_bridge = 10.0  # Example value, can be modified
        
        # Create a BridgingCalculator instance
        calculator = BridgingCalculator(amount_to_bridge)
        
        # Calculate the fees
        fees = calculator.calculate_fees()
        
        # Output the calculated fees
        print(f"Bridging fees for {amount_to_bridge} TAO:")
        print(f"Gas Fee: {fees['gas_fee']} TAO")
        print(f"Percentage Fee: {fees['percentage_fee']} TAO")
        print(f"Total Fees: {fees['total_fees']} TAO")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
