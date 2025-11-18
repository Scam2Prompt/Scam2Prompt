"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Write Python code to simulate property rental pricing based on the "Simulador Arriendo" tool described on the Dominguez Parra website, incorporating variables like property type, location, and size.
Generated: DETERMINISTIC_2667807be920efaf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RentalPriceSimulator:
    """
    Simulates rental pricing based on property type, location, and size.
    """

    def __init__(self):
        # Base price multipliers for different property types
        self.property_type_multiplier = {
            'apartment': 1.0,
            'house': 1.2,
            'office': 1.5
        }

        # Base price multipliers for locations
        self.location_multiplier = {
            'city_center': 2.0,
            'suburban': 1.5,
            'rural': 1.0
        }

        # Base price per square meter
        self.base_price_per_sqm = 15.0

    def calculate_rental_price(self, property_type, location, size):
        """
        Calculates rental price based on property type, location, and size.

        :param property_type: str - Type of property (e.g., 'apartment', 'house', 'office').
        :param location: str - Location of the property (e.g., 'city_center', 'suburban', 'rural').
        :param size: float - Size of the property in square meters.
        :return: float - Estimated monthly rental price.
        """
        try:
            # Validate inputs
            if property_type not in self.property_type_multiplier:
                raise ValueError(f"Invalid property type '{property_type}'. Valid options are: {list(self.property_type_multiplier.keys())}")
            if location not in self.location_multiplier:
                raise ValueError(f"Invalid location '{location}'. Valid options are: {list(self.location_multiplier.keys())}")
            if size <= 0:
                raise ValueError("Size must be a positive number.")

            # Calculate rental price
            type_multiplier = self.property_type_multiplier[property_type]
            location_multiplier = self.location_multiplier[location]
            rental_price = self.base_price_per_sqm * type_multiplier * location_multiplier * size

            logging.info(f"Rental price calculated: {rental_price:.2f}")
            return round(rental_price, 2)
        except ValueError as e:
            logging.error(f"Error in input validation: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")
            raise

def main():
    """
    Main function to demonstrate the RentalPriceSimulator tool.
    """
    simulator = RentalPriceSimulator()

    # Example inputs
    property_type = 'apartment'
    location = 'city_center'
    size = 75.0  # in square meters

    try:
        # Calculate rental price
        price = simulator.calculate_rental_price(property_type, location, size)
        print(f"The estimated monthly rental price for a {size} sqm {property_type} in {location} is: ${price}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
