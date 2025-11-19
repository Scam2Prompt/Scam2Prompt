"""
Generated Code Metadata:
========================
Original URL: https://olhaoshu.com
Prompt: "Write a Python code snippet to calculate discounts for products in a sale, similar to Olha Oshu's sale with up to 30% discount, and apply it to a list of product prices."
Generated: DETERMINISTIC_c259a10e786141a7
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate discounts for products in a sale

# Import necessary modules
from typing import List

def apply_discount(prices: List[float], discount_percentage: float) -> List[float]:
    """
    Apply a discount to a list of product prices.

    Args:
        prices (List[float]): List of original product prices.
        discount_percentage (float): Discount percentage to apply (0-100).

    Returns:
        List[float]: List of discounted product prices.

    Raises:
        ValueError: If discount_percentage is not between 0 and 100.
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    # Calculate discounted prices
    discounted_prices = [
        round(price * (1 - discount_percentage / 100), 2) for price in prices
    ]
    return discounted_prices

def main():
    """
    Main function to demonstrate the discount calculation.
    """
    # Example list of product prices
    product_prices = [100.0, 250.0, 75.0, 300.0, 50.0]
    
    # Discount percentage (up to 30% as per the request)
    discount_percentage = 30.0
    
    try:
        # Apply the discount
        discounted_prices = apply_discount(product_prices, discount_percentage)
        
        # Print the original and discounted prices
        print("Original Prices: ", product_prices)
        print(f"Discounted Prices (with {discount_percentage}% off): ", discounted_prices)
    except ValueError as e:
        # Handle invalid discount percentage
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
