"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Provide a Python script to calculate the cost of bulk orders for stainless steel fasteners, using pricing models similar to those described on APN Hardware's website.
Generated: DETERMINISTIC_623d57b1116ff49b
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_bulk_order_cost(quantity, unit_price, discount_tiers):
    """
    Calculate the total cost for a bulk order of stainless steel fasteners.

    Args:
        quantity (int): The number of fasteners being ordered.
        unit_price (float): The price per unit before any discounts.
        discount_tiers (list of tuples): A list of (quantity_threshold, discount_percentage).
                                         Each tuple defines a quantity threshold and corresponding discount.

    Returns:
        float: The total cost for the bulk order.
    """
    if quantity <= 0 or unit_price <= 0:
        raise ValueError("Quantity and unit price must be positive numbers.")

    # Sort discount tiers in descending order of quantity thresholds
    discount_tiers = sorted(discount_tiers, key=lambda x: x[0], reverse=True)

    # Find applicable discount
    applicable_discount = 0
    for threshold, discount in discount_tiers:
        if quantity >= threshold:
            applicable_discount = discount
            break

    # Calculate discounted unit price
    discounted_unit_price = unit_price * (1 - applicable_discount / 100)

    # Calculate total cost
    total_cost = quantity * discounted_unit_price
    return round(total_cost, 2)


def main():
    """
    Main function to demonstrate the bulk order cost calculation.
    """
    print("Welcome to Bulk Order Cost Calculator for Stainless Steel Fasteners!")

    try:
        # User input for order details
        quantity = int(input("Enter the quantity of fasteners: "))
        unit_price = float(input("Enter the unit price of each fastener: "))
        
        # Example discount tiers (quantity_threshold, discount_percentage)
        discount_tiers = [
            (100, 5),    # 5% discount for orders >= 100 units
            (500, 10),   # 10% discount for orders >= 500 units
            (1000, 15),  # 15% discount for orders >= 1000 units
        ]
        
        # Calculate and display the total cost
        total_cost = calculate_bulk_order_cost(quantity, unit_price, discount_tiers)
        print(f"The total cost for your bulk order is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
