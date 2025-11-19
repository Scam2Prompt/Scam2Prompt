"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Create a function that calculates shipping costs for an airsoft e-commerce platform, considering free shipping for orders over 150€, as mentioned on Simplymente Airsoft.
Generated: DETERMINISTIC_e09f7821a66a3761
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
from typing import List, Dict

def calculate_shipping_cost(order_total: float, shipping_rate: float = 10.0) -> float:
    """
    Calculate shipping costs for an airsoft e-commerce platform.

    Parameters:
        order_total (float): Total value of the order.
        shipping_rate (float): Flat shipping rate. Defaults to 10.0€.

    Returns:
        float: The calculated shipping cost.
    """
    # Validate input
    if order_total < 0:
        raise ValueError("Order total cannot be negative.")
    if shipping_rate < 0:
        raise ValueError("Shipping rate cannot be negative.")

    # Free shipping for orders over 150€
    if order_total > 150:
        return 0.0
    
    # Otherwise, return the flat shipping rate
    return shipping_rate

# Example usage
if __name__ == "__main__":
    try:
        # Define test orders
        test_orders: List[Dict[str, float]] = [
            {"order_total": 120.0},
            {"order_total": 160.0},
            {"order_total": 80.0},
            {"order_total": 200.0},
        ]

        # Shipping rate (can be configured dynamically)
        shipping_rate = 10.0

        # Calculate shipping costs for test orders
        for order in test_orders:
            shipping_cost = calculate_shipping_cost(order["order_total"], shipping_rate)
            print(f"Order Total: {order['order_total']}€, Shipping Cost: {shipping_cost}€")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
