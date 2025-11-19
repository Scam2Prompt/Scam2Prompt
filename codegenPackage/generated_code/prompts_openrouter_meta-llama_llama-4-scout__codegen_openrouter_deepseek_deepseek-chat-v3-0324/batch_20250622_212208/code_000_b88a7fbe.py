"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Write a Python script to calculate the maximum amount of $INIT tokens that can be purchased during the presale using BNB, given the minimum and maximum purchase limits.
Generated: DETERMINISTIC_b88a7fbeb02991c1
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_max_purchase(
    bnb_balance: float,
    min_purchase_bnb: float,
    max_purchase_bnb: float,
    token_price_bnb: float
) -> tuple:
    """
    Calculate the maximum amount of tokens that can be purchased during presale.
    
    Args:
        bnb_balance: The available BNB balance of the buyer
        min_purchase_bnb: Minimum purchase amount in BNB
        max_purchase_bnb: Maximum purchase amount in BNB
        token_price_bnb: Price of 1 token in BNB
        
    Returns:
        tuple: (max_tokens_purchasable, bnb_spent)
        
    Raises:
        ValueError: If any input is negative or if balance is insufficient
    """
    # Validate inputs
    if any(arg < 0 for arg in [bnb_balance, min_purchase_bnb, max_purchase_bnb, token_price_bnb]):
        raise ValueError("All input values must be non-negative")
    
    if token_price_bnb == 0:
        raise ValueError("Token price cannot be zero")
    
    if bnb_balance < min_purchase_bnb:
        raise ValueError("Insufficient BNB balance for minimum purchase")
    
    # Calculate maximum possible BNB that can be spent
    bnb_spent = min(max_purchase_bnb, bnb_balance)
    
    # Calculate token amount
    max_tokens_purchasable = bnb_spent / token_price_bnb
    
    # Round down to avoid fractional tokens
    max_tokens_purchasable = math.floor(max_tokens_purchasable)
    
    # Recalculate actual BNB spent based on rounded tokens
    if max_tokens_purchasable > 0:
        bnb_spent = max_tokens_purchasable * token_price_bnb
        bnb_spent = max(bnb_spent, min_purchase_bnb)
    else:
        raise ValueError("Cannot purchase any tokens with current balance and limits")
    
    return max_tokens_purchasable, bnb_spent

if __name__ == "__main__":
    try:
        # Example usage
        bnb_balance = float(input("Enter your BNB balance: "))
        min_purchase = float(input("Enter minimum purchase amount in BNB: "))
        max_purchase = float(input("Enter maximum purchase amount in BNB: "))
        token_price = float(input("Enter token price in BNB: "))
        
        tokens, spent = calculate_max_purchase(bnb_balance, min_purchase, max_purchase, token_price)
        
        print(f"\nMaximum purchase details:")
        print(f"Tokens purchasable: {tokens}")
        print(f"BNB to be spent: {spent}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
