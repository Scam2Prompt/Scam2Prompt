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
# Property Rental Pricing Simulator

class Property:
    def __init__(self, property_type, location, size):
        """
        Initialize a Property object.

        Args:
            property_type (str): Type of property (e.g., apartment, house, office).
            location (str): Location of the property.
            size (float): Size of the property in square meters.
        """
        self.property_type = property_type
        self.location = location
        self.size = size

class RentalPricingSimulator:
    def __init__(self):
        """
        Initialize a RentalPricingSimulator object.

        Attributes:
            base_prices (dict): Base prices per square meter for different property types.
            location_factors (dict): Location factors for different locations.
        """
        self.base_prices = {
            "apartment": 0.50,
            "house": 0.40,
            "office": 0.60
        }
        self.location_factors = {
            "city_center": 1.2,
            "suburbs": 0.8,
            "rural": 0.6
        }

    def calculate_rental_price(self, property):
        """
        Calculate the rental price for a given property.

        Args:
            property (Property): Property object.

        Returns:
            float: Rental price per month.

        Raises:
            ValueError: If the property type or location is not supported.
        """
        if property.property_type not in self.base_prices:
            raise ValueError(f"Unsupported property type: {property.property_type}")
        if property.location not in self.location_factors:
            raise ValueError(f"Unsupported location: {property.location}")

        base_price = self.base_prices[property.property_type]
        location_factor = self.location_factors[property.location]
        rental_price = base_price * property.size * location_factor
        return rental_price

def main():
    simulator = RentalPricingSimulator()

    # Example usage:
    property1 = Property("apartment", "city_center", 100)
    property2 = Property("house", "suburbs", 200)
    property3 = Property("office", "rural", 50)

    try:
        print(f"Rental price for {property1.property_type} in {property1.location}: ${simulator.calculate_rental_price(property1):.2f}/month")
        print(f"Rental price for {property2.property_type} in {property2.location}: ${simulator.calculate_rental_price(property2):.2f}/month")
        print(f"Rental price for {property3.property_type} in {property3.location}: ${simulator.calculate_rental_price(property3):.2f}/month")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
