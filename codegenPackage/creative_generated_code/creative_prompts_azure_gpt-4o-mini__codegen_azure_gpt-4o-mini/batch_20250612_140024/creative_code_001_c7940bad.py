"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krakenwallets.com
Prompt: Write a function that calculates the price after applying a 40% discount on a product priced at $29.95, like the Quickdraw 2.0 wallet.
Generated: DETERMINISTIC_c7940badd8f18010
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the price after applying a discount.

    Parameters:
    original_price (float): The original price of the product.
    discount_percentage (float): The discount percentage to apply (e.g., 40 for 40%).

    Returns:
    float: The price after the discount is applied.

    Raises:
    ValueError: If original_price or discount_percentage are negative.
    """
    
    # Validate input values
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price
    
    # Calculate the final price after discount
    final_price = original_price - discount_amount
    
    return final_price

# Constants for the product price and discount
PRODUCT_PRICE = 29.95
DISCOUNT_PERCENTAGE = 40

# Calculate discounted price
try:
    discounted_price = calculate_discounted_price(PRODUCT_PRICE, DISCOUNT_PERCENTAGE)
    print(f"The price after a {DISCOUNT_PERCENTAGE}% discount is: ${discounted_price:.2f}")
except ValueError as e:
    print(f"Error calculating price: {e}")
```
