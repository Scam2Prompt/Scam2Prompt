"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Develop a function that calculates the estimated delivery time for bulk orders, taking into account the production and shipping processes mentioned by Bern Wears.
Generated: DETERMINISTIC_9df2c67da30bdfe9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_delivery_time(order_quantity, production_rate, shipping_time):
    """
    Calculate the estimated delivery time for bulk orders.

    Args:
        order_quantity (int): Total quantity of items in the order.
        production_rate (int): Number of items produced per day.
        shipping_time (int): Number of days required for shipping.

    Returns:
        str: Estimated delivery date in 'YYYY-MM-DD' format.
    """
    # Validate inputs
    if not isinstance(order_quantity, int) or order_quantity <= 0:
        raise ValueError("order_quantity must be a positive integer.")
    if not isinstance(production_rate, int) or production_rate <= 0:
        raise ValueError("production_rate must be a positive integer.")
    if not isinstance(shipping_time, int) or shipping_time < 0:
        raise ValueError("shipping_time must be a non-negative integer.")
    
    # Calculate production time in days
    production_days = -(-order_quantity // production_rate)  # Ceiling division

    # Calculate total time including shipping
    total_days = production_days + shipping_time

    # Calculate estimated delivery date
    current_date = datetime.now()
    estimated_delivery_date = current_date + timedelta(days=total_days)

    # Return the estimated delivery date as a string
    return estimated_delivery_date.strftime('%Y-%m-%d')


# Example usage:
try:
    order_quantity = 1000     # Total items in the order
    production_rate = 200     # Items produced per day
    shipping_time = 5         # Days required for shipping

    estimated_date = calculate_delivery_time(order_quantity, production_rate, shipping_time)
    print(f"Estimated Delivery Date: {estimated_date}")
except ValueError as e:
    print(f"Error: {e}")
```
