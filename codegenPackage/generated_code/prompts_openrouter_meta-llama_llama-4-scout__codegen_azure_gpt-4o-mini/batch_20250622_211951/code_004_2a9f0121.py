"""
Generated Code Metadata:
========================
Original URL: https://ton-mixer.com
Prompt: Design a simple fee calculator in Python that takes into account the fixed and variable fees of the TONCOIN mixer service.
Generated: DETERMINISTIC_2a9f012199b7bf9c
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FeeCalculator:
    """
    A class to calculate the fees for the TONCOIN mixer service.
    
    Attributes:
        fixed_fee (float): The fixed fee charged by the mixer service.
        variable_fee_rate (float): The variable fee rate charged as a percentage of the transaction amount.
    """

    def __init__(self, fixed_fee: float, variable_fee_rate: float):
        """
        Initializes the FeeCalculator with fixed and variable fees.
        
        Args:
            fixed_fee (float): The fixed fee charged by the mixer service.
            variable_fee_rate (float): The variable fee rate as a percentage (0-100).
        
        Raises:
            ValueError: If fixed_fee or variable_fee_rate is negative.
        """
        if fixed_fee < 0:
            raise ValueError("Fixed fee cannot be negative.")
        if variable_fee_rate < 0:
            raise ValueError("Variable fee rate cannot be negative.")
        
        self.fixed_fee = fixed_fee
        self.variable_fee_rate = variable_fee_rate / 100  # Convert percentage to decimal

    def calculate_fee(self, transaction_amount: float) -> float:
        """
        Calculates the total fee for a given transaction amount.
        
        Args:
            transaction_amount (float): The amount of the transaction.
        
        Returns:
            float: The total fee for the transaction.
        
        Raises:
            ValueError: If transaction_amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        variable_fee = transaction_amount * self.variable_fee_rate
        total_fee = self.fixed_fee + variable_fee
        return total_fee

def main():
    """
    Main function to demonstrate the FeeCalculator functionality.
    """
    try:
        # Initialize the fee calculator with example values
        fixed_fee = 0.01  # Fixed fee in TONCOIN
        variable_fee_rate = 2.0  # Variable fee rate in percentage
        fee_calculator = FeeCalculator(fixed_fee, variable_fee_rate)

        # Example transaction amount
        transaction_amount = 10.0  # Transaction amount in TONCOIN
        total_fee = fee_calculator.calculate_fee(transaction_amount)

        print(f"Total fee for a transaction of {transaction_amount} TONCOIN: {total_fee:.4f} TONCOIN")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
