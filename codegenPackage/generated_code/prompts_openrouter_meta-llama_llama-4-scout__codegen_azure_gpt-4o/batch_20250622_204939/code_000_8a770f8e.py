"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Write a Python code to calculate the total cost of a shopping cart containing a CADEIRA GAMER XZONE CGR-01-GR and a Memória para Notebook NTC NTCKF2666ND4-8GB, considering a 7% discount à vista.
Generated: DETERMINISTIC_8a770f8eb0ccbc91
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

# Import necessary modules
import sys

def calculate_total_cost(cart_items, discount_rate):
    """
    Calculate the total cost of items in the shopping cart after applying a discount.

    Args:
        cart_items (list of dict): A list of dictionaries where each dictionary represents an item
                                   with 'name' and 'price' keys.
        discount_rate (float): The discount rate to be applied (e.g., 0.07 for 7%).

    Returns:
        float: The total cost after applying the discount.
    """
    try:
        # Calculate the total price of items in the cart
        total_price = sum(item['price'] for item in cart_items)

        # Apply the discount
        discounted_price = total_price * (1 - discount_rate)

        return round(discounted_price, 2)  # Return the total cost rounded to 2 decimal places
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while calculating the total cost: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to calculate the total cost of a shopping cart.
    """
    # Define the shopping cart items
    shopping_cart = [
        {"name": "CADEIRA GAMER XZONE CGR-01-GR", "price": 899.90},
        {"name": "Memória para Notebook NTC NTCKF2666ND4-8GB", "price": 149.90}
    ]

    # Define the discount rate (7% à vista)
    discount_rate = 0.07

    # Calculate the total cost
    total_cost = calculate_total_cost(shopping_cart, discount_rate)

    if total_cost is not None:
        # Print the total cost
        print(f"Total cost after {discount_rate * 100:.0f}% discount: R$ {total_cost}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
