"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Create a function that calculates the cost of advertising in specific locations based on the pricing structure provided by WOW MEDIA.
Generated: DETERMINISTIC_64a4582a8f97c76c
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AdvertisingCostCalculator:
    """
    A class to calculate the cost of advertising based on the pricing structure provided by WOW MEDIA.
    """

    def __init__(self):
        # Pricing structure for different locations (per unit cost)
        self.pricing_structure = {
            'Location_A': 100.0,  # Cost per unit for Location A
            'Location_B': 150.0,  # Cost per unit for Location B
            'Location_C': 200.0,  # Cost per unit for Location C
        }

    def calculate_cost(self, location, units):
        """
        Calculate the total cost of advertising for the specified location and number of units.

        :param location: The advertising location (string).
        :param units: The number of advertising units (int).
        :returns: Total cost (float).
        :raises ValueError: If the location is not valid or if units is not positive.
        """
        # Validate input parameters
        if location not in self.pricing_structure:
            raise ValueError(f"Invalid location '{location}'. Valid locations are: {list(self.pricing_structure.keys())}.")
        
        if not isinstance(units, int) or units <= 0:
            raise ValueError("Units must be a positive integer.")

        # Calculate total cost
        cost_per_unit = self.pricing_structure[location]
        total_cost = cost_per_unit * units
        
        return total_cost

# Example usage
if __name__ == "__main__":
    calculator = AdvertisingCostCalculator()
    try:
        location = 'Location_A'
        units = 5
        cost = calculator.calculate_cost(location, units)
        print(f"The total cost for advertising in {location} for {units} units is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
