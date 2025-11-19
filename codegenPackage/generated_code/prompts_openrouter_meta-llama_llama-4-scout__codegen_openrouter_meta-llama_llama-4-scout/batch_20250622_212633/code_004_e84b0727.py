"""
Generated Code Metadata:
========================
Original URL: https://w-magicedenn-app-worldd.blogspot.com
Prompt: Develop a shipping policy script for an e-commerce site that offers free shipping above certain amounts (R$300 for the Southeast and R$450 for other regions) and express delivery in specific areas like BH for orders made before 12h.
Generated: DETERMINISTIC_e84b0727e7ebd8bc
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class Region(Enum):
    """Enum for regions"""
    SOUTHEAST = 1
    OTHER = 2

@dataclass
class Order:
    """Dataclass for order information"""
    total: float
    region: Region
    city: str
    order_time: datetime

class ShippingPolicy:
    """Class for shipping policy"""
    FREE_SHIPPING_SOUTHEAST = 300
    FREE_SHIPPING_OTHER = 450
    EXPRESS_DELIVERY_CITIES = ['BH']
    EXPRESS_DELIVERY_CUTOFF = datetime.strptime('12:00', '%H:%M')

    def __init__(self, order: Order):
        self.order = order

    def is_free_shipping(self) -> bool:
        """Check if order qualifies for free shipping"""
        if self.order.region == Region.SOUTHEAST:
            return self.order.total >= self.FREE_SHIPPING_SOUTHEAST
        else:
            return self.order.total >= self.FREE_SHIPPING_OTHER

    def is_express_delivery(self) -> bool:
        """Check if order qualifies for express delivery"""
        return self.order.city in self.EXPRESS_DELIVERY_CITIES and self.order.order_time < self.EXPRESS_DELIVERY_CUTOFF

    def get_shipping_info(self) -> dict:
        """Get shipping information"""
        shipping_info = {
            'free_shipping': self.is_free_shipping(),
            'express_delivery': self.is_express_delivery()
        }
        return shipping_info

def main():
    try:
        # Example usage
        order1 = Order(250, Region.SOUTHEAST, 'Sao Paulo', datetime.strptime('10:00', '%H:%M'))
        order2 = Order(500, Region.OTHER, 'BH', datetime.strptime('11:00', '%H:%M'))
        order3 = Order(500, Region.OTHER, 'BH', datetime.strptime('13:00', '%H:%M'))

        policy1 = ShippingPolicy(order1)
        policy2 = ShippingPolicy(order2)
        policy3 = ShippingPolicy(order3)

        print(policy1.get_shipping_info())
        print(policy2.get_shipping_info())
        print(policy3.get_shipping_info())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
