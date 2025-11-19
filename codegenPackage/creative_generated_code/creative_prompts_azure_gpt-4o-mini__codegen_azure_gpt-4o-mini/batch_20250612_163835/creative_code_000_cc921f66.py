"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate the optimal cooler size for a camping trip based on the Engel Coolers product line.
Generated: DETERMINISTIC_cc921f6640a3becf
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Cooler:
    """
    Represents a cooler with a specific capacity and recommended usage.
    """
    
    def __init__(self, name: str, capacity: float):
        """
        Initializes a Cooler instance.

        :param name: The name of the cooler.
        :param capacity: The capacity of the cooler in quarts.
        """
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} - {self.capacity} quarts"


class CoolerCalculator:
    """
    A class to calculate the optimal cooler size based on user needs.
    """

    def __init__(self, coolers: list):
        """
        Initializes the CoolerCalculator with a list of coolers.

        :param coolers: List of Cooler objects.
        """
        self.coolers = coolers

    def calculate_optimal_cooler(self, total_food_weight: float, days: int) -> Cooler:
        """
        Calculates the optimal cooler based on food weight and duration of the trip.

        :param total_food_weight: Total weight of food in pounds.
        :param days: Number of days for the camping trip.
        :return: The optimal Cooler object.
        """
        # Calculate required capacity in quarts
        required_capacity = self._calculate_required_capacity(total_food_weight, days)
        
        # Find the smallest cooler that meets the required capacity
        optimal_cooler = min((cooler for cooler in self.coolers if cooler.capacity >= required_capacity),
                             key=lambda cooler: cooler.capacity,
                             default=None)

        if optimal_cooler is None:
            raise ValueError("No cooler available to meet the required capacity.")

        return optimal_cooler

    def _calculate_required_capacity(self, total_food_weight: float, days: int) -> float:
        """
        Helper method to calculate the required cooler capacity based on food weight and days.

        :param total_food_weight: Total weight of food in pounds.
        :param days: Number of days for the camping trip.
        :return: Required cooler capacity in quarts.
        """
        # Assuming approximately 1 quart is needed for 1 pound of food
        # and additional capacity is needed for ice (1 quart of ice for each quart of food)
        required_quarts = (total_food_weight * 2) / 1.25  # 1 quart = ~1.25 lbs
        return required_quarts


def main():
    # List of Engel Coolers with capacities in quarts
    coolers = [
        Cooler("Engel 19 Quart", 19),
        Cooler("Engel 30 Quart", 30),
        Cooler("Engel 40 Quart", 40),
        Cooler("Engel 65 Quart", 65),
        Cooler("Engel 75 Quart", 75)
    ]

    calculator = CoolerCalculator(coolers)

    # Example usage
    try:
        total_food_weight = float(input("Enter total food weight in pounds: "))
        days = int(input("Enter number of days for the trip: "))
        optimal_cooler = calculator.calculate_optimal_cooler(total_food_weight, days)
        print(f"The optimal cooler for your trip is: {optimal_cooler}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
