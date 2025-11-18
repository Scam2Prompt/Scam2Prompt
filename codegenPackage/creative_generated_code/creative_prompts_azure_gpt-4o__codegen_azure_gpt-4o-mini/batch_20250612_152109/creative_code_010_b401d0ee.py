"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write a script to analyze the discounts on Meat Master products (e.g., -30% on Caja China Premium Grande) and calculate the final price for a bulk purchase.
Generated: DETERMINISTIC_b401d0eed3bd5a03
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# meat_master_discount_calculator.py

from typing import List, Tuple

class Product:
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param original_price: Original price of the product
        :param discount_percentage: Discount percentage (as a whole number, e.g., 30 for 30%)
        """
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def final_price(self) -> float:
        """
        Calculates the final price after applying the discount.

        :return: Final price after discount
        """
        discount_amount = (self.discount_percentage / 100) * self.original_price
        return self.original_price - discount_amount

def calculate_bulk_purchase(products: List[Tuple[str, float, float]], quantity: int) -> float:
    """
    Calculates the total price for a bulk purchase of multiple products with discounts.

    :param products: List of product details, where each product is a tuple of (name, original_price, discount_percentage)
    :param quantity: Quantity of each product to purchase
    :return: Total price for the bulk purchase
    """
    total_cost = 0.0

    for name, original_price, discount_percentage in products:
        try:
            product = Product(name, original_price, discount_percentage)
            total_cost += product.final_price() * quantity
        except Exception as e:
            print(f"Error processing product '{name}': {e}")
            continue

    return total_cost

def main():
    """
    Main function to analyze discounts on Meat Master products and calculate total price.
    """
    # Sample products for analysis
    products = [
        ("Caja China Premium Grande", 200.00, 30),
        ("Asado de Tira", 100.00, 20),
        ("Chorizo Argentino", 50.00, 15)
    ]

    # Set the quantity for bulk purchase
    quantity = 10

    # Calculate the total cost for the bulk purchase
    total_price = calculate_bulk_purchase(products, quantity)

    # Display the result
    print(f"Total price for {quantity} units of each product: ${total_price:.2f}")

if __name__ == "__main__":
    main()
```
