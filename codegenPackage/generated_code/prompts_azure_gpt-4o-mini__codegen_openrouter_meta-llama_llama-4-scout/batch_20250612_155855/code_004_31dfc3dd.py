"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Provide an example of how to calculate the number of BULLDOGITO tokens received based on a given value in a swap transaction.
Generated: DETERMINISTIC_31dfc3dd02539ca0
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bulldogito_tokens(
    swap_transaction_value: float, 
    bulldogito_token_price: float, 
    swap_fee_percentage: float = 0.003  # 0.3% swap fee
) -> float:
    """
    Calculates the number of BULLDOGITO tokens received based on a given value in a swap transaction.

    Args:
    - swap_transaction_value (float): The value of the swap transaction.
    - bulldogito_token_price (float): The current price of one BULLDOGITO token.
    - swap_fee_percentage (float, optional): The percentage of swap fee. Defaults to 0.003 (0.3%).

    Returns:
    - float: The number of BULLDOGITO tokens received.

    Raises:
    - ValueError: If any of the input values are negative.
    - ZeroDivisionError: If the BULLDOGITO token price is zero.
    """

    # Validate input values
    if swap_transaction_value < 0:
        raise ValueError("Swap transaction value cannot be negative.")
    if bulldogito_token_price <= 0:
        raise ValueError("BULLDOGITO token price must be greater than zero.")
    if swap_fee_percentage < 0:
        raise ValueError("Swap fee percentage cannot be negative.")

    try:
        # Calculate the swap fee
        swap_fee = swap_transaction_value * swap_fee_percentage

        # Calculate the value after swap fee
        value_after_fee = swap_transaction_value - swap_fee

        # Calculate the number of BULLDOGITO tokens received
        bulldogito_tokens_received = value_after_fee / bulldogito_token_price

        return bulldogito_tokens_received

    except Exception as e:
        # Log and re-raise any unexpected exceptions
        print(f"An error occurred: {str(e)}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        swap_transaction_value = 1000.0
        bulldogito_token_price = 10.0

        tokens_received = calculate_bulldogito_tokens(swap_transaction_value, bulldogito_token_price)
        print(f"Number of BULLDOGITO tokens received: {tokens_received:.4f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
