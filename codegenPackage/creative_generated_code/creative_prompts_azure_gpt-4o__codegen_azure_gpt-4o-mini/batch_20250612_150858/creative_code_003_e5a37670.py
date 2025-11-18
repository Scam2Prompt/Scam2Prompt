"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-tumbler.to
Prompt: Develop a Python program that calculates the random commission (0.5% to 1%) charged by the ETH Tumbler service for a given Ether transaction amount.
Generated: DETERMINISTIC_e5a37670b3b230c2
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class EtherTumbler:
    """
    A class to represent an Ether Tumbler service which calculates random commission 
    for transaction amounts.
    """

    def __init__(self, min_commission_rate=0.005, max_commission_rate=0.01):
        """
        Initializes the EtherTumbler with commission rate boundaries.
        
        Args:
            min_commission_rate (float): Minimum commission rate (default is 0.5%).
            max_commission_rate (float): Maximum commission rate (default is 1%).
        """
        self.min_commission_rate = min_commission_rate
        self.max_commission_rate = max_commission_rate

    def calculate_commission(self, transaction_amount):
        """
        Calculates the commission for a given transaction amount.
        
        Args:
            transaction_amount (float): The amount of Ether for the transaction.
        
        Returns:
            float: The calculated commission.
        
        Raises:
            ValueError: If the transaction amount is non-positive.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Randomly select a commission rate within the specified range
        commission_rate = random.uniform(self.min_commission_rate, self.max_commission_rate)
        
        # Calculate the commission based on the transaction amount
        commission = transaction_amount * commission_rate
        
        return commission

def main():
    """
    Main function to execute the Ether Tumbler commission calculation.
    """
    try:
        # Example transaction amount; in production, this could be user input or another source
        transaction_amount = float(input("Enter the Ether transaction amount: "))

        tumbler = EtherTumbler()
        commission = tumbler.calculate_commission(transaction_amount)

        print(f"The commission charged by the ETH Tumbler service for the transaction is: {commission:.10f} ETH")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
