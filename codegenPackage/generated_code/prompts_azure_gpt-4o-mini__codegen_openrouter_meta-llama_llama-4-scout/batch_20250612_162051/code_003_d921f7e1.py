"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Develop a function in Python that calculates the total cost for renting a luxury villa, taking into account amenities such as a jacuzzi and outdoor shower, as featured in Diamond Villa Corfu.
Generated: DETERMINISTIC_d921f7e1b09f2b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class Amenity(Enum):
    """ Enum for villa amenities """
    JACUZZI = 50
    OUTDOOR_SHOWER = 75
    POOL = 100
    PRIVATE_GARDEN = 150

class VillaRentalCalculator:
    """ Calculates total cost for renting a luxury villa """

    def __init__(self, base_rate: float, amenities: Dict[Amenity, bool]):
        """
        Initializes the VillaRentalCalculator.

        Args:
        - base_rate (float): The base rental rate of the villa.
        - amenities (Dict[Amenity, bool]): A dictionary of amenities and their availability.
        """
        self.base_rate = base_rate
        self.amenities = amenities

    def calculate_total_cost(self, nights: int) -> float:
        """
        Calculates the total cost for renting the villa.

        Args:
        - nights (int): The number of nights the villa is rented.

        Returns:
        - float: The total cost for renting the villa.

        Raises:
        - ValueError: If the number of nights is not a positive integer.
        """
        if not isinstance(nights, int) or nights <= 0:
            raise ValueError("Number of nights must be a positive integer")

        # Calculate the base cost
        base_cost = self.base_rate * nights

        # Calculate the amenities cost
        amenities_cost = sum(amenity.value for amenity, available in self.amenities.items() if available)

        # Calculate the total cost
        total_cost = base_cost + (amenities_cost * nights)

        return total_cost

def main():
    # Define the base rate and amenities for Diamond Villa Corfu
    base_rate = 500.0
    amenities = {
        Amenity.JACUZZI: True,
        Amenity.OUTDOOR_SHOWER: True,
        Amenity.POOL: True,
        Amenity.PRIVATE_GARDEN: True
    }

    # Create a VillaRentalCalculator instance
    calculator = VillaRentalCalculator(base_rate, amenities)

    # Calculate the total cost for 7 nights
    try:
        total_cost = calculator.calculate_total_cost(7)
        print(f"Total cost for 7 nights: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
