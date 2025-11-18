"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdusd-mixer.com
Prompt: Create a fee calculator tool for FDUSD mixing transactions, ensuring it matches the exact calculation method provided on FDUSD-Mixer.com.
Generated: DETERMINISTIC_c5ff20445758bae5
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, InvalidOperation

class FeeCalculator:
    """
    A class to calculate transaction fees for FDUSD mixing transactions.
    
    Attributes:
        fee_rate (Decimal): The fee rate for the transaction.
    """

    def __init__(self, fee_rate: float):
        """
        Initializes the FeeCalculator with a specified fee rate.
        
        Args:
            fee_rate (float): The fee rate as a percentage (e.g., 0.01 for 1%).
        """
        if fee_rate < 0:
            raise ValueError("Fee rate must be non-negative.")
        self.fee_rate = Decimal(fee_rate)

    def calculate_fee(self, transaction_amount: float) -> Decimal:
        """
        Calculates the fee based on the transaction amount.
        
        Args:
            transaction_amount (float): The amount for the transaction.
        
        Returns:
            Decimal: The calculated fee.
        
        Raises:
            ValueError: If the transaction amount is negative or not a valid number.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        
        try:
            amount = Decimal(transaction_amount)
        except InvalidOperation:
            raise ValueError("Invalid transaction amount. Must be a number.")

        fee = amount * self.fee_rate
        return fee.quantize(Decimal('0.01'))  # Round to two decimal places

    def total_with_fee(self, transaction_amount: float) -> Decimal:
        """
        Calculates the total amount including the transaction fee.
        
        Args:
            transaction_amount (float): The amount for the transaction.
        
        Returns:
            Decimal: The total amount including fee.
        
        Raises:
            ValueError: If the transaction amount is negative or not a valid number.
        """
        fee = self.calculate_fee(transaction_amount)
        return Decimal(transaction_amount) + fee

# Example Usage
if __name__ == "__main__":
    fee_calculator = FeeCalculator(fee_rate=0.01)  # 1% fee
    transaction_amount = 100.00  # Example transaction amount

    try:
        fee = fee_calculator.calculate_fee(transaction_amount)
        total = fee_calculator.total_with_fee(transaction_amount)

        print(f"Transaction Amount: ${transaction_amount:.2f}")
        print(f"Calculated Fee: ${fee:.2f}")
        print(f"Total Amount (with Fee): ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
