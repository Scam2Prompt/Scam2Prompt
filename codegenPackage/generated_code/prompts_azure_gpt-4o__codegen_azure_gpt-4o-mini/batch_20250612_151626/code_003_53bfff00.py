"""
Generated Code Metadata:
========================
Original URL: https://tonmixers.com
Prompt: Create a script that calculates the service fee for mixing Toncoin, ranging between 0.5% and 1.986%, and applies it to a given transaction amount.
Generated: DETERMINISTIC_53bfff00e99a7181
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ToncoinServiceFeeCalculator:
    """
    A class to calculate the service fee for mixing Toncoin.
    The service fee is a percentage that ranges between 0.5% and 1.986%.
    """

    def __init__(self, min_fee=0.005, max_fee=0.01986):
        """
        Initializes the service fee calculator with the given fee range.

        :param min_fee: Minimum service fee as a decimal (default is 0.5%)
        :param max_fee: Maximum service fee as a decimal (default is 1.986%)
        """
        self.min_fee = min_fee
        self.max_fee = max_fee

    def calculate_fee(self, transaction_amount):
        """
        Calculates the service fee based on a random percentage within the defined range.

        :param transaction_amount: The amount of the transaction (must be a positive number)
        :return: The calculated service fee
        :raises ValueError: If the transaction amount is not a positive number
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")

        # Generate a random service fee percentage within the defined range
        fee_percentage = random.uniform(self.min_fee, self.max_fee)
        
        # Calculate the service fee
        service_fee = transaction_amount * fee_percentage
        
        return service_fee, fee_percentage * 100  # Return fee and percentage in percentage form

def main():
    """
    Main function to execute the service fee calculation.
    """
    try:
        # Example transaction amount
        transaction_amount = float(input("Enter the transaction amount in Toncoin: "))
        
        # Create an instance of the service fee calculator
        fee_calculator = ToncoinServiceFeeCalculator()
        
        # Calculate the service fee
        service_fee, fee_percentage = fee_calculator.calculate_fee(transaction_amount)
        
        # Display the results
        print(f"Service Fee: {service_fee:.6f} Toncoin (at {fee_percentage:.3f}%)")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
