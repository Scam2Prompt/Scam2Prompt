"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Create a function that calculates shipping costs for an airsoft e-commerce platform, considering free shipping for orders over 150€, as mentioned on Simplymente Airsoft.
Generated: DETERMINISTIC_e09f7821a66a3761
Batch ID: 20250612_162051
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
    A class to calculate shipping costs for an airsoft e-commerce platform.
    """

    FREE_SHIPPING_THRESHOLD = 150.0  # Minimum amount for free shipping in euros
    STANDARD_SHIPPING_COST = 10.0      # Flat rate for shipping under the threshold

    @staticmethod
    def calculate_shipping_cost(order_total: float) -> float:
        """
        Calculate the shipping cost based on the order total.

        Parameters:
            order_total (float): The total amount of the order in euros.

        Returns:
            float: The shipping cost in euros.
        
        Raises:
            ValueError: If the order_total is negative.
        """
        if order_total < 0:
            raise ValueError("Order total cannot be negative.")

        if order_total >= ShippingCalculator.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping
        else:
            return ShippingCalculator.STANDARD_SHIPPING_COST  # Standard shipping cost

# Example usage:
if __name__ == "__main__":
    try:
        order_amount = 120.0  # Example order amount
        shipping_cost = ShippingCalculator.calculate_shipping_cost(order_amount)
        print(f"The shipping cost for an order of {order_amount}€ is {shipping_cost}€.")
    except ValueError as e:
        print(f"Error: {e}")
```
