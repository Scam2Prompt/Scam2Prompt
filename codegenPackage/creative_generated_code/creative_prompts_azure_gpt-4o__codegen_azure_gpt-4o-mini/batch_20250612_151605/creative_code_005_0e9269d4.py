"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-mixer-mix.com
Prompt: Develop a Python program that calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee, as outlined on the USDT Mixer website.
Generated: DETERMINISTIC_0e9269d4cd633ed9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionFeeCalculator:
    """
    A class to calculate the service fee for USDT transactions based on
    the number of Coinjoins and the initiation fee.
    """

    def __init__(self, initiation_fee: float, coinjoin_fee: float):
        """
        Initializes the TransactionFeeCalculator with the given fees.

        :param initiation_fee: The initial fee charged for initiating a transaction.
        :param coinjoin_fee: The fee charged per Coinjoin.
        """
        if initiation_fee < 0 or coinjoin_fee < 0:
            raise ValueError("Fees must be non-negative.")
        
        self.initiation_fee = initiation_fee
        self.coinjoin_fee = coinjoin_fee

    def calculate_total_fee(self, num_coinjoins: int) -> float:
        """
        Calculates the total service fee based on the number of Coinjoins.

        :param num_coinjoins: The number of Coinjoins for the transaction.
        :return: The total service fee.
        :raises ValueError: If the number of Coinjoins is negative.
        """
        if num_coinjoins < 0:
            raise ValueError("Number of Coinjoins must be non-negative.")

        # Total fee is the sum of the initiation fee and the variable fees for Coinjoins
        total_fee = self.initiation_fee + (self.coinjoin_fee * num_coinjoins)
        return total_fee


def main():
    """
    The main function to execute the fee calculation logic.
    """
    try:
        # Initialize the service fee calculator with example fees
        initiation_fee = float(input("Enter the initiation fee: "))
        coinjoin_fee = float(input("Enter the Coinjoin fee per transaction: "))
        
        fee_calculator = TransactionFeeCalculator(initiation_fee, coinjoin_fee)

        # Get the number of Coinjoins from user input
        num_coinjoins = int(input("Enter the number of Coinjoins: "))

        # Calculate and display the total fee
        total_fee = fee_calculator.calculate_total_fee(num_coinjoins)
        print(f"The total service fee for {num_coinjoins} Coinjoins is: ${total_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
