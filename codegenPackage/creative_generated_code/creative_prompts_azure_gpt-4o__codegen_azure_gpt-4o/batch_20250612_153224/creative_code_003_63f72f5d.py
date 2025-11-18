"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Write code to calculate discounted prices for products, including support for percentage-based discounts (e.g., -75%, -20%) and display the original and current price.
Generated: DETERMINISTIC_63f72f5decbe9635
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# product_discount_calculator.py

# Import the necessary module for error handling
from typing import List, Tuple

def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price of a product given the original price and the discount percentage.

    Parameters:
    original_price (float): The original price of the product.
    discount_percentage (float): The discount percentage to be applied.

    Returns:
    float: The discounted price after applying the discount.
    """
    if original_price < 0:
        raise ValueError("Original price must be a positive value.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    # Calculate the discounted price
    discounted_price = original_price * (1 - discount_percentage / 100)
    return round(discounted_price, 2)


def display_prices(products: List[Tuple[str, float, float]]) -> None:
    """
    Display original and discounted prices for a list of products.

    Parameters:
    products (List[Tuple[str, float, float]]): A list of tuples where each tuple contains:
        - Product name (str)
        - Original price (float)
        - Discount percentage (float)
    """
    print("Product Prices:")
    print("-" * 50)
    for product in products:
        name, original_price, discount_percentage = product
        try:
            discounted_price = calculate_discounted_price(original_price, discount_percentage)
            print(f"Product: {name}")
            print(f"Original Price: ${original_price:.2f}")
            print(f"Discount Percentage: {discount_percentage}%")
            print(f"Discounted Price: ${discounted_price:.2f}")
            print("-" * 50)
        except ValueError as e:
            print(f"Error for product '{name}': {e}")
            print("-" * 50)


if __name__ == "__main__":
    # Example usage
    products = [
        ("Laptop", 1000.0, 20.0),
        ("Smartphone", 800.0, 15.0),
        ("Headphones", 150.0, 75.0),
        ("Mouse", 50.0, 10.0),
        ("Keyboard", -20.0, 5.0),  # Example of invalid price
        ("Monitor", 200.0, 110.0),  # Example of invalid discount percentage
    ]

    # Display product prices
    display_prices(products)
```
