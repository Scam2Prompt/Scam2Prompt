"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-mixer.com
Prompt: Develop a program in Python that calculates the random commission (1%-5%) applied by a TRON mixer service and adjusts the final transaction amount accordingly.
Generated: DETERMINISTIC_cbfe01e9c7378aa7
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_final_transaction_amount(original_amount):
    """
    Calculate the final transaction amount after applying a random commission.

    Parameters:
        original_amount (float): The original transaction amount in TRX (TRON cryptocurrency).

    Returns:
        dict: A dictionary containing commission percentage, commission amount, 
              and the final transaction amount.
    """
    if original_amount <= 0:
        raise ValueError("Original amount must be greater than 0.")

    # Generate a random commission percentage between 1% and 5%
    commission_percentage = random.uniform(1, 5)

    # Calculate the commission amount
    commission_amount = (commission_percentage / 100) * original_amount

    # Calculate the final transaction amount after deducting the commission
    final_amount = original_amount - commission_amount

    return {
        "commission_percentage": round(commission_percentage, 2),
        "commission_amount": round(commission_amount, 6),
        "final_transaction_amount": round(final_amount, 6)
    }

def main():
    """
    Main function to handle user input and calculate the transaction details.
    """
    try:
        # Accept the original transaction amount from the user
        original_amount = float(input("Enter the original transaction amount (in TRX): "))

        # Calculate the adjusted transaction details
        transaction_details = calculate_final_transaction_amount(original_amount)

        # Display the results
        print("\nTransaction Details:")
        print(f"Original Amount: {original_amount:.6f} TRX")
        print(f"Commission Percentage: {transaction_details['commission_percentage']}%")
        print(f"Commission Amount: {transaction_details['commission_amount']} TRX")
        print(f"Final Transaction Amount: {transaction_details['final_transaction_amount']} TRX")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
