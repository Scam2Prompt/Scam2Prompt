"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchases-blocksdags.pages.dev
Prompt: Write a code snippet to calculate the total amount of BDAG coins I can purchase with a given amount of ETH or BNB.
Generated: DETERMINISTIC_189ac6845895dadc
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required module
from typing import Union

# Define the function to calculate the total BDAG coins
def calculate_bdag_coins(amount: float, coin_type: str, eth_price: float, bnb_price: float, bdag_rate: float) -> float:
    """
    Calculate the total BDAG coins that can be purchased with a given amount of ETH or BNB.

    Args:
        amount (float): The amount of ETH or BNB the user wants to spend.
        coin_type (str): The type of cryptocurrency ('ETH' or 'BNB').
        eth_price (float): Current market price of 1 ETH in USD.
        bnb_price (float): Current market price of 1 BNB in USD.
        bdag_rate (float): Current rate of BDAG coins per 1 USD.

    Returns:
        float: The total BDAG coins that can be purchased.
    """
    # Validate input parameters
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    if coin_type not in ['ETH', 'BNB']:
        raise ValueError("Invalid coin type. Use 'ETH' or 'BNB'.")
    if eth_price <= 0 or bnb_price <= 0 or bdag_rate <= 0:
        raise ValueError("Prices and rate must be greater than 0.")

    # Calculate BDAG coins based on the coin type
    if coin_type == 'ETH':
        usd_equivalent = amount * eth_price
    elif coin_type == 'BNB':
        usd_equivalent = amount * bnb_price

    # Calculate the number of BDAG coins purchasable
    bdag_coins = usd_equivalent * bdag_rate

    return bdag_coins


# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        amount_to_spend = 2.5  # Example: 2.5 ETH or BNB
        cryptocurrency_type = "ETH"  # Choose between "ETH" or "BNB"
        current_eth_price = 1600.0  # Example: 1 ETH = 1600 USD
        current_bnb_price = 300.0   # Example: 1 BNB = 300 USD
        bdag_exchange_rate = 50.0   # Example: 1 USD = 50 BDAG coins

        # Calculate BDAG coins
        total_bdag_coins = calculate_bdag_coins(
            amount=amount_to_spend,
            coin_type=cryptocurrency_type,
            eth_price=current_eth_price,
            bnb_price=current_bnb_price,
            bdag_rate=bdag_exchange_rate
        )

        # Output the result
        print(f"Total BDAG coins purchasable: {total_bdag_coins:.2f}")

    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
