"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Write a Python function that calculates the market value of a property based on the guidelines provided by the ABNT – NBR 14.653 standards mentioned on the website.
Generated: DETERMINISTIC_5abf9251956badbd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyValueCalculator:
    """
    A class to calculate the market value of a property based on ABNT – NBR 14.653 standards.
    """

    def __init__(self, area: float, location_factor: float, property_type_factor: float):
        """
        Initializes the PropertyValueCalculator with the necessary parameters.

        :param area: The area of the property in square meters.
        :param location_factor: A multiplier based on the property's location.
        :param property_type_factor: A multiplier based on the type of property (e.g., residential, commercial).
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        if location_factor <= 0:
            raise ValueError("Location factor must be a positive number.")
        if property_type_factor <= 0:
            raise ValueError("Property type factor must be a positive number.")

        self.area = area
        self.location_factor = location_factor
        self.property_type_factor = property_type_factor

    def calculate_market_value(self) -> float:
        """
        Calculates the market value of the property.

        :return: The calculated market value of the property.
        """
        # Base price per square meter (this can be adjusted based on market conditions)
        base_price_per_sqm = 1000.0  # Example base price in currency units

        # Calculate the market value
        market_value = (self.area * base_price_per_sqm) * self.location_factor * self.property_type_factor

        return market_value

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of PropertyValueCalculator
        property_calculator = PropertyValueCalculator(area=120.0, location_factor=1.2, property_type_factor=1.5)
        
        # Calculate and print the market value
        market_value = property_calculator.calculate_market_value()
        print(f"The market value of the property is: {market_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
