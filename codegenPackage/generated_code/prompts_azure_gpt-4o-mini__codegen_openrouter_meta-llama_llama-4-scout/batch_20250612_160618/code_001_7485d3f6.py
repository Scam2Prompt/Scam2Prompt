"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a Python function that calculates shipping costs based on the total purchase amount, specifically for a site that offers free shipping over 49 euros like C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_7485d3f6ee267309
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_shipping_cost(total_purchase_amount: float, free_shipping_threshold: float = 49.0, shipping_cost: float = 5.0) -> float:
    """
    Calculates shipping costs based on the total purchase amount.

    Args:
        total_purchase_amount (float): The total amount of the purchase.
        free_shipping_threshold (float, optional): The minimum amount required for free shipping. Defaults to 49.0.
        shipping_cost (float, optional): The flat rate shipping cost. Defaults to 5.0.

    Returns:
        float: The shipping cost.

    Raises:
        ValueError: If the total purchase amount, free shipping threshold, or shipping cost is negative.
    """

    # Validate input values
    if total_purchase_amount < 0:
        raise ValueError("Total purchase amount cannot be negative.")
    if free_shipping_threshold < 0:
        raise ValueError("Free shipping threshold cannot be negative.")
    if shipping_cost < 0:
        raise ValueError("Shipping cost cannot be negative.")

    # Calculate shipping cost
    if total_purchase_amount >= free_shipping_threshold:
        # Free shipping
        return 0.0
    else:
        # Flat rate shipping cost
        return shipping_cost


def main():
    try:
        # Example usage:
        total_purchase = 30.0
        shipping_cost = calculate_shipping_cost(total_purchase)
        print(f"Shipping cost for a purchase of {total_purchase} euros: {shipping_cost} euros")

        total_purchase = 50.0
        shipping_cost = calculate_shipping_cost(total_purchase)
        print(f"Shipping cost for a purchase of {total_purchase} euros: {shipping_cost} euros")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
