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
"""
Program to calculate transaction fees on SaitaChain
Author: Expert Programmer
Description: This script calculates transaction fees based on SaitaChain's fixed fee structure 
             and provides details about block finality time.
Language: Python
"""

# Import necessary modules
import time

class SaitaChainTransactionFeeCalculator:
    """
    A class to represent the SaitaChain transaction fee calculator.
    """

    def __init__(self, fixed_fee: float = 0.0018, block_finality_time: int = 6):
        """
        Initialize the transaction fee calculator with fixed fee and finality time.

        :param fixed_fee: Fixed transaction fee in STC (default: 0.0018 STC)
        :param block_finality_time: Block finality time in seconds (default: 6 seconds)
        """
        self.fixed_fee = fixed_fee
        self.block_finality_time = block_finality_time
    
    def calculate_fee(self, num_transactions: int) -> float:
        """
        Calculate the total transaction fee based on the number of transactions.

        :param num_transactions: Number of transactions to be processed
        :return: Total transaction fee in STC
        """
        if num_transactions < 0:
            raise ValueError("Number of transactions cannot be negative.")
        return num_transactions * self.fixed_fee
    
    def get_block_finality_time(self) -> int:
        """
        Get the block finality time for transactions.

        :return: Block finality time in seconds
        """
        return self.block_finality_time

def main():
    """
    Main function to interact with the SaitaChainTransactionFeeCalculator.
    """
    # Instantiate the calculator
    calculator = SaitaChainTransactionFeeCalculator()

    print("Welcome to SaitaChain Transaction Fee Calculator!")
    
    try:
        # Prompt user for number of transactions
        num_transactions = int(input("Enter the number of transactions: "))
        
        # Calculate the transaction fees
        total_fee = calculator.calculate_fee(num_transactions)
        print(f"Total Transaction Fee: {total_fee:.4f} STC")

        # Display block finality time
        print(f"Block Finality Time: {calculator.get_block_finality_time()} seconds")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Measure execution time for the script
    start_time = time.time()
    
    main()
    
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} seconds")
```
