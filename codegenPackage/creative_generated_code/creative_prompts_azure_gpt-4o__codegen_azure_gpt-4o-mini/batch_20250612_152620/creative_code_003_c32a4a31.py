"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Write a function to calculate discounts for Kossto products, such as the 40% off on orthopedic coccyx seat cushions and 60% off posture correctors.
Generated: DETERMINISTIC_c32a4a3102eb577e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class to represent a product with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Apply a discount to the product price.

        Args:
            discount_percentage (float): The percentage discount to apply.

        Returns:
            float: The final price after discount.

        Raises:
            ValueError: If discount_percentage is not between 0 and 100.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (discount_percentage / 100) * self.price
        final_price = self.price - discount_amount
        return final_price


def calculate_discounted_prices(products: list[Product]) -> dict:
    """
    Calculate the discounted prices for a list of products.

    Args:
        products (list[Product]): A list of Product instances.

    Returns:
        dict: A dictionary with product names as keys and their discounted prices as values.
    """
    discounted_prices = {}
    
    for product in products:
        if product.name == "Orthopedic Coccyx Seat Cushion":
            discount = 40
        elif product.name == "Posture Corrector":
            discount = 60
        else:
            discount = 0
        
        discounted_price = product.apply_discount(discount)
        discounted_prices[product.name] = discounted_price
    
    return discounted_prices


# Example usage
if __name__ == "__main__":
    try:
        products = [
            Product("Orthopedic Coccyx Seat Cushion", 50.00),
            Product("Posture Corrector", 30.00),
        ]
        
        discounted_prices = calculate_discounted_prices(products)
        for name, price in discounted_prices.items():
            print(f"{name}: ${price:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
