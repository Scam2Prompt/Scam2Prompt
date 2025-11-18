"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Write a Python program that calculates the discount percentage for Harman Kardon products currently on sale, based on the original and sale prices listed on Harman Kardon Philippines.
Generated: DETERMINISTIC_0451f915c9db98a4
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_discount_percentage(original_price: float, sale_price: float) -> float:
    """
    Calculate the discount percentage based on the original price and sale price.

    Args:
        original_price (float): The original price of the product.
        sale_price (float): The sale price of the product.

    Returns:
        float: The discount percentage represented as a percentage of the original price.

    Raises:
        ValueError: If original_price is less than or equal to zero or if sale_price is negative.
    """
    if original_price <= 0:
        raise ValueError("Original price must be greater than zero.")
    if sale_price < 0:
        raise ValueError("Sale price cannot be negative.")

    discount = original_price - sale_price
    discount_percentage = (discount / original_price) * 100
    return discount_percentage


def main():
    """
    Main function to execute the discount calculation for Harman Kardon products.
    Prompts the user for original and sale prices, and displays the discount percentage.
    """
    try:
        original_price = float(input("Enter the original price of the Harman Kardon product: "))
        sale_price = float(input("Enter the sale price of the Harman Kardon product: "))

        discount_percentage = calculate_discount_percentage(original_price, sale_price)
        print(f"The discount percentage is: {discount_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
