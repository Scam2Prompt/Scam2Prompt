"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing multiple pet products from villagepetbrazz, taking into account installment payment options.
Generated: DETERMINISTIC_9f89ad7cce9456bf
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for handling decimal calculations
from decimal import Decimal, InvalidOperation

def calculate_total_cost(products, installment_months=1):
    """
    Calculate the total cost of purchasing multiple pet products. 
    This function also supports installment payment options.

    Parameters:
        products (list of dict): A list of dictionaries where each dictionary contains 
                                 'name' (str): Name of the product,
                                 'price' (str or numeric): Price of the product,
                                 'quantity' (int): Quantity of the product to be purchased.
        installment_months (int): Number of months for installment payments. Default is 1 (no installments).

    Returns:
        dict: A dictionary containing:
              'total_cost': Total cost of the products (Decimal),
              'monthly_installment': Monthly installment amount (Decimal) if installments are chosen.

    Raises:
        ValueError: If input data is invalid (e.g., negative price, invalid quantity, or installment months <= 0).
    """
    
    try:
        # Validate installment months
        if installment_months <= 0:
            raise ValueError("Installment months must be greater than 0.")

        # Initialize total cost
        total_cost = Decimal('0')

        # Loop through each product and calculate its cost
        for product in products:
            # Validate product keys
            if 'price' not in product or 'quantity' not in product:
                raise ValueError("Each product must have 'price' and 'quantity' keys.")

            # Convert price to Decimal for precise calculations
            try:
                price = Decimal(product['price'])
            except InvalidOperation:
                raise ValueError(f"Invalid price value for product: {product.get('name', 'Unknown')}")

            # Validate price and quantity
            if price < 0:
                raise ValueError(f"Price cannot be negative for product: {product.get('name', 'Unknown')}")
            if product['quantity'] < 0:
                raise ValueError(f"Quantity cannot be negative for product: {product.get('name', 'Unknown')}")

            # Accumulate total cost
            total_cost += price * product['quantity']

        # Calculate monthly installment if applicable
        monthly_installment = total_cost / Decimal(installment_months)

        # Return result as a dictionary
        return {
            'total_cost': total_cost,
            'monthly_installment': monthly_installment
        }

    except ValueError as e:
        # Handle ValueError exceptions and propagate error message
        raise ValueError(f"Error calculating total cost: {str(e)}")
    except Exception as e:
        # Handle unexpected exceptions gracefully
        raise Exception(f"An unexpected error occurred: {str(e)}")


# Example Usage:
# products = [
#     {'name': 'Dog Food', 'price': '25.50', 'quantity': 3},
#     {'name': 'Cat Toy', 'price': '15.99', 'quantity': 2},
#     {'name': 'Aquarium Filter', 'price': '45.00', 'quantity': 1}
# ]
# result = calculate_total_cost(products, installment_months=3)
# print(result)
```
