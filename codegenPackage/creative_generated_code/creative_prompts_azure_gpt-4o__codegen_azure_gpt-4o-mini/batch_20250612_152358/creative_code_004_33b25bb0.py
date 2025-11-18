"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xodus3.net
Prompt: Write code to calculate the total transaction cost for bridging assets using the Xodus3 platform, including fees and destination address validation.
Generated: DETERMINISTIC_33b25bb082de3288
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class BridgeTransaction:
    def __init__(self, amount: float, fee_percentage: float, destination_address: str):
        """
        Initializes the BridgeTransaction with the necessary parameters.

        :param amount: The amount of assets to bridge.
        :param fee_percentage: The percentage fee applied to the transaction.
        :param destination_address: The destination address to send the assets.
        """
        self.amount = amount
        self.fee_percentage = fee_percentage
        self.destination_address = destination_address

        # Validate the destination address format
        self.validate_destination_address()

    def validate_destination_address(self):
        """
        Validates the destination address format.
        
        Raises:
            TransactionError: If the destination address format is invalid.
        """
        # Example regex for a generic address format
        address_pattern = r'^[a-zA-Z0-9]{26,35}$'
        if not re.match(address_pattern, self.destination_address):
            raise TransactionError("Invalid destination address format.")

    def calculate_fee(self) -> float:
        """
        Calculates the transaction fee based on the amount and fee percentage.

        :return: The calculated fee.
        """
        return self.amount * (self.fee_percentage / 100)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total transaction cost including the fee.

        :return: The total transaction cost.
        """
        fee = self.calculate_fee()
        total_cost = self.amount + fee
        return total_cost

def main():
    """
    Main function to execute the transaction calculation.
    """
    try:
        # Example values for the transaction
        amount = 1000.0  # Amount to bridge
        fee_percentage = 2.5  # Fee as a percentage
        destination_address = "1ABCD2EFGHIJKLMNOPQRSTUVWXYZ"  # Example address

        # Create a BridgeTransaction instance
        transaction = BridgeTransaction(amount, fee_percentage, destination_address)

        # Calculate total transaction cost
        total_cost = transaction.calculate_total_cost()
        print(f"Total transaction cost: ${total_cost:.2f}")

    except TransactionError as e:
        print(f"Transaction error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
