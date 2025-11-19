"""
Generated Code Metadata:
========================
Original URL: https://mixtum.me
Prompt: Write a program to calculate commission fees for Bitcoin mixing transactions, using the range of 4-5% mentioned on mixtum.me.
Generated: DETERMINISTIC_b011ecc48424c6ef
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Commission Fee Calculator for Bitcoin Mixing Transactions

Calculates the commission fee for Bitcoin mixing transactions based on a fixed range of 4-5%.
"""

def calculate_commission_fee(amount: float, fee_percentage: float = 4.5) -> float:
    """
    Calculates the commission fee for a Bitcoin mixing transaction.

    Args:
    - amount (float): The amount of the Bitcoin transaction.
    - fee_percentage (float): The commission fee percentage (default: 4.5%).

    Returns:
    - float: The calculated commission fee.

    Raises:
    - ValueError: If the transaction amount or fee percentage is invalid.
    """
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    if fee_percentage < 0 or fee_percentage > 100:
        raise ValueError("Fee percentage must be between 0 and 100.")

    commission_fee = (amount * fee_percentage) / 100
    return commission_fee


def calculate_transaction_amount_after_fee(amount: float, fee_percentage: float = 4.5) -> float:
    """
    Calculates the transaction amount after deducting the commission fee.

    Args:
    - amount (float): The amount of the Bitcoin transaction.
    - fee_percentage (float): The commission fee percentage (default: 4.5%).

    Returns:
    - float: The transaction amount after deducting the commission fee.

    Raises:
    - ValueError: If the transaction amount or fee percentage is invalid.
    """
    commission_fee = calculate_commission_fee(amount, fee_percentage)
    transaction_amount_after_fee = amount - commission_fee
    return transaction_amount_after_fee


def main():
    try:
        amount = float(input("Enter the Bitcoin transaction amount: "))
        fee_percentage = 4  # minimum fee
        print(f"Commission fee at {fee_percentage}%: {calculate_commission_fee(amount, fee_percentage):.8f} BTC")
        print(f"Transaction amount after fee at {fee_percentage}%: {calculate_transaction_amount_after_fee(amount, fee_percentage):.8f} BTC")

        fee_percentage = 5  # maximum fee
        print(f"\nCommission fee at {fee_percentage}%: {calculate_commission_fee(amount, fee_percentage):.8f} BTC")
        print(f"Transaction amount after fee at {fee_percentage}%: {calculate_transaction_amount_after_fee(amount, fee_percentage):.8f} BTC")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
