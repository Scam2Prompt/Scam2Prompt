"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Generate a script to automate customer quotes for bulk salt and UltraGLOW™ Snow and Ice Melt orders, factoring in delivery zones and product availability.
Generated: DETERMINISTIC_ab3a444480ca25ed
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Tuple

# Constants for delivery zones and product availability
DELIVERY_ZONES = {
    "Zone 1": {"min_order": 100, "max_order": 500, "delivery_fee": 10},
    "Zone 2": {"min_order": 501, "max_order": 1000, "delivery_fee": 20},
    "Zone 3": {"min_order": 1001, "max_order": 5000, "delivery_fee": 30},
}

PRODUCTS = {
    "bulk_salt": {"price_per_unit": 0.5, "available": True},
    "ultraglow": {"price_per_unit": 1.0, "available": True},
}

class OrderError(Exception):
    """Custom exception for order processing errors."""
    pass

def calculate_quote(order: Dict[str, int], delivery_zone: str) -> Tuple[float, float]:
    """
    Calculate the total quote for the order based on product quantities and delivery zone.

    Args:
        order (Dict[str, int]): A dictionary with product names as keys and quantities as values.
        delivery_zone (str): The delivery zone for the order.

    Returns:
        Tuple[float, float]: Total cost and delivery fee.

    Raises:
        OrderError: If the order is invalid or delivery zone is not found.
    """
    if delivery_zone not in DELIVERY_ZONES:
        raise OrderError(f"Invalid delivery zone: {delivery_zone}")

    total_cost = 0.0
    delivery_fee = DELIVERY_ZONES[delivery_zone]["delivery_fee"]

    for product, quantity in order.items():
        if product not in PRODUCTS or not PRODUCTS[product]["available"]:
            raise OrderError(f"Product not available: {product}")
        
        if quantity < 0:
            raise OrderError(f"Invalid quantity for {product}: {quantity}")

        total_cost += PRODUCTS[product]["price_per_unit"] * quantity

    # Check if the total order meets the minimum order requirement for the delivery zone
    if total_cost < DELIVERY_ZONES[delivery_zone]["min_order"]:
        raise OrderError(f"Minimum order of {DELIVERY_ZONES[delivery_zone]['min_order']} required for {delivery_zone}")

    return total_cost, delivery_fee

def main():
    # Example order
    order = {
        "bulk_salt": 300,
        "ultraglow": 200,
    }
    delivery_zone = "Zone 1"

    try:
        total_cost, delivery_fee = calculate_quote(order, delivery_zone)
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Delivery Fee: ${delivery_fee:.2f}")
        print(f"Total Amount Due: ${total_cost + delivery_fee:.2f}")
    except OrderError as e:
        print(f"Error processing order: {e}")

if __name__ == "__main__":
    main()
```
