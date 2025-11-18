"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Write a program to calculate transaction fees on SaitaChain, considering its fixed fee of 0.0018 STC and block finality time of 6 seconds.
Generated: DETERMINISTIC_f603352fc6839775
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class SaitaChainTransaction:
    """
    A class to represent a SaitaChain transaction and calculate fees.
    """

    FIXED_FEE = 0.0018  # Fixed transaction fee in STC
    FINALITY_TIME = 6   # Block finality time in seconds

    def __init__(self, amount: float):
        """
        Initialize the transaction with a specified amount.
        
        Args:
            amount (float): The amount for the transaction.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        self.amount = amount
        self.transaction_fee = self.calculate_fee()

    def calculate_fee(self) -> float:
        """
        Calculate transaction fees.
        
        Returns:
            float: The transaction fee in STC.
        """
        return self.FIXED_FEE

    def process_transaction(self) -> str:
        """
        Simulate processing the transaction.
        
        Returns:
            str: A message indicating the transaction status.
        """
        time.sleep(self.FINALITY_TIME)  # Simulate block finality time
        return f"Transaction of {self.amount} STC processed with a fee of {self.transaction_fee} STC."

def main():
    """
    Main function to execute the transaction processing.
    """
    try:
        amount = float(input("Enter the transaction amount in STC: "))
        transaction = SaitaChainTransaction(amount)
        result = transaction.process_transaction()
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
