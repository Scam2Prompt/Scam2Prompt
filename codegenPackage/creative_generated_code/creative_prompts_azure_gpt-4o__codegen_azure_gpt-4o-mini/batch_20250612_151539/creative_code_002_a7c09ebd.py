"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Create a function to calculate discounted prices for furniture items, referencing the discount examples provided on the Joss Home site (e.g., "Ліжко двоспальне Коко коричневе" with a discount from $800 to $744).
Generated: DETERMINISTIC_a7c09ebd4c91a1aa
Batch ID: 20250612_151539
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
    Calculate the discounted price of an item.

    Args:
        original_price (float): The original price of the item.
        discount_percentage (float): The discount percentage to apply.

    Returns:
        float: The final price after applying the discount.

    Raises:
        ValueError: If the original price or discount percentage is negative.
    """
    # Validate input parameters
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price
    
    # Calculate the final price after discount
    final_price = original_price - discount_amount

    # Return the final price rounded to two decimal places
    return round(final_price, 2)

# Example usage:
if __name__ == "__main__":
    try:
        original_price = 800.00  # Original price of the furniture item
        discount_percentage = 7.0  # Discount of 7%

        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"The discounted price is: ${discounted_price}")
    except ValueError as e:
        print(f"Error: {e}")
```
