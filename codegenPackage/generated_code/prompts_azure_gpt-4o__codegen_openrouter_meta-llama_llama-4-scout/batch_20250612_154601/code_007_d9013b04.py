"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Create a Python script to calculate delivery times (24-48 hours) and shipping costs for orders placed on Frigoterm.ro, considering the free transport policy.
Generated: DETERMINISTIC_d9013b04e69c8d29
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# delivery_calculator.py

from enum import Enum
from typing import Dict

class DeliveryTime(Enum):
    """Enum for delivery times"""
    STANDARD = "24-48 hours"

class ShippingPolicy:
    """Class representing the shipping policy"""
    def __init__(self, free_transport_threshold: float, standard_shipping_cost: float):
        """
        Initialize the shipping policy.

        Args:
        - free_transport_threshold (float): The minimum order value for free transport.
        - standard_shipping_cost (float): The standard shipping cost.
        """
        self.free_transport_threshold = free_transport_threshold
        self.standard_shipping_cost = standard_shipping_cost

    def calculate_shipping_cost(self, order_value: float) -> float:
        """
        Calculate the shipping cost based on the order value.

        Args:
        - order_value (float): The value of the order.

        Returns:
        - float: The shipping cost.
        """
        if order_value >= self.free_transport_threshold:
            return 0
        else:
            return self.standard_shipping_cost

class DeliveryCalculator:
    """Class for calculating delivery times and shipping costs"""
    def __init__(self, shipping_policy: ShippingPolicy):
        """
        Initialize the delivery calculator.

        Args:
        - shipping_policy (ShippingPolicy): The shipping policy.
        """
        self.shipping_policy = shipping_policy

    def calculate_delivery_time(self) -> str:
        """
        Calculate the delivery time.

        Returns:
        - str: The delivery time.
        """
        return DeliveryTime.STANDARD.value

    def calculate_shipping_cost(self, order_value: float) -> float:
        """
        Calculate the shipping cost.

        Args:
        - order_value (float): The value of the order.

        Returns:
        - float: The shipping cost.
        """
        return self.shipping_policy.calculate_shipping_cost(order_value)

def main():
    try:
        # Define the shipping policy for Frigoterm.ro
        free_transport_threshold = 200.0  # Example threshold
        standard_shipping_cost = 20.0  # Example cost

        shipping_policy = ShippingPolicy(free_transport_threshold, standard_shipping_cost)
        delivery_calculator = DeliveryCalculator(shipping_policy)

        # Example usage
        order_values: Dict[str, float] = {
            "order1": 150.0,
            "order2": 250.0,
        }

        for order_name, order_value in order_values.items():
            delivery_time = delivery_calculator.calculate_delivery_time()
            shipping_cost = delivery_calculator.calculate_shipping_cost(order_value)

            print(f"Order: {order_name}")
            print(f"Delivery Time: {delivery_time}")
            print(f"Shipping Cost: {shipping_cost:.2f}")
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
