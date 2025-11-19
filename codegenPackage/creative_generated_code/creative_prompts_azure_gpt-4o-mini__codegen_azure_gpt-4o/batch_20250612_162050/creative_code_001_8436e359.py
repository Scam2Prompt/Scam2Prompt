"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Write a function that calculates discounts for clothing items during seasonal sales, like the 30% off offer mentioned on Vaarabella's site.
Generated: DETERMINISTIC_8436e359962ac066
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate discounts for clothing items during seasonal sales

def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price for a clothing item.

    Parameters:
        original_price (float): The original price of the item. Must be non-negative.
        discount_percentage (float): The percentage discount to apply. Must be between 0 and 100.

    Returns:
        float: The final price of the item after applying the discount.

    Raises:
        ValueError: If original_price is negative or discount_percentage is out of range.
    """
    # Validate input values
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    # Calculate the discount amount
    discount_amount = original_price * (discount_percentage / 100)
    
    # Calculate the final price after applying the discount
    discounted_price = original_price - discount_amount
    
    # Ensure the discounted price is rounded to two decimal places for currency formatting
    return round(discounted_price, 2)

# Example usage:
if __name__ == "__main__":
    try:
        original_price = 100.0  # Example original price
        discount_percentage = 30.0  # Example discount percentage (e.g., 30% off)
        
        # Calculate the discounted price
        final_price = calculate_discounted_price(original_price, discount_percentage)
        
        # Print the result
        print(f"The final price after a {discount_percentage}% discount is: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
```
