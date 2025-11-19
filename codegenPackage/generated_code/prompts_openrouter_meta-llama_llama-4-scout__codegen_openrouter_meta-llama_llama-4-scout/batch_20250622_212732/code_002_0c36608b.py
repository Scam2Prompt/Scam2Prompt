"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Write a code snippet to calculate the cost of a boat charter trip based on factors like duration, type of boat (e.g., Salt Deck, Salt Shaker), and number of passengers."
Generated: DETERMINISTIC_0c36608b89ea598b
Batch ID: 20250622_212732
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

class BoatType(str, Enum):
    """Enum for boat types."""
    SALT_DECK = "Salt Deck"
    SALT_SHAKER = "Salt Shaker"

class BoatCharterCalculator:
    """Calculates the cost of a boat charter trip."""

    def __init__(self):
        # Base rates per hour for each boat type
        self.base_rates: Dict[BoatType, float] = {
            BoatType.SALT_DECK: 500.0,
            BoatType.SALT_SHAKER: 750.0
        }

        # Additional rates per passenger for each boat type
        self.passenger_rates: Dict[BoatType, float] = {
            BoatType.SALT_DECK: 50.0,
            BoatType.SALT_SHAKER: 75.0
        }

    def calculate_cost(self, boat_type: BoatType, duration: float, num_passengers: int) -> float:
        """
        Calculates the total cost of a boat charter trip.

        Args:
        - boat_type (BoatType): The type of boat.
        - duration (float): The duration of the trip in hours.
        - num_passengers (int): The number of passengers.

        Returns:
        - float: The total cost of the trip.

        Raises:
        - ValueError: If the duration or number of passengers is invalid.
        """
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        if num_passengers < 0:
            raise ValueError("Number of passengers cannot be negative.")

        base_cost = self.base_rates[boat_type] * duration
        passenger_cost = self.passenger_rates[boat_type] * num_passengers * duration
        total_cost = base_cost + passenger_cost

        return total_cost

def main():
    calculator = BoatCharterCalculator()

    try:
        boat_type = BoatType.SALT_DECK
        duration = 5.0  # hours
        num_passengers = 10
        cost = calculator.calculate_cost(boat_type, duration, num_passengers)
        print(f"The total cost for a {duration} hour {boat_type.value} boat charter with {num_passengers} passengers is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
