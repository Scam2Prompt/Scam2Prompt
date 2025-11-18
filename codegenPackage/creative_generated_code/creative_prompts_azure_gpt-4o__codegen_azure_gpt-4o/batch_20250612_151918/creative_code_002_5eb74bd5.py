"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a script to calculate the total cost of a shopping cart with CMQLF products, including discounts like "-2,00 €" on detox teas or "-3,00 €" on solid mouthwash.
Generated: DETERMINISTIC_5eb74bd58c9c6d00
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(cart):
    """
    Calculate the total cost of the shopping cart, applying discounts where applicable.

    Parameters:
        cart (list): A list of dictionaries where each dictionary represents a product
                     and contains "name", "price", and "quantity".

    Returns:
        float: The total cost after discounts.
    """
    # Discounts dictionary (product names mapped to their respective discounts)
    discounts = {
        "detox tea": -2.00,   # €2.00 off per unit
        "solid mouthwash": -3.00  # €3.00 off per unit
    }

    total_cost = 0.0

    try:
        for item in cart:
            # Retrieve product details
            name = item.get("name", "").lower()  # Product name (case-insensitive)
            price = item.get("price", 0.0)  # Base price of the product
            quantity = item.get("quantity", 1)  # Quantity of the product

            # Ensure price and quantity are valid numbers
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError(f"Invalid price for product '{name}': {price}")
            if not isinstance(quantity, int) or quantity < 1:
                raise ValueError(f"Invalid quantity for product '{name}': {quantity}")

            # Apply discount if applicable
            discount = discounts.get(name, 0.0)
            discounted_price = price + discount  # Apply discount
            if discounted_price < 0:
                raise ValueError(f"Discounted price for '{name}' cannot be negative.")

            # Accumulate the total cost
            total_cost += discounted_price * quantity

    except Exception as e:
        print(f"Error calculating total cost: {e}")
        sys.exit(1)  # Exit the program with an error code

    return total_cost


if __name__ == "__main__":
    # Example shopping cart
    shopping_cart = [
        {"name": "detox tea", "price": 10.00, "quantity": 2},
        {"name": "solid mouthwash", "price": 8.00, "quantity": 1},
        {"name": "shampoo", "price": 5.50, "quantity": 3},
    ]

    # Calculate and print the total cost
    total = calculate_total_cost(shopping_cart)
    print(f"Total cost of the shopping cart: €{total:.2f}")
```
