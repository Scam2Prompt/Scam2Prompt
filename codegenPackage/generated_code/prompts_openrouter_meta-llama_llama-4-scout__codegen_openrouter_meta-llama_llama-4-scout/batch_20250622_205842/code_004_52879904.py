"""
Generated Code Metadata:
========================
Original URL: https://supertrumpcoin-io.pages.dev
Prompt: Write a script to calculate the tax on transactions for a cryptocurrency token with a 0.3% tax rate and 0.8% going to a specific wallet.
Generated: DETERMINISTIC_5287990422e9fdce
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_calculator.py

def calculate_tax(transaction_amount: float, tax_rate: float = 0.003, wallet_rate: float = 0.008) -> dict:
    """
    Calculates the tax on a transaction for a cryptocurrency token.

    Args:
    - transaction_amount (float): The amount of the transaction.
    - tax_rate (float, optional): The tax rate. Defaults to 0.3% (0.003).
    - wallet_rate (float, optional): The rate going to a specific wallet. Defaults to 0.8% (0.008).

    Returns:
    - dict: A dictionary containing the tax amount and wallet amount.
    """

    # Validate input
    if transaction_amount < 0:
        raise ValueError("Transaction amount cannot be negative")

    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1")

    if wallet_rate < 0 or wallet_rate > 1:
        raise ValueError("Wallet rate must be between 0 and 1")

    # Calculate tax amount
    tax_amount = transaction_amount * tax_rate

    # Calculate wallet amount
    wallet_amount = transaction_amount * wallet_rate

    # Return results as a dictionary
    return {
        "tax_amount": tax_amount,
        "wallet_amount": wallet_amount,
        "transaction_amount": transaction_amount - tax_amount - wallet_amount
    }


def main():
    try:
        # Example usage
        transaction_amount = 1000.0
        result = calculate_tax(transaction_amount)
        print(f"Transaction Amount: {result['transaction_amount']}")
        print(f"Tax Amount: {result['tax_amount']}")
        print(f"Wallet Amount: {result['wallet_amount']}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
