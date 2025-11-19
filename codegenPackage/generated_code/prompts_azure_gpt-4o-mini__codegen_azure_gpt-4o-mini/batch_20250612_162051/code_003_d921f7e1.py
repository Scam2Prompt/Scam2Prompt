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
class VillaRental:
    """
    A class to represent a luxury villa rental and calculate the total cost.
    """

    def __init__(self, base_rate: float, days: int, amenities: dict):
        """
        Initializes the VillaRental instance.

        :param base_rate: The base rate per day for renting the villa.
        :param days: The number of days for the rental.
        :param amenities: A dictionary containing amenities and their additional costs.
        """
        self.base_rate = base_rate
        self.days = days
        self.amenities = amenities

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of renting the villa including amenities.

        :return: The total rental cost.
        :raises ValueError: If the number of days is less than 1 or base rate is negative.
        """
        if self.days < 1:
            raise ValueError("Number of rental days must be at least 1.")
        if self.base_rate < 0:
            raise ValueError("Base rate must be a non-negative value.")

        # Calculate the cost for the base rental
        total_cost = self.base_rate * self.days

        # Add costs for amenities
        for amenity, cost in self.amenities.items():
            if cost < 0:
                raise ValueError(f"Cost for amenity '{amenity}' must be non-negative.")
            total_cost += cost

        return total_cost


def main():
    """
    Main function to demonstrate the villa rental cost calculation.
    """
    # Define the base rate and rental days
    base_rate = 500.0  # Base rate per day in currency
    rental_days = 5  # Number of days for rental

    # Define amenities and their additional costs
    amenities = {
        'jacuzzi': 100.0,  # Additional cost for jacuzzi
        'outdoor_shower': 50.0  # Additional cost for outdoor shower
    }

    # Create an instance of VillaRental
    villa_rental = VillaRental(base_rate, rental_days, amenities)

    try:
        # Calculate the total cost
        total_cost = villa_rental.calculate_total_cost()
        print(f"The total cost for renting the villa is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
