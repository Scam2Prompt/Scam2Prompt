"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from the "Venta de Garage" section of the Ortopedic website, including discounts on items like "Silla de ruedas Premium Full Equipada" and "Jeringas desechables."
Generated: DETERMINISTIC_6e75c2c046d85dee
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(cart, discounts):
    """
    Calculate the total cost of items in the shopping cart, including applicable discounts.
    
    Args:
        cart (dict): Dictionary containing item names as keys and their respective prices as values.
        discounts (dict): Dictionary containing item names as keys and their respective discount percentages as values.
    
    Returns:
        float: The total cost of the items after applying discounts.
    """
    try:
        total_cost = 0.0
        
        for item, price in cart.items():
            if item in discounts:
                # Apply discount if a discount exists for the item
                discount_percentage = discounts[item]
                discounted_price = price - (price * (discount_percentage / 100))
                total_cost += discounted_price
            else:
                # No discount, add price as is
                total_cost += price
        
        return total_cost
    except Exception as e:
        print(f"Error calculating total cost: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to execute the script logic.
    """
    # Example shopping cart with items and prices
    shopping_cart = {
        "Silla de ruedas Premium Full Equipada": 1200.00,
        "Jeringas desechables": 100.00,
        "Cama ortopédica ajustable": 2500.00,
        "Bastón plegable ajustable": 50.00
    }

    # Example discounts on specific items (percentage)
    discounts = {
        "Silla de ruedas Premium Full Equipada": 10,  # 10% discount
        "Jeringas desechables": 5  # 5% discount
    }

    # Calculate total cost with discounts
    total_cost = calculate_total_cost(shopping_cart, discounts)

    if total_cost is not None:
        print(f"The total cost of your purchase is: ${total_cost:.2f}")
    else:
        print("Failed to calculate the total cost. Please try again.")


if __name__ == "__main__":
    main()
```
