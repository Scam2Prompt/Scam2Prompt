"""
Generated Code Metadata:
========================
Original URL: https://bridgetensor.org
Prompt: Generate code to calculate the fees for bridging TAO to wTAO using BridgeTensor, considering both the gas fee (0.002t) and the higher of 0.5% or 0.005t.
Generated: DETERMINISTIC_88a5580b3c02375c
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BridgeFeeCalculator:
    """
    A class to calculate the fees for bridging TAO to wTAO using BridgeTensor.
    """

    def __init__(self, amount_tao):
        """
        Initializes the BridgeFeeCalculator with the amount of TAO to bridge.

        :param amount_tao: The amount of TAO to be bridged.
        """
        if amount_tao <= 0:
            raise ValueError("Amount of TAO must be greater than zero.")
        self.amount_tao = amount_tao
        self.gas_fee = 0.002  # Fixed gas fee in t
        self.percentage_fee_rate = 0.005  # 0.5% fee rate
        self.minimum_percentage_fee = 0.005  # Minimum fee in t

    def calculate_fees(self):
        """
        Calculates the total fees for bridging TAO to wTAO.

        :return: The total fees in t.
        """
        # Calculate the percentage fee based on the amount of TAO
        percentage_fee = self.amount_tao * self.percentage_fee_rate
        
        # Determine the higher fee between the percentage fee and the minimum fee
        higher_fee = max(percentage_fee, self.minimum_percentage_fee)

        # Calculate the total fees including gas fee
        total_fees = higher_fee + self.gas_fee

        return total_fees

    def display_fees(self):
        """
        Displays the calculated fees for bridging TAO to wTAO.
        """
        try:
            total_fees = self.calculate_fees()
            print(f"Total fees for bridging {self.amount_tao} TAO to wTAO: {total_fees:.6f} t")
        except Exception as e:
            print(f"An error occurred while calculating fees: {e}")


# Example usage
if __name__ == "__main__":
    try:
        amount_to_bridge = float(input("Enter the amount of TAO to bridge: "))
        fee_calculator = BridgeFeeCalculator(amount_to_bridge)
        fee_calculator.display_fees()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
