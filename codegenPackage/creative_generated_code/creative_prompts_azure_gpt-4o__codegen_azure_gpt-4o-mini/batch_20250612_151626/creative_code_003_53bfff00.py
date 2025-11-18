"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonmixers.com
Prompt: Create a script that calculates the service fee for mixing Toncoin, ranging between 0.5% and 1.986%, and applies it to a given transaction amount.
Generated: DETERMINISTIC_53bfff00e99a7181
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ToncoinServiceFeeCalculator:
    """A class to calculate the service fee for mixing Toncoin transactions."""

    def __init__(self, min_fee=0.005, max_fee=0.01986):
        """
        Initializes the fee calculator with given minimum and maximum fees.

        Args:
            min_fee (float): Minimum service fee as a decimal (0.5%).
            max_fee (float): Maximum service fee as a decimal (1.986%).
        """
        self.min_fee = min_fee
        self.max_fee = max_fee

    def calculate_fee(self, amount):
        """
        Calculates the service fee for a given transaction amount.

        Args:
            amount (float): The transaction amount for which to calculate the fee.

        Returns:
            float: The calculated service fee.

        Raises:
            ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Randomly select a fee percentage within the defined range
        fee_percentage = random.uniform(self.min_fee, self.max_fee)
        
        # Calculate the service fee
        fee = amount * fee_percentage
        return fee

def main():
    """Main function to execute the service fee calculation."""
    try:
        transaction_amount = float(input("Enter the transaction amount in Toncoin: "))
        
        calculator = ToncoinServiceFeeCalculator()
        service_fee = calculator.calculate_fee(transaction_amount)

        print(f"The calculated service fee is: {service_fee:.6f} Toncoin")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
