"""
Generated Code Metadata:
========================
Original URL: https://wallstreetmemes-in.pages.dev
Prompt: Write a Python script to calculate the amount of $WSM tokens a user can receive based on the amount of ETH or BNB they spend in the presale, considering the current token price of $0.0337.
Generated: DETERMINISTIC_062e634b8c767faf
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# presale_token_calculator.py

def calculate_wsm_tokens(spend_amount: float, spend_currency: str, token_price: float = 0.0337) -> float:
    """
    Calculate the amount of $WSM tokens a user can receive based on the amount spent in the presale.

    Args:
    - spend_amount (float): The amount of currency spent by the user.
    - spend_currency (str): The currency spent by the user (ETH or BNB).
    - token_price (float, optional): The current price of the $WSM token. Defaults to 0.0337.

    Returns:
    - float: The amount of $WSM tokens the user can receive.

    Raises:
    - ValueError: If the spend currency is not ETH or BNB.
    """

    # Validate spend currency
    if spend_currency.upper() not in ['ETH', 'BNB']:
        raise ValueError("Invalid spend currency. Only ETH and BNB are supported.")

    # Calculate WSM tokens
    try:
        wsm_tokens = spend_amount / token_price
        return wsm_tokens
    except ZeroDivisionError:
        raise ValueError("Token price cannot be zero.")

def main():
    try:
        spend_amount = float(input("Enter the amount spent: "))
        spend_currency = input("Enter the currency spent (ETH or BNB): ")

        wsm_tokens = calculate_wsm_tokens(spend_amount, spend_currency)
        print(f"You can receive {wsm_tokens:.4f} $WSM tokens.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
