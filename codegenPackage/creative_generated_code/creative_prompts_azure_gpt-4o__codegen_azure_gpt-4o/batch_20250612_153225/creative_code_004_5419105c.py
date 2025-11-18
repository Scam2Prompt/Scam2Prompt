"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Provide a Python example for handling shipping policies and returns for an online store that sells items like "Battery Chargers" and "Power Inverters," referencing the Volport website structure.
Generated: DETERMINISTIC_5419105c248d6a8d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script handles shipping policies and return management for an online store.
It simulates a backend structure that can be extended to integrate with a website like Volport.
"""

from datetime import datetime, timedelta

class ShippingPolicy:
    """Class to manage shipping policies for the store."""

    def __init__(self):
        # Shipping policy details
        self.domestic_shipping_time = timedelta(days=5)  # Domestic shipping time (e.g., 5 days)
        self.international_shipping_time = timedelta(days=15)  # International shipping time (e.g., 15 days)
        self.free_shipping_threshold = 100.0  # Free shipping for orders above $100
        self.flat_shipping_rate = 10.0  # Flat rate for orders below $100

    def calculate_shipping_cost(self, cart_total):
        """
        Calculate shipping cost based on the cart total.
        :param cart_total: Total value of the items in the shopping cart.
        :return: Shipping cost (float).
        """
        if cart_total >= self.free_shipping_threshold:
            return 0.0  # Free shipping
        return self.flat_shipping_rate

    def estimated_delivery_time(self, is_international):
        """
        Calculate estimated delivery time based on shipping origin and destination.
        :param is_international: Boolean indicating whether the shipment is international.
        :return: Estimated delivery date (datetime).
        """
        if is_international:
            return datetime.now() + self.international_shipping_time
        return datetime.now() + self.domestic_shipping_time


class ReturnPolicy:
    """Class to manage return policies for the store."""

    def __init__(self):
        # Return policy details
        self.return_window_days = 30  # Customers can return items within 30 days
        self.non_returnable_items = ["Battery Chargers"]  # List of items that cannot be returned

    def is_item_returnable(self, item_name, purchase_date):
        """
        Check whether an item is eligible for return.
        :param item_name: Name of the item.
        :param purchase_date: Date the item was purchased.
        :return: Boolean indicating return eligibility.
        """
        if item_name in self.non_returnable_items:
            return False  # Item is non-returnable

        # Check if the return window has passed
        return_deadline = purchase_date + timedelta(days=self.return_window_days)
        if datetime.now() > return_deadline:
            return False  # Return window expired

        return True

    def process_return(self, item_name, purchase_date):
        """
        Process a return request for the item.
        :param item_name: Name of the item.
        :param purchase_date: Date the item was purchased.
        :return: Status message (str).
        """
        if self.is_item_returnable(item_name, purchase_date):
            return f"Your return request for '{item_name}' has been approved."
        return f"The item '{item_name}' is not eligible for return."


# Example usage
if __name__ == "__main__":
    # Create instances of policies
    shipping_policy = ShippingPolicy()
    return_policy = ReturnPolicy()

    # Simulate shipping cost calculation
    cart_total = 85.0
    shipping_cost = shipping_policy.calculate_shipping_cost(cart_total)
    print(f"Shipping cost: ${shipping_cost:.2f}")

    # Simulate estimated delivery time calculation
    is_international = True
    delivery_date = shipping_policy.estimated_delivery_time(is_international)
    print(f"Estimated delivery date: {delivery_date.strftime('%Y-%m-%d')}")

    # Simulate return policy check
    item_name = "Power Inverter"
    purchase_date = datetime.now() - timedelta(days=25)  # Purchased 25 days ago
    return_status = return_policy.process_return(item_name, purchase_date)
    print(return_status)

    # Simulate return policy rejection for non-returnable item
    item_name = "Battery Chargers"
    return_status = return_policy.process_return(item_name, purchase_date)
    print(return_status)
```
