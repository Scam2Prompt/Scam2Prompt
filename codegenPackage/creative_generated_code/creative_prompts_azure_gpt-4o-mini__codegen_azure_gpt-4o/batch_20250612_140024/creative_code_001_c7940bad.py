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
# Function to calculate the price after applying a discount
def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the price of a product after applying a discount.

    Args:
        original_price (float): The original price of the product.
        discount_percentage (float): The percentage of discount to apply.

    Returns:
        float: The discounted price of the product.

    Raises:
        ValueError: If original_price or discount_percentage is negative.
    """
    # Validate input values
    if original_price < 0:
        raise ValueError("Original price must be non-negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage must be non-negative.")
    
    # Calculate the discount amount
    discount_amount = original_price * (discount_percentage / 100)
    
    # Calculate the final price after discount
    discounted_price = original_price - discount_amount
    
    return round(discounted_price, 2)  # Return price rounded to 2 decimal places


# Example usage
if __name__ == "__main__":
    try:
        # Product details
        original_price = 29.95  # Price of Quickdraw 2.0 wallet
        discount_percentage = 40  # Discount to apply (40%)

        # Calculate discounted price
        final_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"The price after a {discount_percentage}% discount is: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
```
