"""
Generated Code Metadata:
========================
Original URL: https://harmankardon.com.ph
Prompt: Write a Python program that calculates the discount percentage for Harman Kardon products currently on sale, based on the original and sale prices listed on Harman Kardon Philippines.
Generated: DETERMINISTIC_0451f915c9db98a4
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Harman Kardon Philippines Discount Calculator

Calculates the discount percentage for Harman Kardon products currently on sale.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_discount(original_price, sale_price):
    """
    Calculates the discount percentage.

    Args:
        original_price (float): The original price of the product.
        sale_price (float): The sale price of the product.

    Returns:
        float: The discount percentage.

    Raises:
        ValueError: If the original or sale price is negative.
        ZeroDivisionError: If the original price is zero.
    """
    if original_price < 0 or sale_price < 0:
        raise ValueError("Prices cannot be negative.")

    if original_price == 0:
        raise ZeroDivisionError("Original price cannot be zero.")

    discount = original_price - sale_price
    discount_percentage = (discount / original_price) * 100

    return discount_percentage


def main():
    try:
        # Example usage
        products = [
            {"name": "Harman Kardon Onyx Studio 7", "original_price": 24995, "sale_price": 19995},
            {"name": "Harman Kardon Citation 500", "original_price": 34995, "sale_price": 29995},
            {"name": "Harman Kardon Aura Studio 3", "original_price": 19995, "sale_price": 17995},
        ]

        for product in products:
            discount_percentage = calculate_discount(product["original_price"], product["sale_price"])
            print(f"Product: {product['name']}")
            print(f"Original Price: ₱{product['original_price']:,}")
            print(f"Sale Price: ₱{product['sale_price']:,}")
            print(f"Discount Percentage: {discount_percentage:.2f}%")
            print("-" * 50)

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
