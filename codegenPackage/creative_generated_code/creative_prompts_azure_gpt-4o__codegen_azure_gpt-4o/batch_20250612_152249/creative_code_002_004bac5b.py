"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Create a Python script that calculates the number of $MBAG tokens a user can purchase based on the current presale price (e.g., 1 $USDT = 3,333.33 $MBAG) and their selected payment method.
Generated: DETERMINISTIC_004bac5bddc62421
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_tokens(payment_amount, payment_currency, presale_price):
    """
    Calculate the number of tokens ($MBAG) a user can purchase.

    Args:
        payment_amount (float): The amount of payment in the selected currency (e.g., $USDT).
        payment_currency (str): The currency the user is paying with (e.g., "USDT").
        presale_price (float): The current presale price (e.g., 1 USDT = 3333.33 MBAG).

    Returns:
        float: The amount of $MBAG tokens the user can purchase.
    """
    try:
        # Ensure the payment amount is positive
        if payment_amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        # Calculate the number of tokens
        tokens = payment_amount * presale_price
        return tokens
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def main():
    """
    Main execution function for the script.
    """
    try:
        # Presale price example: 1 $USDT = 3333.33 $MBAG
        presale_price = 3333.33  # The conversion rate

        # User inputs
        payment_amount = float(input("Enter the payment amount (e.g., 10): "))
        payment_currency = input("Enter the payment currency (e.g., USDT): ").upper()

        if payment_currency != "USDT":
            raise ValueError("Currently, only USDT is accepted as a payment method.")

        # Calculate tokens
        tokens = calculate_tokens(payment_amount, payment_currency, presale_price)
        
        # Output the result
        print(f"You can purchase {tokens:.2f} $MBAG tokens with {payment_amount} {payment_currency}.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
