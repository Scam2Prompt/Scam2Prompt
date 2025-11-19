"""
Generated Code Metadata:
========================
Original URL: https://ethereumixer.to
Prompt: Generate code to calculate the random commission (0.5% to 1%) charged by an Ethereum mixer for a given transaction amount.
Generated: DETERMINISTIC_26b359feb693a29c
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def calculate_commission(transaction_amount: float) -> float:
    """
    Calculate a random commission for an Ethereum mixer based on the transaction amount.

    The commission is a random percentage between 0.5% and 1% of the transaction amount.

    Args:
        transaction_amount (float): The amount of the transaction in Ethereum.

    Returns:
        float: The calculated commission amount.

    Raises:
        ValueError: If the transaction amount is negative or zero.
    """
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    # Generate a random commission percentage between 0.5% and 1%
    commission_percentage = random.uniform(0.005, 0.01)

    # Calculate the commission amount
    commission_amount = transaction_amount * commission_percentage

    return commission_amount

def main():
    try:
        # Example transaction amount in Ethereum
        transaction_amount = 1.0  # Replace with the desired transaction amount

        # Calculate the commission
        commission = calculate_commission(transaction_amount)

        # Output the result
        print(f"Transaction Amount: {transaction_amount} ETH")
        print(f"Commission Charged: {commission:.6f} ETH")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
