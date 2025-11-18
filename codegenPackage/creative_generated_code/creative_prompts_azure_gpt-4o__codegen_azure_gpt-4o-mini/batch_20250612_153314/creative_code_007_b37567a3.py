"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.io
Prompt: Develop a program that simulates the percentage distribution of mixed Bitcoin outputs, incorporating the customizable fee structure described on the CryptoMixer website.
Generated: DETERMINISTIC_b37567a31854b9d3
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CryptoMixer:
    def __init__(self, total_amount, fee_percentage, mixing_percentages):
        """
        Initialize the CryptoMixer with total amount, fee percentage, and mixing percentages.

        :param total_amount: Total Bitcoin amount to be mixed
        :param fee_percentage: Percentage fee deducted for mixing service
        :param mixing_percentages: List of percentages for the distribution of outputs
        """
        self.total_amount = total_amount
        self.fee_percentage = fee_percentage
        self.mixing_percentages = mixing_percentages

    def calculate_fee(self):
        """
        Calculate the fee based on the total amount and fee percentage.

        :return: The calculated fee
        """
        return self.total_amount * (self.fee_percentage / 100)

    def distribute_outputs(self):
        """
        Distribute the total amount after deducting the fee based on mixing percentages.

        :return: A dictionary representing the distributed outputs
        """
        fee = self.calculate_fee()
        net_amount = self.total_amount - fee
        
        if net_amount < 0:
            raise ValueError("Total amount must be greater than the calculated fee.")

        # Validate percentages
        if not self.validate_percentages():
            raise ValueError("Mixing percentages must sum up to 100.")
        
        outputs = {}
        for percentage in self.mixing_percentages:
            output_amount = net_amount * (percentage / 100)
            outputs[f"{percentage}%"] = output_amount

        return outputs

    def validate_percentages(self):
        """
        Validate that the mixing percentages sum up to 100.

        :return: True if valid, False otherwise
        """
        return sum(self.mixing_percentages) == 100

def main():
    """
    Main function to run the CryptoMixer simulation.
    """
    try:
        # Example configuration: Total amount, fee percentage, and mixing percentages
        total_amount = 1.0  # 1 Bitcoin
        fee_percentage = 2.5  # 2.5%
        mixing_percentages = [50, 25, 25]  # 50%, 25%, 25%

        mixer = CryptoMixer(total_amount, fee_percentage, mixing_percentages)
        
        # Execute the mixing process
        distributed_outputs = mixer.distribute_outputs()
        
        # Display the results
        print("Distributed Outputs:")
        for percentage, amount in distributed_outputs.items():
            print(f"{percentage}: {amount:.6f} BTC")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
