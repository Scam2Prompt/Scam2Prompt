"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Write code to implement a "Free Shipping" feature for orders above a specified amount (e.g., ₹1999) in an e-commerce checkout system.
Generated: DETERMINISTIC_a3bf098dad14460a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
class CheckoutSystem:
    """
    A class to represent an e-commerce checkout system with a free shipping feature.
    """
    
    def __init__(self, free_shipping_threshold):
        """
        Initializes the checkout system with a free shipping threshold.

        Args:
            free_shipping_threshold (float): The minimum order amount for free shipping.
        """
        self.free_shipping_threshold = free_shipping_threshold

    def calculate_shipping_cost(self, order_amount):
        """
        Calculates the shipping cost for an order based on the free shipping threshold.

        Args:
            order_amount (float): The total amount of the order.

        Returns:
            float: The shipping cost for the order.
        """
        try:
            # Validate that the order amount is a non-negative number
            if order_amount < 0:
                raise ValueError("Order amount cannot be negative.")

            # Free shipping for orders above or equal to the threshold
            if order_amount >= self.free_shipping_threshold:
                return 0.0  # Free shipping

            # Flat rate shipping cost for orders below the threshold
            return 50.0  # Example shipping cost (₹50)

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define the free shipping threshold (₹1999 in this case)
    FREE_SHIPPING_THRESHOLD = 1999

    # Initialize the checkout system
    checkout_system = CheckoutSystem(FREE_SHIPPING_THRESHOLD)

    # Sample orders
    orders = [2500, 1500, -100, 1999, 0]

    # Process each order and display the shipping cost
    for order in orders:
        shipping_cost = checkout_system.calculate_shipping_cost(order)
        if shipping_cost is not None:
            print(f"Order Amount: ₹{order:.2f}, Shipping Cost: ₹{shipping_cost:.2f}")
```
