"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Write Python code to calculate the cost of bulk orders for 3D-printed PU golf grips, factoring in customization fees, shipping costs, and discounts as described on the Longhui Golf website.
Generated: DETERMINISTIC_dfdda4472e405721
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GolfGripOrder:
    def __init__(self, quantity, base_price, customization_fee, shipping_cost, discount_percent=0):
        """
        Initialize the GolfGripOrder with order details.

        :param quantity: Number of grips being ordered
        :param base_price: Base price per grip
        :param customization_fee: Cost for customizations per grip
        :param shipping_cost: Total shipping cost for the order
        :param discount_percent: Discount percentage to be applied to the total order (default is 0)
        """
        self.quantity = quantity
        self.base_price = base_price
        self.customization_fee = customization_fee
        self.shipping_cost = shipping_cost
        self.discount_percent = discount_percent

    def validate_order(self):
        """
        Validate that the order details are acceptable.

        :raises ValueError: If any of the input values are invalid
        """
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if self.base_price < 0:
            raise ValueError("Base price cannot be negative.")
        if self.customization_fee < 0:
            raise ValueError("Customization fee cannot be negative.")
        if self.shipping_cost < 0:
            raise ValueError("Shipping cost cannot be negative.")
        if not (0 <= self.discount_percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")

    def calculate_total_cost(self):
        """
        Calculate the total cost of the order including customization and shipping.
        Apply discount if applicable.

        :return: Total cost of the order
        """
        self.validate_order()

        # Calculate the total cost without discount
        total_cost = (self.base_price + self.customization_fee) * self.quantity + self.shipping_cost
        
        # Apply discount
        if self.discount_percent > 0:
            discount_amount = total_cost * (self.discount_percent / 100)
            total_cost -= discount_amount

        return total_cost

    def display_order_summary(self):
        """
        Display a summary of the order with total cost.

        :return: Order summary as a string
        """
        total_cost = self.calculate_total_cost()
        summary = (
            f"Order Summary:\n"
            f"- Quantity: {self.quantity}\n"
            f"- Base Price per Grip: ${self.base_price:.2f}\n"
            f"- Customization Fee per Grip: ${self.customization_fee:.2f}\n"
            f"- Shipping Cost: ${self.shipping_cost:.2f}\n"
            f"- Discount: {self.discount_percent}%\n"
            f"- Total Cost: ${total_cost:.2f}\n"
        )

        return summary


# Example usage:
if __name__ == "__main__":
    try:
        order = GolfGripOrder(
            quantity=100,
            base_price=10.00,
            customization_fee=2.50,
            shipping_cost=50.00,
            discount_percent=5
        )
        print(order.display_order_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
