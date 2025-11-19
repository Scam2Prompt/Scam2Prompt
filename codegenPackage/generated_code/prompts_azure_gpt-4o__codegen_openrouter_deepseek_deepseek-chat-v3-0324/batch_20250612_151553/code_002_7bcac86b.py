"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Create a script to calculate bulk purchase discounts for items like "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی" based on the discount percentages provided on the website.
Generated: DETERMINISTIC_7bcac86b009ec920
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bulk Purchase Discount Calculator

This script calculates the total cost of bulk purchases with tiered discounts based on quantity.
The discount tiers are configurable and can be adjusted as needed.
"""

import sys
from typing import Dict, List, Tuple

# Discount tiers configuration: (min_quantity, discount_percentage)
DISCOUNT_TIERS = [
    (1, 0),     # 0% discount for 1-9 items
    (10, 5),    # 5% discount for 10-49 items
    (50, 10),   # 10% discount for 50-99 items
    (100, 15),  # 15% discount for 100+ items
]

def calculate_discount(quantity: int, unit_price: float) -> Tuple[float, float, float]:
    """
    Calculate the total cost with applicable discount based on quantity.
    
    Args:
        quantity: Number of items purchased
        unit_price: Price per item before discount
        
    Returns:
        Tuple of (discount_percentage, discount_amount, total_price)
    """
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    if unit_price <= 0:
        raise ValueError("Unit price must be a positive number")

    # Determine the applicable discount tier
    discount_percentage = 0
    for tier in sorted(DISCOUNT_TIERS, reverse=True):
        if quantity >= tier[0]:
            discount_percentage = tier[1]
            break

    # Calculate discount and total price
    discount_amount = (unit_price * quantity) * (discount_percentage / 100)
    total_price = (unit_price * quantity) - discount_amount
    
    return discount_percentage, discount_amount, total_price

def format_currency(amount: float) -> str:
    """
    Format currency amount for display.
    
    Args:
        amount: Numeric amount to format
        
    Returns:
        Formatted string with currency symbol
    """
    return f"{amount:,.2f} ریال"

def main():
    try:
        # Get user input
        product_name = input("نام محصول را وارد کنید: ")
        unit_price = float(input("قیمت واحد محصول (ریال): "))
        quantity = int(input("تعداد مورد نیاز: "))

        # Calculate discount and totals
        discount_percent, discount_amount, total_price = calculate_discount(quantity, unit_price)

        # Display results
        print("\n--- خلاصه سفارش ---")
        print(f"محصول: {product_name}")
        print(f"تعداد: {quantity}")
        print(f"قیمت واحد: {format_currency(unit_price)}")
        print(f"تخفیف: {discount_percent}% ({format_currency(discount_amount)})")
        print(f"قیمت نهایی: {format_currency(total_price)}")

    except ValueError as e:
        print(f"خطا: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"خطای غیرمنتظره: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
