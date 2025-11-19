"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Write a code snippet to implement a coffee brewing calculator, taking into account factors like coffee-to-water ratio and brewing time.
Generated: DETERMINISTIC_a956e09073345ca2
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Coffee Brewing Calculator

Calculates the optimal coffee and water quantities for a brew based on the coffee-to-water ratio and brewing time.

Author: [Your Name]
Date: [Today's Date]
"""

class CoffeeBrewingCalculator:
    def __init__(self, coffee_to_water_ratio=1/15, brewing_time=4):
        """
        Initializes the CoffeeBrewingCalculator with a default coffee-to-water ratio and brewing time.

        Args:
            coffee_to_water_ratio (float, optional): The ratio of coffee to water in grams per milliliter. Defaults to 1/15.
            brewing_time (int, optional): The brewing time in minutes. Defaults to 4.
        """
        self.coffee_to_water_ratio = coffee_to_water_ratio
        self.brewing_time = brewing_time

    def calculate_coffee_quantity(self, water_quantity):
        """
        Calculates the optimal coffee quantity based on the water quantity and coffee-to-water ratio.

        Args:
            water_quantity (float): The quantity of water in milliliters.

        Returns:
            float: The optimal coffee quantity in grams.
        """
        return water_quantity * self.coffee_to_water_ratio

    def calculate_water_quantity(self, coffee_quantity):
        """
        Calculates the optimal water quantity based on the coffee quantity and coffee-to-water ratio.

        Args:
            coffee_quantity (float): The quantity of coffee in grams.

        Returns:
            float: The optimal water quantity in milliliters.
        """
        if self.coffee_to_water_ratio == 0:
            raise ValueError("Coffee-to-water ratio cannot be zero")
        return coffee_quantity / self.coffee_to_water_ratio

    def validate_brewing_time(self):
        """
        Validates the brewing time.

        Raises:
            ValueError: If the brewing time is not within the recommended range (3-5 minutes).
        """
        if not 3 <= self.brewing_time <= 5:
            raise ValueError("Brewing time must be between 3 and 5 minutes")


def main():
    try:
        calculator = CoffeeBrewingCalculator()

        print("Coffee Brewing Calculator")
        print("-------------------------")

        water_quantity = float(input("Enter the water quantity in milliliters: "))
        coffee_quantity = calculator.calculate_coffee_quantity(water_quantity)

        print(f"Optimal coffee quantity: {coffee_quantity:.2f} grams")

        calculator.brewing_time = int(input("Enter the brewing time in minutes: "))
        calculator.validate_brewing_time()

        print(f"Brewing time validated: {calculator.brewing_time} minutes")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
