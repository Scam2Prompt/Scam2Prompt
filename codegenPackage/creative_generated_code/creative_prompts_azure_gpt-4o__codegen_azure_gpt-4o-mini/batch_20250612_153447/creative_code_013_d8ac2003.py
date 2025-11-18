"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Provide code to calculate transaction fees on a Layer 2 blockchain, ensuring they are substantially lower than Ethereum Layer 1 fees, as highlighted in Pepe Unchained.
Generated: DETERMINISTIC_d8ac20031f527316
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class Layer2TransactionFeeCalculator:
    """
    A class to calculate transaction fees on a Layer 2 blockchain.
    The fees are expected to be significantly lower than Ethereum Layer 1 fees.

    Attributes:
        base_fee (decimal.Decimal): The base fee for transactions.
        fee_multiplier (decimal.Decimal): A multiplier to adjust fees based on transaction complexity.
    """

    def __init__(self, base_fee: float, fee_multiplier: float = 1.0):
        """
        Initializes the fee calculator with a base fee and an optional fee multiplier.

        Args:
            base_fee (float): The base transaction fee for Layer 2.
            fee_multiplier (float): A multiplier to adjust fees for complex transactions.
        """
        self.base_fee = decimal.Decimal(base_fee)
        self.fee_multiplier = decimal.Decimal(fee_multiplier)

    def calculate_fee(self, transaction_complexity: float) -> decimal.Decimal:
        """
        Calculates the transaction fee based on the complexity of the transaction.

        Args:
            transaction_complexity (float): A value representing the complexity of the transaction.

        Returns:
            decimal.Decimal: The calculated transaction fee.
        """
        if transaction_complexity < 0:
            raise ValueError("Transaction complexity cannot be negative.")

        # Calculate the fee based on complexity
        complexity_factor = decimal.Decimal(transaction_complexity)
        total_fee = self.base_fee * (self.fee_multiplier + complexity_factor)

        return total_fee.quantize(decimal.Decimal('0.0001'))  # Round to 4 decimal places

def main():
    """
    Main function to run the transaction fee calculation.
    """

    try:
        # Example base fee for Layer 2 transactions, significantly lower than Ethereum Layer 1 fees
        base_fee = 0.001  # Example fee in ETH

        # Create a fee calculator instance
        fee_calculator = Layer2TransactionFeeCalculator(base_fee)

        # Example transaction complexities
        complexities = [0.0, 0.5, 1.0, 2.0]  # Different transaction complexities

        # Calculate and display fees for each complexity
        for complexity in complexities:
            fee = fee_calculator.calculate_fee(complexity)
            print(f"Transaction Complexity: {complexity}, Transaction Fee: {fee} ETH")

    except ValueError as e:
        print(f"Error calculating transaction fee: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
