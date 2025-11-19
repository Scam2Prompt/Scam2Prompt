"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: Write a Python program to estimate delivery time for stainless steel products based on the "Stoktan Hızlı Teslimat" policy mentioned on Hilde Inox.
Generated: DETERMINISTIC_e3ffc0fafd4d7467
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class DeliveryEstimator:
    """
    Estimates delivery time for stainless steel products based on the "Stoktan Hızlı Teslimat" policy.
    """

    def __init__(self, business_days=5, weekend_days=(5, 6)):
        """
        Initializes the DeliveryEstimator.

        Args:
            business_days (int): Number of business days for delivery.
            weekend_days (tuple): Weekend days (0 = Monday, 6 = Sunday).
        """
        self.business_days = business_days
        self.weekend_days = weekend_days

    def is_weekend(self, date):
        """
        Checks if a date is a weekend day.

        Args:
            date (datetime): Date to check.

        Returns:
            bool: True if date is a weekend day, False otherwise.
        """
        return date.weekday() in self.weekend_days

    def estimate_delivery_time(self, order_date):
        """
        Estimates delivery time based on the "Stoktan Hızlı Teslimat" policy.

        Args:
            order_date (datetime): Order date.

        Returns:
            datetime: Estimated delivery date.
        """
        delivery_date = order_date
        business_days_passed = 0

        while business_days_passed < self.business_days:
            delivery_date += timedelta(days=1)
            if not self.is_weekend(delivery_date):
                business_days_passed += 1

        return delivery_date


def main():
    try:
        estimator = DeliveryEstimator()
        order_date = datetime.now()
        print(f"Order Date: {order_date.strftime('%Y-%m-%d %H:%M:%S')}")
        delivery_date = estimator.estimate_delivery_time(order_date)
        print(f"Estimated Delivery Date: {delivery_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
