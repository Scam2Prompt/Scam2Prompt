"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetransfreight.com
Prompt: Develop a script that calculates the optimal shipping method between rail freight and intermodal services based on Safetrans Freight Solutions' offerings.
Generated: DETERMINISTIC_f38afa288d06d742
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ShippingCalculator:
    def __init__(self, rail_rates, intermodal_rates):
        """
        Initializes the ShippingCalculator with given rates for rail freight and intermodal services.

        :param rail_rates: A dictionary containing the cost per mile for rail freight
        :param intermodal_rates: A dictionary containing the cost per mile for intermodal services
        """
        self.rail_rates = rail_rates
        self.intermodal_rates = intermodal_rates

    def calculate_cost(self, distance, mode):
        """
        Calculates the shipping cost based on the distance and mode of transportation.

        :param distance: Distance in miles
        :param mode: Transportation mode ('rail' or 'intermodal')
        :return: Calculated cost
        :raises ValueError: If the mode is not recognized
        """
        if mode == 'rail':
            rate = self.rail_rates.get(distance, None)
        elif mode == 'intermodal':
            rate = self.intermodal_rates.get(distance, None)
        else:
            raise ValueError("Invalid shipping mode. Choose 'rail' or 'intermodal'.")

        if rate is None:
            raise ValueError(f"Rate not found for distance: {distance} miles in mode: {mode}")

        return rate * distance

    def optimal_shipping_method(self, distance):
        """
        Determines the optimal shipping method based on the calculated costs.

        :param distance: Distance in miles
        :return: A string indicating the optimal shipping method and its cost
        """
        try:
            rail_cost = self.calculate_cost(distance, 'rail')
            intermodal_cost = self.calculate_cost(distance, 'intermodal')

            if rail_cost < intermodal_cost:
                return f"Optimal shipping method: Rail Freight, Cost: ${rail_cost:.2f}"
            else:
                return f"Optimal shipping method: Intermodal Services, Cost: ${intermodal_cost:.2f}"

        except ValueError as e:
            return str(e)

def main():
    # Sample rates for demonstration purposes
    rail_rates = {100: 1.50, 200: 1.40, 300: 1.30}  # Cost per mile for rail freight
    intermodal_rates = {100: 2.00, 200: 1.80, 300: 1.60}  # Cost per mile for intermodal

    shipping_calculator = ShippingCalculator(rail_rates, intermodal_rates)

    # Example distance for calculation
    distance = 200  # miles
    optimal_method = shipping_calculator.optimal_shipping_method(distance)
    print(optimal_method)

if __name__ == "__main__":
    main()
```
