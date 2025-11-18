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
class ShippingPolicy:
    """
    A class to represent the shipping policy for an online store.
    """

    def __init__(self, shipping_cost, free_shipping_threshold):
        """
        Initializes the ShippingPolicy with the given parameters.

        :param shipping_cost: Cost of shipping for orders below the threshold.
        :param free_shipping_threshold: Minimum order amount for free shipping.
        """
        self.shipping_cost = shipping_cost
        self.free_shipping_threshold = free_shipping_threshold

    def calculate_shipping(self, order_total):
        """
        Calculate the shipping cost based on the order total.

        :param order_total: Total amount of the order.
        :return: Shipping cost.
        """
        if order_total >= self.free_shipping_threshold:
            return 0
        return self.shipping_cost


class ReturnPolicy:
    """
    A class to represent the return policy for an online store.
    """

    def __init__(self, return_days, accept_opened_items):
        """
        Initializes the ReturnPolicy with the given parameters.

        :param return_days: Number of days within which returns are accepted.
        :param accept_opened_items: Whether opened items can be returned.
        """
        self.return_days = return_days
        self.accept_opened_items = accept_opened_items

    def is_returnable(self, purchase_date, item_opened):
        """
        Check if an item is returnable based on purchase date and condition.

        :param purchase_date: Date of purchase.
        :param item_opened: Whether the item was opened.
        :return: True if the item can be returned, False otherwise.
        """
        from datetime import datetime, timedelta

        if item_opened and not self.accept_opened_items:
            return False
        
        # Calculate the return window
        return_window = purchase_date + timedelta(days=self.return_days)
        return datetime.now() <= return_window


# Example usage
if __name__ == '__main__':
    # Example initialization of policies
    shipping_policy = ShippingPolicy(shipping_cost=5.99, free_shipping_threshold=50.00)
    return_policy = ReturnPolicy(return_days=30, accept_opened_items=False)

    # Simulate an order scenario
    order_total = 45.00
    print(f"Shipping cost for an order of ${order_total}: ${shipping_policy.calculate_shipping(order_total)}")

    # Simulate return scenario
    from datetime import datetime
    purchase_date = datetime.strptime('2023-09-15', '%Y-%m-%d')
    item_opened = False
    can_return = return_policy.is_returnable(purchase_date, item_opened)
    print(f"Can the item be returned? {'Yes' if can_return else 'No'}")
```
