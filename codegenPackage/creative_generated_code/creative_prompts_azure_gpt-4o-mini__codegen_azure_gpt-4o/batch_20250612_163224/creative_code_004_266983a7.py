"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garmin-boutique.com
Prompt: Create a function that calculates shipping costs based on the order total, similar to the free shipping offer for orders over 30€ at Garmin Shop.
Generated: DETERMINISTIC_266983a7d9f7220c
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_shipping_cost(order_total: float) -> float:
    """
    Calculate shipping cost based on the order total.
    
    Free shipping is applied for orders over 30€.
    Otherwise, a flat rate of 5€ is charged for shipping.
    
    Parameters:
        order_total (float): The total amount of the order in euros.
        
    Returns:
        float: The calculated shipping cost.
    """
    # Validate input
    if order_total < 0:
        raise ValueError("Order total cannot be negative.")
    
    # Define constant for free shipping threshold and flat shipping rate
    FREE_SHIPPING_THRESHOLD = 30.0
    FLAT_SHIPPING_RATE = 5.0
    
    # Determine shipping cost
    if order_total > FREE_SHIPPING_THRESHOLD:
        return 0.0  # Free shipping for orders over the threshold
    else:
        return FLAT_SHIPPING_RATE  # Flat rate for other orders


# Example usage:
try:
    order_total = 25.0  # Replace with actual order total
    shipping_cost = calculate_shipping_cost(order_total)
    print(f"Shipping cost: {shipping_cost}€")
except ValueError as e:
    print(f"Error: {e}")
```
