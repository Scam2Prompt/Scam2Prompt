"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Create a script to calculate shipping costs for promotional items based on the free shipping threshold of Rp. 10,000,000 mentioned on the Merchandiso website.
Generated: DETERMINISTIC_d9bc2d30705a1acd
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for promotional items based on a free shipping threshold.
    """

    FREE_SHIPPING_THRESHOLD = 10000000  # Free shipping threshold in Rupiah
    SHIPPING_COST = 50000  # Flat shipping cost in Rupiah

    def __init__(self, order_amount):
        """
        Initializes the ShippingCalculator with the order amount.

        :param order_amount: Total amount of the order in Rupiah
        """
        self.order_amount = order_amount

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order amount.

        :return: Shipping cost in Rupiah
        """
        if self.order_amount < 0:
            raise ValueError("Order amount cannot be negative.")

        if self.order_amount >= self.FREE_SHIPPING_THRESHOLD:
            return 0  # Free shipping

        return self.SHIPPING_COST  # Flat shipping cost

    def display_shipping_cost(self):
        """
        Displays the shipping cost based on the order amount.
        """
        try:
            shipping_cost = self.calculate_shipping_cost()
            print(f"Order Amount: Rp. {self.order_amount}")
            print(f"Shipping Cost: Rp. {shipping_cost}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        order_amount_input = float(input("Enter the order amount in Rupiah: Rp. "))
        shipping_calculator = ShippingCalculator(order_amount_input)
        shipping_calculator.display_shipping_cost()
    except ValueError:
        print("Invalid input. Please enter a valid number for the order amount.")
```
