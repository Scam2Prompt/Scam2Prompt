"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Create a Python script to simulate bulk order placement for products such as "کابل Ldnio LC631C دو سر تایپ سی" and calculate the total cost after applying discounts.
Generated: DETERMINISTIC_acfbac50e3d59423
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define a class to represent the product
class Product:
    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param price: Price of the product per item
        :param discount: Discount percentage (0-100), default is 0.0
        """
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_discounted_price(self) -> float:
        """
        Calculate the price after applying the discount.
        
        :return: The discounted price for a single product
        """
        if self.discount < 0 or self.discount > 100:
            raise ValueError("Discount must be in the range 0-100.")
        return self.price * (1 - self.discount / 100)

# Function to calculate total cost of bulk orders
def calculate_total_cost(products: list[Product], quantities: list[int]) -> float:
    """
    Calculate the total cost for a bulk order of products.

    :param products: List of Product objects
    :param quantities: List of quantities corresponding to each product
    :return: Total cost of the bulk order after applying discounts
    """
    if len(products) != len(quantities):
        raise ValueError("Products and quantities lists must be of the same length.")
    
    total_cost = 0.0
    for product, quantity in zip(products, quantities):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        total_cost += product.calculate_discounted_price() * quantity
    
    return total_cost

# Main function to simulate bulk order placement
def main():
    """
    Main function to simulate bulk order placement and calculate total cost.
    """
    try:
        # Example Product list
        products = [
            Product(name="کابل Ldnio LC631C دو سر تایپ سی", price=150000, discount=15),
            Product(name="کابل تایپ سی معمولی", price=100000, discount=10),
        ]
        
        # Example quantities for the products
        quantities = [5, 3]  # 5 units of the first product, 3 units of the second product
        
        # Calculate total cost
        total_cost = calculate_total_cost(products, quantities)
        
        print(f"Total cost for the bulk order: {total_cost:.2f} ریال")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Execute the main function
if __name__ == "__main__":
    main()
```
