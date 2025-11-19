"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Develop a function that calculates the estimated delivery time for bulk orders, taking into account the production and shipping processes mentioned by Bern Wears.
Generated: DETERMINISTIC_9df2c67da30bdfe9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

def calculate_delivery_time(order_quantity, production_rate, shipping_time_days):
    """
    Calculate the estimated delivery time for bulk orders.

    Parameters:
    - order_quantity (int): The total number of items in the order.
    - production_rate (int): The number of items produced per day.
    - shipping_time_days (int): The number of days required for shipping.

    Returns:
    - str: The estimated delivery date in 'YYYY-MM-DD' format.
    """
    try:
        # Validate inputs
        if order_quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")
        if production_rate <= 0:
            raise ValueError("Production rate must be greater than zero.")
        if shipping_time_days < 0:
            raise ValueError("Shipping time cannot be negative.")

        # Calculate production time in days
        production_time_days = (order_quantity + production_rate - 1) // production_rate  # Ceiling division

        # Calculate total delivery time
        total_delivery_time_days = production_time_days + shipping_time_days

        # Calculate the estimated delivery date
        today = datetime.now()
        estimated_delivery_date = today + timedelta(days=total_delivery_time_days)

        # Return the delivery date in 'YYYY-MM-DD' format
        return estimated_delivery_date.strftime('%Y-%m-%d')

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage:
if __name__ == "__main__":
    # Example parameters
    order_quantity = 500
    production_rate = 50
    shipping_time_days = 5

    # Calculate and print the estimated delivery date
    delivery_date = calculate_delivery_time(order_quantity, production_rate, shipping_time_days)
    print(f"Estimated Delivery Date: {delivery_date}")
```
