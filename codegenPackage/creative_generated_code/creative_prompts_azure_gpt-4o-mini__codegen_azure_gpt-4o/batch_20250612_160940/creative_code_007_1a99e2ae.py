"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdaggs.pages.dev
Prompt: What are the minimum requirements for purchasing BDAG coins with ETH or BNB on BlockDAG?
Generated: DETERMINISTIC_1a99e2ae36b44f59
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing required modules
from decimal import Decimal

# Define constants
MIN_ETH_AMOUNT = Decimal('0.01')  # Minimum ETH required for purchase
MIN_BNB_AMOUNT = Decimal('0.05')  # Minimum BNB required for purchase
SUPPORTED_COINS = ['ETH', 'BNB']  # Coins supported for purchasing BDAG

class BlockDAGPurchaseError(Exception):
    """Custom exception for errors during BDAG coin purchase."""
    pass

def check_purchase_requirements(coin: str, amount: Decimal) -> bool:
    """
    Verify whether the purchase requirements for BDAG coins are met.

    Args:
        coin (str): The cryptocurrency being used for purchase (e.g., 'ETH', 'BNB').
        amount (Decimal): The amount of cryptocurrency being used.

    Returns:
        bool: True if requirements are met, False otherwise.

    Raises:
        BlockDAGPurchaseError: If the coin is unsupported or amount is insufficient.
    """
    # Validate the coin type
    if coin not in SUPPORTED_COINS:
        raise BlockDAGPurchaseError(f"Unsupported coin '{coin}'. Supported coins are: {', '.join(SUPPORTED_COINS)}")

    # Validate the amount based on coin type
    if coin == 'ETH' and amount < MIN_ETH_AMOUNT:
        raise BlockDAGPurchaseError(f"For ETH purchases, you need at least {MIN_ETH_AMOUNT} ETH.")
    elif coin == 'BNB' and amount < MIN_BNB_AMOUNT:
        raise BlockDAGPurchaseError(f"For BNB purchases, you need at least {MIN_BNB_AMOUNT} BNB.")
    
    # Requirements are met
    return True

def main():
    """
    Main function to demonstrate the BDAG coin purchase requirements.

    Note: Replace the input values below with actual user inputs or function calls in production.
    """
    try:
        # Example input values (replace with dynamic values in production)
        user_coin = 'ETH'  # Coin type
        user_amount = Decimal('0.02')  # Amount of the coin

        # Check if user meets the requirements
        if check_purchase_requirements(user_coin, user_amount):
            print(f"Purchase requirements met for {user_coin} with {user_amount} amount.")
    except BlockDAGPurchaseError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
