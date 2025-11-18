"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb-mixer.eth.limo
Prompt: Develop a script to calculate the mixing fees for BNB transactions based on the fee structure provided by BNB Mixer.
Generated: DETERMINISTIC_69f82ac71a13e621
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mixing_fee(transaction_amount):
    """
    Calculate the mixing fees for a given BNB transaction amount based on BNB Mixer's fee structure.
    
    Fee Structure:
    - Flat fee of 0.01 BNB for all transactions
    - Additional percentage fee based on the transaction amount:
        - 1% for amounts <= 1 BNB
        - 0.8% for amounts > 1 BNB and <= 10 BNB
        - 0.5% for amounts > 10 BNB
    
    Args:
        transaction_amount (float): The amount of BNB being transacted

    Returns:
        float: The total mixing fee
    """
    # Validate input
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than 0")

    # Flat fee
    flat_fee = 0.01

    # Calculate percentage fee based on transaction amount
    if transaction_amount <= 1:
        percentage_fee = transaction_amount * 0.01
    elif transaction_amount <= 10:
        percentage_fee = transaction_amount * 0.008
    else:
        percentage_fee = transaction_amount * 0.005

    # Total fee
    total_fee = flat_fee + percentage_fee
    return total_fee


def main():
    """
    Main function to prompt user for transaction amount and calculate mixing fees.
    """
    try:
        # Prompt user for transaction amount
        transaction_amount = float(input("Enter the BNB transaction amount: "))

        # Calculate mixing fee
        mixing_fee = calculate_mixing_fee(transaction_amount)

        # Display the result
        print(f"Total Mixing Fee: {mixing_fee:.6f} BNB")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
