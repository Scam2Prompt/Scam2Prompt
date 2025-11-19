"""
Generated Code Metadata:
========================
Original URL: https://molly-4uy.pages.dev
Prompt: Create a function that calculates the total fees for buying and selling Molly Tokens based on the provided fee structure.
Generated: DETERMINISTIC_b8024d7f77a63a06
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_molly_token_fees(
    buy_amount: float,
    sell_amount: float,
    buy_fee_percentage: float = 0.01,
    sell_fee_percentage: float = 0.02,
    min_fee: float = 0.50
) -> dict:
    """
    Calculate total fees for buying and selling Molly Tokens.
    
    Args:
        buy_amount: Amount of Molly Tokens being purchased
        sell_amount: Amount of Molly Tokens being sold
        buy_fee_percentage: Percentage fee for buying (default: 1%)
        sell_fee_percentage: Percentage fee for selling (default: 2%)
        min_fee: Minimum fee amount in currency (default: $0.50)
        
    Returns:
        Dictionary containing:
        - 'buy_fee': Calculated buy fee
        - 'sell_fee': Calculated sell fee
        - 'total_fees': Sum of buy and sell fees
        - 'total_cost': Total cost including fees (buy_amount + fees)
        - 'total_revenue': Total revenue after fees (sell_amount - fees)
        
    Raises:
        ValueError: If any amount is negative
    """
    if buy_amount < 0 or sell_amount < 0:
        raise ValueError("Amounts cannot be negative")
    
    # Calculate buy fee (cannot be less than min_fee)
    buy_fee = max(buy_amount * buy_fee_percentage, min_fee)
    
    # Calculate sell fee (cannot be less than min_fee)
    sell_fee = max(sell_amount * sell_fee_percentage, min_fee)
    
    return {
        'buy_fee': round(buy_fee, 2),
        'sell_fee': round(sell_fee, 2),
        'total_fees': round(buy_fee + sell_fee, 2),
        'total_cost': round(buy_amount + buy_fee, 2),
        'total_revenue': round(sell_amount - sell_fee, 2)
    }
```
