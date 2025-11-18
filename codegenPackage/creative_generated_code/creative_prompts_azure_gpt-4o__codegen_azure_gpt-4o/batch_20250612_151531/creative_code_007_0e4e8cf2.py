"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Create a function to calculate shipping costs for thermal paper rolls based on order size and destination, referencing the distribution model of Apos Chile.
Generated: DETERMINISTIC_0e4e8cf24858d430
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

def calculate_shipping_cost(order_size, destination):
    """
    Calculate shipping costs for thermal paper rolls based on order size and destination.

    Parameters:
        order_size (int): The number of thermal paper rolls in the order.
        destination (str): The destination country or region ("Domestic", "International").
    
    Returns:
        float: The calculated shipping cost.
    
    Raises:
        ValueError: If order_size is not a positive integer or destination is invalid.
    """
    # Validate input parameters
    if not isinstance(order_size, int) or order_size <= 0:
        raise ValueError("Order size must be a positive integer.")
    if destination not in ["Domestic", "International"]:
        raise ValueError("Destination must be 'Domestic' or 'International'.")

    # Define base shipping rates and per-roll cost
    BASE_RATE_DOMESTIC = 5.0  # Base rate for domestic shipping
    BASE_RATE_INTERNATIONAL = 20.0  # Base rate for international shipping
    COST_PER_ROLL_DOMESTIC = 0.50  # Cost per roll for domestic shipping
    COST_PER_ROLL_INTERNATIONAL = 1.50  # Cost per roll for international shipping

    # Assign costs based on destination
    if destination == "Domestic":
        base_rate = BASE_RATE_DOMESTIC
        cost_per_roll = COST_PER_ROLL_DOMESTIC
    else:  # destination == "International"
        base_rate = BASE_RATE_INTERNATIONAL
        cost_per_roll = COST_PER_ROLL_INTERNATIONAL

    # Calculate shipping costs
    shipping_cost = base_rate + (order_size * cost_per_roll)

    # Apply bulk discount for large orders
    BULK_DISCOUNT_THRESHOLD = 100  # Orders of 100 rolls or more qualify for a discount
    BULK_DISCOUNT_RATE = 0.10  # 10% discount

    if order_size >= BULK_DISCOUNT_THRESHOLD:
        shipping_cost *= (1 - BULK_DISCOUNT_RATE)  # Apply discount

    # Round the cost to two decimal places for better presentation
    return round(shipping_cost, 2)


# Example usage (uncomment for testing):
# try:
#     cost = calculate_shipping_cost(120, "International")
#     print(f"Shipping cost: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}")
```
