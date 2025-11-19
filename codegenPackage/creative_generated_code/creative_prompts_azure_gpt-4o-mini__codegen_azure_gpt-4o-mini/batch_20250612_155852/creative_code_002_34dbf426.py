"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgetensor.org
Prompt: Create a function that calculates the fees for bridging TAO to wTAO using the fee structure provided by BridgeTensor, ensuring it accounts for both the gas fee and the percentage fee.
Generated: DETERMINISTIC_34dbf426408e4ff7
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BridgingFeeCalculator:
    """
    A class to calculate the fees for bridging TAO to wTAO 
    based on the fee structure provided by BridgeTensor.
    """

    def __init__(self, gas_fee: float, percentage_fee: float):
        """
        Initializes the fee calculator with given gas and percentage fees.

        :param gas_fee: The fixed gas fee for the bridging process.
        :param percentage_fee: The percentage fee applied to the amount being bridged.
        """
        self.gas_fee = gas_fee
        self.percentage_fee = percentage_fee

    def calculate_fees(self, amount: float) -> float:
        """
        Calculates the total fees for bridging an amount of TAO to wTAO.

        :param amount: The amount of TAO being bridged.
        :return: The total fees incurred for the bridging process.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate the percentage fee based on the amount
        percentage_fee_amount = (self.percentage_fee / 100) * amount
        
        # Total fees is the sum of gas fee and percentage fee
        total_fees = self.gas_fee + percentage_fee_amount
        
        return total_fees

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with example gas fee and percentage fee
        fee_calculator = BridgingFeeCalculator(gas_fee=0.5, percentage_fee=2.0)
        
        # Amount to bridge
        amount_to_bridge = 100.0
        
        # Calculate fees
        total_fees = fee_calculator.calculate_fees(amount_to_bridge)
        print(f"Total fees for bridging {amount_to_bridge} TAO to wTAO: {total_fees:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
