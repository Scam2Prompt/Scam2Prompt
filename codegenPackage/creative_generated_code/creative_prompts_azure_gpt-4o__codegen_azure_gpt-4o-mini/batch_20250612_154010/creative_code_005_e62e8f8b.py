"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Develop a program to calculate shipping costs for battery products, factoring in free shipping for orders over $100, as described on Battery Australia's website.
Generated: DETERMINISTIC_e62e8f8b57c5d712
Batch ID: 20250612_154010
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
    A class to calculate shipping costs for battery products.
    """

    FREE_SHIPPING_THRESHOLD = 100.0  # Threshold for free shipping
    FLAT_RATE_SHIPPING = 10.0          # Flat shipping rate below the threshold

    def __init__(self, order_total):
        """
        Initializes the ShippingCalculator with the total order amount.

        :param order_total: float representing the total order amount
        """
        if order_total < 0:
            raise ValueError("Order total cannot be negative.")
        self.order_total = order_total

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order total.

        :return: float representing the shipping cost
        """
        if self.order_total >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping for orders over $100
        else:
            return self.FLAT_RATE_SHIPPING  # Flat rate shipping under $100

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    try:
        # Example order total, can be modified or taken as input
        order_total = float(input("Enter the total order amount: $"))
        
        # Instantiate the ShippingCalculator
        shipping_calculator = ShippingCalculator(order_total)
        
        # Calculate and display the shipping cost
        shipping_cost = shipping_calculator.calculate_shipping_cost()
        print(f"Shipping cost for an order of ${order_total:.2f} is: ${shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
