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
"""
Discount Calculator for Product Sale
=====================================

Calculates discounts for products in a sale and applies it to a list of product prices.

Discounts are based on the product price:
- Up to 10% discount for prices $10 and above
- Up to 20% discount for prices $20 and above
- Up to 30% discount for prices $50 and above

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_discount(price):
    """
    Calculates the discount for a given product price.

    Args:
        price (float): The product price.

    Returns:
        float: The discount amount.
    """
    if price < 0:
        raise ValueError("Price cannot be negative")

    if price >= 50:
        return price * 0.3  # 30% discount
    elif price >= 20:
        return price * 0.2  # 20% discount
    elif price >= 10:
        return price * 0.1  # 10% discount
    else:
        return 0  # No discount


def apply_discounts(prices):
    """
    Applies discounts to a list of product prices.

    Args:
        prices (list[float]): A list of product prices.

    Returns:
        list[tuple[float, float, float]]: A list of tuples containing the original price, discount amount, and discounted price.
    """
    results = []
    for price in prices:
        try:
            discount = calculate_discount(price)
            discounted_price = price - discount
            results.append((price, discount, discounted_price))
        except Exception as e:
            print(f"Error processing price {price}: {str(e)}")
    return results


def main():
    # Example usage
    product_prices = [15, 25, 55, 5, 100]
    results = apply_discounts(product_prices)

    print("Original Price\tDiscount Amount\tDiscounted Price")
    for original_price, discount, discounted_price in results:
        print(f"${original_price:.2f}\t\t${discount:.2f}\t\t${discounted_price:.2f}")


if __name__ == "__main__":
    main()
```
