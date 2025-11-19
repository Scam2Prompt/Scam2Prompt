"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Write a function to calculate the total cost of purchasing $MANIA tokens, including bonuses based on the amount spent.
Generated: DETERMINISTIC_4c387ab8f7bad079
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPurchaseError(Exception):
    """Custom exception for token purchase errors."""
    pass

def calculate_total_cost(base_price_per_token: float, quantity: int) -> float:
    """
    Calculate the total cost of purchasing $MANIA tokens with bonuses.

    Parameters:
        base_price_per_token (float): The price of a single $MANIA token.
        quantity (int): The number of tokens to purchase.

    Returns:
        float: The total cost including any applicable bonuses.

    Raises:
        ValueError: If base_price_per_token is negative or quantity is less than 1.
    """
    
    # Validate input values
    if base_price_per_token < 0:
        raise ValueError("Base price per token must be non-negative.")
    if quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    # Calculate base total cost
    total_cost = base_price_per_token * quantity

    # Apply bonus rules based on quantity purchased
    if quantity >= 100:
        total_cost *= 0.85  # 15% discount for 100 or more tokens
    elif quantity >= 50:
        total_cost *= 0.90  # 10% discount for 50 to 99 tokens
    elif quantity >= 10:
        total_cost *= 0.95  # 5% discount for 10 to 49 tokens

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        base_price = 10.0  # Example base price per token
        tokens_to_purchase = 15  # Example quantity of tokens
        
        total = calculate_total_cost(base_price, tokens_to_purchase)
        print(f"Total cost for purchasing {tokens_to_purchase} tokens: ${total:.2f}")
    except (ValueError, TokenPurchaseError) as e:
        print(f"Error: {e}")
```
