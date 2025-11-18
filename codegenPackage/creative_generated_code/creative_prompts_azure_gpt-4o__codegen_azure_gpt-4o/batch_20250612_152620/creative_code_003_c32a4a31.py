"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Write a function to calculate discounts for Kossto products, such as the 40% off on orthopedic coccyx seat cushions and 60% off posture correctors.
Generated: DETERMINISTIC_c32a4a3102eb577e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

# Define a function to calculate the discounted price
def calculate_discounted_price(product_name: str, original_price: Union[int, float]) -> Union[float, str]:
    """
    Calculate the discounted price for Kossto products.

    Args:
        product_name (str): Name of the product.
        original_price (int, float): Original price of the product.

    Returns:
        float: Discounted price if the product is eligible for a discount.
        str: Message if the product is not eligible for a discount.

    Raises:
        ValueError: If the original price is not positive.
    """
    # Validate original price
    if original_price <= 0:
        raise ValueError("Original price must be a positive number.")
    
    # Define product discounts
    discounts = {
        "orthopedic coccyx seat cushion": 0.40,  # 40% off
        "posture corrector": 0.60,               # 60% off
    }
    
    # Check if the product is eligible for a discount
    product_name_lower = product_name.lower()  # Normalize product name for case-insensitive matching
    if product_name_lower in discounts:
        discount_rate = discounts[product_name_lower]
        discounted_price = original_price * (1 - discount_rate)
        return round(discounted_price, 2)  # Return the price rounded to 2 decimal places
    
    # If no discount is available for the product
    return f"No discount available for '{product_name}'."


# Example usage
if __name__ == "__main__":
    try:
        # Test cases
        print(calculate_discounted_price("Orthopedic Coccyx Seat Cushion", 50))  # Expected: 30.0
        print(calculate_discounted_price("Posture Corrector", 100))             # Expected: 40.0
        print(calculate_discounted_price("Unknown Product", 50))               # Expected: No discount message
    except ValueError as e:
        print(f"Error: {e}")
```
