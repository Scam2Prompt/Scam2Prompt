"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write Python code to calculate cryptocurrency transaction fees on Coinbase, factoring in a 1.49% card payment fee and a 0.5% spread for a given transaction amount.
Generated: DETERMINISTIC_8acc64e7d99e828f
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Coinbase Transaction Fee Calculator

Calculates the total fees for a cryptocurrency transaction on Coinbase,
including a 1.49% card payment fee and a 0.5% spread.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_transaction_fees(transaction_amount: float) -> dict:
    """
    Calculates the total fees for a cryptocurrency transaction on Coinbase.

    Args:
        transaction_amount (float): The amount of the transaction.

    Returns:
        dict: A dictionary containing the transaction amount, card payment fee, spread, and total fee.
    """

    # Check for non-positive transaction amount
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Define the card payment fee and spread rates
    CARD_PAYMENT_FEE_RATE = 0.0149  # 1.49%
    SPREAD_RATE = 0.005  # 0.5%

    # Calculate the card payment fee
    card_payment_fee = transaction_amount * CARD_PAYMENT_FEE_RATE

    # Calculate the spread
    spread = transaction_amount * SPREAD_RATE

    # Calculate the total fee
    total_fee = card_payment_fee + spread

    # Calculate the total amount paid by the user
    total_amount_paid = transaction_amount + total_fee

    # Return the fees as a dictionary
    return {
        "transaction_amount": transaction_amount,
        "card_payment_fee": card_payment_fee,
        "spread": spread,
        "total_fee": total_fee,
        "total_amount_paid": total_amount_paid,
    }


def main():
    try:
        # Example usage
        transaction_amount = 100.0
        fees = calculate_transaction_fees(transaction_amount)

        print("Transaction Fees:")
        print(f"  Transaction Amount: ${fees['transaction_amount']:.2f}")
        print(f"  Card Payment Fee: ${fees['card_payment_fee']:.2f}")
        print(f"  Spread: ${fees['spread']:.2f}")
        print(f"  Total Fee: ${fees['total_fee']:.2f}")
        print(f"  Total Amount Paid: ${fees['total_amount_paid']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
