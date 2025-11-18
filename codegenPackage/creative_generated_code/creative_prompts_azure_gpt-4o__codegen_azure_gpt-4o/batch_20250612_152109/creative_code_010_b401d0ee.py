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
import re

def parse_discount(product_description):
    """
    Extracts discount percentage from the product description.

    Args:
        product_description (str): Description of the product, e.g., "-30% on Caja China Premium Grande"

    Returns:
        float: Discount percentage as a decimal value (e.g., 0.3 for 30% discount)
    """
    try:
        match = re.search(r'-(\d+)%', product_description)
        if match:
            discount_percentage = int(match.group(1)) / 100
            return discount_percentage
        else:
            raise ValueError("No discount percentage found in the product description.")
    except Exception as e:
        raise ValueError(f"Error parsing discount: {e}")


def calculate_final_price(original_price, discount_percentage):
    """
    Calculates the final price of a product after applying the discount.

    Args:
        original_price (float): Original price of the product.
        discount_percentage (float): Discount percentage as a decimal value.

    Returns:
        float: Final price after discount.
    """
    try:
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 1):
            raise ValueError("Discount percentage must be between 0 and 1.")

        final_price = original_price * (1 - discount_percentage)
        return round(final_price, 2)
    except Exception as e:
        raise ValueError(f"Error calculating final price: {e}")


def bulk_purchase_analysis(products, quantities):
    """
    Calculates the total cost for a bulk purchase of products.

    Args:
        products (list of dict): List of product dictionaries with 'description' and 'price' keys.
                                 e.g., [{'description': '-30% on Caja China Premium Grande', 'price': 100.0}]
        quantities (list of int): List of quantities corresponding to each product.

    Returns:
        float: Total cost for the bulk purchase.
    """
    try:
        if len(products) != len(quantities):
            raise ValueError("Products and quantities lists must have the same length.")

        total_cost = 0.0

        for product, quantity in zip(products, quantities):
            discount_percentage = parse_discount(product['description'])
            final_price = calculate_final_price(product['price'], discount_percentage)
            total_cost += final_price * quantity

        return round(total_cost, 2)
    except Exception as e:
        raise ValueError(f"Error in bulk purchase analysis: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # List of products and their prices
        products = [
            {'description': '-30% on Caja China Premium Grande', 'price': 100.0},
            {'description': '-20% on Meat Master BBQ Grill', 'price': 200.0},
            {'description': '-50% on Caja China Mini', 'price': 50.0},
        ]

        # Quantities for each product
        quantities = [2, 1, 4]

        # Calculate total cost for bulk purchase
        total_cost = bulk_purchase_analysis(products, quantities)
        print(f"Total cost for bulk purchase: ${total_cost}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
