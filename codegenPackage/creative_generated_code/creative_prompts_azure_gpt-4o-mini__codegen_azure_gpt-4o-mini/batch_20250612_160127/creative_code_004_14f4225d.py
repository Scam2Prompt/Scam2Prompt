"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micmarktrade.com
Prompt: Create a function that calculates trading fees based on the competitive pricing structure outlined by MIC markets.
Generated: DETERMINISTIC_14f4225dd8eebdd4
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingFeeCalculator:
    """
    A class to calculate trading fees based on the competitive pricing structure
    outlined by MIC markets.
    """

    def __init__(self, base_fee: float = 0.001, min_fee: float = 1.0):
        """
        Initialize the TradingFeeCalculator with a base fee and minimum fee.

        :param base_fee: The percentage fee charged on the transaction amount (default is 0.001 or 0.1%)
        :param min_fee: The minimum fee charged per transaction (default is 1.0)
        """
        if base_fee < 0 or min_fee < 0:
            raise ValueError("Fees must be non-negative.")
        self.base_fee = base_fee
        self.min_fee = min_fee

    def calculate_fee(self, transaction_amount: float) -> float:
        """
        Calculate the trading fee for a given transaction amount.

        :param transaction_amount: The total amount of the transaction
        :return: The calculated trading fee
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Calculate the raw fee based on the base fee percentage
        fee = transaction_amount * self.base_fee
        
        # The fee should not be less than the minimum fee
        return max(fee, self.min_fee)

# Example usage
if __name__ == "__main__":
    try:
        calculator = TradingFeeCalculator(base_fee=0.001, min_fee=1.0)
        transaction_amount = 5000  # Example transaction amount
        trading_fee = calculator.calculate_fee(transaction_amount)
        
        print(f"The trading fee for a transaction amount of {transaction_amount} is: {trading_fee}")
    except ValueError as e:
        print(f"Error: {e}")
```
