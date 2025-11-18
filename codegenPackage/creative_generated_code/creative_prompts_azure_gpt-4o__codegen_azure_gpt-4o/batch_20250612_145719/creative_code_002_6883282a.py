"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Provide a Python function that calculates discounts for bulk USDT exchanges based on the platform's "量大价优" (bulk pricing) policy.
Generated: DETERMINISTIC_6883282a56965eb7
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_usdt_discount(amount_usdt: float) -> float:
    """
    Calculate the discount for bulk USDT exchanges based on the platform's "量大价优" policy.

    Args:
        amount_usdt (float): The amount of USDT for the exchange.

    Returns:
        float: The discounted price after applying the bulk pricing policy.

    Raises:
        ValueError: If the input amount_usdt is not positive.
    """

    # Validate input
    if amount_usdt <= 0:
        raise ValueError("The amount of USDT must be greater than 0.")

    # Bulk pricing tiers (threshold -> discount percentage)
    # Larger amounts receive larger discounts
    pricing_tiers = [
        (1000, 0.02),   # 2% discount for 1,000 <= USDT < 5,000
        (5000, 0.05),   # 5% discount for 5,000 <= USDT < 10,000
        (10000, 0.1),   # 10% discount for 10,000 <= USDT < 50,000
        (50000, 0.15),  # 15% discount for USDT >= 50,000
    ]

    # Default discount is 0 for amounts less than the lowest tier
    discount_percentage = 0.0

    # Determine applicable discount percentage based on tiers
    for threshold, discount in pricing_tiers:
        if amount_usdt >= threshold:
            discount_percentage = discount

    # Calculate the final price after applying the discount
    discounted_price = amount_usdt * (1 - discount_percentage)

    return discounted_price


# Example usage:
if __name__ == "__main__":
    try:
        usdt_amount = 12000  # Example input
        final_price = calculate_usdt_discount(usdt_amount)
        print(f"Original price: {usdt_amount} USDT")
        print(f"Discounted price: {final_price:.2f} USDT")
    except ValueError as e:
        print(f"Error: {e}")
```
