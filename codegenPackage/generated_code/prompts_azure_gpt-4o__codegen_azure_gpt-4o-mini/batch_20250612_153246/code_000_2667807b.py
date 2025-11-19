"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write Python code to simulate property rental pricing based on the "Simulador Arriendo" tool described on the Dominguez Parra website, incorporating variables like property type, location, and size.
Generated: DETERMINISTIC_2667807be920efaf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PropertyRentalSimulator:
    """
    A simulator for property rental pricing based on property type, location, and size.
    """

    def __init__(self):
        # Define base prices for different property types
        self.base_prices = {
            'apartment': 1000,
            'house': 1500,
            'studio': 800,
            'villa': 2000
        }
        
        # Define location multipliers
        self.location_multipliers = {
            'city_center': 1.5,
            'suburbs': 1.2,
            'rural': 0.8
        }
        
        # Define size price per square meter
        self.size_price_per_sqm = 10

    def calculate_rental_price(self, property_type, location, size):
        """
        Calculate the rental price based on property type, location, and size.

        :param property_type: Type of the property (e.g., apartment, house, studio, villa)
        :param location: Location of the property (e.g., city_center, suburbs, rural)
        :param size: Size of the property in square meters
        :return: Calculated rental price
        """
        try:
            # Validate inputs
            if property_type not in self.base_prices:
                raise ValueError(f"Invalid property type: {property_type}")
            if location not in self.location_multipliers:
                raise ValueError(f"Invalid location: {location}")
            if size <= 0:
                raise ValueError("Size must be a positive number")

            # Calculate the base price
            base_price = self.base_prices[property_type]
            # Apply location multiplier
            location_price = base_price * self.location_multipliers[location]
            # Calculate final price based on size
            final_price = location_price + (self.size_price_per_sqm * size)

            return round(final_price, 2)

        except ValueError as e:
            print(f"Error: {e}")
            return None

def main():
    simulator = PropertyRentalSimulator()
    
    # Example usage
    property_type = 'apartment'
    location = 'city_center'
    size = 50  # in square meters

    rental_price = simulator.calculate_rental_price(property_type, location, size)
    
    if rental_price is not None:
        print(f"The estimated rental price for a {size} sqm {property_type} in {location} is: ${rental_price}")

if __name__ == "__main__":
    main()
```
