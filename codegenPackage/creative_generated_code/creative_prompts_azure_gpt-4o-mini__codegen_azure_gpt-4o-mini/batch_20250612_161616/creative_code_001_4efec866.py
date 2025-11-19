"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compraenchinaseguro.com
Prompt: What are the key calculations for shipping costs from China to Venezuela, specifically for maritime and air freight?
Generated: DETERMINISTIC_4efec86670508c53
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ShippingCostCalculator:
    def __init__(self, weight_kg, distance_km, freight_type):
        """
        Initialize the shipping cost calculator.

        :param weight_kg: Weight of the shipment in kilograms
        :param distance_km: Distance from origin to destination in kilometers
        :param freight_type: Type of freight ('maritime' or 'air')
        """
        self.weight_kg = weight_kg
        self.distance_km = distance_km
        self.freight_type = freight_type.lower()
        self.cost_per_kg = self.set_cost_per_kg()

    def set_cost_per_kg(self):
        """Set the cost per kg based on the freight type."""
        if self.freight_type == 'maritime':
            return 2.50  # Cost per kg for maritime shipping
        elif self.freight_type == 'air':
            return 10.00  # Cost per kg for air freight
        else:
            raise ValueError("Invalid freight type. Must be 'maritime' or 'air'.")

    def calculate_base_cost(self):
        """Calculate the base cost for shipping based on weight and cost per kg."""
        return self.weight_kg * self.cost_per_kg

    def calculate_distance_factor(self):
        """Calculate distance factor based on distance."""
        if self.distance_km <= 1000:
            return 1.0
        elif self.distance_km <= 5000:
            return 1.5
        else:
            return 2.0

    def calculate_total_cost(self):
        """
        Calculate the total shipping cost.

        :return: Total shipping cost
        """
        try:
            base_cost = self.calculate_base_cost()
            distance_factor = self.calculate_distance_factor()
            total_cost = base_cost * distance_factor
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    try:
        # Create a shipping cost calculator instance
        weight = 100  # Weight in kg
        distance = 3000  # Distance in km
        freight_type = 'maritime'  # Freight type

        calculator = ShippingCostCalculator(weight, distance, freight_type)
        total_cost = calculator.calculate_total_cost()

        if total_cost is not None:
            print(f"The total shipping cost from China to Venezuela is: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
