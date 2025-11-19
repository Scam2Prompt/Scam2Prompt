"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-celer.network
Prompt: Create a function that calculates transaction fees using CELR tokens within the Celer Network ecosystem.
Generated: DETERMINISTIC_9f7dba108f977aab
Batch ID: 20250612_155607
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
    A class to calculate transaction fees using CELR tokens within the Celer Network ecosystem.
    """

    def __init__(self, base_fee: float, fee_rate: float):
        """
        Initializes the TransactionFeeCalculator with a base fee and fee rate.
        
        :param base_fee: The fixed base fee for each transaction in CELR tokens.
        :param fee_rate: The variable fee rate per unit of transaction value in CELR tokens.
        """
        if base_fee < 0 or fee_rate < 0:
            raise ValueError("Base fee and fee rate must be non-negative values.")
        
        self.base_fee = base_fee
        self.fee_rate = fee_rate

    def calculate_fee(self, transaction_value: float) -> float:
        """
        Calculates the transaction fee based on the transaction value.
        
        :param transaction_value: The value of the transaction in CELR tokens.
        
        :return: The total transaction fee in CELR tokens.
        :raises ValueError: If the transaction value is negative.
        """
        if transaction_value < 0:
            raise ValueError("Transaction value must be a non-negative value.")
        
        # Calculate the variable fee
        variable_fee = transaction_value * self.fee_rate
        
        # Total fee is the sum of base fee and variable fee
        total_fee = self.base_fee + variable_fee
        
        return total_fee

# Example usage:
if __name__ == "__main__":
    # Initialize the transaction fee calculator with a base fee of 0.01 CELR and a fee rate of 0.001
    fee_calculator = TransactionFeeCalculator(base_fee=0.01, fee_rate=0.001)

    try:
        # Calculate the fee for a transaction value of 100 CELR
        transaction_value = 100.0
        fee = fee_calculator.calculate_fee(transaction_value)
        print(f"The transaction fee for {transaction_value} CELR is: {fee:.4f} CELR")
    except ValueError as e:
        print(f"Error calculating fee: {e}")
```
