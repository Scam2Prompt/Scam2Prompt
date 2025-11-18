"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Develop a program to calculate discounts for bulk purchases from Condi Shop, such as "Confectionery sprinkles in bulk" or "Wholesale chocolate."
Generated: DETERMINISTIC_04fc757a4775f81b
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_bulk_discount(quantity, unit_price):
    """
    Calculate the total price with discounts for bulk purchases.

    Discounts:
    - 10% off for quantities between 50 and 99.
    - 20% off for quantities between 100 and 199.
    - 30% off for quantities >= 200.

    :param quantity: Number of units purchased
    :param unit_price: Price per unit
    :return: Final price after applying discount
    """
    if quantity < 0 or unit_price < 0:
        raise ValueError("Quantity and unit price must both be non-negative.")

    if quantity >= 200:
        discount_rate = 0.30
    elif quantity >= 100:
        discount_rate = 0.20
    elif quantity >= 50:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    total_price = quantity * unit_price
    discount = total_price * discount_rate
    final_price = total_price - discount

    return final_price

def main():
    """
    Main function to handle user input and calculate the discounted price.
    """
    try:
        # Prompt user for quantity and unit price
        quantity = int(input("Enter the quantity of items purchased: "))
        unit_price = float(input("Enter the unit price of the item: "))

        # Calculate the final price
        final_price = calculate_bulk_discount(quantity, unit_price)

        # Display the result
        print(f"The total price after discount is: ${final_price:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
