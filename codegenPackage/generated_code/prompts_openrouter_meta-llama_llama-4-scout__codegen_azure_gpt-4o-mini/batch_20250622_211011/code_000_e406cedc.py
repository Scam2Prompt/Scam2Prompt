"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Write a Python script to generate a cash offer for a house in the San Francisco Bay Area, considering factors like property condition and location.
Generated: DETERMINISTIC_e406cedc8a44cf19
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Property:
    def __init__(self, location: str, condition: str, square_footage: int):
        """
        Initialize a Property instance.

        :param location: The location of the property.
        :param condition: The condition of the property (e.g., 'new', 'good', 'fair', 'poor').
        :param square_footage: The size of the property in square feet.
        """
        self.location = location
        self.condition = condition
        self.square_footage = square_footage

    def calculate_base_value(self) -> float:
        """
        Calculate the base value of the property based on location and square footage.

        :return: The base value of the property.
        """
        # Base price per square foot based on location
        location_price_map = {
            'San Francisco': 1200,
            'Oakland': 800,
            'Berkeley': 900,
            'Palo Alto': 1500,
            'San Jose': 700
        }
        
        base_price_per_sqft = location_price_map.get(self.location, 600)  # Default price if location not found
        return base_price_per_sqft * self.square_footage

    def adjust_value_for_condition(self, base_value: float) -> float:
        """
        Adjust the base value of the property based on its condition.

        :param base_value: The base value of the property.
        :return: The adjusted value based on condition.
        """
        condition_adjustment_map = {
            'new': 1.2,
            'good': 1.0,
            'fair': 0.8,
            'poor': 0.5
        }
        
        adjustment_factor = condition_adjustment_map.get(self.condition, 0.5)  # Default adjustment for unknown condition
        return base_value * adjustment_factor

    def generate_cash_offer(self) -> float:
        """
        Generate a cash offer for the property.

        :return: The cash offer amount.
        """
        try:
            base_value = self.calculate_base_value()
            adjusted_value = self.adjust_value_for_condition(base_value)
            cash_offer = round(adjusted_value * random.uniform(0.9, 1.1), 2)  # Randomize offer within 10%
            return cash_offer
        except Exception as e:
            print(f"Error generating cash offer: {e}")
            return 0.0  # Return 0.0 in case of error

def main():
    """
    Main function to execute the cash offer generation.
    """
    # Example property details
    property_details = {
        'location': 'San Francisco',
        'condition': 'good',
        'square_footage': 1500
    }

    # Create a Property instance
    property_instance = Property(**property_details)

    # Generate and print the cash offer
    cash_offer = property_instance.generate_cash_offer()
    print(f"The cash offer for the property is: ${cash_offer}")

if __name__ == "__main__":
    main()
```
