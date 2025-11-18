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

class Order:
    """Class to represent an order with delivery time and shipping cost calculation."""
    
    def __init__(self, order_amount):
        """
        Initializes the Order object.

        Parameters:
            order_amount (float): The total amount of the order.
        """
        self.order_amount = order_amount
        self.shipping_cost = self.calculate_shipping_cost()
        self.delivery_time = self.calculate_delivery_time()

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order amount.
        
        Returns:
            float: Shipping cost. Returns 0.0 if amount is above the free transport threshold.
        """
        FREE_TRANSPORT_THRESHOLD = 100.0  # Example threshold for free transport
        if self.order_amount >= FREE_TRANSPORT_THRESHOLD:
            return 0.0  # Free transport for orders above the threshold
        else:
            return 15.0  # Flat shipping cost for orders below the threshold

    def calculate_delivery_time(self):
        """
        Determines the delivery time based on the current date and time.

        Returns:
            str: Estimated delivery time in days.
        """
        current_time = datetime.datetime.now()
        delivery_days = 1 if current_time.hour < 16 else 2  # Deliver next day if before 4 PM, otherwise in 2 days
        delivery_date = current_time + datetime.timedelta(days=delivery_days)
        return delivery_date.strftime("%Y-%m-%d %H:%M:%S")

    def display_order_details(self):
        """
        Displays the order details including amount, shipping cost, and delivery time.
        """
        print(f"Order Amount: €{self.order_amount:.2f}")
        print(f"Shipping Cost: €{self.shipping_cost:.2f}")
        print(f"Estimated Delivery Time: {self.delivery_time}")

def main():
    """Main function to execute the order processing."""
    try:
        order_amount = float(input("Enter the order amount in EUR: "))
        if order_amount < 0:
            raise ValueError("Order amount must be a non-negative value.")

        order = Order(order_amount)
        order.display_order_details()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
