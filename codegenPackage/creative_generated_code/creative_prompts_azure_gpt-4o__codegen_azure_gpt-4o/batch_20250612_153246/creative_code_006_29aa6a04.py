"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Develop a Python script to calculate the total cost of wine purchases from Kadma Winery's online shop, including multiple items.
Generated: DETERMINISTIC_29aa6a04ed093ec8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(cart, price_list):
    """
    Calculate the total cost of wine purchases given a shopping cart and price list.

    Args:
        cart (dict): A dictionary where the keys are wine names and the values are quantities.
        price_list (dict): A dictionary where the keys are wine names and the values are unit prices.

    Returns:
        float: Total cost of the wine purchases.

    Raises:
        ValueError: If an item in the cart is not found in the price list.
        TypeError: If input data is not in the correct format.
    """
    if not isinstance(cart, dict) or not isinstance(price_list, dict):
        raise TypeError("Both cart and price_list must be dictionaries.")

    total_cost = 0.0
    for wine, quantity in cart.items():
        if wine not in price_list:
            raise ValueError(f"Wine '{wine}' not found in the price list.")
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError(f"Invalid quantity '{quantity}' for wine '{wine}'.")
        total_cost += price_list[wine] * quantity

    return total_cost


def main():
    """
    Main function to demonstrate the calculation of the total cost of wine purchases.
    """
    try:
        # Example price list: wine name -> price per unit
        price_list = {
            "Chardonnay": 15.99,
            "Merlot": 12.50,
            "Cabernet Sauvignon": 18.75,
            "Pinot Noir": 20.00
        }

        # Example shopping cart: wine name -> quantity
        cart = {
            "Chardonnay": 3,
            "Merlot": 2,
            "Cabernet Sauvignon": 1
        }

        # Calculate the total cost
        total = calculate_total_cost(cart, price_list)
        print(f"Total cost of wine purchases: ${total:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except TypeError as te:
        print(f"Error: {te}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
