"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Write code to calculate shipping costs for bulk orders of fasteners based on APN Hardware's nationwide delivery model.
Generated: DETERMINISTIC_c3c00a4b73e4d2a0
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for bulk orders of fasteners based on APN Hardware's delivery model.
    
    Attributes:
        base_shipping_rate (float): The base shipping rate per order.
        bulk_discount_threshold (int): The minimum quantity for bulk order discount.
        bulk_discount_rate (float): The discount rate applied to bulk orders.
    """

    def __init__(self, base_shipping_rate: float, bulk_discount_threshold: int, bulk_discount_rate: float):
        """
        Initializes the ShippingCostCalculator with the specified parameters.

        Args:
            base_shipping_rate (float): The base shipping rate per order.
            bulk_discount_threshold (int): The minimum quantity for bulk order discount.
            bulk_discount_rate (float): The discount rate applied to bulk orders.
        """
        self.base_shipping_rate = base_shipping_rate
        self.bulk_discount_threshold = bulk_discount_threshold
        self.bulk_discount_rate = bulk_discount_rate

    def calculate_shipping_cost(self, quantity: int) -> float:
        """
        Calculates the shipping cost based on the quantity of fasteners ordered.

        Args:
            quantity (int): The quantity of fasteners in the order.

        Returns:
            float: The total shipping cost.

        Raises:
            ValueError: If the quantity is negative or zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        shipping_cost = self.base_shipping_rate

        # Apply bulk discount if applicable
        if quantity >= self.bulk_discount_threshold:
            shipping_cost *= (1 - self.bulk_discount_rate)

        return shipping_cost


def main():
    """
    The main function to demonstrate the usage of the ShippingCostCalculator.
    """

    # Set the parameters for the shipping cost calculator
    base_rate = 10.00  # Base shipping rate in dollars
    bulk_threshold = 100  # Minimum quantity for bulk discount
    bulk_discount = 0.10  # 10% bulk discount

    # Create an instance of the ShippingCostCalculator
    calculator = ShippingCostCalculator(base_rate, bulk_threshold, bulk_discount)

    # Example quantities to calculate shipping costs for
    quantities = [50, 100, 250]

    # Calculate and print the shipping costs for the example quantities
    for quantity in quantities:
        try:
            cost = calculator.calculate_shipping_cost(quantity)
            print(f"Shipping cost for {quantity} fasteners: ${cost:.2f}")
        except ValueError as e:
            print(f"Error calculating shipping cost for quantity {quantity}: {e}")


if __name__ == "__main__":
    main()
```
