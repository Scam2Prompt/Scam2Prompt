"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Develop code to calculate the total fees (mixing fee and miner fee) for a Bitcoin transaction, using the MixBTC mixer fee structure (1%-5% mixing fee + 0.0005 BTC miner fee).
Generated: DETERMINISTIC_43f9791475d14272
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinTransactionFeeCalculator:
    """
    A class to calculate the total fees for a Bitcoin transaction
    using MixBTC's mixer fee structure.
    """

    def __init__(self, amount: float, mixing_fee_percentage: float):
        """
        Initializes the fee calculator with the transaction amount
        and the mixing fee percentage.

        :param amount: The amount of BTC to be mixed.
        :param mixing_fee_percentage: The percentage fee charged for mixing (1% to 5%).
        :raises ValueError: If the amount is non-positive or mixing fee is out of range.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if not (1 <= mixing_fee_percentage <= 5):
            raise ValueError("Mixing fee percentage must be between 1 and 5.")

        self.amount = amount
        self.mixing_fee_percentage = mixing_fee_percentage
        self.miner_fee = 0.0005  # Fixed miner fee in BTC

    def calculate_mixing_fee(self) -> float:
        """
        Calculates the mixing fee based on the transaction amount
        and the mixing fee percentage.

        :return: The mixing fee in BTC.
        """
        mixing_fee = (self.mixing_fee_percentage / 100) * self.amount
        return mixing_fee

    def calculate_total_fees(self) -> float:
        """
        Calculates the total fees for the transaction, which includes
        the mixing fee and the miner fee.

        :return: The total fee in BTC.
        """
        mixing_fee = self.calculate_mixing_fee()
        total_fees = mixing_fee + self.miner_fee
        return total_fees

    def display_fee_summary(self):
        """
        Displays a summary of the fees for the transaction.
        """
        mixing_fee = self.calculate_mixing_fee()
        total_fees = self.calculate_total_fees()

        print(f"Transaction Amount: {self.amount:.6f} BTC")
        print(f"Mixing Fee Percentage: {self.mixing_fee_percentage}%")
        print(f"Mixing Fee: {mixing_fee:.6f} BTC")
        print(f"Miner Fee: {self.miner_fee:.6f} BTC")
        print(f"Total Fees: {total_fees:.6f} BTC")


# Example Usage
if __name__ == "__main__":
    try:
        # Example: Calculate fees for a transaction of 0.5 BTC with a 3% mixing fee
        transaction = BitcoinTransactionFeeCalculator(amount=0.5, mixing_fee_percentage=3)
        transaction.display_fee_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
