"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a Python function that calculates shipping costs based on the total purchase amount, specifically for a site that offers free shipping over 49 euros like C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_7485d3f6ee267309
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_shipping_cost(purchase_amount: float) -> float:
    """
    Calculate shipping costs based on the purchase amount. 
    Free shipping is applied for orders over 49 euros.
    
    Args:
        purchase_amount (float): Total purchase amount in euros.
    
    Returns:
        float: Shipping cost in euros. Returns 0 for free shipping.
        
    Raises:
        ValueError: If the purchase amount is negative.
    """
    # Define the shipping cost for orders below the free shipping threshold
    SHIPPING_COST = 5.0  # euros
    FREE_SHIPPING_THRESHOLD = 49.0  # euros
    
    # Validate the input
    if purchase_amount < 0:
        raise ValueError("Purchase amount cannot be negative")
    
    # Determine shipping cost
    if purchase_amount >= FREE_SHIPPING_THRESHOLD:
        return 0.0  # Free shipping for orders over the threshold
    else:
        return SHIPPING_COST  # Fixed shipping cost for orders below the threshold


# Example Usage:
# try:
#     cost = calculate_shipping_cost(30.0)
#     print(f"Shipping cost: {cost} euros")
# except ValueError as e:
#     print(f"Error: {e}")
```
