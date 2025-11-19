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
class ShippingCalculator:
    """
    A class to calculate the shipping cost for an order of electronic components.
    """

    FREE_SHIPPING_THRESHOLD = 100.0  # Minimum order value for free shipping
    BASE_SHIPPING_COST = 10.0          # Base shipping cost
    PER_ITEM_COST = 2.0                 # Additional cost per item

    def __init__(self, order_value, item_count):
        """
        Initializes the ShippingCalculator with the order value and item count.

        :param order_value: Total value of the order
        :param item_count: Number of items in the order
        """
        self.order_value = order_value
        self.item_count = item_count

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order value and item count.

        :return: The calculated shipping cost
        :raises ValueError: If order_value or item_count is negative
        """
        if self.order_value < 0 or self.item_count < 0:
            raise ValueError("Order value and item count must be non-negative.")

        # Check for free shipping eligibility
        if self.order_value >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping

        # Calculate shipping cost
        shipping_cost = self.BASE_SHIPPING_COST + (self.item_count * self.PER_ITEM_COST)
        return shipping_cost

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    try:
        # Example order details
        order_value = float(input("Enter the total order value: "))
        item_count = int(input("Enter the number of items: "))

        # Create a ShippingCalculator instance
        shipping_calculator = ShippingCalculator(order_value, item_count)

        # Calculate and display the shipping cost
        shipping_cost = shipping_calculator.calculate_shipping_cost()
        print(f"The shipping cost for your order is: ${shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
