"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Provide Python code to calculate shipping costs for an online store offering free shipping for orders above $1,999 MXN, with products like "Ceraplus Ostomy Barriers".
Generated: DETERMINISTIC_6f34ea2482da9f3a
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs based on order amount.
    
    Attributes:
        free_shipping_threshold (float): The minimum order amount for free shipping.
    """

    def __init__(self, free_shipping_threshold=1999.0):
        """
        Initializes the ShippingCalculator with the specified free shipping threshold.

        Args:
            free_shipping_threshold (float): The threshold for free shipping.
        """
        self.free_shipping_threshold = free_shipping_threshold

    def calculate_shipping_cost(self, order_amount):
        """
        Calculate the shipping cost based on the order amount.

        Args:
            order_amount (float): The total amount of the order.

        Returns:
            float: The shipping cost. Returns 0 if above the free shipping threshold.

        Raises:
            ValueError: If the order_amount is negative.
        """
        if order_amount < 0:
            raise ValueError("Order amount cannot be negative.")

        if order_amount >= self.free_shipping_threshold:
            return 0.0  # Free shipping for eligible orders
        else:
            return 100.0  # Fixed shipping cost for orders below threshold

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    try:
        # Example order amounts
        orders = [1500.0, 2000.0, -500.0, 1999.0]

        # Initialize the shipping calculator
        shipping_calculator = ShippingCalculator()

        for order in orders:
            shipping_cost = shipping_calculator.calculate_shipping_cost(order)
            print(f"Order Amount: {order} MXN - Shipping Cost: {shipping_cost} MXN")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
