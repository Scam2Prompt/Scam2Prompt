"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a function to calculate total costs for products like "OLEO DE MOTOR 2100 PROTECT+ 10W30" and "CAPACETE PARA BIKE WILD," including discounts or taxes, referencing "autopecasbrazz."
Generated: DETERMINISTIC_59e312385b98db4c
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def calculate_total_cost(products: List[Dict[str, float]], discounts: float = 0.0, tax_rate: float = 0.0) -> float:
    """
    Calculate the total cost for a list of products with discounts and taxes applied.

    Parameters:
        products (List[Dict[str, float]]): A list of dictionaries containing product details, 
                                           each with 'name' (str) and 'price' (float).
                                           Example: [{'name': 'OLEO DE MOTOR 2100 PROTECT+ 10W30', 'price': 100.0}]
        discounts (float): Total discount to be applied (percentage between 0 and 100). Default is 0.0.
        tax_rate (float): Tax rate to be applied (percentage between 0 and 100). Default is 0.0.

    Returns:
        float: The total cost after applying discounts and taxes.

    Raises:
        ValueError: If any product price is negative or discounts/tax_rate are invalid.
    """
    # Input validation
    if discounts < 0 or discounts > 100:
        raise ValueError("Discounts must be between 0 and 100.")
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Tax rate must be between 0 and 100.")
    for product in products:
        if product['price'] < 0:
            raise ValueError(f"Product price cannot be negative. Invalid price for {product['name']}.")

    # Calculate total price before adjustments
    total_price = sum(product['price'] for product in products)
    
    # Apply discount
    discount_amount = total_price * (discounts / 100)
    total_price -= discount_amount

    # Apply taxes
    tax_amount = total_price * (tax_rate / 100)
    total_price += tax_amount

    # Return final total cost
    return round(total_price, 2)


# Example usage
if __name__ == "__main__":
    try:
        products = [
            {'name': 'OLEO DE MOTOR 2100 PROTECT+ 10W30', 'price': 100.0},
            {'name': 'CAPACETE PARA BIKE WILD', 'price': 50.0}
        ]
        discounts = 10.0  # 10% discount
        tax_rate = 5.0    # 5% tax
        total_cost = calculate_total_cost(products, discounts, tax_rate)
        print(f"Total cost: R$ {total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
