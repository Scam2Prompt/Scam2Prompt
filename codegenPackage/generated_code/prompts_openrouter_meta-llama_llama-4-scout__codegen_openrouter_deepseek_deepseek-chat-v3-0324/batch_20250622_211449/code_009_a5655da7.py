"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Generate a Python code snippet to calculate the total cost of a bulk order of industrial filters, including discounts and shipping costs.
Generated: DETERMINISTIC_a5655da7a2c77d51
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_order_cost(
    unit_price: float,
    quantity: int,
    discount_threshold: int = 100,
    discount_rate: float = 0.1,
    shipping_base: float = 50.0,
    shipping_per_unit: float = 0.5,
    tax_rate: float = 0.08
) -> float:
    """
    Calculate the total cost of a bulk order including discounts, shipping, and tax.

    Args:
        unit_price: Price per filter unit.
        quantity: Number of units ordered.
        discount_threshold: Minimum quantity to qualify for discount (default: 100).
        discount_rate: Discount rate applied if threshold is met (default: 0.1).
        shipping_base: Base shipping cost (default: 50.0).
        shipping_per_unit: Additional shipping cost per unit (default: 0.5).
        tax_rate: Tax rate applied to subtotal (default: 0.08).

    Returns:
        Total order cost after discounts, shipping, and tax.

    Raises:
        ValueError: If any numeric parameter is negative.
    """
    # Validate input parameters
    if any(arg < 0 for arg in [unit_price, quantity, discount_threshold, 
                              discount_rate, shipping_base, shipping_per_unit, tax_rate]):
        raise ValueError("All numeric parameters must be non-negative")

    # Calculate subtotal with potential discount
    subtotal = unit_price * quantity
    if quantity >= discount_threshold:
        subtotal *= (1 - discount_rate)

    # Calculate shipping cost
    shipping_cost = shipping_base + (shipping_per_unit * quantity)

    # Calculate tax and total
    tax = subtotal * tax_rate
    total = subtotal + shipping_cost + tax

    return round(total, 2)  # Round to 2 decimal places for currency
```
