"""
Generated Code Metadata:
========================
Original URL: https://compraenchinaseguro.com
Prompt: What are the key calculations for shipping costs from China to Venezuela, specifically for maritime and air freight?
Generated: DETERMINISTIC_4efec86670508c53
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ShippingCostCalculator:
    """
    A class to calculate shipping costs for maritime and air freight from China to Venezuela.
    """

    def __init__(self, weight_kg, distance_km, shipping_method):
        """
        Initializes the ShippingCostCalculator with weight, distance, and shipping method.

        :param weight_kg: Weight of the shipment in kilograms
        :param distance_km: Distance from China to Venezuela in kilometers
        :param shipping_method: Method of shipping ('maritime' or 'air')
        """
        self.weight_kg = weight_kg
        self.distance_km = distance_km
        self.shipping_method = shipping_method.lower()
        self.cost_per_kg = self._set_cost_per_kg()

    def _set_cost_per_kg(self):
        """
        Sets the cost per kilogram based on the shipping method.

        :return: Cost per kilogram
        :raises ValueError: If the shipping method is not recognized
        """
        if self.shipping_method == 'maritime':
            return 5.0  # Cost per kg for maritime shipping
        elif self.shipping_method == 'air':
            return 20.0  # Cost per kg for air shipping
        else:
            raise ValueError("Shipping method must be 'maritime' or 'air'.")

    def calculate_cost(self):
        """
        Calculates the total shipping cost based on weight, distance, and shipping method.

        :return: Total shipping cost
        """
        try:
            total_cost = self.weight_kg * self.cost_per_kg
            return total_cost
        except Exception as e:
            print(f"Error calculating cost: {e}")
            return None

    def calculate_delivery_time(self):
        """
        Estimates delivery time based on shipping method.

        :return: Estimated delivery time in days
        """
        if self.shipping_method == 'maritime':
            return math.ceil(self.distance_km / 500)  # Approx. 500 km/day for maritime
        elif self.shipping_method == 'air':
            return math.ceil(self.distance_km / 1000)  # Approx. 1000 km/day for air
        else:
            return None

# Example usage
if __name__ == "__main__":
    try:
        weight = 100  # Weight in kg
        distance = 15000  # Distance in km
        method = 'air'  # Shipping method

        calculator = ShippingCostCalculator(weight, distance, method)
        cost = calculator.calculate_cost()
        delivery_time = calculator.calculate_delivery_time()

        print(f"Total shipping cost: ${cost:.2f}")
        print(f"Estimated delivery time: {delivery_time} days")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
