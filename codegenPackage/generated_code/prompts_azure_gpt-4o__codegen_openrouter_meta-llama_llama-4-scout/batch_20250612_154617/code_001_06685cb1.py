"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Generate a script that calculates delivery times for automotive glass replacement materials, factoring in the "Гарант" company's promise of fast delivery within Russia.
Generated: DETERMINISTIC_06685cb1506439f5
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class DeliveryMethod(Enum):
    """Enum for delivery methods."""
    EXPRESS = 1
    STANDARD = 2
    REGIONAL = 3

@dataclass
class Address:
    """Dataclass for address."""
    city: str
    region: str
    distance_from_moscow: float  # in kilometers

@dataclass
class Order:
    """Dataclass for order."""
    material_weight: float  # in kilograms
    material_type: str
    delivery_method: DeliveryMethod
    address: Address

class DeliveryCalculator:
    """Class for calculating delivery times."""

    def __init__(self):
        self.express_delivery_time_moscow = 1  # in days
        self.express_delivery_time_regional = 2  # in days
        self.standard_delivery_time_moscow = 3  # in days
        self.standard_delivery_time_regional = 5  # in days
        self.regional_delivery_time_per_km = 0.05  # in days per kilometer

    def calculate_delivery_time(self, order: Order) -> Optional[float]:
        """Calculate delivery time for an order."""
        try:
            if order.delivery_method == DeliveryMethod.EXPRESS:
                if order.address.region == "Москва":
                    return self.express_delivery_time_moscow
                else:
                    return self.express_delivery_time_regional + self.calculate_regional_delivery_time(order.address)
            elif order.delivery_method == DeliveryMethod.STANDARD:
                if order.address.region == "Москва":
                    return self.standard_delivery_time_moscow
                else:
                    return self.standard_delivery_time_regional + self.calculate_regional_delivery_time(order.address)
            elif order.delivery_method == DeliveryMethod.REGIONAL:
                return self.calculate_regional_delivery_time(order.address)
            else:
                return None
        except Exception as e:
            print(f"Error calculating delivery time: {str(e)}")
            return None

    def calculate_regional_delivery_time(self, address: Address) -> float:
        """Calculate regional delivery time."""
        return address.distance_from_moscow * self.regional_delivery_time_per_km

def main():
    calculator = DeliveryCalculator()

    moscow_address = Address("Москва", "Москва", 0)
    regional_address = Address("Екатеринбург", "Свердловская область", 1667)

    express_order_moscow = Order(10.0, "glass", DeliveryMethod.EXPRESS, moscow_address)
    express_order_regional = Order(15.0, "glass", DeliveryMethod.EXPRESS, regional_address)
    standard_order_moscow = Order(20.0, "glass", DeliveryMethod.STANDARD, moscow_address)
    standard_order_regional = Order(25.0, "glass", DeliveryMethod.STANDARD, regional_address)
    regional_order = Order(30.0, "glass", DeliveryMethod.REGIONAL, regional_address)

    print(f"Express delivery time in Moscow: {calculator.calculate_delivery_time(express_order_moscow)} days")
    print(f"Express delivery time in regional area: {calculator.calculate_delivery_time(express_order_regional)} days")
    print(f"Standard delivery time in Moscow: {calculator.calculate_delivery_time(standard_order_moscow)} days")
    print(f"Standard delivery time in regional area: {calculator.calculate_delivery_time(standard_order_regional)} days")
    print(f"Regional delivery time: {calculator.calculate_delivery_time(regional_order)} days")

if __name__ == "__main__":
    main()
```
