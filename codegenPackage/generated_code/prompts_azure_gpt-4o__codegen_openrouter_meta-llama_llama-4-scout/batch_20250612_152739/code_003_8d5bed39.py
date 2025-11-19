"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Write a function in Python to calculate the shipping costs for international orders based on the TiburonFishingReels.com policy, ensuring the order value does not exceed $200 and uses a third-party shipping address.
Generated: DETERMINISTIC_8d5bed39002edfa9
Batch ID: 20250612_152739
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
    Calculates shipping costs for international orders based on TiburonFishingReels.com policy.
    """

    def __init__(self, order_value, shipping_address):
        """
        Initializes the ShippingCalculator.

        Args:
            order_value (float): The total value of the order.
            shipping_address (str): The third-party shipping address.

        Raises:
            ValueError: If the order value exceeds $200.
            TypeError: If the order value or shipping address is of incorrect type.
        """
        if not isinstance(order_value, (int, float)):
            raise TypeError("Order value must be a number.")
        if not isinstance(shipping_address, str):
            raise TypeError("Shipping address must be a string.")

        if order_value > 200:
            raise ValueError("Order value cannot exceed $200.")

        self.order_value = order_value
        self.shipping_address = shipping_address

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order value.

        Returns:
            float: The calculated shipping cost.
        """
        # Base shipping cost for international orders
        base_cost = 20.0

        # Additional cost per pound
        additional_cost_per_pound = 5.0

        # Assume a default weight of 1 pound for simplicity
        # In a real-world application, this would be retrieved from the order details
        weight_in_pounds = 1

        # Calculate the shipping cost
        shipping_cost = base_cost + (additional_cost_per_pound * weight_in_pounds)

        # Apply a discount for orders over $100
        if self.order_value > 100:
            shipping_cost *= 0.9  # 10% discount

        return shipping_cost


def main():
    try:
        order_value = 150.0
        shipping_address = "Third-Party Shipping Address"

        calculator = ShippingCalculator(order_value, shipping_address)
        shipping_cost = calculator.calculate_shipping_cost()

        print(f"Shipping cost: ${shipping_cost:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
