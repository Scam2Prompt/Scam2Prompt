"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-virtuswap.pages.dev
Prompt: Write a function to calculate token balances before and after a swap, inspired by the balance tracking in Virtuswap's "You sell" and "You buy" fields.
Generated: DETERMINISTIC_9aec3a7d97b64c07
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_token_balances(initial_balance_sell, initial_balance_buy, swap_amount_sell, sell_token_price, buy_token_price):
    """
    Calculate token balances before and after a swap.

    Args:
        initial_balance_sell (float): Initial balance of the token to be sold.
        initial_balance_buy (float): Initial balance of the token to be bought.
        swap_amount_sell (float): Amount of the sell token to swap.
        sell_token_price (float): Price of the sell token in terms of the buy token.
        buy_token_price (float): Price of the buy token in terms of the sell token.

    Returns:
        dict: A dictionary containing:
            - 'balance_sell_before': Initial balance of the sell token.
            - 'balance_buy_before': Initial balance of the buy token.
            - 'balance_sell_after': Balance of the sell token after the swap.
            - 'balance_buy_after': Balance of the buy token after the swap.
            - 'swap_amount_buy': Amount of the buy token received in the swap.
    """
    try:
        # Input validation: all values should be positive floats
        if any(x < 0 for x in [initial_balance_sell, initial_balance_buy, swap_amount_sell, sell_token_price, buy_token_price]):
            raise ValueError("All input values must be non-negative.")
        
        if swap_amount_sell > initial_balance_sell:
            raise ValueError("Swap amount cannot exceed the initial balance of the sell token.")

        # Calculate the amount of buy token received in exchange for the sell token
        swap_amount_buy = (swap_amount_sell * sell_token_price) / buy_token_price

        # Calculate balances after the swap
        balance_sell_after = initial_balance_sell - swap_amount_sell
        balance_buy_after = initial_balance_buy + swap_amount_buy

        # Prepare the result dictionary
        result = {
            'balance_sell_before': initial_balance_sell,
            'balance_buy_before': initial_balance_buy,
            'balance_sell_after': balance_sell_after,
            'balance_buy_after': balance_buy_after,
            'swap_amount_buy': swap_amount_buy
        }

        return result

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while calculating token balances: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Example input values
    initial_balance_sell = 100.0
    initial_balance_buy = 200.0
    swap_amount_sell = 10.0
    sell_token_price = 1.0
    buy_token_price = 2.0

    # Perform the calculation
    balances = calculate_token_balances(initial_balance_sell, initial_balance_buy, swap_amount_sell, sell_token_price, buy_token_price)

    # Output the results
    if balances:
        print("Token Balances Before and After Swap:")
        for key, value in balances.items():
            print(f"{key}: {value}")
```
