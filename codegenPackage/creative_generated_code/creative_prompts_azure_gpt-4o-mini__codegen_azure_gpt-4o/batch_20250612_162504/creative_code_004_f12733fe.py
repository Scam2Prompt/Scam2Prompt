"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-sale1.vercel.app
Prompt: Generate a function that calculates the total cost in SOL for purchasing a specified amount of BeyBlade (BBD) tokens at the current price of 0.0500 SOL each.
Generated: DETERMINISTIC_f12733fea6cc849f
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost_in_sol(token_price: float, token_amount: int) -> float:
    """
    Calculate the total cost in SOL for purchasing a specified amount of BeyBlade (BBD) tokens.

    Parameters:
        token_price (float): The price of one BBD token in SOL.
        token_amount (int): The number of BBD tokens to purchase.

    Returns:
        float: The total cost in SOL for the specified number of tokens.
    """
    # Validate inputs
    if token_price <= 0:
        raise ValueError("Token price must be a positive number.")
    if token_amount < 0:
        raise ValueError("Token amount must be a non-negative integer.")

    # Calculate total cost
    total_cost = token_price * token_amount
    return total_cost


def main():
    """
    Main function to demonstrate the calculation of total cost in SOL for BBD tokens.
    """
    try:
        # Define constant price per token
        BBD_TOKEN_PRICE = 0.0500  # Price of 1 BBD token in SOL

        # Example token amount to purchase
        token_amount = 100  # Change this value to test different amounts

        # Calculate and display the total cost
        total_cost = calculate_total_cost_in_sol(BBD_TOKEN_PRICE, token_amount)
        print(f"The total cost for purchasing {token_amount} BBD tokens is {total_cost:.4f} SOL.")

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
