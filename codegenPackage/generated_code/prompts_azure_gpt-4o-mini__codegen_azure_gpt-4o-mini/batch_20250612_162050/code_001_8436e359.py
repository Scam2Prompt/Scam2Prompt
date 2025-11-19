"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: Write a function that calculates discounts for clothing items during seasonal sales, like the 30% off offer mentioned on Vaarabella's site.
Generated: DETERMINISTIC_8436e359962ac066
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price of an item.

    Parameters:
    original_price (float): The original price of the item.
    discount_percentage (float): The discount percentage to apply (e.g., 30 for 30%).

    Returns:
    float: The price after applying the discount.

    Raises:
    ValueError: If original_price or discount_percentage is negative.
    """
    # Validate input values
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price
    
    # Calculate the final price after discount
    discounted_price = original_price - discount_amount
    
    return discounted_price

# Example usage
if __name__ == "__main__":
    try:
        original_price = 100.0  # Example original price
        discount_percentage = 30.0  # Example discount percentage
        final_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
