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
# Function to calculate the discounted price of a clothing item
def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price of a clothing item.

    Parameters:
        original_price (float): The original price of the item.
        discount_percentage (float): The discount percentage to be applied.

    Returns:
        float: The discounted price of the item.

    Raises:
        ValueError: If original_price or discount_percentage is negative.
        TypeError: If original_price or discount_percentage is not a number.
    """
    # Validate input types
    if not isinstance(original_price, (int, float)):
        raise TypeError("original_price must be a number (int or float).")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("discount_percentage must be a number (int or float).")

    # Validate input values
    if original_price < 0:
        raise ValueError("original_price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("discount_percentage cannot be negative.")

    # Calculate the discount amount
    discount_amount = original_price * (discount_percentage / 100)

    # Calculate the final price after applying the discount
    discounted_price = original_price - discount_amount

    # Ensure the discounted price is not negative (edge case)
    discounted_price = max(discounted_price, 0)

    return round(discounted_price, 2)  # Return the price rounded to 2 decimal places


# Example usage
if __name__ == "__main__":
    try:
        original_price = 100.0  # Example original price
        discount_percentage = 30.0  # Example discount percentage
        final_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"The final price after a {discount_percentage}% discount is: ${final_price}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
