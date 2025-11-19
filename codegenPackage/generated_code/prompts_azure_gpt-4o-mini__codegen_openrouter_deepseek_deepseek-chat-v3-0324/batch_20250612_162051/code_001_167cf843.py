"""
Generated Code Metadata:
========================
Original URL: https://www.reliableridesllc.org
Prompt: Write a function that calculates the rental price per day for a vehicle based on the model and any applicable discounts, inspired by the pricing structure of Reliable Rides LLC.
Generated: DETERMINISTIC_167cf843b1e1129e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_rental_price(model: str, days: int, is_member: bool = False, promo_code: str = None) -> float:
    """
    Calculate the daily rental price for a vehicle based on model, rental duration, and discounts.

    Args:
        model (str): The vehicle model (e.g., "economy", "standard", "luxury").
        days (int): The number of rental days (must be >= 1).
        is_member (bool, optional): Whether the customer is a member. Defaults to False.
        promo_code (str, optional): Applicable promotion code. Defaults to None.

    Returns:
        float: The calculated daily rental price after discounts.

    Raises:
        ValueError: If model is invalid or days is less than 1.
    """
    # Base prices per model (in dollars)
    model_prices = {
        "economy": 40.00,
        "standard": 60.00,
        "luxury": 100.00
    }

    # Validate input
    if model.lower() not in model_prices:
        raise ValueError(f"Invalid model. Must be one of: {list(model_prices.keys())}")
    if days < 1:
        raise ValueError("Days must be at least 1")

    # Get base price
    base_price = model_prices[model.lower()]

    # Apply discounts
    final_price = base_price

    # Member discount (10%)
    if is_member:
        final_price *= 0.9

    # Promo code discounts
    if promo_code:
        promo_code = promo_code.lower().strip()
        if promo_code == "welcome20":
            final_price *= 0.8  # 20% off
        elif promo_code == "summer15":
            final_price *= 0.85  # 15% off
        elif promo_code == "weekend10":
            if days <= 3:  # Only applicable for short rentals
                final_price *= 0.9  # 10% off

    # Long-term rental discount (applied after other discounts)
    if days > 7:
        final_price *= 0.95  # Additional 5% off for rentals >7 days

    return round(final_price, 2)
```
