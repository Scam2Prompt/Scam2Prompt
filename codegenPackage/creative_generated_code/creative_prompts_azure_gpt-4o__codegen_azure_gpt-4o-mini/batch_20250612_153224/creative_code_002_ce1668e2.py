"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Generate code to calculate discounts for Bollé products, such as the CHRONOSHIELD TITANIUM MATTE – VOLT+ ULTRAVIOLET POLARIZED, based on original and current prices.
Generated: DETERMINISTIC_ce1668e24bb01aaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    def __init__(self, name: str, original_price: float, current_price: float):
        """
        Initializes a Product instance.

        :param name: Name of the product.
        :param original_price: Original price of the product.
        :param current_price: Current price of the product.
        """
        self.name = name
        self.original_price = original_price
        self.current_price = current_price

    def calculate_discount(self) -> float:
        """
        Calculates the discount percentage based on the original and current prices.

        :return: Discount percentage as a float, or None if there's no discount.
        """
        if self.original_price <= 0:
            raise ValueError("Original price must be greater than zero.")
        
        discount_amount = self.original_price - self.current_price
        if discount_amount <= 0:
            return 0.0  # No discount

        discount_percentage = (discount_amount / self.original_price) * 100
        return round(discount_percentage, 2)

    def __str__(self):
        """
        Returns a string representation of the product.

        :return: A formatted string with product details.
        """
        return (f"Product: {self.name}, "
                f"Original Price: ${self.original_price:.2f}, "
                f"Current Price: ${self.current_price:.2f}, "
                f"Discount: {self.calculate_discount()}%")

# Example usage
if __name__ == "__main__":
    # Create a product instance
    try:
        chronoshield = Product("CHRONOSHIELD TITANIUM MATTE – VOLT+ ULTRAVIOLET POLARIZED", 200.00, 150.00)
        # Print product details including discount
        print(chronoshield)
    except ValueError as e:
        print(f"Error: {e}")
```
