"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write a script to analyze the discounts on Meat Master products (e.g., -30% on Caja China Premium Grande) and calculate the final price for a bulk purchase.
Generated: DETERMINISTIC_b401d0eed3bd5a03
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """Class to represent a product with a name, original price, and discount percentage."""
    
    def __init__(self, name: str, original_price: float, discount_percentage: float):
        self.name = name
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def final_price(self) -> float:
        """Calculate the final price after applying the discount."""
        if self.original_price < 0 or not (0 <= self.discount_percentage <= 100):
            raise ValueError("Original price must be non-negative and discount percentage must be between 0 and 100.")
        discount_amount = (self.discount_percentage / 100) * self.original_price
        return self.original_price - discount_amount

def calculate_bulk_purchase(products: list, quantities: list) -> float:
    """Calculate the total price for a bulk purchase of products."""
    if len(products) != len(quantities):
        raise ValueError("The number of products must match the number of quantities.")
    
    total_price = 0.0
    for product, quantity in zip(products, quantities):
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        total_price += product.final_price() * quantity
    return total_price

def main():
    """Main function to execute the discount analysis and bulk purchase calculation."""
    # Sample data for Meat Master products
    products_data = [
        {"name": "Caja China Premium Grande", "original_price": 300.0, "discount_percentage": 30},
        {"name": "Meat Master BBQ Set", "original_price": 150.0, "discount_percentage": 20},
        {"name": "Premium Meat Selection", "original_price": 200.0, "discount_percentage": 25}
    ]
    
    # Convert product data to Product objects
    products = []
    for item in products_data:
        product = Product(item['name'], item['original_price'], item['discount_percentage'])
        products.append(product)

    # Quantities for bulk purchase
    quantities = [2, 3, 1]  # Number of each product to purchase

    try:
        total_cost = calculate_bulk_purchase(products, quantities)
        print(f"Total cost for bulk purchase: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
