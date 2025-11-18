"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Create a Python script to calculate delivery times (24-48 hours) and shipping costs for orders placed on Frigoterm.ro, considering the free transport policy.
Generated: DETERMINISTIC_d9013b04e69c8d29
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ShippingCalculator:
    """
    A class to calculate delivery times and shipping costs for Frigoterm orders.
    """

    def __init__(self):
        # Define shipping cost and free shipping threshold
        self.shipping_cost = 20.0  # Flat shipping cost in RON
        self.free_shipping_threshold = 300.0  # Free shipping for orders above this amount in RON

    def calculate_delivery_time(self):
        """
        Calculates the delivery time (24-48 hours).
        Returns:
            str: Estimated delivery time as a string.
        """
        min_delivery_time = datetime.timedelta(hours=24)
        max_delivery_time = datetime.timedelta(hours=48)
        now = datetime.datetime.now()
        
        # Generate delivery time range
        delivery_start = now + min_delivery_time
        delivery_end = now + max_delivery_time
        return f"Estimated delivery: {delivery_start.strftime('%Y-%m-%d %H:%M:%S')} - {delivery_end.strftime('%Y-%m-%d %H:%M:%S')}"

    def calculate_shipping_cost(self, order_amount):
        """
        Calculates the shipping cost based on the order amount.
        
        Args:
            order_amount (float): Total order amount in RON.
            
        Returns:
            float: Shipping cost; 0 for orders above the free shipping threshold.
        """
        if order_amount < 0:
            raise ValueError("Order amount cannot be negative.")
        # Free shipping for orders above the threshold
        return 0.0 if order_amount >= self.free_shipping_threshold else self.shipping_cost

def main():
    """
    Main function to handle user input and perform calculations.
    """
    try:
        # Instantiate the calculator
        calculator = ShippingCalculator()

        # Get order amount from user
        order_amount = float(input("Enter the total order amount (RON): "))

        # Calculate delivery time
        delivery_time = calculator.calculate_delivery_time()
        print(delivery_time)

        # Calculate shipping cost
        shipping_cost = calculator.calculate_shipping_cost(order_amount)
        if shipping_cost == 0.0:
            print("Shipping is free for orders above 300 RON!")
        else:
            print(f"Shipping cost: {shipping_cost:.2f} RON")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for any unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
