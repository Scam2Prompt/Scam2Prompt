"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcticpablotoken.world
Prompt: Create a function to calculate the total cost of Arctic Pablo tokens ($APC) based on the current price of $0.000026 per token and the amount entered by the user. Ensure compatibility with ETH, BNB, and SOL payment methods.
Generated: DETERMINISTIC_467a65679fc51631
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost(amount: float, token_price: float = 0.000026) -> dict:
    """
    Calculate the total cost of Arctic Pablo tokens ($APC) based on the amount requested.

    Args:
    - amount (float): The number of $APC tokens to purchase.
    - token_price (float, optional): The price per $APC token. Defaults to 0.000026.

    Returns:
    - dict: A dictionary containing the total cost in different cryptocurrencies.

    Raises:
    - ValueError: If the amount is negative or zero.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    # Calculate the total cost in USD
    total_cost_usd = amount * token_price

    # Assuming conversion rates (mocked values for ETH, BNB, and SOL)
    conversion_rates = {
        'ETH': 2000.00,  # Example conversion rate for 1 ETH to USD
        'BNB': 300.00,   # Example conversion rate for 1 BNB to USD
        'SOL': 20.00     # Example conversion rate for 1 SOL to USD
    }

    # Calculate the total cost in each cryptocurrency
    total_cost_crypto = {
        currency: total_cost_usd / rate for currency, rate in conversion_rates.items()
    }

    return total_cost_crypto

if __name__ == "__main__":
    try:
        # Example usage
        tokens_to_purchase = float(input("Enter the number of $APC tokens to purchase: "))
        total_cost = calculate_total_cost(tokens_to_purchase)
        print(f"Total cost for {tokens_to_purchase} $APC tokens:")
        for currency, cost in total_cost.items():
            print(f"{currency}: {cost:.6f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
