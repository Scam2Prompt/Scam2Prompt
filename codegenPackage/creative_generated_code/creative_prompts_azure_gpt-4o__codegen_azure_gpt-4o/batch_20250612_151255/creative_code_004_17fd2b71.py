"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachains.pages.dev
Prompt: Write a script to calculate transaction fees in SaitaChain's native token (STC) for a given number of transactions, considering its 0.0018 STC fee per transaction.
Generated: DETERMINISTIC_17fd2b71a7f02b31
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# transaction_fee_calculator.py

"""
This script calculates the total transaction fees in SaitaChain's native token (STC)
based on the number of transactions provided by the user.
The fee per transaction is fixed at 0.0018 STC.

Usage:
    Run the script and input the number of transactions when prompted.
"""

# Constants
FEE_PER_TRANSACTION = 0.0018  # Fee per transaction in STC

def calculate_transaction_fee(num_transactions):
    """
    Calculate the total transaction fee.

    Args:
        num_transactions (int): The number of transactions.

    Returns:
        float: Total transaction fee in STC.
    """
    return num_transactions * FEE_PER_TRANSACTION

def main():
    """
    Main function to interact with the user and calculate transaction fees.
    """
    try:
        # Prompt user for the number of transactions
        user_input = input("Enter the total number of transactions: ")

        # Validate and convert user input to an integer
        num_transactions = int(user_input)
        if num_transactions < 0:
            raise ValueError("Number of transactions cannot be negative.")

        # Calculate the total transaction fee
        total_fee = calculate_transaction_fee(num_transactions)

        # Display the result
        print(f"Total transaction fee for {num_transactions} transactions: {total_fee:.6f} STC")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
