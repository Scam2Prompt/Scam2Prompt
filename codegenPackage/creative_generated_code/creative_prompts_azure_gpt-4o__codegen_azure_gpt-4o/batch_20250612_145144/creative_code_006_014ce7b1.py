"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Generate code to calculate shipping costs for products purchased from an online store that "ENVIAMOS PARA TODO O BRASIL" via the postal service.
Generated: DETERMINISTIC_014ce7b1301fd63e
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_calculator.py

import math

class ShippingCalculator:
    """
    A class to calculate shipping costs for products purchased in Brazil.
    It supports postal service delivery to any location in the country.
    """

    def __init__(self):
        # Shipping cost parameters (these values can be updated based on the postal service rates)
        self.base_cost = 10.0  # Base cost in BRL for shipping
        self.cost_per_kg = 5.0  # Cost in BRL per kilogram
        self.cost_per_km = 0.02  # Cost in BRL per kilometer

    def calculate_shipping_cost(self, weight_kg, distance_km):
        """
        Calculate the shipping cost based on product weight and delivery distance.

        :param weight_kg: Weight of the product in kilograms
        :param distance_km: Distance to delivery location in kilometers
        :return: Total shipping cost in BRL
        """
        # Validate input arguments
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        if distance_km <= 0:
            raise ValueError("Distance must be greater than zero.")

        # Calculate shipping cost using formula
        shipping_cost = self.base_cost + (self.cost_per_kg * weight_kg) + (self.cost_per_km * distance_km)
        
        # Round cost to two decimal places for currency formatting
        return round(shipping_cost, 2)

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    # Create an instance of the ShippingCalculator
    calculator = ShippingCalculator()

    try:
        # Sample inputs (replace with actual user input in production)
        weight_kg = float(input("Enter the weight of the product in kilograms: "))
        distance_km = float(input("Enter the delivery distance in kilometers: "))

        # Calculate the shipping cost
        cost = calculator.calculate_shipping_cost(weight_kg, distance_km)

        # Print the result
        print(f"The total shipping cost is: R$ {cost:.2f}")
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
