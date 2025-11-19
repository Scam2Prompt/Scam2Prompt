"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate code to calculate the shipping cost for an order of electronic components, considering free shipping rules and conditions.
Generated: DETERMINISTIC_d6369433967d5251
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ShippingCalculator:
    """
    Calculates shipping cost for an order of electronic components.

    Attributes:
        free_shipping_minimum (float): Minimum order amount for free shipping.
        standard_shipping_rate (float): Standard shipping rate per item.
        express_shipping_rate (float): Express shipping rate per item.
    """

    def __init__(self, free_shipping_minimum=100.0, standard_shipping_rate=5.0, express_shipping_rate=10.0):
        """
        Initializes the ShippingCalculator.

        Args:
            free_shipping_minimum (float, optional): Minimum order amount for free shipping. Defaults to 100.0.
            standard_shipping_rate (float, optional): Standard shipping rate per item. Defaults to 5.0.
            express_shipping_rate (float, optional): Express shipping rate per item. Defaults to 10.0.
        """
        self.free_shipping_minimum = free_shipping_minimum
        self.standard_shipping_rate = standard_shipping_rate
        self.express_shipping_rate = express_shipping_rate

    def calculate_shipping_cost(self, order_amount, num_items, shipping_type="standard"):
        """
        Calculates the shipping cost for an order.

        Args:
            order_amount (float): Total amount of the order.
            num_items (int): Number of items in the order.
            shipping_type (str, optional): Type of shipping. Defaults to "standard".

        Returns:
            float: Shipping cost.

        Raises:
            ValueError: If shipping type is not "standard" or "express".
        """
        if shipping_type not in ["standard", "express"]:
            raise ValueError("Invalid shipping type. Must be 'standard' or 'express'.")

        # Check if order qualifies for free shipping
        if order_amount >= self.free_shipping_minimum:
            return 0.0

        # Calculate shipping cost based on shipping type
        if shipping_type == "standard":
            return num_items * self.standard_shipping_rate
        else:
            return num_items * self.express_shipping_rate


def main():
    calculator = ShippingCalculator()

    # Example usage:
    order_amount = 50.0
    num_items = 2
    shipping_type = "standard"

    try:
        shipping_cost = calculator.calculate_shipping_cost(order_amount, num_items, shipping_type)
        print(f"Shipping cost: ${shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
