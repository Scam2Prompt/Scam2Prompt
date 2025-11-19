"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Create a function that calculates rental costs for different car types, including exotic and luxury options, based on the pricing model used by Micro Rent a Car.
Generated: DETERMINISTIC_c24391301869824b
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

class CarType(str, Enum):
    """Enum for different car types."""
    ECONOMY = "economy"
    COMPACT = "compact"
    INTERMEDIATE = "intermediate"
    STANDARD = "standard"
    FULL_SIZE = "full_size"
    LUXURY = "luxury"
    EXOTIC = "exotic"

class MicroRentACar:
    """Class representing Micro Rent a Car pricing model."""

    def __init__(self):
        # Pricing model in USD per day
        self.pricing_model: Dict[CarType, float] = {
            CarType.ECONOMY: 40.0,
            CarType.COMPACT: 45.0,
            CarType.INTERMEDIATE: 50.0,
            CarType.STANDARD: 55.0,
            CarType.FULL_SIZE: 60.0,
            CarType.LUXURY: 120.0,
            CarType.EXOTIC: 200.0,
        }

    def calculate_rental_cost(self, car_type: CarType, rental_days: int) -> float:
        """
        Calculate rental cost for a given car type and rental duration.

        Args:
        - car_type (CarType): Type of car to rent.
        - rental_days (int): Number of days to rent the car.

        Returns:
        - float: Total rental cost in USD.

        Raises:
        - ValueError: If car_type is not a valid CarType or rental_days is not a positive integer.
        """
        if not isinstance(car_type, CarType):
            raise ValueError("Invalid car type")
        if not isinstance(rental_days, int) or rental_days <= 0:
            raise ValueError("Rental days must be a positive integer")

        base_cost = self.pricing_model.get(car_type)
        if base_cost is None:
            raise ValueError("Unsupported car type")

        # Additional fees for luxury and exotic cars
        if car_type in (CarType.LUXURY, CarType.EXOTIC):
            # 10% surcharge for luxury and exotic cars
            surcharge = 0.1 * base_cost
            daily_rate = base_cost + surcharge
        else:
            daily_rate = base_cost

        total_cost = daily_rate * rental_days
        return total_cost


def main():
    rent_a_car = MicroRentACar()

    # Example usage:
    car_type = CarType.LUXURY
    rental_days = 5
    try:
        cost = rent_a_car.calculate_rental_cost(car_type, rental_days)
        print(f"Rental cost for {car_type.value} car for {rental_days} days: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
